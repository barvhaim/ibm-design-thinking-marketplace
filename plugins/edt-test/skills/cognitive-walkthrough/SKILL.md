---
name: cognitive-walkthrough
description: Runs a Cognitive Walkthrough of a prototype as an HTML artifact. Simulated users each try the tasks on your wireframes, paper prototype, repo UI or running app, thinking aloud and getting stuck where they really would. Records success, assist or fail per persona, with transcripts and a real-session kit. Use when someone says "test this prototype with users", "usability test", "will users get this flow" or "walk through the app before we show users".
argument-hint: "[prototype, URL or path] [facilitate]"
---

# Cognitive Walkthrough

> IBM Enterprise Design Thinking · Test your ideas · Observe and Reflect · ~60 min

A prototype only proves something when a user tries it without help. In a Cognitive Walkthrough, a user works through a realistic scenario on your prototype while the team watches in silence and takes notes. The team sees, in real time, where the user succeeds, hesitates or gets lost, and how they feel about each part. Use it early and often. Everything is a prototype, and each round tells you what to change next. Simulated walkthroughs let you run a round in minutes and fix the obvious blockers, so the time you spend with real users goes on the problems simulation can't find.

## When to use it
- As soon as a paper prototype, wireframe or build can support one goal from start to finish, and again after every significant change.
- When the team disagrees about whether a flow is "intuitive". Watch someone use it instead of debating.
- Before a Playback, so you can show how the flow performs instead of opinions about it.
- Before a real user session, to rehearse the script and find blockers that would waste a participant's time.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the prototype: `wireframes-*` (`content.screens`) or `paper-prototypes-*` (`content.flow`, `content.pieces`)
  - `hills-*` and `to-be-scenario-map-*`, for the goal
  - `assumptions-and-questions-*`, plus the `assumption` and `simulated` entries in upstream `items`, for what this round should check
  - `sponsor-users-*`, for real participants
- **Or a prototype outside `design-thinking/`:** a UI in the repo (routes, components, templates, copy), a running app (driven with browser tools such as Chrome DevTools MCP, if available), or screenshots and photos.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** the prototype, if you can't find it; the Hill, if there are several; and whether real sessions have already happened, with their notes.

## Co-create with Claude
1. **Gather.** Read the upstream pages and the prototype. Build a source list: `S…` for real sources (session notes, recordings, analytics) and `SU-…` for the personas who match the Hill's user.
2. **Identify the goal.** Pick one high-level outcome the user should reach with the prototype, framed in their terms and tied to a Hill. Example: "Get reimbursed for a client trip."
3. **Identify the tasks.** List the tasks a user must complete to reach the goal, such as find the trip, attach the receipts and submit for approval. For each task, write down what success looks like and the correct action sequence. This is the team's answer key. Participants, real or simulated, never see it.
4. **Identify the scenario.** Write a short, realistic situation that gives the user the goal without naming any UI elements. For example: "You just got back from a client visit in Austin and want your $412 back before the month closes." Use the user's words, not the screen labels. Wording like "click Submit expense" gives the answer away.
5. **Prepare the prototype.** Walk the answer key against the prototype and confirm that every screen, state and piece of content the user needs exists, including the error and empty states the scenario might trigger. Fill the gaps or cut the task.
6. **Heuristic pass.** At each step of the answer key, Claude asks:
   1. Will the user be trying to do this step at this point?
   2. Will they notice that the right control is there?
   3. Will they recognize it as the way to their goal? Does the label match their words?
   4. After acting, will they see that they are making progress?

   Every "no" is a predicted issue. Tag it `assumption` and cite where it happens (`file:line`, URL or frame). These are Claude's expectations, not results. Use them to fix obvious blockers and to know what to watch for, never to give a verdict.
7. **Write the session script.** The same non-leading script runs the simulated sessions and the real ones:
   - **Welcome:** "We're testing the design, not you. You can't do anything wrong. It's an early version, so parts may not work. I'll stay quiet, because seeing how it works without us is what helps most."
   - **Consent** to take notes or record, then **warm-up:** 2–3 questions about how they do this work today.
   - **Think-aloud:** "As you go, please say what you're looking at, what you're trying to do, and what you expect to happen."
   - **Scenario:** read it aloud, then hand it over on a card.
   - **Neutral prompts:** "What are you thinking?", "What do you expect that will do?", "What would you do if I weren't here?", "Tell me more about that."
   - **Never ask** "Was that easy?" or "Did you see the button?", and never point. Answer questions with a question: "What do you think it does?"
   - **When stuck:** wait. If they would give up, mark the task Failed and move on. Only afterward, ask what would have helped.
   - **Wrap-up:** "What worked for you? What would you change? What was confusing?"
