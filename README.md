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

## Running Locally (Without Cursor)

You don't need Cursor to use the generators — they're standalone Python scripts.

### 1. Install Python

macOS:
```bash
# Check if Python 3 is installed
python3 --version

# If not, install via Xcode command-line tools (ships with Python 3)
xcode-select --install
```

Windows:
- Download from [python.org](https://www.python.org/downloads/) (check "Add to PATH" during install)

### 2. Set Up a Virtual Environment (Recommended)

```bash
cd scale-slide-generator

# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Edit and Run

Open `generate_deck.py` in any text editor, update the `DECK` dict with your content, then:

```bash
python3 generate_deck.py --theme dark
python3 generate_deck.py --theme light
```

Output files land in `output/`. Open them with PowerPoint, Keynote, or Google Slides.

---

## Working with Reference Documents

### Drop-off Workflow

If you have existing documents (PWS files, templates, prior presentations) you want the AI to reference when building slides, drop them into the project and tell Cursor where they are:

1. Place files anywhere in the repo (e.g., `templates/`, or create a folder like `references/`)
2. In Cursor Agent mode, tell it what you dropped and what to do:

```
I added our Q4 status report to templates/Q4_Status_Report.docx.
Extract the key metrics and milestones and build a 4-slide summary deck.
Generate in dark mode.
```

Cursor can read `.docx`, `.pptx`, `.pdf`, `.csv`, `.json`, and plain text files directly — no special setup needed.

### Supported File Types for Drop-off

| Type | Extensions | Notes |
|------|-----------|-------|
| Word | `.docx` | Full paragraph and table extraction |
| PowerPoint | `.pptx` | Slide text and structure |
| PDF | `.pdf` | Text extraction (not scanned images) |
| Data | `.csv`, `.json`, `.xlsx` | Structured data for tables and metrics |
| Text | `.txt`, `.md` | Plain text content |

---

## Integrating External Tools and Apps

For teams that want deeper integration beyond file drop-off, Cursor supports MCP (Model Context Protocol) servers that connect to external services directly.

### Google Drive Integration

Upload generated files to Google Drive without leaving Cursor:

1. Set environment variables (see `.env.example`):
   ```bash
   export GOOGLE_CLIENT_ID=your-client-id
   export GOOGLE_CLIENT_SECRET=your-client-secret
   ```
2. Run the one-time auth flow:
   ```bash
   python3 utils/gdrive_auth.py
   ```
3. Upload from Cursor Agent mode:
   ```
   Generate the deck in dark mode, then upload it to Google Drive.
   ```

For persistent Drive access, set up the [Google Drive MCP server](https://github.com/anthropics/model-context-protocol) in Cursor settings so the AI can browse, read, and write to Drive natively.

### Adding MCP Servers

MCP servers let Cursor interact with external tools (Slack, Jira, Confluence, email, databases, etc.) through the chat interface. To add one:

1. Open **Cursor Settings > MCP**
2. Add the server config (name, command, args)
3. Restart Cursor

Once connected, you can prompt across tools:

```
Pull the latest milestone dates from the Jira board, update the table slide, and regenerate the deck.
```

```
Read the exec summary from the Google Doc at [URL] and create a content slide from it.
```

See Cursor's [MCP documentation](https://docs.cursor.com/context/model-context-protocol) for setup instructions.

### Adding Python Packages

To extend the generators with additional capabilities (e.g., charts, image embedding, data fetching):

1. Install the package:
   ```bash
   pip install matplotlib  # example
   ```
2. Add it to `requirements.txt`
3. Ask Cursor to use it:
   ```
   Add a new "chart" layout that uses matplotlib to render a bar chart
   as an image and embed it in the slide. Here's the data: ...
   ```

---

## Custom Themes

To add a theme, extend the `THEMES` dict in `generate_deck.py`:

> *"Add a 'navy' theme with dark navy backgrounds, white text, and gold/teal accent colors"*

Or copy the `"dark"` entry, rename it, and adjust the RGB values. The `_BAR_PALETTE_*` lists control the cycling bar/accent colors used across phases and metric cards.
