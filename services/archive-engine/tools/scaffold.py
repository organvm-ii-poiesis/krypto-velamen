#!/usr/bin/env python3
"""Scaffold a new Field I fragment from the QV33R template.

Reads drafts/TEMPLATE.md, pre-fills dial values from a preset or via
interactive prompts, and writes a dated fragment file to drafts/.
"""

import argparse
import os
import sys
from datetime import date
from pathlib import Path

# Resolve project root relative to this script
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "drafts" / "TEMPLATE.md"
DRAFTS_DIR = PROJECT_ROOT / "drafts"

# Six preset configurations from ENCODING-WORKSHEET.md (lines 157-203)
PRESETS = {
    "confessional-whisper": {
        "rimbaud_drift": 70,
        "wilde_mask": 20,
        "burroughs_control": 10,
        "description": "Sensory, intimate, fragmented. Language that feels like remembering a body.",
    },
    "defensive-wit": {
        "rimbaud_drift": 10,
        "wilde_mask": 80,
        "burroughs_control": 30,
        "description": "Sharp, social, performative. What is mocked reveals what is protected.",
    },
    "systems-dread": {
        "rimbaud_drift": 20,
        "wilde_mask": 15,
        "burroughs_control": 85,
        "description": "Clinical, procedural, uneasy. Every human feeling translated into systems.",
    },
    "bright-surface-dark-water": {
        "rimbaud_drift": 40,
        "wilde_mask": 60,
        "burroughs_control": 20,
        "description": "Polished, warm, sociable — but something is wrong underneath.",
    },
    "surveillance-fugue": {
        "rimbaud_drift": 50,
        "wilde_mask": 10,
        "burroughs_control": 60,
        "description": "Sensory but anxious. Intimacy only in stolen moments between checks.",
    },
    "archive-grief": {
        "rimbaud_drift": 60,
        "wilde_mask": 30,
        "burroughs_control": 30,
        "description": "Elegiac, layered, historically aware. The past accessed only in pieces.",
    },
}

MASK_TYPES = [
    "voyant_alibi", "aesthetic_alibi", "systems_metaphor",
    "genre_displacement", "confessional_redirect", "camp", "precision_as_concealment", "other",
]

SIGNAL_TYPES = [
    "sensory_surplus", "recognition_trigger", "structural_paranoia",
    "pronoun_drift", "negative_space", "overdetermined_detail", "other",
]


def prompt_dial(name: str, description: str) -> int:
    """Interactively prompt for a dial value 0-100."""
    while True:
        raw = input(f"  {name} (0-100) [{description}]: ").strip()
        if not raw:
            return 0
        try:
            val = int(raw)
            if 0 <= val <= 100:
                return val
            print("    Must be 0-100.")
        except ValueError:
            print("    Enter a number.")


def prompt_choice(name: str, options: list[str]) -> str:
    """Interactively prompt for a choice from a list."""
    print(f"  {name} — options: {', '.join(options)}")
    raw = input(f"  > ").strip()
    return raw if raw else ""


def prompt_text(name: str) -> str:
    """Interactively prompt for free text."""
    return input(f"  {name}: ").strip()