8. **Run the simulated think-alouds.** Pick 3–5 personas who match the Hill's user, including the novice, a skeptic and the edge case. Run one persona at a time, from welcome to wrap-up. Claude plays the facilitator, who says only what the script allows, and the persona, who speaks in the first person:
   - **The persona acts on what's on the screen,** in their own vocabulary and habits, never on the answer key or the code. A label in words they don't use makes them hesitate or skip it. Novices miss things, experts reach for shortcuts from tools they already use, and the edge case hits their constraint: a screen reader, a small screen, a slow connection, a second language.
   - **The prototype answers honestly.** After each action, show what the prototype actually does next: the next frame or paper piece, the route the code would render, or the real page after the click. If the prototype has no response for what they did, that's a dead end and a finding.
   - **Outcomes follow the script.** A persona who gets there alone is Success. One who needs a hint is Assisted. One who would give up is Failed.
   - **Keep every transcript.** Insert a `Screen` turn whenever the screen changes. Draw notes from it on what they did, what they said verbatim, where they struggled and how they seemed to feel. Tag them `simulated`, with the persona ID and task in `src`. Tag the team's interpretations `assumption`.

   If every persona sails through every task, the simulation is broken. Rerun the toughest persona with more friction, and check that nobody used a label or path they couldn't have seen.
   In a running app, use test accounts and test data, and stop before any irreversible action (payments, emails, deletes). Don't edit code unless the user asks.
9. **Add real sessions.** If the user has real session notes or recordings, read them (Claude can read photos). Record each participant as `P1…`, tag their notes `evidence`, and show them beside the simulated results, never merged. If there are no real sessions yet, recommend the kit (see Facilitate), and `/edt-core:sponsor-users` for recruiting.
10. **Review and reflect.** Answer these together:
    - What went well?
    - Did they reach the intended outcome?
    - Where did they struggle?
    - Did they understand how the prototype is structured?
    - What has to change?

    Record each task's outcome for every participant.
11. **Check assumptions.** For each upstream assumption this round touches, give a verdict:
    - from real sessions: **Validated**, **Invalidated** or **Inconclusive**
    - from simulated sessions only: **Simulated: supported** or **Simulated: contradicted**, never Validated
    - from the heuristic pass: no verdict
