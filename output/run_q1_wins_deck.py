#!/usr/bin/env python3
"""
Standalone Q1 2026 Wins deck generator.
Uses generate_deck tooling — no repo changes. Output: Q1_2026_Wins_{theme}.pptx

Run from project root:
    python3 output/run_q1_wins_deck.py
    python3 output/run_q1_wins_deck.py --theme light
"""
import argparse
import sys
from pathlib import Path

# Allow importing generate_deck from project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Q1_2026_Wins",
    "slides": [
        {"layout": "title", "title": "Q1 2026 · Wins & What's Next", "subtitle": "Scale AI · Internal"},
        {"layout": "section", "title": "Agenda"},
        {
            "layout": "content",
            "title": "Today's Agenda",
            "bullets": [
                "Overview",
                "Key Metrics",
                "Product Highlights",
                "Customer Wins",
                "Roadmap",
                "Q&A",
            ],
        },
        {"layout": "section", "title": "The Shift"},
        {
            "layout": "two_column",
            "title": "Before Q1 vs After Q1",
            "left_title": "Before Q1",
            "left_bullets": [
                "Manual processes across workflows",
                "Siloed data and fragmented views",
                "Slow iteration cycles",
                "Reactive support model",
            ],
            "right_title": "After Q1",
            "right_bullets": [
                "Automated pipelines end-to-end",
                "Unified view across systems",
                "Rapid deployment cycles",
                "Proactive scaling and support",
            ],
        },
        {"layout": "section", "title": "Key Metrics"},
        {
            "layout": "metrics",
            "title": "Q1 2026 Highlights",
            "metrics": [
                {"label": "Revenue Growth", "value": "+32%", "detail": "YoY"},
                {"label": "New Customers", "value": "47", "detail": "This quarter"},
                {"label": "NPS", "value": "72", "detail": "Up from 65"},
                {"label": "Deployments", "value": "340", "detail": "This quarter"},
            ],
        },
        {"layout": "section", "title": "Product Highlights"},
        {
            "layout": "content",
            "title": "What We Shipped",
            "bullets": [
                "Donovan v2 launch — enterprise-grade RAG with new guardrails",
                "RAG pipeline 3x faster — sub-second retrieval at scale",
                "New compliance module — SOC 2, HIPAA, FedRAMP readiness",
            ],
        },
        {"layout": "section", "title": "Customer Wins"},
        {
            "layout": "table",
            "title": "Top 5 Customer Wins",
            "headers": ["Customer", "Use Case", "Impact", "Go-Live"],
            "rows": [
                ["Acme Corp", "Document intelligence", "40% faster processing", "Mar 2026"],
                ["Defense Inc", "Threat analysis", "Unified IR workflow", "Feb 2026"],
                ["HealthCo", "Clinical summaries", "Compliance-ready RAG", "Apr 2026"],
                ["FinServe", "Fraud detection", "Real-time alerts", "Mar 2026"],
                ["GovAgency", "Public records search", "10x query volume", "Jan 2026"],
            ],
        },
        {"layout": "section", "title": "Q2 Roadmap"},
        {
            "layout": "gantt",
            "title": "Q2 2026 Roadmap",
            "subtitle": "Scale AI · Internal",
            "quarters": ["Q2 2026"],
            "months": ["Apr", "May", "Jun"],
            "phases": ["Product", "GTM", "Ops"],
            "tasks": [
                ("Product", "Donovan v2.1 release", 0, 1, False, "15 May 2026"),
                ("Product", "Multi-region deployment", 1, 2, False, "30 Jun 2026"),
                ("GTM", "Q2 launch campaign", 0, 0, True, "1 Apr 2026"),
                ("GTM", "Enterprise sales enablement", 0, 2, False, None),
                ("Ops", "Infra scaling & monitoring", 0, 2, False, None),
                ("Ops", "Q2 closeout", 2, 2, True, "30 Jun 2026"),
            ],
        },
        {"layout": "title", "title": "Questions?", "subtitle": "Scale AI"},
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Q1 2026 Wins deck (standalone)")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
