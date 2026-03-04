# Scale Slide Generator

Generate branded PowerPoint decks from Python data structures. 13 slide layouts, dark + light themes, Scale styling, built-in QA pipeline.

## Quick Start

```bash
python3 generate_deck.py --theme dark
python3 generate_deck.py --theme light
```

## Layouts

| Layout | Purpose |
|--------|---------|
| `title` | Opening slide with title + subtitle |
| `section` | Section divider |
| `content` | Title + bullet list |
| `two_column` | Side-by-side comparison |
| `metrics` | KPI cards (2-8 items) |
| `table` | Data table with proportional columns |
| `gantt` | Roadmap with task bars and milestones |
| `image` | Full-width image with optional caption |
| `quote` | Centered quotation with attribution |
| `fact` | Single dominant stat/number callout |
| `process` | Horizontal chevron flow (3-6 steps) |
| `timeline` | Event-based horizontal timeline |
| `image_content` | Image + bullets side by side |

## Creating a Deck

Create a script in `output/`:

```python
from scaledeck import main

DECK = {
    "filename": "My_Deck",
    "slides": [
        {"layout": "title", "title": "My Presentation", "subtitle": "Scale AI"},
        {"layout": "fact", "value": "99.7%", "label": "Uptime", "detail": "Exceeds SLA by 50bps"},
        {"layout": "content", "title": "Key points", "bullets": ["Point A", "Point B"]},
    ],
}

main(theme_name="dark", deck=DECK)
```

## Per-Slide Style Overrides

Any slide can override theme colors:

```python
{"layout": "section", "title": "Special Section", "background_color": "1A1A2E", "accent_color": "E94560"}
```

## QA Pipeline

The generator runs automatic quality checks after every build:
- Shapes within slide bounds
- Font sizes above 7pt
- Speaker notes present
- Insight-led titles (not topic labels)
- Layout variety (warns on repetition)

## Project Structure

```
scaledeck/          Core package (themes, branding, layouts, validation, QA)
generate_deck.py    CLI wrapper
output/             Generated decks + standalone scripts
templates/          Source .pptx brand templates
assets/             Backgrounds and logos
utils/              Google Drive upload helpers
tests/              Gantt overlap tests
mcp_server.py       MCP server for Cursor/Claude Code integration
```

## Requirements

```
python-pptx>=1.0.0
python-docx>=1.1.0
Pillow>=9.0.0
```
