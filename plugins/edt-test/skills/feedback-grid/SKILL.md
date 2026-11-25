---
name: feedback-grid
description: Sorts feedback into a Feedback Grid (Works well, Needs to change, Questions, New ideas) as an HTML artifact. Feedback comes from real users, teammates and stakeholders, or from simulated feedback sessions run one persona at a time. Then it clusters themes, checks assumptions and agrees actions. Use after a user test, Cognitive Walkthrough, Playback or demo, or when someone says "organize this feedback", "what did people think" or "make sense of these comments".
argument-hint: "[what was reviewed] [facilitate]"
---

# Feedback Grid

> IBM Enterprise Design Thinking · Test your ideas · Reflect · ~30 min

Feedback is easy to collect and easy to lose. The Feedback Grid gives every comment a place to land, so the team can see what to keep, what to fix, what is still unclear and what new ideas surfaced. Then the team acts on it right away instead of letting the notes go stale. It closes a turn of the Loop: what you observed in a test or Playback becomes a reflection, and that reflection decides what you make next. Who said something matters as much as what they said, so the grid keeps users' feedback apart from the team's opinions, and real users apart from simulated ones.

## When to use it
- Any time you expect feedback: during or right after a user observation, a Cognitive Walkthrough, a Playback or a client engagement.
- When feedback is scattered across transcripts, chat threads, tickets, survey comments or photos of a wall.
- When the team argues about "what users said" and nobody has sorted it.
- When there's no user feedback yet and you want a fast first read from simulated users before a real session.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the feedback itself: `cognitive-walkthrough-*`, `paper-prototypes-*`, `wireframes-*` and `playbacks-*`. Carry their notes over with their tags and sources unchanged.
  - what the feedback can check: `hills-*`, `assumptions-and-questions-*`, and the `assumption` and `simulated` entries in upstream `items`
- **Raw feedback the user points to:** session notes, transcripts, chat or survey exports, tickets, or photos of a physical grid (Claude can read images). This is real evidence.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing and you need simulated sessions, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** what was reviewed, if you can't find it, and the group of each real person who gave feedback (user, sponsor user, teammate or stakeholder), if the notes don't say.

## Co-create with Claude
1. **Frame it.** Record what was reviewed, when, and who gave feedback. Name the Hill or the upstream assumptions this feedback could confirm or challenge.
2. **Collect.** Real feedback comes first. Then fill the gaps with simulated feedback sessions:
   - Run them when there's no user feedback yet, or when a kind of user from the Hill is missing from the real feedback.
   - Pick 3–5 personas, including a skeptic and the edge case, and run one at a time. Show each persona the reviewed thing as they would meet it, such as the frames, the page, or a demo narrated like a screen share.
   - Ask open prompts in this order, with "Tell me more about that" as the only probe:
     1. "What would you want us to keep?"
     2. "What gets in your way, or what would you change?"
     3. "What's unclear, or what are you wondering about?"
     4. "What would you add, or do differently?"
   - Stay in character. People are often indifferent, mix praise and complaint in one sentence, and push back on things the team is proud of. Never ask "Do you like it?"
   - Keep every transcript.

   Simulate users only. Teammate and stakeholder feedback comes from real people.
3. **Set up the grid.** Use four quadrants: **Works well**, **Needs to change**, **Questions** and **New ideas**.
4. **Capture.** Break the input into atomic notes:
   - **One point per note,** in the giver's words where possible.
   - **Give each note a source:** the participant code (`P…` for a real person, `SU-…` for a simulated one), their group, and the session and date.
   - **Tag each note:**
     - `evidence`: something a real user said or did, or a teammate's or stakeholder's comment on feasibility, effort or business fit, with their group in `src`
     - `simulated`: anything from a simulated session
     - `assumption`: the team's explanation of why something happened, and any teammate's or stakeholder's claim about what users want or do
     - `question`: something nobody knows yet
   - **Placement rules:**
     - **Needs to change** states the problem, not the fix. Put proposed fixes in **New ideas**.
     - Split a mixed comment ("love the list, hate the filters") into two notes.
     - Put what people asked, or visibly didn't understand, in **Questions**. Confusion is often the strongest usability signal you have.
5. **Cluster.** Group similar notes within and across quadrants. Name each theme as a short sentence ("People can't tell which trips still need receipts"), not a single word. For each theme, count the notes and the distinct people behind them, by group. Point out patterns, contradictions (one group praises what another flags), any theme that rests on a single voice, and any theme that rests only on simulated users.
6. **Check assumptions.** Map the themes to the Hill and the upstream assumptions, and give each a verdict:
   - **Validated**, **Invalidated** or **Mixed:** only from real users' feedback
   - **Simulated: supported** or **Simulated: contradicted:** when only simulated users speak to it, never Validated
   - **Untested:** when nothing speaks to it

   Cite the notes behind every verdict. Teammate and stakeholder feedback speaks to feasibility and business fit, not to what users need.
7. **Decide actions now.** The method expects action straight after the activity. For each top theme, propose **change**, **investigate** (it becomes a new Question) or **keep**, with an owner, a date and the next activity. A theme backed only by simulated users defaults to investigate with real users, unless the change is cheap. Confirm the actions with the user before you write them down.
8. **Play back** the grid, and put the simulated themes the team leans on most at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/feedback-grid-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0:00–0:03 Intro: say what is being reviewed, and that feedback is a gift
  - 0:03–0:05 Set up: show the grid and walk through the four quadrants
  - 0:05–0:17 Capture: people write silently, during the demo or Playback or right after it
  - 0:17–0:25 Cluster: sort similar notes, name the themes, dot-vote the top 3
  - 0:25–0:30 Act: agree an action, an owner and a date for each top theme
