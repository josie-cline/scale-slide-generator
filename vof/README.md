# VoF (Valley of Fire)

Valley of Fire monthly status reports and OP2/OP3 roadmap generation.

## Generators

| Script | Output | Themes |
|--------|--------|--------|
| `generate_vof_roadmap.py` | Gantt roadmap slide (.pptx) | dark, light |
| `generate_vof_msr.py` | Monthly status report (.docx) | N/A |

## Commands

```bash
# Roadmap — dark or light
python3 vof/generate_vof_roadmap.py --theme dark
python3 vof/generate_vof_roadmap.py --theme light

# Monthly status report (uses template from scale_ai_disa/)
python3 vof/generate_vof_msr.py
```

## Output

Generated files go to `vof/output/` (gitignored).
