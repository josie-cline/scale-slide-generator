#!/usr/bin/env python3
"""
MCP server exposing the Scale slide generator as tools for Cursor/Claude Code.

Setup: Cursor Settings -> MCP -> Add -> command: python3 mcp_server.py
"""
import json
import sys
from pathlib import Path

# Ensure project root is on the path regardless of working directory
sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("ERROR: 'mcp' package not installed. pip install 'mcp[cli]'", file=sys.stderr)
    sys.exit(1)

from generate_deck import main as generate_main, THEMES, RENDERERS
from utils.validate_deck import (
    validate_deck,
    _LAYOUT_REQUIRED_KEYS as _LAYOUT_REQUIRED,
    _LAYOUT_OPTIONAL_KEYS as _LAYOUT_OPTIONAL,
)

mcp = FastMCP("scale-slide-generator", version="2.0.0")


@mcp.tool()
def generate_deck(deck_json: str, theme: str = "dark") -> str:
    """Generate a Scale-branded PowerPoint deck from a DECK JSON definition."""
    if theme not in THEMES:
        return f"Error: theme must be 'dark' or 'light', got '{theme}'"
    try:
        deck = json.loads(deck_json)
    except json.JSONDecodeError as e:
        return f"Error: invalid JSON — {e}"
    errors = validate_deck(deck)
    if errors:
        return "Validation errors:\n" + "\n".join(f"  - {e}" for e in errors)
    try:
        path = generate_main(theme_name=theme, deck=deck)
        return f"Deck generated: {path}"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def list_layouts() -> str:
    """List all available slide layouts and their data keys."""
    lines = ["Available layouts:\n"]
    for layout in sorted(RENDERERS.keys()):
        req = _LAYOUT_REQUIRED.get(layout, [])
        opt = _LAYOUT_OPTIONAL.get(layout, [])
        lines.append(f"  {layout}:")
        lines.append(f"    required: {', '.join(req)}")
        lines.append(f"    optional: {', '.join(opt)}")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def validate_deck_json(deck_json: str) -> str:
    """Validate a DECK dict without generating."""
    try:
        deck = json.loads(deck_json)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"
    errors = validate_deck(deck)
    if not errors:
        return "Valid — {} slides".format(len(deck.get("slides", [])))
    return "Errors:\n" + "\n".join(f"  - {e}" for e in errors)


if __name__ == "__main__":
    mcp.run()
