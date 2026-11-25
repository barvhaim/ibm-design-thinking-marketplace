---
name: daily-syncs
description: Sets up and runs a short daily team sync and keeps a running HTML log page of updates, blockers and action plans, updated in place. It can also draft your own update from your recent git activity, read-only. Use when the user says "daily sync", "standup", "write my standup update", "what did I do yesterday?", "set up a team sync", "log today's blockers", or wants the team to share updates, ask for help and flag blockers early.
argument-hint: "[setup | my-update | log] [team] [facilitate]"
---

# Daily Syncs

> IBM Enterprise Design Thinking · Align your team · Reflect · ~15 min

A Daily Sync keeps everyone aware of what teammates are doing. It gives people a regular moment to ask for help, and it surfaces blockers while they are still small. It is a quick, peer-to-peer Reflect moment in the Loop, not a status report to a manager. The team stays aligned on intent without giving up the focus time that Make work needs.

**Simulated users here.** None. A Daily Sync is about real teammates' real work, so Claude doesn't simulate users or teammates, and the log page has no simulated banner. Every entry comes from what a teammate said or posted, or from the user's own git history.

## When to use it
- Every day, as the name says. You can change the cadence, but keep the purpose: staying in touch about day-to-day work.
- A new team or workstream forms and needs to decide who syncs, and when.
- You want a quick draft of your own update before the sync starts.
- Blockers keep resurfacing and you want a record of them to bring to the retrospective.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the team's log, `daily-syncs-<team>.html`: the setup, past entries and open blockers. If only an older `daily-syncs-<team>.md` exists, read it and carry its setup and open blockers into the new HTML page.
  - `hills-*`, `user-stories-*` and `experience-based-roadmap-*`, so updates can tie back to user outcomes
  - `hopes-and-fears-*`, for working agreements about meetings and focus time
- **Ask the user only for:**
  - the team members and their disciplines, their time zones, and the tracker or board you use
  - for `my-update`: your git author email, if `git config user.email` is not set, and anything you worked on that git does not show

## Co-create with Claude
**A. Set up the sync** (`setup`)
1. **Identify who needs to share.** These are the people whose work depends on each other's day to day. Aim for a diverse group across disciplines, such as design, engineering, research and product. Don't limit it to one function. If more than about 8 people would attend, suggest splitting into smaller syncs.
2. **Find a regular time.** Choose a slot that works for everyone across time zones. Balance the need for alignment against uninterrupted work time. Next to an existing break is often better than in the middle of a focus block.
3. **Agree on the format.** Use three questions, a timebox, a facilitator who rotates, a parking lot, and an async fallback for days when someone can't attend. Write all of this into the Setup section of the log page, and publish it.

**B. Draft my update** (`my-update`). Read-only.
1. Find the window since the last sync. Use the date of the latest entry on the log page, or "yesterday", or "last Friday" on a Monday.
2. Gather read-only signals. Never run anything that changes state: no commit, push, checkout, stash or reset.
   - `git config user.email`
   - `git log --all --no-merges --since="<window>" --author="<email>" --pretty=format:'%h %ad %s' --date=short`
   - `git status --short` and `git branch --show-current`, for work that is still in progress
   - If `gh` is available: `gh pr list --author "@me" --state all --limit 10`
3. Turn the commits into 1–3 outcome statements, grouped by feature or story. Do not paste raw commit messages, and skip noise such as formatting and merge commits. Where you can, link each outcome to a Hill or story.
4. Tag everything inferred from git `assumption` until the user confirms it. A confirmed outcome becomes `evidence`, with the PR or commit as its source. Then ask:
   - "What did you do that git won't show, such as research, reviews or design?"
   - "What's next?"
   - "Is anything blocking you, and who could help?"

   Git can't see blockers.
5. Give a short update the user can paste or read aloud, about 30–60 seconds spoken, holding only confirmed items. Then add it as the user's row in today's entry on the log page and republish. If the team has no log yet, create the page with a Setup stub to fill in later.

**C. Log a sync** (`log`)
1. For each person, record what they finished, what's next, and any blocker, in their own words from the sync, chat thread or notes. Never write an update for a teammate who didn't give one; mark them absent instead.
2. For each blocker, write a one-line **action plan**: who will help, by when, and where it gets resolved. Don't try to solve the blocker inside the sync.
3. Move discussions and announcements to the **after-sync** list.
4. Update the open blockers. Close resolved ones. If a blocker has been open for 3 or more syncs, flag it for the retrospective.
5. Update the page in place: the new entry becomes the latest sync, the previous one moves into the earlier-syncs table, and the Playback is refreshed. Republish the same file so the link stays the same.

