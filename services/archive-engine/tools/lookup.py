#!/usr/bin/env python3
"""Look up mechanisms from the Master Mechanism Atlas.

Supports three query modes:
  --dials rimbaud=70,wilde=20,burroughs=10  → mechanisms activated at those settings
  --mechanism "negative_space"               → full Atlas entry for a mechanism
  --author bishop                            → all mechanisms attributed to an author
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ATLAS_PATH = PROJECT_ROOT / "research" / "synthesis" / "MECHANISM-ATLAS.md"

# Dial activation levels mapped to numeric thresholds
ACTIVATION = {"primary": 2, "moderate": 1, "rare": 0}

# Author name normalization
AUTHOR_ALIASES = {
    "rimbaud": "Rimbaud", "wilde": "Wilde", "burroughs": "Burroughs",
    "forster": "Forster", "cavafy": "Cavafy", "baldwin": "Baldwin",
    "genet": "Genet", "delany": "Delany", "bishop": "Bishop",
    "acker": "Acker", "lorde": "Lorde",
}


def parse_atlas() -> list[dict]:
    """Parse MECHANISM-ATLAS.md Part I into structured entries."""
    if not ATLAS_PATH.exists():
        print(f"Error: Atlas not found at {ATLAS_PATH}")
        sys.exit(1)

    text = ATLAS_PATH.read_text(encoding="utf-8")

    # Split on mechanism headers: ### N. Name
    entries = []
    blocks = re.split(r"\n### \d+\.\s+", text)

    for block in blocks[1:]:  # skip preamble before first ###
        entry = {"raw": block}

        # Name is the first line
        lines = block.strip().split("\n")
        entry["name"] = lines[0].strip()

        # Definition
        defn = re.search(r"\*\*Definition\*\*:\s*(.+?)(?=\n\*\*)", block, re.DOTALL)
        entry["definition"] = defn.group(1).strip() if defn else ""

        # Authors
        authors = re.search(r"\*\*Authors\*\*:\s*(.+?)(?=\n\*\*)", block, re.DOTALL)
        entry["authors_raw"] = authors.group(1).strip() if authors else ""
        # Extract author names
        entry["authors"] = re.findall(r"(Rimbaud|Wilde|Burroughs|Forster|Cavafy|Baldwin|Genet|Delany|Bishop|Acker|Lorde)", entry["authors_raw"])

        # Dial activation
        dial_line = re.search(r"\*\*Dial Activation\*\*:\s*(.+)", block)
        entry["dials"] = {"rimbaud": "rare", "wilde": "rare", "burroughs": "rare"}
        if dial_line:
            raw = dial_line.group(1).lower()
            for dial_name in ("rimbaud", "wilde", "burroughs"):
                for level in ("primary", "moderate", "rare"):
                    # Match patterns like "Rimbaud primary" or "Rimbaud P"
                    pattern = rf"{dial_name}\s+(?:{level}|{level[0]}(?:\s|\|))"
                    if re.search(pattern, raw):
                        entry["dials"][dial_name] = level
                        break

        # Craft rule
        craft = re.search(r"\*\*Craft Rule\*\*:\s*(.+?)(?=\n\*\*|\n---|\Z)", block, re.DOTALL)
        entry["craft_rule"] = craft.group(1).strip() if craft else ""

        # Related mechanisms
        related = re.search(r"\*\*Related Mechanisms\*\*:\s*(.+?)(?=\n---|\Z)", block, re.DOTALL)
        entry["related"] = related.group(1).strip() if related else ""

        entries.append(entry)

    return entries


def dial_score(entry: dict, rimbaud: int, wilde: int, burroughs: int) -> float:
    """Score a mechanism's relevance to given dial settings.

    Higher scores = stronger activation at the given settings.
    A mechanism marked 'primary' for a high dial scores highest.
    """
    score = 0.0
    for dial_name, dial_val in [("rimbaud", rimbaud), ("wilde", wilde), ("burroughs", burroughs)]:
        level = entry["dials"].get(dial_name, "rare")
        activation = ACTIVATION.get(level, 0)
        # Weight by how high the dial is set (0-100 normalized to 0-1)
        score += activation * (dial_val / 100.0)
    return score


def print_entry(entry: dict, verbose: bool = True):
    """Print a mechanism entry."""
    print(f"\n  {entry['name']}")
    print(f"  {'─' * len(entry['name'])}")
    if verbose:
        print(f"  Definition: {entry['definition']}")
        print(f"  Authors: {', '.join(entry['authors'])}")
        dials = entry["dials"]
        print(f"  Dials: R={dials['rimbaud']} | W={dials['wilde']} | B={dials['burroughs']}")
        print(f"  Craft Rule: {entry['craft_rule']}")
        if entry["related"]:
            print(f"  Related: {entry['related']}")


def cmd_dials(entries: list[dict], dial_str: str):
    """Look up mechanisms by dial settings."""
    # Parse "rimbaud=70,wilde=20,burroughs=10"
    dials = {"rimbaud": 50, "wilde": 50, "burroughs": 50}
    for part in dial_str.split(","):
        key, _, val = part.strip().partition("=")
        key = key.strip().lower()
        if key in dials:
            dials[key] = int(val.strip())

    r, w, b = dials["rimbaud"], dials["wilde"], dials["burroughs"]
    print(f"\nMechanisms activated at R={r} / W={w} / B={b}:")

    scored = [(dial_score(e, r, w, b), e) for e in entries]
    scored.sort(key=lambda x: -x[0])

    # Show mechanisms with score > 0.5 (meaningful activation)
    shown = 0
    for score, entry in scored:
        if score < 0.5:
            break
        print_entry(entry)
        print(f"  Activation score: {score:.2f}")
        shown += 1

    if shown == 0:
        # Fall back to top 5
        print("  (No strong activations — showing top 5 by relevance)")
        for score, entry in scored[:5]:
            print_entry(entry, verbose=False)
            print(f"  Activation score: {score:.2f}")
            shown += 1

    print(f"\n--- {shown} mechanisms shown ---")


def cmd_mechanism(entries: list[dict], query: str):
    """Look up a specific mechanism by name."""
    query_lower = query.lower().replace("_", " ").replace("-", " ")
    matches = [e for e in entries if query_lower in e["name"].lower().replace("-", " ")]

    if not matches:
        print(f"\nNo mechanism matching '{query}'. Try a partial name.")
        # Suggest close matches
        suggestions = [e["name"] for e in entries if any(w in e["name"].lower() for w in query_lower.split())]
        if suggestions:
            print("  Did you mean:")
            for s in suggestions[:5]:
                print(f"    - {s}")
        return

    for entry in matches:
        print_entry(entry)

    print(f"\n--- {len(matches)} match(es) ---")


def cmd_author(entries: list[dict], author: str):
    """Look up all mechanisms attributed to an author."""
    normalized = AUTHOR_ALIASES.get(author.lower(), author.title())
    matches = [e for e in entries if normalized in e["authors"]]

    if not matches:
        print(f"\nNo mechanisms found for author '{author}'.")
        print(f"  Available authors: {', '.join(sorted(AUTHOR_ALIASES.values()))}")
        return

    print(f"\nMechanisms attributed to {normalized} ({len(matches)} total):")

    # Sort: primary first, then moderate, then rare
    def author_priority(entry):
        # Check if this author is primary in the raw text
        raw = entry["authors_raw"].lower()
        idx = raw.find(normalized.lower())
        if idx == -1:
            return 2
        # Look for "primary" near the author name
        context = raw[idx:idx+100]
        if "primary" in context:
            return 0
        if "moderate" in context:
            return 1
        return 2

    matches.sort(key=author_priority)
    for entry in matches:
        print_entry(entry, verbose=False)

    print(f"\n--- {len(matches)} mechanisms for {normalized} ---")


def main():
    parser = argparse.ArgumentParser(
        description="Look up mechanisms from the Master Mechanism Atlas.",
        epilog="Examples:\n"
               "  python lookup.py --dials rimbaud=70,wilde=20,burroughs=10\n"
               "  python lookup.py --mechanism negative_space\n"
               "  python lookup.py --author bishop",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dials", help="Dial settings (e.g. rimbaud=70,wilde=20,burroughs=10)")
    group.add_argument("--mechanism", help="Mechanism name (partial match)")
    group.add_argument("--author", help="Author name")
    args = parser.parse_args()

    entries = parse_atlas()
    print(f"Loaded {len(entries)} mechanisms from Atlas.")

    if args.dials:
        cmd_dials(entries, args.dials)
    elif args.mechanism:
        cmd_mechanism(entries, args.mechanism)
    elif args.author:
        cmd_author(entries, args.author)


if __name__ == "__main__":
    main()
