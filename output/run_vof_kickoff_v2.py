#!/usr/bin/env python3
"""
Valley of Fire OP2 Kickoff — Creative v2.
Narrative-driven deck: every title passes the "would a GM lean in?" test.

Run from project root:
    python3 output/run_vof_kickoff_v2.py
    python3 output/run_vof_kickoff_v2.py --theme light
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Valley_of_Fire_OP2_Kickoff_v2",
    "slides": [
        # ── 1. Title ──────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Valley of Fire · OP2 Kickoff",
            "subtitle": "Project ASCEND · HC1084-25-0001 · Scale AI",
        },

        # ── 2. What the next 90 days look like ────────────────────────
        {
            "layout": "content",
            "title": "What the Next 90 Days Look Like",
            "bullets": [
                "Your analysts get hours back — every app they rely on stays live and supported",
                "Two apps graduate from prototype to production (IR Review & INTEL Agent)",
                "ServiceNow finally connects — no more manual ticket re-entry",
                "We scope up to 3 new apps if you exercise CLIN 0013",
                "Monthly reviews with zero surprises — you'll see what we see",
            ],
        },

        # ── 3. We've been listening ───────────────────────────────────
        {
            "layout": "two_column",
            "title": "We've Been Listening — Here's What We Heard",
            "left_title": "The Friction",
            "left_bullets": [
                "Every RFI starts with six tabs and a prayer",
                "Analysts spend hours stitching IRs, PULSE, ACE, and SIGACTS by hand",
                "CCIR calls are guesswork dressed up as process",
                "Site risk lives in someone's head, not a dashboard",
            ],
            "right_title": "The Fix",
            "right_bullets": [
                "Threat Hunt: ask in English, get a sourced draft back in seconds",
                "Historical Retro: one search across every data source at once",
                "CCIR Decision Support: MET / NOT MET against real criteria, instantly",
                "Site Risk Analysis: ranked heat maps with export to CSV, XML, JSON",
            ],
        },

        # ── 4. What OP1 actually proved ───────────────────────────────
        {
            "layout": "metrics",
            "title": "What OP1 Actually Proved",
            "metrics": [
                {"label": "Apps Delivered", "value": "9", "detail": "6 custom workflows your team uses daily"},
                {"label": "Users on SIPR", "value": "200+", "detail": "Cleared analysts across Donovan"},
                {"label": "ATO Status", "value": "Active", "detail": "No gaps through Aug 2026"},
                {"label": "Production Ready", "value": "4 in v1", "detail": "2 more graduating this period"},
            ],
        },

        # ── 5. Six tools your analysts rely on ────────────────────────
        {
            "layout": "content",
            "title": "Six Tools Your Analysts Rely On",
            "bullets": [
                "Threat Hunt — Ask a question in English, get a sourced RFI draft back in seconds",
                "IR Review — Drop a tipper CSV, get incident intelligence with patterns surfaced",
                "Historical Retro — One search across IRs, PULSE, ACE, and SIGACTS simultaneously",
                "CCIR Decision Support — Incidents checked against criteria: MET or NOT MET, no debate",
                "Site Risk Analysis — Risk rankings and heat maps, exportable on the spot",
            ],
        },

        # ── 6. Where we're taking you in OP2 ─────────────────────────
        {
            "layout": "two_column",
            "title": "Where We're Taking You in OP2",
            "left_title": "What Stays Solid",
            "left_bullets": [
                "All 9 apps sustained for 200+ users on SIPR",
                "Platform licenses, patches, and security current",
                "Monthly MTR / MFR — you always know where we stand",
                "ATO coverage continuous through Aug 2026",
            ],
            "right_title": "What Levels Up",
            "right_bullets": [
                "IR Review & INTEL Agent promoted from v0 to v1",
                "ServiceNow data connection goes live (pending CCB)",
                "Up to 3 new apps if CLIN 0013 is exercised",
                "Scoping starts for OP3 growth opportunities",
            ],
        },

        # ── 7. The plan, on one page ─────────────────────────────────
        {
            "layout": "gantt",
            "title": "The Plan, on One Page",
            "subtitle": "Valley of Fire · Project ASCEND · HC1084-25-0001",
            "quarters": ["Q1 2026", "Q2 2026", "Q3 2026"],
            "months": ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
            "phases": [
                "App Maturity",
                "Data & Integration",
                "Platform Sustainment",
                "Program Deliverables",
                "Optional / Growth",
            ],
            "tasks": [
                ("App Maturity", "IR Review & INTEL Agent v0 → v1", 0, 1, False, "1 Mar 2026"),
                ("Data & Integration", "ServiceNow data connection", 0, 3, False, "Upon CCB"),
                ("Data & Integration", "New data connections (OP3)", 4, 6, False, None),
                ("Platform Sustainment", "9-app sustainment + platform updates", 0, 6, False, None),
                ("Program Deliverables", "OP2 PoC Plan", 0, 0, True, "20 Feb 2026"),
                ("Program Deliverables", "OP2 Closeout & Dataset Transition", 2, 3, False, "14 May 2026"),
                ("Program Deliverables", "OP3 Closeout & Dataset Transition", 5, 6, False, "14 Aug 2026"),
                ("Program Deliverables", "Monthly MTR / MFR", 0, 6, False, "7 Feb 2026"),
                ("Optional / Growth", "New app scoping (CLIN 0013)", 4, 6, False, None),
                ("Optional / Growth", "Up to 3 new apps delivered", 5, 6, False, "14 Aug 2026"),
            ],
        },

        # ── 8. What we owe you, and when ─────────────────────────────
        {
            "layout": "table",
            "title": "What We Owe You, and When",
            "headers": ["Deliverable", "Owner", "Due Date"],
            "rows": [
                ["OP2 PoC Plan", "Scale", "20 Feb 2026"],
                ["IR Review & INTEL Agent → v1", "Scale", "NLT 14 days post award"],
                ["ServiceNow Integration", "Scale + Gov POC", "Upon CCB approval"],
                ["Monthly MTR / MFR", "Scale", "Monthly (starting 7 Feb)"],
                ["OP2 Closeout & Dataset Transition", "Scale", "14 May 2026"],
            ],
        },

        # ── 9. How we'll know this worked ────────────────────────────
        {
            "layout": "content",
            "title": "How We'll Know This Worked",
            "bullets": [
                "Your analysts stop context-switching between six tools",
                "IR Review and INTEL Agent are in production — not waiting on a demo",
                "ServiceNow tickets flow without manual re-entry",
                "Monthly reviews surface problems before they become surprises",
                "We walk into OP3 with a clear path and options on the table",
            ],
        },

        # ── 10. What we need from each other ─────────────────────────
        {
            "layout": "two_column",
            "title": "What We Need From Each Other",
            "left_title": "From Us",
            "left_bullets": [
                "Demo IR Review & INTEL Agent for v1 sign-off",
                "Unblock ServiceNow data connection end-to-end",
                "Monthly MTR / MFR with no surprises",
                "Proactive scoping for optional CLIN 0013 apps",
            ],
            "right_title": "From You",
            "right_bullets": [
                "CCB approval for ServiceNow integration",
                "Stakeholder availability for app demos",
                "Decision on CLIN 0013 — exercise or defer",
                "Feedback loops that keep us pointed right",
            ],
        },

        # ── 11. Closing ──────────────────────────────────────────────
        {
            "layout": "title",
            "title": "We're in This With You",
            "subtitle": "Scale AI · Project ASCEND",
        },
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate VoF OP2 Kickoff v2 (creative)")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
