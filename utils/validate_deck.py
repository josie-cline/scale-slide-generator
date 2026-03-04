"""
Validate a DECK dict before rendering to catch errors early.

Usage:
    from utils.validate_deck import validate_deck
    errors = validate_deck(deck)
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
"""

VALID_LAYOUTS = {
    "title", "section", "content", "two_column", "metrics",
    "table", "gantt", "chart", "quote", "fact", "process",
}

_LAYOUT_REQUIRED_KEYS = {
    "title":      ["title"],
    "section":    ["title"],
    "content":    ["title"],
    "two_column": ["title"],
    "metrics":    ["title", "metrics"],
    "table":      ["title", "headers"],
    "gantt":      ["title", "months", "phases", "tasks"],
    "chart":      ["title", "categories", "series"],
    "quote":      ["quote"],
    "fact":       ["value"],
    "process":    ["title", "steps"],
}

_LAYOUT_OPTIONAL_KEYS = {
    "title":      ["subtitle", "notes"],
    "section":    ["notes"],
    "content":    ["bullets", "notes"],
    "two_column": ["left_title", "left_bullets", "right_title", "right_bullets", "notes"],
    "metrics":    ["notes"],
    "table":      ["rows", "notes"],
    "gantt":      ["subtitle", "quarters", "notes"],
    "chart":      ["chart_type", "notes"],
    "quote":      ["title", "attribution", "notes"],
    "fact":       ["title", "label", "detail", "notes"],
    "process":    ["notes"],
}


def validate_deck(deck: dict) -> "list[str]":
    """Return a list of error strings. Empty list means the deck is valid."""
    errors = []

    if not isinstance(deck, dict):
        return [f"DECK must be a dict, got {type(deck).__name__}"]

    if "slides" not in deck:
        errors.append("DECK missing required key 'slides'")
        return errors

    if not isinstance(deck["slides"], list):
        errors.append(f"DECK['slides'] must be a list, got {type(deck['slides']).__name__}")
        return errors

    if len(deck["slides"]) == 0:
        errors.append("DECK['slides'] is empty — need at least one slide")

    for i, slide in enumerate(deck["slides"]):
        prefix = f"Slide {i + 1}"

        if not isinstance(slide, dict):
            errors.append(f"{prefix}: must be a dict, got {type(slide).__name__}")
            continue

        layout = slide.get("layout")
        if not layout:
            errors.append(f"{prefix}: missing 'layout' key")
            continue
        if layout not in VALID_LAYOUTS:
            errors.append(f"{prefix}: unknown layout '{layout}' (valid: {', '.join(sorted(VALID_LAYOUTS))})")
            continue

        required = _LAYOUT_REQUIRED_KEYS[layout]
        optional = _LAYOUT_OPTIONAL_KEYS.get(layout, [])
        valid_keys = set(required + optional + ["layout"])

        for key in required:
            if key not in slide:
                errors.append(f"{prefix} ({layout}): missing required key '{key}'")

        unknown = set(slide.keys()) - valid_keys
        if unknown:
            errors.append(f"{prefix} ({layout}): unknown keys {unknown} (valid: {sorted(valid_keys)})")

        _validate_slide_types(slide, layout, prefix, errors)

    return errors


def _validate_slide_types(slide: dict, layout: str, prefix: str, errors: list):
    """Type-check slide values based on layout."""
    if layout == "content":
        bullets = slide.get("bullets")
        if bullets is not None and not isinstance(bullets, list):
            errors.append(f"{prefix} ({layout}): 'bullets' must be a list")
        elif bullets:
            for j, b in enumerate(bullets):
                if not isinstance(b, str):
                    errors.append(f"{prefix} ({layout}): bullets[{j}] must be a string, got {type(b).__name__}")

    elif layout == "two_column":
        for key in ("left_bullets", "right_bullets"):
            val = slide.get(key)
            if val is not None and not isinstance(val, list):
                errors.append(f"{prefix} ({layout}): '{key}' must be a list")

    elif layout == "metrics":
        metrics = slide.get("metrics", [])
        if not isinstance(metrics, list):
            errors.append(f"{prefix} ({layout}): 'metrics' must be a list")
        else:
            for j, m in enumerate(metrics):
                if not isinstance(m, dict):
                    errors.append(f"{prefix} ({layout}): metrics[{j}] must be a dict")
                    continue
                for req in ("label", "value"):
                    if req not in m:
                        errors.append(f"{prefix} ({layout}): metrics[{j}] missing '{req}'")

    elif layout == "table":
        headers = slide.get("headers")
        if headers is not None and not isinstance(headers, list):
            errors.append(f"{prefix} ({layout}): 'headers' must be a list")
        rows = slide.get("rows")
        if rows is not None:
            if not isinstance(rows, list):
                errors.append(f"{prefix} ({layout}): 'rows' must be a list of lists")
            elif headers:
                n_cols = len(headers)
                for j, row in enumerate(rows):
                    if not isinstance(row, list):
                        errors.append(f"{prefix} ({layout}): rows[{j}] must be a list")
                    elif len(row) != n_cols:
                        errors.append(f"{prefix} ({layout}): rows[{j}] has {len(row)} columns, expected {n_cols}")

    elif layout == "gantt":
        for key in ("months", "phases"):
            val = slide.get(key)
            if val is not None and not isinstance(val, list):
                errors.append(f"{prefix} ({layout}): '{key}' must be a list")
        tasks = slide.get("tasks", [])
        if not isinstance(tasks, list):
            errors.append(f"{prefix} ({layout}): 'tasks' must be a list")
        else:
            for j, t in enumerate(tasks):
                if not isinstance(t, (list, tuple)):
                    errors.append(f"{prefix} ({layout}): tasks[{j}] must be a tuple/list of (phase, name, start, end, is_milestone, due)")
                elif len(t) != 6:
                    errors.append(f"{prefix} ({layout}): tasks[{j}] needs 6 elements (phase, name, start, end, is_milestone, due), got {len(t)}")

    elif layout == "chart":
        categories = slide.get("categories")
        if categories is not None and not isinstance(categories, list):
            errors.append(f"{prefix} ({layout}): 'categories' must be a list")
        series = slide.get("series")
        if series is not None:
            if not isinstance(series, list):
                errors.append(f"{prefix} ({layout}): 'series' must be a list of dicts")
            else:
                for j, s in enumerate(series):
                    if not isinstance(s, dict):
                        errors.append(f"{prefix} ({layout}): series[{j}] must be a dict")
                        continue
                    for req in ("name", "values"):
                        if req not in s:
                            errors.append(f"{prefix} ({layout}): series[{j}] missing '{req}'")
                    if "values" in s and not isinstance(s["values"], (list, tuple)):
                        errors.append(f"{prefix} ({layout}): series[{j}]['values'] must be a list")

    elif layout == "process":
        steps = slide.get("steps")
        if steps is not None:
            if not isinstance(steps, list):
                errors.append(f"{prefix} ({layout}): 'steps' must be a list")
            else:
                for j, s in enumerate(steps):
                    if not isinstance(s, dict):
                        errors.append(f"{prefix} ({layout}): steps[{j}] must be a dict with 'label'")
                    elif "label" not in s:
                        errors.append(f"{prefix} ({layout}): steps[{j}] missing required key 'label'")
