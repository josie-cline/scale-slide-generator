#!/usr/bin/env python3
"""
Showcase deck: demonstrates all new features added to the Scale Slide Generator.
  - Speaker notes on every slide
  - Image layout with caption
  - Schema validation (runs automatically)
  - Document ingestion pipeline
  - MCP server integration
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Scale_Slide_Generator_v2_Showcase",
    "slides": [
        # ── Title ─────────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Scale Slide Generator v2",
            "subtitle": "New Capabilities · February 2026",
            "notes": "Welcome everyone. Today we're walking through the five new capabilities we've added to the slide generator. Each one was inspired by studying the best open-source tools on GitHub and pulling in what actually matters for our workflow.",
        },

        # ── Agenda ────────────────────────────────────────────────────
        {
            "layout": "content",
            "title": "What's New",
            "bullets": [
                "Speaker notes on every slide — presenter talking points embedded in PPTX",
                "Image layout — embed diagrams, screenshots, and charts with auto-fit",
                "DECK schema validation — catch typos and missing fields before render",
                "Document ingestion — parse CSV, JSON, DOCX, PDF into slides automatically",
                "MCP server — expose the generator as a tool for Cursor and Claude Code",
            ],
            "notes": "Five features total. We'll go through each one with a live example. The key theme: we're moving from 'AI edits a Python dict' to 'AI calls a validated API.'",
        },

        # ── Section: Speaker Notes ────────────────────────────────────
        {
            "layout": "section",
            "title": "Speaker Notes",
            "notes": "Transition: Let's start with the simplest but most-requested feature.",
        },

        {
            "layout": "two_column",
            "title": "Speaker notes turn decks into self-contained briefings",
            "left_title": "Before",
            "left_bullets": [
                "Deck is visual-only",
                "Talking points live in a separate doc",
                "Presenters wing it or forget context",
                "No institutional memory in the file",
            ],
            "right_title": "After",
            "right_bullets": [
                "Add 'notes' key to any slide dict",
                "Notes render in PowerPoint's notes pane",
                "Presenter View shows them automatically",
                "The deck IS the briefing document",
            ],
            "notes": "This is a live example — you're reading these notes right now in Presenter View. Every slide in this deck has them. Implementation was 2 lines of code.",
        },

        # ── Section: Image Layout ─────────────────────────────────────
        {
            "layout": "section",
            "title": "Image Layout",
            "notes": "Transition: Next up — we can now embed images directly into slides.",
        },

        {
            "layout": "image",
            "title": "Brand assets render at full fidelity with auto-fit",
            "image": "assets/bg_dark.png",
            "caption": "Scale dark theme background — auto-fitted to slide bounds",
            "notes": "The image layout accepts any file path (relative or absolute), auto-detects aspect ratio via Pillow, centers the image, and adds an optional caption. This example shows our dark wallpaper asset rendered as a standalone image slide.",
        },

        # ── Section: Validation ───────────────────────────────────────
        {
            "layout": "section",
            "title": "Schema Validation",
            "notes": "Transition: This is the one that prevents the most frustration.",
        },

        {
            "layout": "content",
            "title": "Every deck is validated before a single pixel is rendered",
            "bullets": [
                "Runs automatically on every call to main()",
                "Checks layout names, required keys, types, and column counts",
                "Catches unknown keys — instant typo detection",
                "Gantt tasks validated for correct tuple structure",
                "Clear error messages: 'Slide 3 (table): rows[0] has 5 columns, expected 4'",
                "Validation available standalone via utils/validate_deck.py",
            ],
            "notes": "Before this, a typo like 'bulets' instead of 'bullets' would silently produce a slide with no content. Now it fails fast with a message telling you exactly what's wrong and where.",
        },

        {
            "layout": "table",
            "title": "Validation catches errors that used to cause silent failures",
            "headers": ["Error Type", "Example", "What You See Now"],
            "rows": [
                ["Unknown layout", "layout: 'chart'", "unknown layout 'chart' (valid: content, gantt, image, ...)"],
                ["Missing key", "metrics slide, no 'metrics'", "missing required key 'metrics'"],
                ["Wrong type", "bullets: 'just a string'", "'bullets' must be a list"],
                ["Column mismatch", "3 headers, 4 cols in row", "rows[0] has 4 columns, expected 3"],
                ["Bad Gantt task", "5-element tuple", "tasks[0] needs 6 elements, got 5"],
                ["Typo in key", "bulltes instead of bullets", "unknown keys {'bulltes'}"],
            ],
            "notes": "This table shows the six categories of errors we catch. Each one previously resulted in either a crash, a silent skip, or a malformed slide. Now they all produce actionable error messages.",
        },

        # ── Section: Ingestion ────────────────────────────────────────
        {
            "layout": "section",
            "title": "Document Ingestion",
            "notes": "Transition: Now let's talk about going from raw files to finished slides.",
        },

        {
            "layout": "two_column",
            "title": "Drop any file — get structured slides back",
            "left_title": "Supported Formats",
            "left_bullets": [
                ".csv → table slides with headers and rows",
                ".json → table slides (array of objects)",
                ".txt / .md → content slides (chunked)",
                ".docx → paragraphs + embedded tables",
                ".pdf → extracted text (via pdfplumber)",
            ],
            "right_title": "How It Works",
            "right_bullets": [
                "ingest_file() → structured dict",
                "ingest_to_slides() → ready-made slide dicts",
                "Plug results directly into DECK['slides']",
                "Works with or without an LLM",
                "Available as MCP tool for Cursor",
            ],
            "notes": "The ingestion module is in utils/ingest.py. It's intentionally LLM-free — pure parsing. An LLM can enhance the output (better titles, summarization), but the base pipeline works standalone.",
        },

        # ── Section: MCP Server ───────────────────────────────────────
        {
            "layout": "section",
            "title": "MCP Server",
            "notes": "Transition: The final piece — making the generator callable as a tool.",
        },

        {
            "layout": "content",
            "title": "The generator is now a first-class MCP tool",
            "bullets": [
                "mcp_server.py exposes 4 tools via Model Context Protocol",
                "generate_deck — build a .pptx from a JSON DECK definition",
                "list_layouts — show all layouts and their required/optional keys",
                "validate_deck_json — dry-run validation without generating",
                "ingest_file_to_slides — parse any document into slide dicts",
            ],
            "notes": "MCP = Model Context Protocol. It's the standard way for AI agents to call external tools. By wrapping our generator as an MCP server, any MCP client — Cursor, Claude Code, custom agents — can generate decks programmatically. Setup: Cursor Settings → MCP → Add → command: python3 mcp_server.py. Requires Python 3.10+.",
        },

        # ── Metrics ───────────────────────────────────────────────────
        {
            "layout": "metrics",
            "title": "What We Shipped",
            "metrics": [
                {"label": "New Features", "value": "5", "detail": "Notes, Image, Validation, Ingest, MCP"},
                {"label": "Layouts", "value": "8", "detail": "Up from 7 (+image)"},
                {"label": "MCP Tools", "value": "4", "detail": "Generate, List, Validate, Ingest"},
                {"label": "Lines Added", "value": "~400", "detail": "Across 4 new files"},
            ],
            "notes": "The total footprint is still small. No new heavyweight dependencies beyond the optional mcp package. Validation, ingestion, and the image layout are all zero-dependency additions (they use python-pptx, Pillow, and stdlib which we already had).",
        },

        # ── What's Next ──────────────────────────────────────────────
        {
            "layout": "content",
            "title": "What's next: from tool to platform",
            "bullets": [
                "Chart layouts — bar, line, and pie charts via python-pptx",
                "Semantic icon search — embed icons by meaning, not filename",
                "CI/CD pipeline — auto-generate recurring decks on schedule",
                "Web UI — simple form for non-technical users to generate decks",
                "Multi-language support — generate decks in any language",
            ],
            "notes": "These are the five items on the roadmap. Chart layouts and icon search are the most requested. CI/CD and web UI are about making this accessible beyond the Cursor IDE. None of these require architectural changes — the modular renderer pattern makes them straightforward additions.",
        },
    ],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
