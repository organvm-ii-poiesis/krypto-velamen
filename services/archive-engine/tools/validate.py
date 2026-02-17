#!/usr/bin/env python3
"""Validate a Field I fragment's YAML frontmatter and structure.

Checks required fields, dial ranges, recognized enum values, and
non-empty fragment section.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install PyYAML>=6.0")
    sys.exit(1)

REQUIRED_FIELDS = [
    "date", "slug", "status",
    "rimbaud_drift", "wilde_mask", "burroughs_control",
    "surface_story", "substrate_story", "mask_type", "signal_type",
    "surveillance_pressure", "plausible_deniability", "affect_cost",
]

DIAL_FIELDS = ["rimbaud_drift", "wilde_mask", "burroughs_control"]

VALID_STATUSES = {"draft", "revision", "final"}

VALID_MASK_TYPES = {
    "voyant_alibi", "aesthetic_alibi", "systems_metaphor",
    "genre_displacement", "confessional_redirect", "camp",
    "precision_as_concealment", "other",
}

VALID_SIGNAL_TYPES = {
    "sensory_surplus", "recognition_trigger", "structural_paranoia",
    "pronoun_drift", "negative_space", "overdetermined_detail", "other",
}


def extract_frontmatter(text: str) -> tuple[dict | None, str]:
    """Extract YAML frontmatter from markdown-fenced block."""
    # Match ```yaml ... ``` block
    match = re.search(r"```yaml\s*\n(.*?)```", text, re.DOTALL)
    if match:
        raw = match.group(1)
        # Strip comment-only lines from mechanisms list for cleaner parse
        cleaned = re.sub(r"^\s*-\s*#.*$", "", raw, flags=re.MULTILINE)
        try:
            data = yaml.safe_load(cleaned)
            return data, ""
        except yaml.YAMLError as e:
            return None, f"YAML parse error: {e}"
    return None, "No ```yaml``` frontmatter block found"


def validate(filepath: Path) -> list[tuple[str, bool, str]]:
    """Run all validation checks. Returns list of (check_name, passed, detail)."""
    results = []

    # Read file
    try:
        text = filepath.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [("file_exists", False, f"File not found: {filepath}")]

    results.append(("file_exists", True, str(filepath)))

    # Parse frontmatter
    data, err = extract_frontmatter(text)
    if data is None:
        results.append(("frontmatter_parse", False, err))
        return results
    results.append(("frontmatter_parse", True, "YAML parsed successfully"))

    # Required fields
    for field in REQUIRED_FIELDS:
        present = field in data
        results.append((f"field:{field}", present, "present" if present else "MISSING"))

    # Dial ranges (0-100)
    for dial in DIAL_FIELDS:
        if dial in data:
            val = data[dial]
            if isinstance(val, (int, float)) and 0 <= val <= 100:
                results.append((f"range:{dial}", True, f"{val} (0-100)"))
            else:
                results.append((f"range:{dial}", False, f"{val} — must be 0-100"))

    # Status enum
    if "status" in data:
        val = data["status"]
        ok = val in VALID_STATUSES
        results.append(("enum:status", ok, f"{val}" + ("" if ok else f" — expected one of {VALID_STATUSES}")))

    # Mask type enum
    if "mask_type" in data and data["mask_type"]:
        val = data["mask_type"]
        ok = val in VALID_MASK_TYPES
        results.append(("enum:mask_type", ok, f"{val}" + ("" if ok else f" — expected one of {VALID_MASK_TYPES}")))

    # Signal type enum
    if "signal_type" in data and data["signal_type"]:
        val = data["signal_type"]
        ok = val in VALID_SIGNAL_TYPES
        results.append(("enum:signal_type", ok, f"{val}" + ("" if ok else f" — expected one of {VALID_SIGNAL_TYPES}")))

    # Plausible deniability (1-5)
    if "plausible_deniability" in data and data["plausible_deniability"]:
        val = data["plausible_deniability"]
        try:
            num = int(val)
            ok = 1 <= num <= 5
            results.append(("range:plausible_deniability", ok, f"{num}" + ("" if ok else " — must be 1-5")))
        except (ValueError, TypeError):
            results.append(("range:plausible_deniability", False, f"{val} — must be integer 1-5"))

    # Fragment section non-empty
    frag_match = re.search(r"## The Fragment\s*\n\s*_Write here\._\s*\n(.*?)(?=\n---|\Z)", text, re.DOTALL)
    if frag_match:
        content = frag_match.group(1).strip()
        has_content = len(content) > 0
        results.append(("fragment_content", has_content, "has content" if has_content else "EMPTY — write your fragment"))
    else:
        # Check if there's any content after "## The Fragment" that isn't the placeholder
        alt_match = re.search(r"## The Fragment\s*\n(.*?)(?=\n---|\Z)", text, re.DOTALL)
        if alt_match:
            content = alt_match.group(1).replace("_Write here._", "").strip()
            has_content = len(content) > 0
            results.append(("fragment_content", has_content, "has content" if has_content else "EMPTY — write your fragment"))
        else:
            results.append(("fragment_content", False, "No '## The Fragment' section found"))

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate a Field I fragment's YAML frontmatter and structure.",
    )
    parser.add_argument("file", help="Path to the fragment markdown file")
    args = parser.parse_args()

    filepath = Path(args.file).resolve()
    results = validate(filepath)

    # Display results
    passed = sum(1 for _, ok, _ in results if ok)
    failed = sum(1 for _, ok, _ in results if not ok)
    total = len(results)

    print(f"\nValidating: {filepath}\n")
    for name, ok, detail in results:
        icon = "PASS" if ok else "FAIL"
        print(f"  [{icon}] {name}: {detail}")

    print(f"\n--- {passed}/{total} checks passed", end="")
    if failed:
        print(f", {failed} failed ---")
        sys.exit(1)
    else:
        print(" ---")


if __name__ == "__main__":
    main()
