#!/usr/bin/env python3
"""
QV33R Poiesis Orchestrator v3.0 — The Integrated Workspace Command Center.
Integrated with CHTHON-ONEIROS (Field II) logic.
"""

import argparse
import os
import re
import sys
import random
from datetime import date
from pathlib import Path

# Try to import rich for enhanced UI, otherwise fallback to standard print
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.text import Text
    from rich import print as rprint
    console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    rprint = print  # Fallback
    console = None

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install PyYAML>=6.0")
    sys.exit(1)

# --- Configuration ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = PROJECT_ROOT / "drafts"
RESEARCH_DIR = PROJECT_ROOT / "research"
ATLAS_PATH = RESEARCH_DIR / "synthesis" / "MECHANISM-ATLAS.md"

# Polarity Constants
POLARITY_A = "concealment"
POLARITY_B = "visibility"

# Author Dials
DIALS_A = ["rimbaud_drift", "wilde_mask", "burroughs_control"]
DIALS_B = ["lorde_voice", "arenas_scream", "acker_piracy"]

# Presets
PRESETS = {
    "confessional-whisper": {"mode": POLARITY_A, "rimbaud_drift": 70, "wilde_mask": 20, "burroughs_control": 10, "desc": "Sensory, intimate, fragmented."},
    "defensive-wit": {"mode": POLARITY_A, "rimbaud_drift": 10, "wilde_mask": 80, "burroughs_control": 30, "desc": "Sharp, social, performative."},
    "systems-dread": {"mode": POLARITY_A, "rimbaud_drift": 20, "wilde_mask": 15, "burroughs_control": 85, "desc": "Clinical, procedural, uneasy."},
    "bright-surface-dark-water": {"mode": POLARITY_A, "rimbaud_drift": 40, "wilde_mask": 60, "burroughs_control": 20, "desc": "Polished, warm, sociable."},
    "surveillance-fugue": {"mode": POLARITY_A, "rimbaud_drift": 50, "wilde_mask": 10, "burroughs_control": 60, "desc": "Sensory but anxious."},
    "archive-grief": {"mode": POLARITY_A, "rimbaud_drift": 60, "wilde_mask": 30, "burroughs_control": 30, "desc": "Elegiac, layered."},
    "mythological-depth": {"mode": POLARITY_B, "lorde_voice": 80, "arenas_scream": 20, "acker_piracy": 10, "desc": "Resilient, cosmological, biomythographical."},
    "sacrificial-scream": {"mode": POLARITY_B, "lorde_voice": 20, "arenas_scream": 90, "acker_piracy": 30, "desc": "Extreme exposure, political urgency."},
    "pirated-self": {"mode": POLARITY_B, "lorde_voice": 10, "arenas_scream": 30, "acker_piracy": 85, "desc": "Fragmented, stolen, terminal collapse."},
}

# --- UI Helpers ---

def ui_header(text):
    if HAS_RICH:
        console.print(Panel(f"[bold cyan]{text}[/bold cyan]", expand=False))
    else:
        print(f"\n=== {text} ===")

def digital_display(text, header="SYSTEM LOG"):
    if HAS_RICH:
        p = Panel(
            Text(text, style="green"),
            title=f"[bold white]{header}[/bold white]",
            border_style="green",
            padding=(1, 2)
        )
        console.print(p)
    else:
        print(f"[{header}]")
        print(text)

# --- Logic ---

