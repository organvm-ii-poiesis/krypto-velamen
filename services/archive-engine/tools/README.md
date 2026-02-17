# QV33R Encoding Engine — Tools

Three CLI tools for working with the QV33R encoding schema. All use Python 3.10+ and PyYAML.

## Setup

```bash
pip install -r tools/requirements.txt
```

PyYAML is also available via Anaconda (`/opt/anaconda3/`).

---

## scaffold.py — Create a New Fragment

Generates a dated fragment file from the template with pre-filled dial values.

```bash
# Using a preset
python tools/scaffold.py --slug "city-after-rain" --preset confessional-whisper

# Interactive mode (prompts for all values)
python tools/scaffold.py --slug "city-after-rain" --interactive

# Bare (empty dials, fill in manually)
python tools/scaffold.py --slug "city-after-rain"
```

**Output**: `drafts/YYYY-MM-DD-{slug}.md`

**Available presets**:
| Preset | R | W | B | Texture |
|--------|---|---|---|---------|
| `confessional-whisper` | 70 | 20 | 10 | Sensory, intimate, fragmented |
| `defensive-wit` | 10 | 80 | 30 | Sharp, social, performative |
| `systems-dread` | 20 | 15 | 85 | Clinical, procedural, uneasy |
| `bright-surface-dark-water` | 40 | 60 | 20 | Polished, warm, troubled |
| `surveillance-fugue` | 50 | 10 | 60 | Sensory but anxious |
| `archive-grief` | 60 | 30 | 30 | Elegiac, layered |

---

## validate.py — Check a Fragment

Validates YAML frontmatter, field completeness, dial ranges, and fragment content.

```bash
python tools/validate.py drafts/2026-02-17-city-after-rain.md
```

**Checks**:
- All required fields present (13 fields)
- Dial values 0-100
- `status` is one of: draft, revision, final
- `mask_type` is a recognized value
- `signal_type` is a recognized value
- `plausible_deniability` is 1-5
- Fragment section is non-empty

**Exit code**: 0 if all pass, 1 if any fail.

---

## lookup.py — Query the Mechanism Atlas

Three query modes for looking up mechanisms from `research/synthesis/MECHANISM-ATLAS.md`.

```bash
# By dial settings — which mechanisms activate here?
python tools/lookup.py --dials rimbaud=70,wilde=20,burroughs=10

# By mechanism name (partial match)
python tools/lookup.py --mechanism "negative_space"

# By author — all mechanisms attributed to this author
python tools/lookup.py --author bishop
```

**Dial query scoring**: Mechanisms are scored by how well their activation profile (primary/moderate/rare for each dial) matches your settings. Higher dial values weight "primary" activations more heavily.

---

## Workflow

1. `scaffold.py --slug "my-piece" --preset confessional-whisper` → creates fragment file
2. Open the file, write the fragment
3. `validate.py drafts/2026-02-17-my-piece.md` → check completeness
4. `lookup.py --dials rimbaud=70,wilde=20,burroughs=10` → discover mechanisms to try
