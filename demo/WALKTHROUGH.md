# Demo Walkthrough: Cradle to Grave

This guide walks through the complete workflow — from installing Cursor to holding a finished slide deck. Follow each step in order. Total time: ~5 minutes.

---

## Prerequisites

- macOS, Windows, or Linux
- Python 3.9+
- A GitHub account
- Internet connection (for cloning and installing packages)

---

## Step 1: Install Cursor

1. Go to [cursor.com](https://cursor.com) and download the installer for your OS
2. Install and launch Cursor
3. Sign in with your account (GitHub SSO works)

> Cursor is a fork of VS Code with built-in AI. If you've used VS Code, the interface will be familiar.

---

## Step 2: Clone the Repo

Open Cursor's integrated terminal (`Ctrl+`` ` or `Cmd+`` `) and run:

```bash
git clone https://github.com/josie-cline/scale-slide-generator.git
```

Then open the folder in Cursor:
- **File > Open Folder** and select `scale-slide-generator`

Cursor will automatically detect the `.cursor/rules/` directory. This gives the AI full context about the project — what generators exist, how to run them, and what the output looks like.

---

## Step 3: Install Dependencies

In the terminal:

```bash
pip install -r requirements.txt
```

This installs `python-pptx` (PowerPoint generation) and `python-docx` (Word document generation). That's it — no complex setup, no databases, no API keys.

---

## Step 4: Explore with Ask Mode (Planning)

Before generating anything, use **Ask mode** to understand what's available and plan your approach.

### Switch to Ask mode

In the Cursor chat panel, click the mode selector (bottom of chat) and choose **Ask**.

### Try these prompts

**Prompt 1: Discover what's available**

```
What slide generators are available in this project? What does each one produce?
```

The AI will explain the four generators (VoF roadmap, VoF MSR, DLA roadmap, DLA PoC Plan), what each outputs, and how to run them.

**Prompt 2: Plan your task**

```
I need to generate a VoF OP2/OP3 roadmap slide. What data does the generator use and what would I need to change if the timeline shifted?
```

The AI will walk you through the `TASKS` list, the `MONTHS` array, and the `QUARTERS` array — the three places where roadmap data lives. It will explain the tuple format and how start/end month indices map to the timeline.

**Prompt 3: Understand themes**

```
What's the difference between dark and light themes? Can I preview both?
```

The AI will describe the color palettes and tell you how to generate both with `--theme dark` and `--theme light`.

> **Why Ask mode?** Ask mode is read-only — the AI can explore the codebase and explain everything without changing any files. It's the right tool for understanding a new project or planning a task before you execute.

---

## Step 5: Generate Slides (Agent Mode)

Now switch to **Agent mode** to generate the actual slides.

### Switch to Agent mode

Click the mode selector and choose **Agent** (or **Normal**).

### Generate the VoF roadmap in dark mode

**Prompt:**

```
Generate the VoF OP2/OP3 roadmap slide in dark mode.
```

**What happens:** The AI runs `python3 vof/generate_vof_roadmap.py --theme dark` and confirms the output path.

**Open the result:**

```bash
open vof/output/VoF_Roadmap_OP2_OP3_dark.pptx
```

### Generate the same roadmap in light mode

**Prompt:**

```
Now generate the same roadmap in light mode.
```

**What happens:** The AI runs the same script with `--theme light`. You now have both versions side by side.

---

## Step 6: Customize Content

This is where the time savings become obvious. Instead of manually editing PowerPoint shapes, you describe the change in plain English.

### Add a new task

**Prompt:**

```
Add a new task to the VoF roadmap: "ServiceNow Integration Testing" under Data & Integration, spanning March through April, with due date "30 Apr 2026". Then regenerate both dark and light themes.
```

**What happens:** The AI:
1. Opens `vof/generate_vof_roadmap.py`
2. Adds a new entry to the `TASKS` list
3. Runs the generator twice (dark and light)
4. Confirms both output files

### Modify existing tasks

**Prompt:**

```
Change the "OP2 Closeout" due date from "14 May 2026" to "21 May 2026" and regenerate in dark mode.
```

### Generate a completely different program's roadmap

**Prompt:**

```
Generate the DLA ASCEND roadmap in both dark and light mode.
```

---

## Step 7: Generate Documents

Slide decks aren't the only output. The same workflow applies to Word documents.

**Prompt:**

```
Generate the VoF monthly status report.
```

**What happens:** The AI runs `python3 vof/generate_vof_msr.py`, which copies the Scale AI DISA template and fills in the current reporting period's content.

---

## Step 8: Review and Deliver

Open the generated files:

```bash
# Roadmaps
open vof/output/VoF_Roadmap_OP2_OP3_dark.pptx
open vof/output/VoF_Roadmap_OP2_OP3_light.pptx

# DLA
open dla_ascend/output/DLA_Roadmap_OP2_OP3_dark.pptx

# MSR
open vof/VoF_Monthly_Status_Report_16Jan-14Feb_2026.docx
```

The files are ready for presentation — no manual formatting required.

---

## Time Comparison

| Task | Manual (PowerPoint) | With Cursor |
|------|-------------------|-------------|
| Create a roadmap slide from scratch | 2-3 hours | ~30 seconds |
| Update 3 task dates and regenerate | 20-30 minutes | ~15 seconds |
| Generate both dark and light versions | Double the above | One extra prompt |
| Add a new task row with Gantt bar | 15-20 minutes | ~10 seconds |
| Generate monthly status report | 1-2 hours | ~10 seconds |

---

## Tips for Effective Prompting

1. **Be specific about the program** — Say "VoF roadmap" or "DLA roadmap", not just "roadmap"
2. **Specify the theme** — Include "dark mode" or "light mode" in your prompt
3. **Describe data changes precisely** — Give exact task names, date ranges, and due dates
4. **Ask the AI to regenerate after changes** — It won't auto-run the script unless you tell it to
5. **Use Ask mode first** if you're unsure what to change — it'll point you to the right code without modifying anything

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'pptx'` | Run `pip install -r requirements.txt` |
| Output file won't open | Close any existing open copy of the file first |
| AI doesn't know about the generators | Make sure you opened the `scale-slide-generator` folder (not a parent directory) so `.cursor/rules/` is detected |
| Want to add a new color theme | Ask the AI: *"Add a 'navy' theme to the VoF roadmap generator with navy blue headers and gold accents"* |
