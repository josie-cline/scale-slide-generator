#!/usr/bin/env python3
"""
Standalone Valley of Fire OP2 Kickoff deck generator.
Uses generate_deck tooling — no repo changes. Output: Valley_of_Fire_OP2_Kickoff_{theme}.pptx

Run from project root:
    python3 output/run_vof_deck.py
    python3 output/run_vof_deck.py --theme light
"""
import argparse
import sys
from pathlib import Path

# Allow importing generate_deck from project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Valley_of_Fire_OP2_Kickoff",
    "slides": [
        {"layout": "title", "title": "Valley of Fire · OP2 Kickoff", "subtitle": "Project ASCEND · HC1084-25-0001 · Scale AI"},
        {"layout": "section", "title": "Agenda"},
        {
            "layout": "content",
            "title": "Today's Agenda",
            "bullets": [
                "Project Overview",
                "OP1 Wins",
                "OP2 Objectives",
                "Platform & Apps",
                "Roadmap",
                "Success Criteria",
            ],
        },
        {"layout": "section", "title": "The Opportunity"},
        {
            "layout": "two_column",
            "title": "Challenge & Solution",
            "left_title": "The Challenge",
            "left_bullets": [
                "Drowning in data across disparate sources",
                "Manual sifting through IRs, PULSE, ACE, SIGACTS",
                "Analyst overload — hours per RFI and report",
                "No unified view for CCIR or site risk",
            ],
            "right_title": "The Solution",
            "right_bullets": [
                "RAG-enabled knowledge bases across sources",
                "Natural language queries for rapid discovery",
                "Reduced burden — seconds instead of hours",
                "Pre-formatted outputs for Splunk, CCIR, mission assurance",
            ],
        },
        {"layout": "section", "title": "OP1 Delivered"},
        {
            "layout": "metrics",
            "title": "OP1 Key Metrics",
            "metrics": [
                {"label": "Apps Delivered", "value": "9", "detail": "6 custom + 3 base"},
                {"label": "Users Supported", "value": "200+", "detail": "Donovan on SIPR"},
                {"label": "ATO Status", "value": "Active", "detail": "Through Aug 2026"},
                {"label": "Production Apps", "value": "4 in v1", "detail": "2 in v0 awaiting demo"},
            ],
        },
        {"layout": "section", "title": "Platform Capabilities"},
        {
            "layout": "content",
            "title": "Workflow Applications",
            "bullets": [
                "Threat Hunt (RFI) — Natural language RFI response drafts with citations",
                "IR Review — Tipper/ticket CSV analysis for incident intelligence",
                "Historical Retro — Cross-source search across IRs, PULSE, ACE, SIGACTS",
                "CCIR Decision Support — Incident vs CCIR criteria with MET/NOT MET",
                "Site Risk Analysis — Risk ranking and heat map with CSV/XML/JSON export",
                "INTEL Agent — IOC extraction and Splunk query generation from threat reports",
            ],
        },
        {"layout": "section", "title": "OP2 Focus"},
        {
            "layout": "content",
            "title": "OP2 Objectives",
            "bullets": [
                "Sustain 9 apps for 200 users on SIPR",
                "Advance IR Review & INTEL Agent from v0 → v1",
                "Complete ServiceNow integration upon CCB approval",
                "Optional: up to 3 new apps (CLIN 0013) if exercised",
            ],
        },
        {"layout": "section", "title": "Roadmap"},
        {
            "layout": "gantt",
            "title": "Project Roadmap: OP2 & OP3",
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
                ("App Maturity", "IR Review & INTEL Agent v0→v1", 0, 1, False, "1 Mar 2026"),
                ("Data & Integration", "Complete ServiceNow data connection", 0, 3, False, "TBD"),
                ("Data & Integration", "New data connections (OP3 optional)", 4, 6, False, None),
                ("Platform Sustainment", "Platform licenses, updates & 9-app sustainment", 0, 6, False, None),
                ("Program Deliverables", "OP2 PoC Plan", 0, 0, True, "20 Feb 2026"),
                ("Program Deliverables", "OP2 Closeout & Dataset Transition", 2, 3, False, "14 May 2026"),
                ("Program Deliverables", "OP3 Closeout & Dataset Transition", 5, 6, False, "14 Aug 2026"),
                ("Program Deliverables", "Monthly MTR / MFR", 0, 6, False, "7 Feb 2026"),
                ("Optional / Growth", "Scoping for new applications", 4, 6, False, None),
                ("Optional / Growth", "Up to 3 new apps (CLIN 0013)", 5, 6, False, "14 Aug 2026"),
            ],
        },
        {"layout": "section", "title": "Key Deliverables"},
        {
            "layout": "table",
            "title": "OP2 Deliverables",
            "headers": ["Deliverable", "Owner", "Due Date"],
            "rows": [
                ["OP2 PoC Plan", "Scale", "20 Feb 2026"],
                ["Apps 5 & 9 v0→v1", "Scale", "NLT 14 days post award"],
                ["ServiceNow Integration", "Scale / Gov POC", "Upon CCB approval"],
                ["Monthly MTR / MFR", "Scale", "Monthly"],
                ["OP2 Closeout", "Scale", "14 May 2026"],
            ],
        },
        {"layout": "section", "title": "Success Criteria"},
        {
            "layout": "content",
            "title": "Success Criteria",
            "bullets": [
                "Platform stability maintained for all 9 apps",
                "End-user access and adoption sustained",
                "ServiceNow live upon CCB approval",
                "Apps 5 & 9 promoted to v1 post-demo",
                "Clear path to OP3 with optional CLINs defined",
            ],
        },
        {"layout": "section", "title": "Next Steps"},
        {
            "layout": "content",
            "title": "Immediate Actions",
            "bullets": [
                "Confirm v0→v1 scope for IR Review & INTEL Agent",
                "Schedule demos for Apps 5 & 9",
                "Unblock ServiceNow CCB approval",
                "Align on optional CLINs (0013/0014) if exercised",
            ],
        },
        {"layout": "title", "title": "Thank You", "subtitle": "Scale AI · Project ASCEND"},
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Valley of Fire OP2 Kickoff deck (standalone)")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
