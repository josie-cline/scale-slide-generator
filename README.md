# Scale Slide Generator

Generate styled PowerPoint decks from a simple data definition. Supports multiple slide layouts — title, section, content, two-column, metrics, table, and gantt — all rendered in Scale styling with dark and light themes.

Designed to be used with [Cursor](https://cursor.com): describe what you need in natural language and get a publication-ready `.pptx` in seconds.

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/josie-cline/scale-slide-generator.git
cd scale-slide-generator

# 2. Install
pip install -r requirements.txt

# 3. Generate
python3 generate_deck.py --theme dark
open output/Example_Deck_dark.pptx
```

---

## Slide Layouts

| Layout | What it renders |
|--------|----------------|
| `title` | Full-slide title with subtitle and accent bar |
| `section` | Section divider with accent background |
| `content` | Title + bullet points |
| `two_column` | Side-by-side comparison with headers |
| `metrics` | KPI cards with values, labels, and detail text |
| `table` | Header row + data rows, styled and alternating |
| `gantt` | Gantt-style roadmap with bars, milestones, and due dates |

Both `--theme dark` and `--theme light` are supported. Pass the flag when running:

```bash
python3 generate_deck.py --theme dark
python3 generate_deck.py --theme light
```

---

## How It Works

Edit the `DECK` definition at the top of `generate_deck.py`. Each slide is a dictionary with a `layout` key and layout-specific content:

```python
DECK = {
    "filename": "My_Presentation",
    "slides": [
        {"layout": "title", "title": "My Presentation", "subtitle": "Scale AI"},
        {"layout": "content", "title": "Agenda", "bullets": ["Item 1", "Item 2"]},
        {"layout": "metrics", "title": "KPIs", "metrics": [
            {"label": "Users", "value": "500+", "detail": "+20% MoM"},
        ]},
    ],
}
```

Run the script and the full deck is generated. Or let Cursor do it — just describe your presentation in the chat.

---

## Using with Cursor

1. **Open in Cursor** — Clone this repo and open the folder
2. **Ask mode** — Explore layouts, plan your deck
   - *"What slide layouts are available?"*
   - *"I need a 5-slide deck for a program review. What should it include?"*
3. **Agent mode** — Describe your deck and let Cursor build it
   - *"Create a deck called 'Q1 Review' with a title slide, two content slides, a metrics slide, and a table"*
   - *"Generate in both dark and light"*
4. **Review** — Open the output `.pptx`

See [`demo/WALKTHROUGH.md`](demo/WALKTHROUGH.md) for a complete step-by-step guide.

---

## Status Reports

For Word document generation (e.g., monthly status reports):

```bash
python3 generate_report.py --inspect     # see template structure
python3 generate_report.py               # generate from template
```

Place your `.docx` template in `templates/`, then update the data mappings in `generate_report.py`.

---

## Project Structure

```
scale-slide-generator/
├── generate_deck.py         # Main slide deck generator
├── generate_report.py       # Status report generator (.docx)
├── requirements.txt         # python-pptx, python-docx
├── .cursor/rules/           # Cursor AI workspace context
├── demo/WALKTHROUGH.md      # Cradle-to-grave demo guide
├── templates/               # Source .docx templates
├── output/                  # Generated files (gitignored)
├── utils/                   # Google Drive upload, helpers
└── examples/                # Reference implementations
```

---

## Custom Themes

To add a theme, extend the `THEMES` dict in `generate_deck.py`:

> *"Add a 'navy' theme with dark navy backgrounds, white text, and gold/teal accent colors"*

Or copy the `"dark"` entry, rename it, and adjust the RGB values. The `_BAR_PALETTE_*` lists control the cycling bar/accent colors used across phases and metric cards.