- **Prompts to read aloud:**
  - "Write before you talk. One thought per note. Add your initials, and who said it if you heard it from a user."
  - "What works well enough that we must keep it?"
  - "What needs to change? Describe the problem, not your fix."
  - "What questions came up, and what are you still wondering?"
  - "What new ideas did this spark?"
  - While clustering: "Which notes are saying the same thing? What's the pattern?"
  - To close: "What will we do about this, who owns it, and by when?"
- **Materials:** a wall or a Mural board with the grid, markers, sticky notes in one color per feedback group (users, teammates, stakeholders) so the source stays visible, and dots for voting. Agree who digitizes the board afterward.
- **An empty board:** a `.quad` with the four quadrants, each holding an empty cluster per feedback group, plus a parking lot and an empty actions table. Optionally seed it with simulated users' notes so the team can react to them, labeled as simulated.

After the session, read the photos or the Mural export and build the results page. Each real note keeps its group, and any simulated notes stay in their own cluster.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/feedback-grid-<topic>.html`.
- **Title:** `<What was reviewed> Feedback Grid`, for example "Expense Flow Feedback Grid".
- **Sections:**
  1. **The grid:** a `.quad` with Works well (+), Needs to change (Δ), Questions (?) and New ideas (!) as its four cells, in reading order. In each cell, put one `.cluster` per feedback group, always in this order: **Users**, **Simulated users**, **Team and stakeholders**. Each cluster holds tagged `.note`s. Users' feedback and the team's opinion never share a cluster.
  2. **Who gave feedback:** a table of ID, group, role, session and date, with the number of notes from each person.
  3. **Themes:** a table of the theme sentence, its quadrants, the note IDs, the distinct people by group ("1 user, 3 simulated, 2 teammates"), and a tag pill. Label single-voice and simulated-only themes in the row.
  4. **Assumptions checked:** a table of assumption, where it came from, verdict pill and note IDs. Real verdicts use `data-tone` (`good` Validated, `bad` Invalidated, `warn` Mixed). Simulated verdicts use a `data-tag="simulated"` pill reading "Simulated: supported" or "Simulated: contradicted". Untested gets a plain pill.
  5. **Actions:** a table of action, theme, change, investigate or keep, owner, due date and the next activity as a `.cmd`.
  6. **Parking lot:** `.notes` for side issues.
  7. **Simulated feedback sessions:** a `details.transcript` per persona. Include this only when you ran any.
  8. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "reviewed": { "what": "", "ref": "", "session": "", "date": "" },
    "givers": [{ "id": "P1", "group": "user|sponsor-user|simulated|teammate|stakeholder", "role": "" }],
    "grid": { "works_well": ["N1"], "needs_to_change": [], "questions": [], "new_ideas": [] },
    "themes": [{ "id": "TH1", "text": "", "quadrants": ["needs_to_change"], "notes": ["N2", "N7"],
                 "people": { "users": 1, "simulated": 3, "team": 0 }, "tag": "simulated" }],
    "assumptions": [{ "text": "", "from": "", "verdict": "validated|invalidated|mixed|simulated-supported|simulated-contradicted|untested", "notes": ["N2"] }],
    "actions": [{ "text": "", "theme": "TH1", "type": "change|investigate|keep", "owner": "", "due": "", "next": "/edt-test:wireframes" }],
    "parking_lot": ["N9"] }
  ```
  `items` holds every note, with `group` set to `"<Quadrant> / <feedback group>"`.

## Quality checks
- Every note has a source and a group. Nothing is invented or "rounded up" from memory.
- One idea per note, and Needs to change notes describe problems rather than solutions.
- Users' feedback stays visibly apart from teammate and stakeholder opinion. A stakeholder's view is evidence of what that stakeholder thinks, not of what users need.
- Themes report how many distinct people raised them, by group. A theme from a single person, or only from simulated users, is labeled as such.
- Works well is filled in. Knowing what to protect matters as much as knowing what to fix.
- Every top theme ends in an action with an owner, or in an explicit decision to park it.
- The simulated personas sound like different people and don't all like the design. If every persona praises it, rerun them with more friction.
- No simulated note is tagged `evidence`, and no simulated result marks an assumption Validated.
- Simulated feedback is reported as counts of simulated users, never as percentages.
- Common pitfalls:
  - defending the design while capturing
  - dropping Questions as noise
  - clustering by quadrant only, which misses cross-quadrant themes
  - merging a real user's comment and a simulated one into a single note
  - leaving the grid on the wall for weeks

## Next
- `/edt-plan:assumptions-and-questions`: update the assumption list with what was validated, contradicted or still untested.
- `/edt-plan:prioritization-grid`: rank the proposed changes by user impact and feasibility.
- `/edt-test:wireframes` or `/edt-test:paper-prototypes`: make the next iteration.
- `/edt-test:cognitive-walkthrough`: retest the changed flow.
- `/edt-core:sponsor-users`: find real users to check the simulated themes.
- `/edt-align:playbacks`: share what you learned and what changes next with stakeholders.
- `/edt-align:retrospectives`: use this instead when the feedback is about how the team works.

## Source
[IBM Enterprise Design Thinking Toolkit: Feedback Grid](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac13)
