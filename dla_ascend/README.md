# DLA ASCEND

DLA roadmap, PoC Plan, and PWS deliverables for Option Periods 2 & 3.

## Generators

| Script | Output | Themes |
|--------|--------|--------|
| `generate_dla_roadmap.py` | Gantt roadmap slide (.pptx) | dark, light |
| `generate_poc_plan_op2.py` | OP2 Proof of Concept Plan (.docx) | N/A |

## Commands

```bash
# Roadmap — dark or light
python3 dla_ascend/generate_dla_roadmap.py --theme dark
python3 dla_ascend/generate_dla_roadmap.py --theme light

# PoC Plan
python3 dla_ascend/generate_poc_plan_op2.py
```

## Utilities

- `fix_table_borders.py` — Fixes table border formatting in generated .docx files
- `gdrive_auth.py` — Google Drive authentication helper
- `upload_to_drive.py` — Upload generated files to Google Drive

## Drop Zone

Place PWS documents in `pws_dropoff/` for processing.

## Output

Generated files go to `dla_ascend/output/` (gitignored).
