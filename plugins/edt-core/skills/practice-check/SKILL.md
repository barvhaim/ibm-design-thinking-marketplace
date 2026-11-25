---
name: practice-check
description: Audit a project against IBM Enterprise Design Thinking. Scores the three Principles, Loop coverage, the three Keys and the reliance on simulated users, using the repo, the design-thinking/ artifacts, PRDs, specs, roadmaps or backlogs. It recommends the highest-impact fixes in an HTML artifact. Use when someone asks "are we doing design thinking right", "review our PRD or roadmap from a user perspective", "how user-centered is this plan", or "what are we missing".
argument-hint: "[path to PRD, spec or roadmap]"
---

# Practice check

> IBM Enterprise Design Thinking · Framework · Reflect · ~20 min

This skill holds up a mirror: it shows how well the team's actual artifacts reflect EDT. It isn't a compliance gate. It finds the one or two gaps that most threaten user outcomes.

## Inputs
- Everything in `design-thinking/`. Read each page's `#edt-data`, including the `items` tags.
- Any documents the user names in `$ARGUMENTS`, such as a PRD, spec, roadmap, backlog export or README.
- If the user names nothing, look for likely files (`docs/`, `*.md`, PRD or spec names) and ask before you read widely.

## Co-create with Claude
1. **Collect evidence.** Read the artifacts. For every judgment, cite the file and the passage. If something is absent, record it as "no evidence found". Don't assume it's missing in reality, because the team may simply not have written it down.
2. **Score each dimension from 0 to 3.** 0 = absent, 1 = mentioned, 2 = practiced, 3 = practiced and recurring.
   - **Principles**
     - **User outcomes:** Are the goals written as what users achieve, or as features shipped? Does the plan separate users from clients? Is there a user-outcome metric?
     - **Restless reinvention:** Are there prototypes, tests and iterations? Or is the plan one big waterfall bet?
     - **Diverse empowered teams:** Is the team cross-functional? Does it have the authority to decide?
   - **The Loop**
     - **Observe:** real user research with dates and sources.
     - **Reflect:** synthesis, alignment and plans.
     - **Make:** concepts, prototypes, shipped increments.
     - Flag analysis paralysis: a lot of observing and reflecting, but nothing made.
   - **Simulation reliance:** count the items by tag across the workspace. Then check whether any Hill, priority or go/no-go decision rests mainly on `simulated` items. Heavy simulation is fine early on, but not at a commitment point.
   - **The Keys**
     - **Hills:** Who/What/Wow, three or fewer plus a Foundation, and free of implementation details.
     - **Sponsor users:** named, recurring, at least one per Hill.
     - **Playbacks:** scheduled at milestones, with feedback recorded.
3. **Find the gaps.** Rank the top 3 by risk to user outcomes. For each, recommend the specific activity that would close it, with its command.
4. **Rewrite one thing.** Show one quick win. For example, rewrite a feature-style goal from the PRD as a draft Hill, and label it as a draft that needs validating.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/practice-check-<date>.html`.
- **Title:** `<Project> Practice Check`.
- **Sections:**
  1. **Scorecard:** a table of dimension, score (0–3, `td.num`), status pill and evidence (the file and passage).
  2. **Evidence balance:** a table of items by tag for each page, and a sentence naming the decisions that rest on simulated items.
  3. **Top gaps:** `.frames`, one per gap, with the risk and the command that closes it.
  4. **Quick win:** before and after, as two `.note.wide` notes. Tag the "after" `assumption`, because it needs validating.
  5. **Playback.**
- **`content` in `#edt-data`:** `{ "scores": {"user_outcomes": 0, "restless_reinvention": 0, "diverse_teams": 0, "observe": 0, "reflect": 0, "make": 0, "hills": 0, "sponsor_users": 0, "playbacks": 0}, "balance": {"evidence": 0, "simulated": 0, "assumption": 0, "question": 0}, "gaps": [{"gap": "", "risk": "", "command": ""}], "quick_win": {"before": "", "after": ""} }`

## Quality checks
- Every score cites evidence, or says "no evidence found".
- The recommendations are few and specific. The team should be able to start within a week.
- The tone is that of a coach, not an auditor.

## Next
- `/edt-core:guide`: talk through the path the recommendations suggest.
- `/edt-core:workshop-planner`: close several gaps in one session.

## Source
[IBM Enterprise Design Thinking: Framework](https://www.ibm.com/training/enterprise-design-thinking/framework)
