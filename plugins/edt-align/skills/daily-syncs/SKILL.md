---
name: daily-syncs
description: Sets up and runs a short daily team sync and keeps a log of blockers and action plans. It can also draft your own update from recent git activity, read-only. Use when the user says "daily sync", "standup", "daily standup", "write my standup update", "what did I do yesterday?", "set up a team sync", "log today's blockers", or wants the team to share updates, ask for help and flag blockers early.
argument-hint: "[setup | my-update | log] [team] [facilitate]"
---

# Daily Syncs

> IBM Enterprise Design Thinking · Align your team · Reflect · ~15 min

A Daily Sync keeps everyone aware of what teammates are doing. It gives people a regular moment to ask for help, and it surfaces blockers while they are still small. It is a quick, peer-to-peer Reflect moment in the Loop, not a status report to a manager. The team stays aligned on intent without giving up the focus time that Make work needs.

## When to use it
- Every day, as the name says. You can change the cadence, but keep the purpose: staying in touch about day-to-day work.
- A new team or workstream forms and needs to decide who syncs, and when.
- You want a quick draft of your own update before the sync starts.
- Blockers keep resurfacing and you want a record of them to bring to the retrospective.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - The existing `daily-syncs*` log: the setup, past entries and open blockers
  - `hills*`, `user-stories*` and `experience-based-roadmap*`, so updates can tie back to user outcomes
  - `hopes-and-fears*`, for working agreements about meetings and focus time
- Ask the user for anything still missing:
  - The team members and their disciplines, their time zones, and the tracker or board you use
  - For "my update": your git author name or email, if `git config user.email` is not set, and anything you worked on that git does not show

## Co-create with Claude
**A. Set up the sync** (`setup`)
1. **Identify who needs to share.** These are the people whose work depends on each other's day to day. Aim for a diverse group across disciplines, such as design, engineering, research and product. Don't limit it to one function. If more than about 8 people would attend, suggest splitting into smaller syncs.
2. **Find a regular time.** Choose a slot that works for everyone across time zones. Balance the need for alignment against uninterrupted work time. Next to an existing break is often better than in the middle of a focus block.
3. **Agree on the format.** Use three questions, a timebox, a facilitator who rotates, a parking lot, and an async fallback for days when someone can't attend. Write all of this into the Setup section of the log.

**B. Draft my update** (`my-update`). Read-only.
1. Find the window since the last sync. Use the date of the latest entry in the log, or "yesterday", or "last Friday" on a Monday.
2. Gather read-only signals. Never run anything that changes state: no commit, push, checkout, stash or reset.
   - `git config user.email`
   - `git log --all --no-merges --since="<window>" --author="<email>" --pretty=format:'%h %ad %s' --date=short`
   - `git status --short` and `git branch --show-current`, for work that is still in progress
   - If `gh` is available: `gh pr list --author "@me" --state all --limit 10`
3. Turn the commits into 1–3 outcome statements, grouped by feature or story. Do not paste raw commit messages, and skip noise such as formatting and merge commits. Where you can, link each outcome to a Hill or story.
4. Mark everything inferred from git as an **Assumption** until the user confirms it. Then ask:
   - "What did you do that git won't show, such as research, reviews or design?"
   - "What's next?"
   - "Is anything blocking you, and who could help?"

   Git can't see blockers.
5. Output a short update the user can paste or read aloud, about 30–60 seconds spoken.

**C. Log a sync** (`log`)
1. For each person, record what they finished, what's next, and any blocker.
2. For each blocker, write a one-line **action plan**: who will help, by when, and where it gets resolved. Don't try to solve the blocker inside the sync.
3. Move discussions and announcements to the **after-sync** list.
4. Update the open-blockers table. Close resolved blockers. If a blocker has been open for 3 or more syncs, flag it for the retrospective.

## Facilitate a live session
**Agenda (15 min)**
- **0–1:** Start on time and name today's facilitator.
- **1–12:** Round robin, about 1–1.5 min each. Each person answers the three questions while the team walks the board.
- **12–14:** Blockers. Give each an owner and an action plan, without solving it in the room.
- **14–15:** Read out the parking lot and after-sync list, then end on time.

**Prompts to read aloud**
- "What have you finished since we last met?"
- "What will you finish before next time?"
- "What's in your way, and who could help?"
- "Let's take that after the sync. Who needs to be in that conversation?"

**Materials:** the team board (physical or digital), a visible timer, a fixed speaking order or a token you pass around, and a parking-lot sheet.

**Board layout (wall or Mural):** columns for **Backlog · In progress · Done**, with an avatar or name on each card. Add a **Blocked** lane or a red flag, and a parking lot on the side. For remote teams, keep cameras on, share the board, and use a fixed speaking order.

**Tips**
- Everyone participates, including leads.
- No side conversations.
- Build on each other with "yes, and…".
- If the sync often runs long, the group is too big or people are solving problems in the room.

**Afterwards:** paste the chat thread or notes, and Claude logs the entry and updates the blockers.

## Output
Save to `design-thinking/daily-syncs-<team>.md`. Keep one running log per team and add new entries at the top:

```markdown
# Daily Syncs: <team>

## Setup
**Members (discipline):** … · **When / where:** … · **Timebox:** 15 min
**Facilitator rotation:** … · **Async fallback:** <channel> · **Board:** <link>

## Open blockers
| Since | Who | Blocker | Help needed from | Action plan | Status |
|---|---|---|---|---|---|

## <YYYY-MM-DD>
| Who | Finished since last time | Next | Blocker |
|---|---|---|---|
| … | <outcome>. Evidence: <PR, commit or ticket> | … | … |

**After-sync / parking lot:** <topic>: <who meets>

## Playback
- **Key takeaways (3–5):** <recurring blockers, cross-discipline dependencies, progress toward the Hills>
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/…`
```

Refresh the Playback section whenever you add an entry. Keep it at the bottom.

## Quality checks
- Updates describe outcomes, such as "the checkout flow passes usability review", not activity lists.
- Every blocker names the help needed and from whom, and has an action plan. It is never solved inside the sync.
- The sync ends on time. Discussions go to the after-sync list.
- Drafted updates come only from the user's own read-only git history. Claude never runs state-changing commands and never reports on teammates' commits unless asked.
- Inferred work is confirmed by the user before it's shared.
- Pitfalls:
  - A status report aimed at a manager
  - Reciting ticket numbers
  - The same blocker every day with no owner
  - A sync so large that half the people are idle

## Next
- `/edt-align:retrospectives`: bring recurring blockers and patterns from this log to the end-of-iteration retro.
- `/edt-align:playbacks`: when the progress is worth showing stakeholders, tell it as a story.
- `/edt-plan:user-stories`: when updates won't map to stories, the backlog needs work.
- `/edt-align:hopes-and-fears`: when a new teammate joins or a new phase begins.

## Source
[IBM Enterprise Design Thinking Toolkit: Daily Syncs](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac19)
