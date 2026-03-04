#!/usr/bin/env python3
"""AFRL Agentic Warfare white paper deck — built from Google Drive doc."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "AFRL_Agentic_Warfare_Brief",
    "slides": [
        {
            "layout": "title",
            "title": "The Through Line",
            "subtitle": "A Unified AI-Native Infrastructure\nfor the Digital Kill Chain\nPrepared for AFRL  ·  January 2026",
            "notes": "White paper presentation for Air Force Research Laboratory. The thesis: three separate Scale workstreams (Zion Delta, Horseshoe Bend, Haleakala) integrate into a single agentic ecosystem for the digital kill chain.",
        },
        {
            "layout": "quote",
            "quote": "A human-on-the-loop digital kill chain requires a single umbrella that creates relationships between data and analysts.",
            "attribution": "Scale AI White Paper — The Through Line",
            "notes": "Frame the problem statement. The Air Force has fragmented data across ACC, 480th ISRW, 363rd ISRW, and AOCs. Individual prototypes work, but they don't talk to each other. Scale's proposal: integrate them.",
        },
        {
            "layout": "process",
            "title": "Three workstreams converge into a unified agentic ecosystem",
            "steps": [
                {"label": "Zion Delta", "detail": "Intelligence backbone — automated PED, ICD-203 SFT, targeting"},
                {"label": "Horseshoe Bend", "detail": "Operational nerve center — defensive posture, red lines, COA gen"},
                {"label": "Haleakala", "detail": "Strategic integration — ATO/ACO chatbots, cross-AOC campaign planning"},
            ],
            "notes": "Three programs, three layers. Zion processes intel (A2). Horseshoe Bend bridges intel to ops (A2>A3). Haleakala integrates across theaters. Together they form a complete digital kill chain.",
        },
        {
            "layout": "content",
            "title": "Zion Delta automates intelligence processing from sensor to analyst",
            "bullets": [
                "Automated A2 reporting — reduces sensor-to-intel latency from hours to minutes",
                "ICD-203 Supervised Fine-Tuning — models trained as domain SMEs that meet IC analytic standards",
                "Tactical quantization — models scaled to run on disconnected devices in DDIL environments",
                "Targeting integration with 118th ISRG — automated target deck generation and verification on SIPR",
            ],
            "notes": "Zion Delta is the deepest workstream. The ICD-203 SFT work is unique — no other company is training models to meet Intelligence Community analytic standards. The tactical quantization angle opens the edge/DDIL market.",
        },
        {
            "layout": "two_column",
            "title": "Horseshoe Bend turns intelligence into operational decisions in real time",
            "left_title": "Capabilities",
            "left_bullets": [
                "Defensive posture reorganization based on red threat activity",
                "Automated red line monitoring with AOC leadership alerting",
                "Course of Action generation for proactive defensive planning",
            ],
            "right_title": "Impact",
            "right_bullets": [
                "Staff officers shift from reactive monitoring to proactive planning",
                "Decision cycle compressed from hours to minutes",
                "Human retains authority — AI handles data extraction and formatting",
            ],
            "notes": "Horseshoe Bend is the A3 play. The key message: AI doesn't replace the staff officer, it gives them decision advantage. The COA generation capability is the differentiator — no competitor offers this at AOC scale.",
        },
        {
            "layout": "fact",
            "value": "40%",
            "label": "Increase in Planner Productivity",
            "detail": "MITRE assessment of AI-assisted planning cycle reduction",
            "title": "The productivity gains are validated by independent assessment",
            "notes": "Third-party validation from MITRE. This is the number that matters to acquisition leadership. 40% productivity gain means the same AOC floor can handle more complexity without adding billets.",
        },
        {
            "layout": "content",
            "title": "The unified architecture enables a kill chain that flows without human bottlenecks",
            "bullets": [
                "Zion Delta identifies a target → Haleakala assesses it against the ATO",
                "Horseshoe Bend alerts the AOC if defensive postures must change",
                "Human analysts verify target decks and approve reorganized plans",
                "Planning cycle drops from hours to minutes across the full F2T2EA cycle",
            ],
            "notes": "This is the 'through line' — the integration story. Each workstream feeds the next. The human stays on the loop for critical decisions while AI handles the data grunt work. The F2T2EA reference (Find, Fix, Track, Target, Engage, Assess) connects to JP 3-60 doctrine.",
        },
        {
            "layout": "content",
            "title": "Scale's approach aligns directly to AFRL solicitation and joint doctrine",
            "bullets": [
                "JP 3-60 (Targeting): Automates the F2T2EA cycle via 118th ISRG integration",
                "FA8750-23-S-7006 Technical Area 1: AI for C2 at operational speed and scale",
                "Scale Public Sector 2026 strategy: Canvas-centered UI with multi-agent collaboration",
                "Objective: prove integration that scales across all AOCs (PACAF, AFCENT, USAFE) and into Army NGC2",
            ],
            "notes": "Doctrine alignment is what acquisition officers need to justify the buy. JP 3-60 and the AFRL solicitation are the anchors. The ambition statement — scaling across all AOCs and into Army — shows this isn't a one-off prototype.",
        },
    ],
}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
