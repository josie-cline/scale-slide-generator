# Scale Slide Generator

Prompt-driven slide and document generation for Scale AI government programs. Describe what you need in natural language inside [Cursor](https://cursor.com); get publication-ready PowerPoint and Word artifacts in seconds.

## What It Does

| Generator | Command | Output |
|-----------|---------|--------|
| VoF Roadmap | `python3 vof/generate_vof_roadmap.py --theme dark` | Gantt-style roadmap slide (OP2 & OP3) |
| VoF MSR | `python3 vof/generate_vof_msr.py` | Monthly status report (.docx) |
| DLA Roadmap | `python3 dla_ascend/generate_dla_roadmap.py --theme dark` | Gantt-style roadmap slide (OP2 & OP3) |
| DLA PoC Plan | `python3 dla_ascend/generate_poc_plan_op2.py` | Proof of Concept plan (.docx) |

Both roadmap generators support `--theme dark` (default) and `--theme light`.

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/josie-cline/scale-slide-generator.git
cd scale-slide-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate a roadmap
python3 vof/generate_vof_roadmap.py --theme dark
open vof/output/VoF_Roadmap_OP2_OP3_dark.pptx
```

## Using with Cursor (Recommended)

This repo is designed to be used inside Cursor IDE with AI assistance. The `.cursor/rules/` directory provides workspace context so the AI understands the project structure, available generators, and how to use them.

### Workflow

1. **Open in Cursor** — Clone this repo and open the folder in Cursor
2. **Ask mode** — Ask questions to explore the project and plan your task
   - *"What generators are available?"*
   - *"I need to update the VoF roadmap with new milestones. What should I change?"*
3. **Agent mode** — Describe what you need and let the AI generate it
   - *"Generate the VoF roadmap in dark mode"*
   - *"Add a new task 'Security Audit' under Platform Sustainment from April to May, then regenerate both themes"*
4. **Review** — Open the output file and verify

See [`demo/WALKTHROUGH.md`](demo/WALKTHROUGH.md) for a complete step-by-step guide.

## Project Structure

```
scale-slide-generator/
├── README.md
├── requirements.txt
├── .cursor/rules/           # Cursor AI workspace context
├── demo/WALKTHROUGH.md      # Cradle-to-grave demo guide
├── vof/                     # Valley of Fire generators
│   ├── generate_vof_roadmap.py
│   ├── generate_vof_msr.py
│   └── output/              # Generated files (gitignored)
├── dla_ascend/              # DLA ASCEND generators
│   ├── generate_dla_roadmap.py
│   ├── generate_poc_plan_op2.py
│   ├── pws_dropoff/         # Drop zone for PWS docs
│   └── output/              # Generated files (gitignored)
└── scale_ai_disa/           # Source templates
    └── ScaleAi DISA - JAN 2026 MSR.docx
```

## Adding New Programs

Each generator is a standalone Python script. To add a new program:

1. Create a new folder (e.g., `new_program/`)
2. Copy an existing generator as a starting point
3. Update the `TASKS`, `MONTHS`, and `THEMES` dictionaries
4. Run it: `python3 new_program/generate_roadmap.py --theme dark`

The `THEMES` dictionary in each generator makes it straightforward to add custom color schemes beyond dark and light.