def get_frontmatter(text):
    match = re.search(r"```yaml\s*\n(.*?)```", text, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None

def cmd_dashboard():
    ui_header("QV33R POIESIS DASHBOARD v3.0")
    total_files = len(list(PROJECT_ROOT.glob("**/*.md")))
    research_files = len(list(RESEARCH_DIR.glob("*.md")))
    draft_files = len(list(DRAFTS_DIR.glob("*.md")))
    
    if HAS_RICH:
        stats = Table(title="Repository Statistics")
        stats.add_column("Category", style="magenta")
        stats.add_column("Count", justify="right", style="green")
        stats.add_row("Total Markdown Files", str(total_files))
        stats.add_row("Research Reports", str(research_files))
        stats.add_row("Creative Fragments", str(draft_files))
        console.print(stats)
    else:
        print(f"Stats: {total_files} files, {research_files} research, {draft_files} drafts.")

def cmd_scaffold(args):
    ui_header(f"SCAFFOLDING FRAGMENT: {args.slug}")
    preset = PRESETS.get(args.preset)
    mode = preset["mode"] if preset else (POLARITY_B if args.visibility else POLARITY_A)
    version = args.version or 0.1
    
    dials = {}
    if preset:
        dials = {k: v for k, v in preset.items() if k not in ["mode", "desc"]}
    else:
        active_dials = DIALS_B if mode == POLARITY_B else DIALS_A
        for d in active_dials: dials[d] = 0
            
    today = date.today().isoformat()
    dial_block = "\n".join([f"{k}: {v}" for k, v in dials.items()])
    
    frontmatter = f"""```yaml
# --- Fragment Metadata ---
date: {today}
slug: "{args.slug}"
version: {version}
status: draft
mode: {mode}

# --- Author Dials (0-100) ---
{dial_block}

# --- Encoding Schema (9 variables) ---
surface_story: ""
substrate_story: ""
mask_type: ""
signal_type: ""
surveillance_pressure: ""
plausible_deniability: ""
affect_cost: ""
multimedia_link: ""
audience_projection: ""

# --- Craft Mechanisms Used ---
mechanisms: []
```"""

    content = f"# Fragment — Field I: Present Waking\n\nMode: **{mode.title()}**\n\n---\n\n{frontmatter}\n\n---\n\n## Surface Notes\n_What axis of identity or cover story is visible?_\n\n---\n\n## Substrate Notes\n_What mythological, emotional, or hidden plot lies beneath?_\n\n---\n\n## The Fragment\n_Write here._\n"
    
    out_path = DRAFTS_DIR / f"{today}-{args.slug}.md"
    out_path.write_text(content, encoding="utf-8")
    rprint(f"[green]Created: {out_path} (v{version})[/green]")

def cmd_validate(args):
    ui_header(f"VALIDATING: {args.file}")
    filepath = Path(args.file)
    if not filepath.exists(): return
    text = filepath.read_text(encoding="utf-8")
    data = get_frontmatter(text)
    if not data:
        rprint("[bold red]Fail: No valid YAML found.[/bold red]")
        return

    errors = []
    required = ["date", "slug", "version", "status", "mode", "surface_story", "substrate_story", "multimedia_link", "audience_projection"]
    for f in required:
        if f not in data: errors.append(f"Missing field: {f}")
    
    if errors:
        for e in errors: rprint(f"  [red]✖[/red] {e}")
        sys.exit(1)
    else:
        rprint("[bold green]✔ v{0} integrity verified.[/bold green]".format(data.get('version', '?.?')))

def cmd_display(args):
    filepath = Path(args.file)
    if not filepath.exists(): return
    text = filepath.read_text(encoding="utf-8")
    data = get_frontmatter(text)
    
    # Extract the fragment text
    frag_match = re.search(r"## The Fragment\s*\n(.*?)(?=\n---|\Z)", text, re.DOTALL)
    content = frag_match.group(1).strip() if frag_match else "EMPTY"
    content = content.replace("_Write here._", "").strip()
    
    header = f"{data.get('mode', 'system').upper()} // {data.get('slug', 'unnamed').upper()} // v{data.get('version', '0.0')}"
    digital_display(content, header=header)

def cmd_flip(args):
    filepath = Path(args.file)
    if not filepath.exists(): return
    text = filepath.read_text(encoding="utf-8")
    data = get_frontmatter(text)
    
    ui_header(f"FLIP SUGGESTION: {data.get('slug')}")
    
    substrate = data.get('substrate_story', 'Unknown Desire')
    surface = data.get('surface_story', 'Mundane Reality')
    
    # Logic: suggest mapping substrate onto a new, distorted surface
    distortions = ["Glitch", "Nightmare", "Archetypal", "Void", "Phantasm"]
    new_surface = f"{random.choice(distortions)} version of {surface}"
    
    rprint(f"[bold yellow]Field I Surface:[/bold yellow] {surface}")
    rprint(f"[bold red]Field I Substrate:[/bold red] {substrate}")
    rprint("-" * 20)
    rprint(f"[bold cyan]Suggested Field II Transformation (The Flip):[/bold cyan]")
    rprint(f"  [bold]New Surface (Dream):[/bold] {new_surface}")
    rprint(f"  [bold]New Substrate (Shadow):[/bold] Primal recursion of '{substrate}'")
    rprint(f"  [bold]Recommended Version:[/bold] v1.0 (The Descent)")
    rprint(f"  [bold]Dial Shift:[/bold] Turn up [magenta]$PHANTASM_OSCILLATION[/magenta]")

def main():
    parser = argparse.ArgumentParser(description="Poiesis Orchestrator v3.0")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    subparsers.add_parser("dashboard", help="Project status")
    
    scaffold_p = subparsers.add_parser("scaffold", help="Create new fragment")
    scaffold_p.add_argument("--slug", required=True)
    scaffold_p.add_argument("--preset", choices=sorted(PRESETS.keys()))
    scaffold_p.add_argument("--visibility", action="store_true")
    scaffold_p.add_argument("--version", type=float, help="Decimal version (default 0.1)")

    validate_p = subparsers.add_parser("validate", help="Check integrity")
    validate_p.add_argument("file")

    display_p = subparsers.add_parser("display", help="Digital-First rendering")
    display_p.add_argument("file")

    flip_p = subparsers.add_parser("flip", help="Suggest Field II transformation")
    flip_p.add_argument("file")

    args = parser.parse_args()

    if args.command == "dashboard": cmd_dashboard()
    elif args.command == "scaffold": cmd_scaffold(args)
    elif args.command == "validate": cmd_validate(args)
    elif args.command == "display": cmd_display(args)
    elif args.command == "flip": cmd_flip(args)
    else: parser.print_help()

if __name__ == "__main__":
    main()
