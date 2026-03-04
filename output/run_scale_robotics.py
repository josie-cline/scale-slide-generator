#!/usr/bin/env python3
"""
The Future of Scale AI & Its Impact on Robotics

Sources: Scale AI blog, Pelian AI, IDTechEx, TechFundingNews,
SiliconAngle, Breaking Defense, public financial data.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Scale_AI_Future_of_Robotics",
    "slides": [
        {
            "layout": "title",
            "title": "The Future of Scale AI\nin Robotics",
            "subtitle": "From Data Infrastructure to Physical Intelligence\nFebruary 2026",
            "notes": "Scale AI sits at the center of the AI revolution. This deck makes the case for why robotics is the company's next massive growth vector — and why the data infrastructure moat that won language AI will win physical AI too.",
        },

        {
            "layout": "section",
            "title": "The Physical AI Inflection Point",
            "notes": "We're at the same moment for robotics that we were at for LLMs in 2022. The models are ready. The hardware is ready. The bottleneck is data.",
        },

        {
            "layout": "metrics",
            "title": "Robotics is entering the same exponential curve LLMs hit in 2023",
            "metrics": [
                {"label": "Global Robotics Market", "value": "$108B", "detail": "2025, quadrupling to $416B by 2035"},
                {"label": "Physical AI Market", "value": "$30B+", "detail": "Projected annual by 2028"},
                {"label": "AI Robots Coming Online", "value": "400M", "detail": "Next 4 years"},
                {"label": "Scale AI Valuation", "value": "$29B", "detail": "Post-Meta stake (Jun 2025)"},
            ],
            "notes": "Four numbers that tell the story. The robotics market is $108B today and quadrupling. 400 million AI robots are projected to come online in 4 years. Scale's valuation nearly doubled when Meta took a 49% stake — the market is pricing in this physical AI future.",
        },

        {
            "layout": "two_column",
            "title": "Language AI trained on the internet — physical AI has no equivalent",
            "left_title": "Language AI (2020–2025)",
            "left_bullets": [
                "Trained on public internet text",
                "Data is abundant and cheap",
                "Single modality (text → text)",
                "Scale built the labeling layer",
                "Result: GPT-4, Claude, Gemini",
            ],
            "right_title": "Physical AI (2025–2030)",
            "right_bullets": [
                "Trained on proprietary sensor data",
                "Data is scarce and expensive",
                "Multimodal: video, LiDAR, 3D, telemetry",
                "Scale must build the curation layer",
                "Result: autonomous robots, vehicles, drones",
            ],
            "notes": "The key insight: LLMs had the internet. Physical AI has nothing equivalent. Every robot needs proprietary training data from its specific environment. This is why data infrastructure — not model architecture — is the bottleneck. And it's why Scale's moat transfers directly.",
        },

        {
            "layout": "section",
            "title": "The Robotics Landscape",
            "notes": "Who's building robots, and what do they all need from Scale?",
        },

        {
            "layout": "table",
            "title": "Every major robotics player needs training data at scale",
            "headers": ["Company", "Robot", "Status (2026)", "Scale AI Opportunity"],
            "rows": [
                ["Tesla", "Optimus Gen 3", "Production: 100K units targeted", "Manipulation & navigation data labeling"],
                ["Figure AI", "Figure 02", "BMW deployment, $39B valuation", "Sensor fusion annotation, eval"],
                ["Boston Dynamics", "Atlas (electric)", "30K/year production planned", "3D point cloud + video labeling"],
                ["Unitree", "R1 ($5,900)", "Mass market, backed by ByteDance", "Low-cost data pipelines at volume"],
                ["OpenAI", "Humanoid program", "Hiring roboticists, early stage", "RLHF for physical manipulation"],
                ["Amazon", "Digit (Agility)", "Warehouse deployment scaling", "Pick-and-place annotation"],
            ],
            "notes": "Six companies, six different robots, one common requirement: massive amounts of labeled sensor data. Tesla needs manipulation data for Optimus. Figure AI needs sensor fusion annotation. Boston Dynamics needs 3D labeling. Every row is a Scale customer opportunity.",
        },

        {
            "layout": "section",
            "title": "Scale's Data Moat in Physical AI",
            "notes": "What Scale already has and what it needs to build.",
        },

        {
            "layout": "content",
            "title": "Scale's existing data engine extends directly to robotics",
            "bullets": [
                "3D point cloud annotation — already production-grade for autonomous vehicles",
                "Video labeling at frame-level precision — transferable to robot vision",
                "Sensor fusion pipelines — LiDAR + camera + radar, same stack robots need",
                "RLHF infrastructure — proven on LLMs, applicable to robot policy learning",
                "Data curation at petabyte scale — the exact bottleneck physical AI faces",
                "Government & defense relationships — military robotics is a $50B+ market",
            ],
            "notes": "Scale isn't starting from zero. The autonomous vehicle data pipeline IS a robotics data pipeline. The RLHF infrastructure that trains language models can train robot policies. The defense relationships open military robotics. The moat is real.",
        },

        {
            "layout": "two_column",
            "title": "The competitive threat is real but navigable",
            "left_title": "Encord ($60M Series C, Feb 2026)",
            "left_bullets": [
                "Raised $110M total, $550M valuation",
                "Data volume: 1PB → 5PB in one year",
                "Clients: Toyota, Zipline, Skydio, AXA",
                "Positioning: 'built for physical AI'",
                "Advantage: specialist focus, faster iteration",
            ],
            "right_title": "Scale AI Response",
            "right_bullets": [
                "$29B valuation, Meta backing, 10x+ revenue",
                "Existing AV data engine is production-proven",
                "Government contracts create lock-in moat",
                "Full-stack: labeling + curation + eval + RLHF",
                "Advantage: scale, relationships, breadth",
            ],
            "notes": "Encord is the clearest competitive threat. They raised $60M in Feb 2026 specifically for physical AI data infrastructure. But Scale's advantages are structural: 50x the valuation, government lock-in, and a proven data engine that already handles the exact data types robots generate.",
        },

        {
            "layout": "section",
            "title": "Where Scale Wins",
            "notes": "Three strategic bets that turn Scale's data moat into robotics dominance.",
        },

        {
            "layout": "content",
            "title": "Three strategic bets for Scale in robotics",
            "bullets": [
                "1. Physical AI Data Engine — Extend the AV pipeline to humanoids, drones, and industrial robots. Multimodal annotation (video + LiDAR + telemetry + force/torque) as a platform.",
                "2. Robot RLHF — Apply reinforcement learning from human feedback to robot policy training. Teleoperation data collection + preference labeling for manipulation tasks.",
                "3. Simulation-to-Real Bridge — Synthetic data generation for robotic sim-to-real transfer. Partner with NVIDIA (Omniverse/Cosmos) and build the data quality layer on top.",
            ],
            "notes": "Three bets. The Data Engine is the foundation — it's the thing Scale already does. Robot RLHF is the differentiated play — nobody else has Scale's RLHF infrastructure. Sim-to-real is the force multiplier — synthetic data at Scale quality unlocks infinite training volume.",
        },

        {
            "layout": "metrics",
            "title": "The prize: Scale as the data backbone of the robot economy",
            "metrics": [
                {"label": "TAM by 2030", "value": "$50B+", "detail": "Physical AI data market"},
                {"label": "Robot Units", "value": "400M", "detail": "Coming online by 2030"},
                {"label": "Data per Robot", "value": "10TB+", "detail": "Annual training data needs"},
                {"label": "Scale's Position", "value": "#1", "detail": "Largest AI data company"},
            ],
            "notes": "If every robot needs 10+ TB of annotated training data per year, and 400M robots are coming online, the data infrastructure market is massive. Scale is already #1 in AI data. The question is whether it executes on physical AI before Encord or others eat the market.",
        },

        {
            "layout": "gantt",
            "title": "Scale AI Robotics Roadmap",
            "subtitle": "Projected Strategic Timeline",
            "quarters": ["2026", "2027", "2028"],
            "months": ["H1'26", "H2'26", "H1'27", "H2'27", "H1'28", "H2'28"],
            "phases": [
                "Data Engine",
                "Robot RLHF",
                "Sim-to-Real",
                "Market",
            ],
            "tasks": [
                ("Data Engine", "Extend AV pipeline to humanoids", 0, 1, False, None),
                ("Data Engine", "Multi-sensor annotation platform", 1, 3, False, None),
                ("Robot RLHF", "Teleop data collection tools", 0, 2, False, None),
                ("Robot RLHF", "Policy RLHF at scale", 2, 4, False, None),
                ("Sim-to-Real", "NVIDIA Cosmos integration", 1, 3, False, None),
                ("Sim-to-Real", "Synthetic data quality layer", 3, 5, False, None),
                ("Market", "First humanoid customer", 1, 1, True, None),
                ("Market", "$1B robotics ARR", 5, 5, True, None),
            ],
            "notes": "Three-year roadmap. The data engine extension happens first (H1 2026 — this is happening now). Robot RLHF and sim-to-real follow. The key milestones: first humanoid robot customer by H2 2026, and $1B robotics ARR by H2 2028.",
        },

        {
            "layout": "content",
            "title": "Scale AI doesn't build robots — it makes every robot smarter",
            "bullets": [
                "The company that labels the world's data will label the robot's world",
                "Physical AI's data bottleneck is Scale's language AI playbook, repeated",
                "The AV data engine is already 80% of what humanoid robots need",
                "RLHF for robots is the most defensible moat in the market",
                "The Meta partnership signals: Scale is infrastructure, not an app",
                "First mover in physical AI data wins the next decade",
            ],
            "notes": "Closing argument. Scale doesn't need to build robots. It needs to be the company that every robot builder depends on for data. That's the same playbook that made it essential to OpenAI, Google, and Meta for language AI. The physical AI version is bigger.",
        },
    ],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
