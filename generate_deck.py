#!/usr/bin/env python3
"""
Generate a styled PowerPoint deck for any Scale AI presentation.

Supports multiple slide layouts — title, section, content, two-column,
metrics, table, and gantt — all rendered in Scale styling with dark
and light themes.

Usage:
    python3 generate_deck.py                # dark theme (default)
    python3 generate_deck.py --theme light

Customization:
    Edit the DECK definition below, or ask Cursor:

        "Build me a deck with a title slide, 3 content slides, and a
         metrics slide. Here's the content: ..."
"""
import argparse
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR


# ═══════════════════════════════════════════════════════════════════════════
# DECK DEFINITION — Edit this section for your presentation
# ═══════════════════════════════════════════════════════════════════════════

DECK = {
    "filename": "Example_Deck",
    "slides": [
        # ── Title slide ──────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Quarterly Business Review",
            "subtitle": "Scale AI · Q1 2026",
        },

        # ── Section divider ──────────────────────────────────────────
        {
            "layout": "section",
            "title": "Executive Summary",
        },

        # ── Content slide (title + bullets) ──────────────────────────
        {
            "layout": "content",
            "title": "Key Highlights",
            "bullets": [
                "Deployed platform to production environment",
                "Completed 6 of 6 planned workflow applications",
                "User adoption reached 200+ accounts",
                "Achieved 99.97% platform uptime for the quarter",
            ],
        },

        # ── Two-column comparison ────────────────────────────────────
        {
            "layout": "two_column",
            "title": "Impact: Before & After",
            "left_title": "Manual Process",
            "left_bullets": [
                "3+ hours per report",
                "Inconsistent formatting",
                "Error-prone data entry",
                "Single output per cycle",
            ],
            "right_title": "With Scale Tooling",
            "right_bullets": [
                "Under 30 seconds",
                "Consistent Scale styling",
                "Data-driven generation",
                "Dark + light themes instantly",
            ],
        },

        # ── Metrics / KPI cards ──────────────────────────────────────
        {
            "layout": "metrics",
            "title": "Key Performance Indicators",
            "metrics": [
                {"label": "Active Users", "value": "200+", "detail": "+45% QoQ"},
                {"label": "Applications", "value": "9", "detail": "6 in v1 production"},
                {"label": "Uptime", "value": "99.97%", "detail": "SLA target: 99.5%"},
                {"label": "Avg Response", "value": "< 2s", "detail": "P95 latency"},
            ],
        },

        # ── Table slide ──────────────────────────────────────────────
        {
            "layout": "table",
            "title": "Deliverables Tracker",
            "headers": ["Deliverable", "Owner", "Status", "Due Date"],
            "rows": [
                ["Platform deployment", "Engineering", "Complete", "15 Jan 2026"],
                ["Data integration", "Data Team", "In Progress", "15 Apr 2026"],
                ["User training", "Field Ops", "Planned", "1 May 2026"],
                ["Documentation package", "PM", "In Progress", "30 Apr 2026"],
            ],
        },

        # ── Gantt / roadmap slide ────────────────────────────────────
        {
            "layout": "gantt",
            "title": "Project Roadmap",
            "subtitle": "Scale AI · Option Period 2 & 3",
            "quarters": ["Q1 2026", "Q2 2026", "Q3 2026"],
            "months": ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
            "phases": [
                "Development",
                "Integration",
                "Sustainment",
                "Deliverables",
            ],
            "tasks": [
                ("Development", "Application refinement", 0, 1, False, "1 Mar 2026"),
                ("Integration", "Data source connection", 0, 3, False, "TBD"),
                ("Integration", "New data connections", 4, 6, False, None),
                ("Sustainment", "Platform maintenance", 0, 6, False, None),
                ("Deliverables", "Kickoff", 0, 0, True, "20 Feb 2026"),
                ("Deliverables", "OP2 Closeout", 2, 3, False, "14 May 2026"),
                ("Deliverables", "OP3 Closeout", 5, 6, False, "14 Aug 2026"),
                ("Deliverables", "Monthly reviews", 0, 6, False, None),
            ],
        },
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# THEMES
# ═══════════════════════════════════════════════════════════════════════════

_BAR_PALETTE_DARK = [
    RGBColor(34, 197, 94),
    RGBColor(249, 115, 22),
    RGBColor(139, 92, 246),
    RGBColor(236, 72, 153),
    RGBColor(56, 189, 248),
    RGBColor(251, 191, 36),
    RGBColor(148, 163, 184),
]

_BAR_PALETTE_LIGHT = [
    RGBColor(22, 163, 74),
    RGBColor(234, 88, 12),
    RGBColor(124, 58, 237),
    RGBColor(219, 39, 119),
    RGBColor(14, 165, 233),
    RGBColor(217, 119, 6),
    RGBColor(100, 116, 139),
]

THEMES = {
    "dark": {
        "slide_bg":       RGBColor(15, 23, 42),
        "title_text":     RGBColor(241, 245, 249),
        "subtitle_text":  RGBColor(148, 163, 184),
        "body_text":      RGBColor(226, 232, 240),
        "muted_text":     RGBColor(100, 116, 139),
        "header_bg":      RGBColor(30, 41, 59),
        "header_text":    RGBColor(255, 255, 255),
        "row_even":       RGBColor(30, 41, 59),
        "row_odd":        RGBColor(51, 65, 85),
        "card_bg":        RGBColor(30, 41, 59),
        "card_border":    RGBColor(51, 65, 85),
        "accent":         RGBColor(99, 102, 241),
        "divider":        RGBColor(51, 65, 85),
        "bullet_color":   RGBColor(99, 102, 241),
    },
    "light": {
        "slide_bg":       RGBColor(255, 255, 255),
        "title_text":     RGBColor(15, 23, 42),
        "subtitle_text":  RGBColor(71, 85, 105),
        "body_text":      RGBColor(30, 41, 59),
        "muted_text":     RGBColor(148, 163, 184),
        "header_bg":      RGBColor(241, 245, 249),
        "header_text":    RGBColor(30, 41, 59),
        "row_even":       RGBColor(255, 255, 255),
        "row_odd":        RGBColor(248, 250, 252),
        "card_bg":        RGBColor(248, 250, 252),
        "card_border":    RGBColor(226, 232, 240),
        "accent":         RGBColor(79, 70, 229),
        "divider":        RGBColor(226, 232, 240),
        "bullet_color":   RGBColor(79, 70, 229),
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE RENDERERS — You shouldn't need to edit below this line
# ═══════════════════════════════════════════════════════════════════════════

W = 10     # slide width in inches
H = 7.5    # slide height in inches
MARGIN = 0.7


def _set_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_text(slide, left, top, width, height, text, *,
              size=12, bold=False, color=None, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(Inches(left), Inches(top),
                                   Inches(width), Inches(height))
    p = box.text_frame.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.bold = bold
    if color:
        p.font.color.rgb = color
    p.alignment = align
    return box


def _render_title(slide, data, theme):
    _set_bg(slide, theme["slide_bg"])

    # Accent bar
    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(MARGIN), Inches(2.8), Inches(1.2), Inches(0.06),
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = theme["accent"]
    bar.line.fill.background()

    _add_text(slide, MARGIN, 3.0, W - 2 * MARGIN, 1.2,
              data["title"], size=36, bold=True, color=theme["title_text"])
    if data.get("subtitle"):
        _add_text(slide, MARGIN, 4.2, W - 2 * MARGIN, 0.5,
                  data["subtitle"], size=16, color=theme["subtitle_text"])


def _render_section(slide, data, theme):
    _set_bg(slide, theme["accent"])

    _add_text(slide, MARGIN, 2.8, W - 2 * MARGIN, 1.0,
              data["title"], size=32, bold=True,
              color=RGBColor(255, 255, 255), align=PP_ALIGN.LEFT)

    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(MARGIN), Inches(3.8), Inches(1.5), Inches(0.05),
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = RGBColor(255, 255, 255)
    bar.line.fill.background()


def _render_content(slide, data, theme):
    _set_bg(slide, theme["slide_bg"])

    _add_text(slide, MARGIN, 0.5, W - 2 * MARGIN, 0.6,
              data["title"], size=28, bold=True, color=theme["title_text"])

    # Divider line under title
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(MARGIN), Inches(1.15), Inches(W - 2 * MARGIN), Inches(0.02),
    )
    line.fill.solid()
    line.fill.fore_color.rgb = theme["divider"]
    line.line.fill.background()

    bullets = data.get("bullets", [])
    top = 1.4
    for bullet in bullets:
        # Bullet dot
        dot = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(MARGIN + 0.05), Inches(top + 0.12),
            Inches(0.12), Inches(0.12),
        )
        dot.fill.solid()
        dot.fill.fore_color.rgb = theme["bullet_color"]
        dot.line.fill.background()

        _add_text(slide, MARGIN + 0.35, top, W - 2 * MARGIN - 0.35, 0.4,
                  bullet, size=16, color=theme["body_text"])
        top += 0.55


def _render_two_column(slide, data, theme):
    _set_bg(slide, theme["slide_bg"])

    _add_text(slide, MARGIN, 0.5, W - 2 * MARGIN, 0.6,
              data["title"], size=28, bold=True, color=theme["title_text"])

    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(MARGIN), Inches(1.15), Inches(W - 2 * MARGIN), Inches(0.02),
    )
    line.fill.solid()
    line.fill.fore_color.rgb = theme["divider"]
    line.line.fill.background()

    col_w = (W - 2 * MARGIN - 0.5) / 2
    for col_idx, (title_key, bullets_key) in enumerate([
        ("left_title", "left_bullets"),
        ("right_title", "right_bullets"),
    ]):
        x = MARGIN + col_idx * (col_w + 0.5)

        # Column header
        _add_text(slide, x, 1.4, col_w, 0.5,
                  data.get(title_key, ""), size=18, bold=True,
                  color=theme["accent"])

        top = 2.0
        for bullet in data.get(bullets_key, []):
            dot = slide.shapes.add_shape(
                MSO_SHAPE.OVAL,
                Inches(x + 0.05), Inches(top + 0.1),
                Inches(0.1), Inches(0.1),
            )
            dot.fill.solid()
            dot.fill.fore_color.rgb = theme["bullet_color"]
            dot.line.fill.background()

            _add_text(slide, x + 0.3, top, col_w - 0.3, 0.35,
                      bullet, size=14, color=theme["body_text"])
            top += 0.48


def _render_metrics(slide, data, theme):
    _set_bg(slide, theme["slide_bg"])

    _add_text(slide, MARGIN, 0.5, W - 2 * MARGIN, 0.6,
              data["title"], size=28, bold=True, color=theme["title_text"])

    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(MARGIN), Inches(1.15), Inches(W - 2 * MARGIN), Inches(0.02),
    )
    line.fill.solid()
    line.fill.fore_color.rgb = theme["divider"]
    line.line.fill.background()

    metrics = data.get("metrics", [])
    count = len(metrics)
    if count == 0:
        return

    gap = 0.3
    total_gap = gap * (count - 1)
    card_w = (W - 2 * MARGIN - total_gap) / count
    card_h = 2.2
    card_top = 2.0

    for i, m in enumerate(metrics):
        x = MARGIN + i * (card_w + gap)

        # Card background
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(card_top),
            Inches(card_w), Inches(card_h),
        )
        card.fill.solid()
        card.fill.fore_color.rgb = theme["card_bg"]
        card.line.color.rgb = theme["card_border"]
        card.line.width = Pt(1)

        # Accent bar at top of card
        accent = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(x), Inches(card_top),
            Inches(card_w), Inches(0.06),
        )
        accent.fill.solid()
        accent.fill.fore_color.rgb = _BAR_PALETTE_DARK[i % len(_BAR_PALETTE_DARK)] \
            if theme is THEMES["dark"] else _BAR_PALETTE_LIGHT[i % len(_BAR_PALETTE_LIGHT)]
        accent.line.fill.background()

        # Value
        _add_text(slide, x + 0.2, card_top + 0.3, card_w - 0.4, 0.8,
                  m["value"], size=32, bold=True,
                  color=theme["title_text"], align=PP_ALIGN.CENTER)

        # Label
        _add_text(slide, x + 0.2, card_top + 1.1, card_w - 0.4, 0.4,
                  m["label"], size=13, bold=True,
                  color=theme["subtitle_text"], align=PP_ALIGN.CENTER)

        # Detail
        if m.get("detail"):
            _add_text(slide, x + 0.2, card_top + 1.55, card_w - 0.4, 0.35,
                      m["detail"], size=11,
                      color=theme["muted_text"], align=PP_ALIGN.CENTER)