## Facilitate a live session
Produce `design-thinking/daily-syncs-<team>-kit.html`. It needs:
- **Agenda table (15 min):**
  - 0–1 Start on time and name today's facilitator.
  - 1–12 Round robin, about 1–1.5 min each. Each person answers the three questions while the team walks the board.
  - 12–14 Blockers. Give each an owner and an action plan, without solving it in the room.
  - 14–15 Read out the parking lot and after-sync list, then end on time.
- **Prompts to read aloud:**
  - "What have you finished since we last met?"
  - "What will you finish before next time?"
  - "What's in your way, and who could help?"
  - "Let's take that after the sync. Who needs to be in that conversation?"
- **Materials:** the team board (physical or digital), a visible timer, a fixed speaking order or a token you pass around, and a parking-lot sheet.
- **Board layout:** empty `.cols` for Backlog · In progress · Done · Blocked, with a name on each card, plus a parking lot on the side. For remote teams, keep cameras on, share the board, and use a fixed speaking order.
- **Tips:** everyone participates, including leads. No side conversations. Build on each other with "yes, and…". If the sync often runs long, the group is too big or people are solving problems in the room.

After the sync, paste the chat thread or notes, and Claude logs the entry on the log page and updates the blockers.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/daily-syncs-<team>.html`. Keep one running page per team, update it in place, and republish it after every change. Delete the simulated banner.
- **Title:** `<Team> Daily Syncs`, for example "Payments Team Daily Syncs".
- **Header `.meta`:** Date is the last update. Under Users, give the team size and "no simulated users".
- **Sections:**
  1. **Setup:** a lede with when and where, the timebox, the facilitator rotation, the async fallback and the board link. Then a table of member, discipline and time zone.
  2. **Open blockers:** a table of since, who, blocker, help needed from, action plan, syncs open, and a status pill: `data-tone="warn"` for open, `bad` for open 3 or more syncs and flagged for the retro, `good` for resolved since the last sync.
  3. **Latest sync, <date>:** `.cols` with Finished, Next and Blocked. Each `.note` names the person and the outcome. Its `src` is the person plus the source, such as "Ana · PR #128" or "Ana · said in sync". Tag `evidence` for what a teammate reported or a PR confirms, and `assumption` for anything inferred from git and not yet confirmed. Below it, the after-sync list: each topic and who meets.
  4. **Earlier syncs:** a table of date, who, finished, next and blocker, newest first, with each item's tag as a pill.
  5. **Playback:** refreshed on every update. The takeaways cover recurring blockers, cross-discipline dependencies and progress toward the Hills. "Validate next" lists unconfirmed assumptions and open questions.
- **`content` in `#edt-data`:**
  ```json
  { "team": "",
    "setup": { "members": [{ "name": "", "discipline": "", "tz": "" }], "when": "", "where": "",
               "timebox_min": 15, "facilitator_rotation": [""], "async_fallback": "", "board": "" },
    "entries": [{ "date": "2026-11-25",
                  "updates": [{ "who": "", "finished": ["N1"], "next": ["N2"], "blocker": "B3", "absent": false }],
                  "after_sync": [{ "topic": "", "who": [""] }] }],
    "blockers": [{ "id": "B3", "since": "", "who": "", "text": "", "help_from": "", "plan": "",
                   "syncs_open": 3, "status": "open", "flag_retro": true }] }
  ```
  Keep `entries` newest first. `items` holds every update note, with `group` set to `"<date> / Finished|Next|Blocked"`.

## Quality checks
- Updates describe outcomes, such as "the checkout flow passes usability review", not activity lists.
- Every blocker names the help needed and from whom, and has an action plan. It is never solved inside the sync.
- The sync ends on time. Discussions go to the after-sync list.
- Drafted updates come only from the user's own read-only git history. Claude never runs state-changing commands and never reports on teammates' commits unless asked.
- Every git-inferred item stays `assumption` until the user confirms it, and the paste-ready update holds only confirmed items.
- Nothing on the page is simulated, and no teammate's update is written for them.
- There is one page per team, updated at the same path, so the published link never changes.
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
