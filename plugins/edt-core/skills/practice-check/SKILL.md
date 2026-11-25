---
name: practice-check
description: Audit a project against IBM Enterprise Design Thinking. Scores the three Principles, Loop coverage and the three Keys, using evidence from the repo, the design-thinking/ folder, PRDs, specs, roadmaps or backlogs, and recommends the highest-impact fixes. Use when someone asks "are we doing design thinking right", "review our PRD or roadmap from a user perspective", "how user-centered is this plan", or "what are we missing".
argument-hint: "[path to PRD, spec or roadmap]"
---

# Practice check

> IBM Enterprise Design Thinking · Framework · Reflect · ~20 min

This skill holds up a mirror: it shows how well the team's actual artifacts reflect EDT. It isn't a compliance gate. It finds the one or two gaps that most threaten user outcomes.

## Inputs
- Everything in `design-thinking/`.
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
   - **The Keys**
     - **Hills:** Who/What/Wow, three or fewer plus a Foundation, and free of implementation details.
     - **Sponsor users:** named, recurring, at least one per Hill.
     - **Playbacks:** scheduled at milestones, with feedback recorded.
3. **Find the gaps.** Rank the top 3 by risk to user outcomes. For each, recommend the specific activity that would close it, with its command.
4. **Rewrite one thing.** Show one quick win. For example, rewrite a feature-style goal from the PRD as a draft Hill, and label it as a draft that needs validating.

## Output
Save to `design-thinking/practice-check-<date>.md`:

```markdown
# Practice check: <project> (<date>)
Sources reviewed: …

## Scorecard
| Dimension | Score (0–3) | Evidence |
| --- | --- | --- |
| A focus on user outcomes | | |
| Restless reinvention | | |
| Diverse empowered teams | | |
| Observe | | |
| Reflect | | |
| Make | | |
| Hills | | |
| Sponsor Users | | |
| Playbacks | | |

## Top gaps
1. <gap>: risk: … → run `/<plugin>:<skill>`
2. …
3. …

## Quick win
Before: …
After (draft, needs validation): …

## Playback
- Key takeaways:
- Assumptions to validate:
- Next activity:
```

## Quality checks
- Every score cites evidence, or says "no evidence found".
- The recommendations are few and specific. The team should be able to start within a week.
- The tone is that of a coach, not an auditor.

## Next
- `/edt-core:guide`: talk through the path the recommendations suggest.
- `/edt-core:workshop-planner`: close several gaps in one session.

## Source
[IBM Enterprise Design Thinking: Framework](https://www.ibm.com/training/enterprise-design-thinking/framework)