def _render_table(slide, data, theme):
    _set_bg(slide, theme["slide_bg"])

    _add_text(slide, MARGIN, 0.5, W - 2 * MARGIN, 0.6,
              data["title"], size=28, bold=True, color=theme["title_text"])

    headers = data.get("headers", [])
    rows = data.get("rows", [])
    if not headers:
        return

    n_cols = len(headers)
    n_rows = 1 + len(rows)
    tbl_w = W - 2 * MARGIN
    tbl_top = 1.4

    table_shape = slide.shapes.add_table(
        n_rows, n_cols,
        Inches(MARGIN), Inches(tbl_top),
        Inches(tbl_w), Inches(0.45 * n_rows),
    )
    table = table_shape.table

    col_w = tbl_w / n_cols
    for c in range(n_cols):
        table.columns[c].width = Inches(col_w)

    # Header row
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = theme["header_bg"]
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = theme["header_text"]

    # Data rows
    for r, row_data in enumerate(rows):
        bg = theme["row_odd"] if r % 2 == 1 else theme["row_even"]
        for c, val in enumerate(row_data):
            cell = table.cell(r + 1, c)
            cell.text = str(val)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            p.font.color.rgb = theme["body_text"]


def _render_gantt(slide, data, theme):
    _set_bg(slide, theme["slide_bg"])

    months = data.get("months", [])
    quarters = data.get("quarters", [])
    phases = data.get("phases", [])
    tasks = data.get("tasks", [])

    palette = _BAR_PALETTE_DARK if theme is THEMES["dark"] else _BAR_PALETTE_LIGHT
    bar_colors = {ph: palette[i % len(palette)] for i, ph in enumerate(phases)}
    fallback = RGBColor(148, 163, 184)

    tbl_left = 0.5
    tbl_top = 1.08
    phase_w = 2.7
    chart_w = 5.6
    due_w = 1.1
    hdr_h = 0.4
    row_h = 0.38
    bar_h = 0.22
    bar_pad = 0.03
    month_w = chart_w / len(months) if months else 1
    chart_left = tbl_left + phase_w

    if data.get("subtitle"):
        _add_text(slide, tbl_left, 0.15, 9, 0.3,
                  data["subtitle"], size=9, color=theme["subtitle_text"])

    _add_text(slide, tbl_left, 0.4, 9, 0.55,
              data["title"], size=26, bold=True, color=theme["title_text"])

    total_rows = 2 + len(tasks)
    total_cols = 1 + len(months) + 1
    due_col = total_cols - 1

    table_shape = slide.shapes.add_table(
        total_rows, total_cols,
        Inches(tbl_left), Inches(tbl_top),
        Inches(phase_w + chart_w + due_w),
        Inches(hdr_h * 2 + len(tasks) * row_h),
    )
    table = table_shape.table

    for r in range(2):
        for c in range(total_cols):
            cell = table.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = theme["header_bg"]
            p = cell.text_frame.paragraphs[0]
            p.font.color.rgb = theme["header_text"]
            p.font.size = Pt(12)
            p.font.bold = (r == 0)
            p.alignment = PP_ALIGN.CENTER

    table.cell(0, 0).text = "Deliverable"
    if quarters:
        mpq = len(months) // len(quarters) if quarters else len(months)
        for i, q in enumerate(quarters):
            cs = 1 + i * mpq
            ce = min(1 + (i + 1) * mpq - 1, len(months))
            table.cell(0, cs).text = q
            if ce > cs:
                table.cell(0, cs).merge(table.cell(0, ce))

    table.cell(0, due_col).text = "Due Date"
    table.cell(0, due_col).merge(table.cell(1, due_col))

    table.cell(1, 0).text = ""
    for c, m in enumerate(months):
        table.cell(1, 1 + c).text = m

    table.columns[0].width = Inches(phase_w)
    for c in range(1, due_col):
        table.columns[c].width = Inches(month_w)
    table.columns[due_col].width = Inches(due_w)

    for row in range(2, total_rows):
        task = tasks[row - 2]
        bg = theme["row_odd"] if (row - 2) % 2 == 1 else theme["row_even"]
        for c in range(total_cols):
            cell = table.cell(row, c)
            if c == 0:
                cell.text = task[1]
            elif c == due_col and task[5]:
                cell.text = task[5]
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            if c == 0:
                p = cell.text_frame.paragraphs[0]
                p.font.size = Pt(10)
                p.font.color.rgb = theme["body_text"]
                p.alignment = PP_ALIGN.LEFT
            elif c == due_col:
                p = cell.text_frame.paragraphs[0]
                p.font.size = Pt(10)
                p.font.color.rgb = theme["muted_text"]
                p.alignment = PP_ALIGN.RIGHT

    chart_top = tbl_top + hdr_h * 2
    for i, task in enumerate(tasks):
        phase, _, start_m, end_m, is_milestone, _ = task
        color = bar_colors.get(phase, fallback)
        row_top = chart_top + i * row_h
        cy = row_top + row_h / 2

        if is_milestone:
            sz = 0.18
            cx = chart_left + (start_m + 0.5) * month_w
            shape = slide.shapes.add_shape(
                MSO_SHAPE.DIAMOND,
                Inches(cx - sz / 2), Inches(cy - sz / 2),
                Inches(sz), Inches(sz),
            )
            shape.fill.solid()
            shape.fill.fore_color.rgb = color
            shape.line.fill.background()
        else:
            bt = row_top + (row_h - bar_h) / 2
            bl = chart_left + start_m * month_w + bar_pad
            bw = max(0.25, (end_m - start_m + 1) * month_w - 2 * bar_pad)
            shape = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(bl), Inches(bt), Inches(bw), Inches(bar_h),
            )
            shape.fill.solid()
            shape.fill.fore_color.rgb = color
            shape.line.fill.background()


RENDERERS = {
    "title": _render_title,
    "section": _render_section,
    "content": _render_content,
    "two_column": _render_two_column,
    "metrics": _render_metrics,
    "table": _render_table,
    "gantt": _render_gantt,
}


def main(theme_name: str = "dark"):
    theme = THEMES[theme_name]

    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)

    for slide_data in DECK["slides"]:
        layout = slide_data.get("layout", "content")
        renderer = RENDERERS.get(layout)
        if not renderer:
            print(f"Warning: unknown layout '{layout}', skipping")
            continue
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        renderer(slide, slide_data, theme)

    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(exist_ok=True)
    filename = DECK.get("filename", "Deck")
    out_path = out_dir / f"{filename}_{theme_name}.pptx"
    prs.save(str(out_path))
    print(f"Created {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a styled Scale AI slide deck"
    )
    parser.add_argument(
        "--theme", choices=["dark", "light"], default="dark",
        help="Color theme (default: dark)",
    )
    args = parser.parse_args()
    main(args.theme)
