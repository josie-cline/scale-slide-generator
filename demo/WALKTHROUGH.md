# Demo Walkthrough: Cradle to Grave

Generate a complete styled slide deck from a natural-language description. This guide walks through every step — from installing Cursor to holding a finished `.pptx`. Total time: ~5 minutes.

---

## Prerequisites

- macOS, Windows, or Linux
- Python 3.9+
- A GitHub account

---

## Step 1: Install Cursor

1. Go to [cursor.com](https://cursor.com) and download the installer
2. Install and launch
3. Sign in (GitHub SSO works)

> Cursor is a fork of VS Code with built-in AI. If you've used VS Code, the interface is familiar.

---

## Step 2: Clone the Repo

Open the integrated terminal (`` Ctrl+` `` or `` Cmd+` ``):

```bash
git clone https://github.com/josie-cline/scale-slide-generator.git
```

Open the folder: **File > Open Folder** > select `scale-slide-generator`.

Cursor automatically picks up the `.cursor/rules/` directory, giving the AI full context about the available slide layouts, commands, and project structure.

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Installs `python-pptx` and `python-docx`. No APIs, no databases.

---

## Step 4: Explore with Ask Mode

Switch to **Ask mode** in the chat panel. This is read-only — the AI explores and explains without changing files.

### Example prompts

**What can this tool do?**

```
What slide layouts are supported and what data does each one need?
```

**Plan a deck:**

```
I need a 6-slide presentation for a program kickoff. What layouts should I use and what information do I need to provide?
```

**Understand theming:**

```
How do I generate in dark vs light mode? Can I add a custom theme?
```

---

## Step 5: Build Your Deck (Agent Mode)

Switch to **Agent mode**. Now describe your presentation:

**Prompt:**

```
Create a deck called "Program_Kickoff" with these slides:

1. Title slide: "Program Kickoff" with subtitle "Scale AI · March 2026"
2. Section divider: "Mission & Objectives"
3. Content slide titled "Program Goals" with bullets:
   - Deploy platform to production within 90 days
   - Onboard 150+ users across 3 divisions
   - Deliver 4 workflow applications
   - Achieve ATO by end of Q2
4. Two-column slide titled "Approach" comparing:
   Left "Current State": Manual processes, 3-day turnaround, Siloed data
   Right "Target State": Automated workflows, Real-time access, Unified platform
5. Metrics slide titled "Success Criteria" with:
   - Users: 150+, detail: across 3 divisions
   - Apps: 4, detail: by end of OP1
   - Uptime: 99.5%, detail: SLA target
6. Table slide titled "Milestones" with columns Milestone, Date, Status:
   - Kickoff Meeting, 1 Mar 2026, Complete
   - Environment Setup, 15 Mar 2026, In Progress
   - App 1 Delivery, 15 Apr 2026, Planned
   - ATO Submission, 1 Jun 2026, Planned

Generate in both dark and light mode.
```

**What happens:** Cursor updates the `DECK` dict in `generate_deck.py` and runs it twice.

### Open the results

```bash
open output/Program_Kickoff_dark.pptx
open output/Program_Kickoff_light.pptx
```

---

## Step 6: Make Changes

Describe changes in plain English instead of editing PowerPoint by hand.

### Add a slide

```
Add a gantt slide at the end with title "90-Day Roadmap", months Mar through Jun, and these tasks:
- Setup: Environment provisioning, Mar
- Development: App 1 build, Mar-Apr
- Development: App 2 build, Apr-May
- Testing: User acceptance, May-Jun, due 15 Jun 2026
Regenerate dark mode.
```

### Edit existing content

```
Change the uptime SLA from 99.5% to 99.9% on the metrics slide. Regenerate both themes.
```

### Add a slide type

```
Add a content slide after the section divider titled "Team" with bullets listing 4 team members and their roles. Regenerate dark.
```

---

## Step 7: Status Reports (Optional)

For Word document generation:

```
Inspect the template at templates/example_msr_template.docx so I can see its structure.
```

The AI runs `--inspect`, shows paragraph indices, and you provide the updates for your reporting period.

---

## Step 8: Deliver

```bash
open output/Program_Kickoff_dark.pptx
```

The file is ready for presentation — consistent styling, no manual formatting.

---

## Time Comparison

| Task | Manual (PowerPoint) | With Cursor |
|------|-------------------|-------------|
| Build a 6-slide deck from scratch | 2-4 hours | ~1 minute |
| Add a new slide | 15-30 minutes | ~15 seconds |
| Generate dark + light versions | Double the time | One extra prompt |
| Change content across 3 slides | 15-20 minutes | ~10 seconds |
| Restyle entire deck | Start over | Change `--theme` flag |

---

## Tips

1. **Give all your content in one prompt** — Title, bullets, metrics, table data. The more you provide upfront, the fewer follow-ups needed.
2. **Specify the theme** — Say "dark mode", "light mode", or "both"
3. **Use Ask mode first** if you're unsure what layouts to use
4. **Reference layouts by name** — `title`, `section`, `content`, `two_column`, `metrics`, `table`, `gantt`
5. **Ask for both themes** at the end to get two versions with one prompt

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'pptx'` | `pip install -r requirements.txt` |
| Output won't open | Close any existing copy of the file |
| AI doesn't recognize the project | Open `scale-slide-generator` as the workspace root |
| Need a layout that doesn't exist | *"Add a new layout called 'image_caption' that shows..."* |
| Want custom colors | *"Add a 'navy' theme with dark navy backgrounds and gold accents"* |
