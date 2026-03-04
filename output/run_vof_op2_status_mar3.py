#!/usr/bin/env python3
"""
VoF OP2 Status — March 3, 2026
Current state of Project ASCEND heading into demo week.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "VoF_OP2_Status_Mar3",
    "slides": [
        {
            "layout": "title",
            "title": "Valley of Fire · OP2 Status",
            "subtitle": "Project ASCEND · Week of March 3, 2026 · Scale AI",
        },
        {
            "layout": "metrics",
            "title": "OP2 Snapshot: 17 Days In",
            "metrics": [
                {"label": "OP2 Day", "value": "17", "detail": "of 88 · Feb 15 – May 14"},
                {"label": "Active Users", "value": "200+", "detail": "Donovan on SIPR"},
                {"label": "Apps Live", "value": "9", "detail": "4 in v1 · 2 in v0"},
                {"label": "Days to OP2 Close", "value": "71", "detail": "May 14, 2026"},
            ],
        },
        {
            "layout": "section",
            "title": "This Week",
        },
        {
            "layout": "table",
            "title": "Three Demos on the Calendar — All on SIPR",
            "headers": ["Meeting", "Date / Time", "Audience", "Focus"],
            "rows": [
                ["ASCEND AI Use Cases Demo", "Mar 4 · 0900 EST", "DISA EUCOM, DISA Stuttgart", "CCIR, Mission Assurance, DCO"],
                ["ASCEND Demo – DISA Global", "Mar 4 · 1300 EST", "DISA Global FC + OCTO", "Threat Hunt, IR Review"],
                ["ASCEND Demo – DISA Pacific", "Mar 4 · 1500 EST", "DISA INDOPACOM FC", "Site Risk, INTEL Agent"],
            ],
        },
        {
            "layout": "section",
            "title": "Open Issues",
        },
        {
            "layout": "table",
            "title": "Three Items Need Resolution This Week",
            "headers": ["Issue", "Status", "Owner", "Next Action"],
            "rows": [
                ["PRD: INTEL Agent & IR Review v0→v1", "At Risk", "Josiah / PMO", "Respond to Deepak by Mar 4 AM with feedback ETA"],
                ["DISA scope change request", "Blocked", "Kyle Cadwallader (PMO)", "Confirmed out of scope for CLIN 0004/0008 — requires CLIN 0013 mod"],
                ["Nisha Chandra transition", "Pending", "Mel Redd", "Follow up if no response by EOD Mar 4"],
            ],
        },
        {
            "layout": "section",
            "title": "PRD Situation",
        },
        {
            "layout": "two_column",
            "title": "DISA Scope Dispute — Scale's Position is Clear",
            "left_title": "What DISA Asked",
            "left_bullets": [
                "Replace INTEL Agent + IR Review PRDs",
                "New app: 'Retrospective Threat Correlation Engine'",
                "Scope change submitted mid-PRD review cycle",
                "Deepak Seth requesting Scale feedback by Mar 4",
            ],
            "right_title": "Scale's Position",
            "right_bullets": [
                "New app is out of scope for CLIN 0004 and CLIN 0008",
                "PMO (Kyle) confirmed in writing — contract language is clear",
                "Would require a CLIN 0013 contract modification to proceed",
                "INTEL Agent + IR Review PRDs remain the deliverable",
            ],
        },
        {
            "layout": "section",
            "title": "Roadmap",
        },
        {
            "layout": "gantt",
            "title": "OP2 Roadmap: Feb – May 2026",
            "subtitle": "Valley of Fire · Project ASCEND · HC1084-25-0001",
            "quarters": ["Q1 2026", "Q2 2026"],
            "months": ["Feb", "Mar", "Apr", "May"],
            "phases": [
                "App Maturity",
                "Data & Integration",
                "Platform Sustainment",
                "Program Deliverables",
            ],
            "tasks": [
                ("App Maturity", "IR Review & INTEL Agent v0→v1", 0, 1, False, "TBD post-PRD"),
                ("Data & Integration", "ServiceNow integration", 0, 3, False, "Upon CCB approval"),
                ("Platform Sustainment", "9-app sustainment + ATO-C maintenance", 0, 3, False, None),
                ("Program Deliverables", "OP2 PoC Plan", 0, 0, True, "20 Feb 2026"),
                ("Program Deliverables", "CLIN 0008 labor invoice", 0, 1, False, "Mar 2026"),
                ("Program Deliverables", "Monthly MTR / MFR", 0, 3, False, "Monthly"),
                ("Program Deliverables", "OP2 Closeout", 2, 3, False, "14 May 2026"),
            ],
        },
        {
            "layout": "section",
            "title": "Immediate Actions",
        },
        {
            "layout": "content",
            "title": "This Week's Must-Dos",
            "bullets": [
                "Mar 4 AM — Respond to Deepak with feedback ETA on INTEL Agent + IR Review PRDs",
                "Mar 4 — Attend and support all 3 ASCEND demos (SIPR)",
                "Mar 4 — Follow up with Mel Redd on Nisha Chandra transition if no response",
                "Mar 2026 — Submit CLIN 0008 labor invoice",
                "Ongoing — Align with Kyle Cadwallader on DISA scope change response",
            ],
        },
        {
            "layout": "title",
            "title": "Project ASCEND",
            "subtitle": "Valley of Fire · Scale AI · HC1084-25-0001",
        },
    ],
}

if __name__ == "__main__":
    main(theme_name="dark", deck=DECK)