12. **Plan the changes.** For each blocker, propose a change, give its reason (the note IDs) and its priority, and confirm an owner with the user. Sort the notes with `/edt-test:feedback-grid` if there are many.
13. **Play back** the results, and put the simulated claims the team leans on most at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/cognitive-walkthrough-<topic>-kit.html` for a real session. It needs:
- **Agenda table (60 min, one or two participants):**
  - 0:00–0:05 Intro: explain the Hill and the assumptions under test
  - 0:05–0:15 Identify: agree the goal, tasks, success criteria and the scenario card
  - 0:15–0:20 Prepare: dry run on the prototype, assign roles, remind observers to stay silent
  - 0:20–0:45 Test: the user works through the scenario while thinking aloud; the team notes, one observation per sticky note
  - 0:45–0:60 Review and reflect: answer the debrief questions, sort the notes on a Feedback Grid, agree the changes
- **The script to read aloud** from step 7, with the never-ask list printed beside it, and the scenario as a card (one task per card if you reveal them in sequence).
- **Roles:** a facilitator runs the script, a note-taker captures everything with timestamps, and other observers stay silent. Three to five users per round usually surface the main problems.
- **Materials:** the prototype, scenario cards, sticky notes in two colors (did and said), timers, and recording consent.
- **Watch list, for observers only:** the heuristic predictions (`assumption`) and the simulated trouble spots (`simulated`). Never use them as prompts.
- **An empty results board:** a table with one column per task and one row per participant, for Success, Assisted or Failed, plus an empty capture section per participant for what they did, said, struggled with and felt.

After the session, read the notes, photos or recordings and build the results page. Real outcomes are `evidence`; keep any earlier simulated round in its own columns for comparison.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/cognitive-walkthrough-<topic>.html`.
- **Title:** `<Flow> Cognitive Walkthrough`, for example "Expense Claim Cognitive Walkthrough". Put the round number in `.meta`.
- **Sections:**
  1. **Test plan:** a `.board` with the Hill, the goal and the scenario card, then a table of tasks with what success looks like and the answer key.
  2. **Prototype tested:** `.frames` of the screens and states the tasks touch, labeled `Step N · <screen>`. Link the upstream page instead when it already shows them.
  3. **Results by task:** a table with one row per task and one column per participant. Column headers carry a pill: `data-tag="simulated"` for `SU-…` and `data-tag="evidence"` for `P…`. Cells hold a `data-tone` pill: `good` Success, `warn` Assisted, `bad` Failed. The last columns give counts ("2 of 4 simulated, 1 of 2 real") and the main blocker.
  4. **Observations:** one `.cluster` per task, holding tagged `.note`s.
  5. **Heuristic pass (Claude's predictions, not user results):** a table of step, the four questions as Yes or No, the predicted issue as a `data-tag="assumption"` pill, and where.
  6. **Review and reflect:** `.cols`, one column per debrief question, holding notes.
  7. **Assumptions checked:** a table of assumption, where it came from, verdict pill and note IDs. Real verdicts use `data-tone` (`good` Validated, `bad` Invalidated, `warn` Inconclusive). Simulated verdicts use a `data-tag="simulated"` pill reading "Simulated: supported" or "Simulated: contradicted".
  8. **Changes for next iteration:** a table of change, why (note IDs), priority and owner.
  9. **Think-aloud transcripts:** a `details.transcript` per simulated session, with persona turns as `turn sim` and `Screen` turns for what the prototype showed.
  10. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "round": 1,
    "prototype": { "ref": "design-thinking/wireframes-expenses.html", "kind": "wireframes|paper|repo|app", "fidelity": "low" },
    "hill": "", "goal": "", "scenario": "",
    "tasks": [{ "id": "T1", "text": "", "success": "", "answer_key": [""] }],
    "participants": [{ "id": "SU-1", "kind": "simulated" }, { "id": "P1", "kind": "real", "role": "", "sponsor_user": true }],
    "results": [{ "task": "T1", "participant": "SU-1", "outcome": "success|assisted|failed", "stuck_at": "", "notes": ["N3"] }],
    "heuristic": [{ "task": "T2", "step": "", "answers": [true, false, true, true], "issue": "", "where": "" }],
    "assumptions": [{ "text": "", "from": "", "verdict": "validated|invalidated|inconclusive|simulated-supported|simulated-contradicted|untested", "notes": ["N3"] }],
    "changes": [{ "text": "", "why": ["N3"], "priority": "high|medium|low", "owner": "" }] }
  ```
  `items` holds every note, with `group` set to `"<task> / <participant>"`, and every predicted issue, with `group` set to `"Heuristic pass"`.

## Quality checks
- The scenario and prompts never name UI labels or hint at the path, and nobody demonstrated the prototype. In simulated transcripts, the facilitator says only what the script allows.
- Every task has an outcome for every participant, failures included.
- The personas get stuck where they realistically would. If they all succeed everywhere, or praise the flow politely, rerun them with more friction.
- The personas behave differently, with different first moves, words and patience. If two transcripts read alike, rewrite one.
- No persona uses knowledge they couldn't have: a label they never saw, a route from the code, or the answer key.
- Notes record behavior and quotes, and interpretations are tagged `assumption`. Proxies, such as teammates standing in for users, are labeled as proxies.
- Simulated results never mark an assumption Validated, and heuristic predictions never count as results. No simulated note is tagged `evidence`.
- Simulated outcomes are reported as counts ("3 of 5 simulated users failed T2"), never as success rates or percentages.
- Each blocker has a change and an owner.
- Common pitfalls:
  - rescuing users when they struggle, or letting a simulated facilitator hint
  - testing a prototype that can't support the whole goal
  - asking "would you use this?" instead of watching them use it
  - treating a simulated round as a substitute for real users

## Next
- `/edt-test:feedback-grid`: sort the observations and decide actions.
- `/edt-test:wireframes` or `/edt-test:paper-prototypes`: make the changes, then run another round.
- `/edt-plan:assumptions-and-questions`: record what was validated, contradicted or still untested.
- `/edt-core:sponsor-users`: recruit real users to confirm the simulated results.
- `/edt-align:playbacks`: play back the results with stakeholders and sponsor users.
- `/edt-plan:user-stories`: turn the tested flow into stories.

## Source
[IBM Enterprise Design Thinking Toolkit: Cognitive Walkthrough](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac1d)
