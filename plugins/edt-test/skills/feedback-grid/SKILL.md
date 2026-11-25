---
name: feedback-grid
description: Sort feedback from users, teammates or stakeholders into a Feedback Grid (Works well, Needs to change, Questions, New ideas), cluster it into themes, and turn it into actions and checked assumptions. Use after a user test, Cognitive Walkthrough, Playback, demo or review, or when someone says "organize this feedback", "what did people think", "make sense of these comments" or "we have a pile of notes from the session".
argument-hint: "[what was reviewed] [facilitate]"
---

# Feedback Grid

> IBM Enterprise Design Thinking · Test your ideas · Reflect · ~30 min

Feedback is easy to collect and easy to lose. The Feedback Grid gives every comment a place to land, so the team can see what to keep, what to fix, what is still unclear and what new ideas surfaced. Then the team acts on it right away instead of letting the notes go stale. It closes a turn of the Loop: what you observed in a test or Playback becomes a reflection, and that reflection decides what you make next.

## When to use it
- Any time you expect feedback: during or right after a user observation, a Cognitive Walkthrough, a Playback or a client engagement.
- When feedback is scattered across transcripts, chat threads, tickets, survey comments or photos of a wall.
- When the team argues about "what users said" and nobody has sorted it.

## Inputs
- From `design-thinking/`: `cognitive-walkthrough-*`, `paper-prototypes-*`, `wireframes-*` and `playbacks-*` for the feedback itself, plus `hills-*` and `assumptions-and-questions-*` so you can check what the feedback proves.
- Ask the user for:
  - what was reviewed, with a link or path
  - who gave the feedback, and whether each person is a user, sponsor user, teammate or stakeholder
  - the raw feedback: session notes, transcripts, chat or survey exports, tickets, or photos of a physical grid (Claude can read images)

If there is no raw feedback yet, don't fill the grid. Help the user plan how to collect it with `/edt-test:cognitive-walkthrough` or `/edt-align:playbacks`.

## Co-create with Claude
1. **Frame it.** Record what was reviewed, when, and who gave feedback. Name the Hill or assumptions this feedback could confirm or challenge.
2. **Set up the grid.** Use four quadrants: **Works well**, **Needs to change**, **Questions** and **New ideas**.
3. **Capture.** Break the raw input into atomic notes:
   - Write one point per note, in the giver's words where possible.
   - Give each note a source: participant code or role, session and date, and the person's group (user, sponsor user, teammate, stakeholder).
   - Tag each note. Something a person said or did is **Evidence**. The team's explanation of why it happened is an **Assumption**. Something nobody knows yet is a **Question**.
   - Placement rules:
     - **Needs to change** states the problem, not the fix. Put proposed fixes in **New ideas**.
     - Split a mixed comment ("love the list, hate the filters") into two notes.
     - Put what people asked, or visibly didn't understand, in **Questions**. Confusion is often the strongest usability signal you have.
4. **Cluster.** Group similar notes within and across quadrants. Name each theme as a short sentence ("People can't tell which trips still need receipts"), not a single word. For each theme, count the notes and the distinct people behind them. Point out patterns, contradictions (one group praises what another flags), and any theme that rests on a single voice.
5. **Check assumptions.** Map the themes to the Hill and the assumption list. Mark each assumption **Validated**, **Invalidated**, **Mixed** or **Untested**, and cite the notes behind the verdict. Only feedback from users can validate an assumption about users. Feedback from teammates and stakeholders speaks to feasibility and business fit.
6. **Decide actions now.** The method expects action straight after the activity. For each top theme, propose **change**, **investigate** (it becomes a new Question) or **keep**. Give each one an owner, a date and the activity that comes next. Confirm the actions with the user before you write them down.
7. **Write the artifact** and its Playback.

## Facilitate a live session
**Before:** Draw the grid on a wall or a Mural board. Give everyone a marker and a pad of sticky notes. Agree who digitizes the board afterward.