def build_frontmatter(slug: str, dials: dict, interactive: bool = False) -> str:
    """Build YAML frontmatter block."""
    today = date.today().isoformat()

    if interactive:
        print("\n--- Encoding Schema (7 variables) ---")
        surface_story = prompt_text("$SURFACE_STORY (what does the default reader see?)")
        substrate_story = prompt_text("$SUBSTRATE_STORY (what does the queer-attuned reader detect?)")
        mask_type = prompt_choice("$MASK_TYPE", MASK_TYPES)
        signal_type = prompt_choice("$SIGNAL_TYPE", SIGNAL_TYPES)
        surveillance = prompt_text("$SURVEILLANCE_PRESSURE (who are you hiding from?)")
        deniability = prompt_text("$PLAUSIBLE_DENIABILITY (1-5)")
        affect_cost = prompt_text("$AFFECT_COST (what does concealment do to the feeling?)")
    else:
        surface_story = ""
        substrate_story = ""
        mask_type = ""
        signal_type = ""
        surveillance = ""
        deniability = ""
        affect_cost = ""

    return f"""```yaml
# --- Fragment Metadata ---
date: {today}
slug: "{slug}"
status: draft

# --- Author Dials (0-100) ---
rimbaud_drift: {dials['rimbaud_drift']}       # desire as weather: lyric fracture, sensory overload
wilde_mask: {dials['wilde_mask']}           # truth as performance: wit, ornament, paradox
burroughs_control: {dials['burroughs_control']}    # desire under surveillance: systems, paranoia, mechanism

# --- Encoding Schema (7 variables) ---
surface_story: "{surface_story}"
substrate_story: "{substrate_story}"
mask_type: "{mask_type}"
signal_type: "{signal_type}"
surveillance_pressure: "{surveillance}"
plausible_deniability: "{deniability}"
affect_cost: "{affect_cost}"

# --- Craft Mechanisms Used (check all that apply) ---
mechanisms:
  - # pronoun_drift
  - # negative_space
  - # overdetermined_innocence
  - # public_mask_private_voice
  - # camp_as_encryption
  - # surveillance_as_entity
```"""


def build_fragment(slug: str, dials: dict, preset_name: str | None, interactive: bool) -> str:
    """Assemble the full fragment file content."""
    frontmatter = build_frontmatter(slug, dials, interactive)
    preset_note = f"Preset: **{preset_name}** — {PRESETS[preset_name]['description']}" if preset_name else ""

    return f"""# Fragment — Field I: Present Waking

{preset_note}

---

{frontmatter}

---

## Surface Notes

_What is this piece about on its face? What genre, form, or occasion justifies it?_



---

## Substrate Notes

_What is the real emotional plot? Who is the desire aimed at? What is the danger? What is the cost of being caught?_



---

## The Fragment

_Write here._



---

## Encoding Self-Check

1. **Two-channel test**: Can a straight colleague read this and find it complete? Can a queer reader find more?
2. **Mask integrity**: Does the surface story hold on its own?
3. **Signal presence**: Is there at least one moment where the substrate leaks through?
4. **Deniability check**: If someone hostile asked "what is this about?" — does your answer hold?
5. **Affect cost audit**: What feeling did the concealment distort? That distortion is the piece's real material.
6. **Dial consistency**: Do the dial settings match what you actually wrote?
7. **Safety test**: If it feels safe to post, it doesn't belong in Field I yet.
"""


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new Field I fragment from the QV33R template.",
        epilog="Presets: " + ", ".join(sorted(PRESETS.keys())),
    )
    parser.add_argument("--slug", required=True, help="URL-friendly name (e.g. 'city-after-rain')")
    parser.add_argument(
        "--preset",
        choices=sorted(PRESETS.keys()),
        help="Pre-fill dials from a named preset",
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Prompt for encoding schema values interactively",
    )
    args = parser.parse_args()

    # Resolve dials
    if args.preset:
        preset = PRESETS[args.preset]
        dials = {k: preset[k] for k in ("rimbaud_drift", "wilde_mask", "burroughs_control")}
        print(f"Using preset '{args.preset}': {preset['description']}")
    elif args.interactive:
        print("\n--- Author Dials ---")
        dials = {
            "rimbaud_drift": prompt_dial("rimbaud_drift", "desire as weather"),
            "wilde_mask": prompt_dial("wilde_mask", "truth as performance"),
            "burroughs_control": prompt_dial("burroughs_control", "desire under surveillance"),
        }
    else:
        dials = {"rimbaud_drift": 0, "wilde_mask": 0, "burroughs_control": 0}

    # Build and write
    content = build_fragment(args.slug, dials, args.preset if args.preset else None, args.interactive)
    today = date.today().isoformat()
    out_path = DRAFTS_DIR / f"{today}-{args.slug}.md"

    out_path.write_text(content, encoding="utf-8")
    print(f"Created: {out_path}")


if __name__ == "__main__":
    main()
