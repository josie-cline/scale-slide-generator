#!/usr/bin/env python3
"""
EM Quick-Start: Valley of Fire OP2 Customer Kickoff
Data: GDrive (OP1 Summary) + local (roadmap, PoC plan, MSR)
Standalone — no repo changes. Output: EM_OP2_Kickoff_dark.pptx
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "EM_OP2_Kickoff",
    "slides": [
        {"layout": "title", "title": "Valley of Fire · OP2 Kickoff", "subtitle": "Project ASCEND · HC1084-25-0001 · Scale AI"},
        {"layout": "section", "title": "Agenda"},
        {
            "layout": "content",
            "title": "Today's Agenda",
            "bullets": [
                "Engagement at a Glance",
                "OP1 Wins vs Outstanding",
                "Platform: 9 Apps",
                "OP2 Scope",
                "Blockers & Dependencies",
                "Roadmap",
                "What I Need From You",
            ],
        },
        {"layout": "section", "title": "Engagement at a Glance"},
        {
            "layout": "metrics",
            "title": "Project ASCEND: 9 Apps, 200 Users, 3-Month OP2 Window",
            "metrics": [
                {"label": "Contract", "value": "HC1084-25-0001", "detail": "Project ASCEND"},
                {"label": "OP2 PoP", "value": "Feb 15 – May 14", "detail": "3 months"},
                {"label": "Apps", "value": "9", "detail": "6 custom + 3 base"},
                {"label": "Users", "value": "200+", "detail": "Donovan on SIPR"},
            ],
        },
        {"layout": "section", "title": "OP1 Delivered"},
        {
            "layout": "two_column",
            "title": "OP1 Delivered — 4 in Production, 2 Awaiting Demo",
            "left_title": "What We Shipped",
            "left_bullets": [
                "Analysts drowning in data — we deployed RAG to automate extraction",
                "6 custom apps to DISA-PAC and DISA-EUR; ATO-C through Aug 2026",
                "4 in v1: Threat Hunt, Historical Retro, CCIR, Site Risk",
                "Natural language queries across IRs, PULSE, ACE, SIGACTS",
            ],
            "right_title": "Outstanding",
            "right_bullets": [
                "IR Review & INTEL Agent — v0, awaiting demo; promote to v1 post-feedback",
                "ServiceNow integration — blocked on DISA CCB; architecture ready",
                "Written feedback for Apps 5 & 9 — required within 5 business days of award",
            ],
        },
        {"layout": "section", "title": "Platform Capabilities"},
        {
            "layout": "content",
            "title": "6 Custom Apps + 3 Base: RAG Across IRs, PULSE, ACE, SIGACTS",
            "bullets": [
                "Threat Hunt (RFI) — RFI drafts with citations; replaces manual from-scratch discovery",
                "IR Review — Tipper/ticket CSV → threat indicators and hunt intelligence",
                "Historical Retro — Natural language search across disparate datasets",
                "CCIR Decision Support — Incident vs CCIR criteria; MET/NOT MET determination",
                "Site Risk Analysis — Risk ranking, heat map; CSV/XML/JSON for mission assurance",
                "INTEL Agent — IOC extraction, Splunk query generation from threat reports",
            ],
        },
        {"layout": "section", "title": "OP2 Scope"},
        {
            "layout": "content",
            "title": "OP2 Focus: Sustain 9 Apps, Mature Apps 5 & 9, Unblock ServiceNow",
            "bullets": [
                "Sustain 9 apps for 200 users on SIPR",
                "IR Review & INTEL Agent v0→v1 — NLT 14 days post award",
                "ServiceNow live integration upon Government POC approval",
                "Optional: up to 3 new apps (CLIN 0013) if exercised",
            ],
        },
        {"layout": "section", "title": "Blockers"},
        {
            "layout": "table",
            "title": "Three Blockers Must Clear for OP2 Success",
            "headers": ["Blocker", "Status", "Owner", "Action"],
            "rows": [
                ["ServiceNow CCB approval", "Blocked", "Gov POC", "Designate POC; unblock integration"],
                ["App 5 & 9 demos", "Pending", "Scale", "Schedule with DISA Global / DISA-EUR"],
                ["v0→v1 written feedback", "Pending", "Gov", "Provide within 5 business days of award"],
            ],
        },
        {"layout": "section", "title": "Roadmap"},
        {
            "layout": "gantt",
            "title": "OP2 & OP3 Roadmap: Feb – Aug 2026",
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
        {"layout": "section", "title": "Deliverables"},
        {
            "layout": "table",
            "title": "Key Deliverables: PoC Plan, v1 Refinements, ServiceNow, Closeout",
            "headers": ["Deliverable", "Due Date"],
            "rows": [
                ["OP2 PoC Plan", "20 Feb 2026"],
                ["Apps 5 & 9 v0→v1 refinements", "NLT 14 days post award"],
                ["ServiceNow live data integration", "Upon Gov POC approval"],
                ["Monthly MTR / MFR", "Monthly"],
                ["OP2 Closeout", "14 May 2026"],
            ],
        },
        {"layout": "section", "title": "What I Need From You"},
        {
            "layout": "content",
            "title": "To Hit OP2 Targets, I Need Three Things From You",
            "bullets": [
                "Written feedback for IR Review & INTEL Agent — within 5 business days of award",
                "ServiceNow POC designation — to unblock integration architecture validation",
                "Demo availability — schedule IR Review (DISA Global) and INTEL Agent (DISA-EUR)",
            ],
        },
        {"layout": "title", "title": "Thank You", "subtitle": "Scale AI · Project ASCEND"},
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate EM OP2 Kickoff deck (standalone)")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