**Agenda (30 min):**
- 0:00–0:03 · **Intro.** Say what is being reviewed, and that feedback is a gift.
- 0:03–0:05 · **Set up.** Show the grid and walk through the four quadrants.
- 0:05–0:17 · **Capture.** People write silently, during the demo or Playback or right after it.
- 0:17–0:25 · **Cluster.** The group sorts similar notes, names the themes, and dot-votes the top 3.
- 0:25–0:30 · **Act.** Agree an action, an owner and a date for each top theme.

**Prompts to read aloud:**
- "Write before you talk. One thought per note. Add your initials, and who said it if you heard it from a user."
- "What works well enough that we must keep it?"
- "What needs to change? Describe the problem, not your fix."
- "What questions came up, and what are you still wondering?"
- "What new ideas did this spark?"
- While clustering: "Which notes are saying the same thing? What's the pattern?"
- To close: "What will we do about this, who owns it, and by when?"

**Board layout:**
```
+-----------------------+-----------------------+
|  WORKS WELL       (+) |  NEEDS TO CHANGE  (Δ) |
|                       |                       |
+-----------------------+-----------------------+
|  QUESTIONS        (?) |  NEW IDEAS        (!) |
|                       |                       |
+-----------------------+-----------------------+
 Parking lot: ______________   Actions: owner / date
```
Use one sticky-note color per feedback group (users, teammates, stakeholders) so the source stays visible. Keep side issues in the parking lot. **After the session:** share a photo or a Mural export, and Claude digitizes it into the artifact.

## Output
Save to `design-thinking/feedback-grid-<topic>.md`:

```markdown
# Feedback Grid: <what was reviewed>

- Date / session:
- Reviewed: <prototype, Playback, release> (<link or path>)
- Feedback from: <n users (of which n sponsor users), n teammates, n stakeholders>
- Hill / assumptions in scope:

## Grid
### Works well
| # | Note | Tag | Source (who, group, session) |
| --- | --- | --- | --- |
### Needs to change
| # | Note | Tag | Source |
| --- | --- | --- | --- |
### Questions
| # | Note | Tag | Source |
| --- | --- | --- | --- |
### New ideas
| # | Note | Tag | Source |
| --- | --- | --- | --- |

## Themes
| Theme (a sentence) | Quadrant(s) | Notes | Distinct people (groups) | Interpretation (tag) |
| --- | --- | --- | --- | --- |

## Assumptions checked
| Assumption / Hill claim | Verdict: Validated / Invalidated / Mixed / Untested | Evidence (note #s) |
| --- | --- | --- |

## Actions
| Action | Theme | Change / Investigate / Keep | Owner | Due | Next activity |
| --- | --- | --- | --- | --- | --- |

## Parking lot
- …

## Playback
- Key takeaways (3–5):
- Assumptions and questions to validate next:
- Recommended next activity:
```

## Quality checks
- Every note has a source and a group. Nothing is invented or "rounded up" from memory.
- One idea per note, and Needs to change notes describe problems rather than solutions.
- Feedback from users stays distinguishable from teammate and stakeholder opinion. A stakeholder's view is evidence of what that stakeholder thinks, not of what users need.
- Themes report how many distinct people raised them. A theme from a single person is labeled as such.
- Works well is filled in. Knowing what to protect matters as much as knowing what to fix.
- Every top theme ends in an action with an owner, or in an explicit decision to park it.
- Common pitfalls:
  - defending the design while capturing
  - dropping Questions as noise
  - clustering by quadrant only, which misses cross-quadrant themes
  - leaving the grid on the wall for weeks

## Next
- `/edt-plan:assumptions-and-questions`: update the assumption list with what was validated or invalidated.
- `/edt-plan:prioritization-grid`: rank the proposed changes by user impact and feasibility.
- `/edt-test:wireframes` or `/edt-test:paper-prototypes`: make the next iteration.
- `/edt-test:cognitive-walkthrough`: retest the changed flow with users.
- `/edt-align:playbacks`: share what you learned and what changes next with stakeholders.
- `/edt-align:retrospectives`: use this instead when the feedback is about how the team works.

## Source
[IBM Enterprise Design Thinking Toolkit: Feedback Grid](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac13)
