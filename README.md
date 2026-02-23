# Scale Slide Generator

Prompt-driven slide and document generation for Scale AI programs. Describe what you need in natural language inside [Cursor](https://cursor.com); get publication-ready PowerPoint and Word artifacts in seconds.

---

## What It Does

| Generator | Command | Output |
|-----------|---------|--------|
| **Roadmap** | `python3 generate_roadmap.py --theme dark` | Gantt-style roadmap slide (.pptx) |
| **Status Report** | `python3 generate_report.py` | Monthly status report (.docx) |

Both generators support `--theme dark` (default) and `--theme light`.

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/josie-cline/scale-slide-generator.git
cd scale-slide-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate a roadmap
python3 generate_roadmap.py --theme dark
open output/Program_Name_Roadmap_dark.pptx
```

---

## Using with Cursor (Recommended)

This repo is designed to be used inside [Cursor IDE](https://cursor.com) with AI assistance. The `.cursor/rules/` directory provides workspace context so the AI understands the project automatically.

### Workflow

1. **Open in Cursor** — Clone this repo and open the folder
2. **Ask mode** — Explore and plan before generating
   - *"What generators are available and how do I configure them?"*
   - *"I need a roadmap for a 6-month program with 4 phases. What should I update?"*
3. **Agent mode** — Describe what you need
   - *"Set up the roadmap for my program called Thunderbolt. Here are the tasks: ..."*
   - *"Generate the roadmap in both dark and light mode"*
4. **Review** — Open the output PPTX and deliver

See [`demo/WALKTHROUGH.md`](demo/WALKTHROUGH.md) for a complete step-by-step guide.

---

## Customizing for Your Program

### Roadmap (`generate_roadmap.py`)

Edit the data section at the top of the file (or let Cursor do it):

- **`PROGRAM`** — Name, subtitle, title, period text, footer
- **`QUARTERS`** / **`MONTHS`** — Timeline labels
- **`PHASES`** — Phase names (each gets a unique bar color)
- **`TASKS`** — Task list with phase, name, start/end month, milestone flag, due date

### Status Report (`generate_report.py`)

1. Place your `.docx` template in `templates/`
2. Run `python3 generate_report.py --inspect` to see paragraph and table indices
3. Update `PARAGRAPH_UPDATES` and `TABLE_UPDATES` with your content
4. Run `python3 generate_report.py`

Or just tell Cursor: *"Update the status report for reporting period X with these highlights: ..."*

---

## Project Structure

```
scale-slide-generator/
├── generate_roadmap.py      # Roadmap slide generator (dark/light)
├── generate_report.py       # Status report generator
├── requirements.txt         # python-pptx, python-docx
├── .cursor/rules/           # Cursor AI workspace context
├── demo/WALKTHROUGH.md      # Cradle-to-grave demo guide
├── templates/               # Source .docx templates
├── output/                  # Generated files (gitignored)
├── utils/                   # Google Drive upload, helpers
└── examples/                # Program-specific reference implementations
```

---

## Adding Custom Themes

The `THEMES` dict and `_BAR_PALETTE_*` lists in `generate_roadmap.py` control all colors. To add a custom theme, tell Cursor:

> *"Add a 'navy' theme with dark navy headers, white text, and gold/teal/coral bar colors"*

Or copy the `"dark"` entry in `THEMES`, rename it, and adjust the RGB values.
