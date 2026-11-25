---
name: retrospectives
description: Runs a retrospective after an iteration as an HTML artifact. The team captures what went well, what didn't and what to try, clusters it, plays it back, and leaves with 2–3 owned experiments. An optional voice-of-the-user column shows what real and simulated users said this iteration. Use when the user says "retro", "retrospective", "sprint retro", "post-mortem", "lessons learned", "what went well / what didn't", or a sprint, release or phase has just ended.
argument-hint: "[sprint, iteration or phase] [facilitate]"
---

# Retrospectives

> IBM Enterprise Design Thinking · Align your team · Reflect · ~60 min

A retrospective is the team reflecting together at the end of a stretch of work. It looks at how the team worked, not only what it shipped, and turns that into concrete ways to improve its workflows and dynamics. It is restless reinvention applied to the team itself: the way you work is a prototype too. A good retro is safe, inclusive and specific. It uses disagreement productively, and it ends with a few owned changes instead of a long list of complaints.

**Simulated users here.** The retro is the team's own reflection, so every note on the board comes from a real teammate, and Claude never simulates one. Users can still have a seat: an optional **Voice of the user** column collects what real and simulated users said during this iteration, taken from the upstream pages' `#edt-data` with their original tags. Claude runs no new simulations for a retro. The column helps the team ask whether its way of working helped or hurt what users got, and how much of its user learning came from real people.

## When to use it
- At the end of a sprint, iteration, release or project phase.
- After a Playback, a launch or an incident, when the team wants to learn from it.
- When friction keeps coming back: missed handoffs, recurring blockers, unclear ownership.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - **Last retro:** earlier `retrospectives-*` pages. What did we agree to try, and did it work?
  - **Kickoff:** `hopes-and-fears-*`. Which hopes came true, and which fears?
  - **Daily syncs:** `daily-syncs-*`. Recurring blockers and the after-sync topics.
  - **Playbacks:** `playbacks-*`. Stakeholder feedback and misalignment.
  - **Plans:** `hills-*`, `experience-based-roadmap-*`. Did we move toward the user outcomes we committed to?
  - **Voice of the user:** any page dated inside the iteration that holds user items, such as `interviews-*`, `contextual-inquiry-*`, `feedback-grid-*`, `cognitive-walkthrough-*` and `playbacks-*`.
- **Optional repo signals, read-only:** `git log --since="<iteration start>" --no-merges --oneline | wc -l`, plus reverts, hotfixes and the PR cycle time from `gh pr list --state merged`. Treat these numbers as prompts for discussion, never as a scorecard.
- **The team's notes:** a chat thread, a form, a Mural export, or a photo of the wall. Claude can read images.
- **Ask the user only for:** the iteration's dates and its goal or Hill, who participated by role, and whether to include the voice-of-the-user column.

## Co-create with Claude
1. **Schedule and scope.** Confirm the iteration window, the goal, and that everyone who did the work can attend or contribute asynchronously. Pull in the inputs above. Then draft a one-paragraph **look back**: the goal, what was delivered, the status of the last retro's experiments, and kickoff fears that came true. Tag each item, citing the page it came from.
2. **Gather the voice of the user (optional).** From the upstream pages, pick the 6–10 user items from this iteration that bear most on the goal, keeping each item's tag and source, so a `simulated` item stays simulated. Count the iteration's user items by tag, for example "3 evidence, 14 simulated". That count is a prompt in its own right: did we hear from any real users?
3. **Set up the prompts.** The default is three columns: **What went well? · What didn't go well? · What might we try next?** Offer the four-quadrant variant for a deeper retro: **Worked well · Needs to change · Unanswered questions · New ideas to try**. Keep the prompts about how we work and what users got, not about who to blame.
4. **Capture.** Each person writes one idea per note, silently. Write before you talk. Claude drafts an async form for the user to send, and helps the user add their own notes. Claude never makes up teammates' input or speaks for a teammate who didn't contribute. Tag each note:
   - `evidence`: the note cites something that happened, with a date, ticket or log.
   - `assumption`: a belief about a cause.
   - `question`: an open unknown.
5. **Cluster.** Group similar notes into titled themes, and count the notes in each. Then flag:
   - Themes that appear in both *went well* and *didn't go well*
   - Repeats from the last retro, which mean an earlier fix didn't stick
   - Where the voice of the user agrees or clashes with the team's view, such as the team calling onboarding a win while users stalled on it
6. **Playback.** One person plays back the positive and the negative clusters. Mark notes the whole team doesn't understand, and have the author clarify them. Claude drafts this playback script.
7. **Ideate and choose.** For each *didn't go well* cluster, generate several ways to address it. Build on each other's ideas with "yes, and…". Pick **2–3 experiments** by collective input, such as dot voting or impact against effort. Each experiment gets:
   - An owner
   - A signal that shows it worked
   - A date to check in, usually the next retro

   Fewer, owned experiments beat many wishes. If most user items were simulated, consider an experiment that gets the team in front of real users, via `/edt-core:sponsor-users`.

## Facilitate a live session
Produce `design-thinking/retrospectives-<iteration>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0–5 Welcome, purpose and ground rules. Review the experiments from the last retro.
  - 5–15 Silent capture across all columns.
  - 15–25 Post the notes and cluster them, then title the themes.
  - 25–35 Playback of the positive and negative clusters, with clarifying questions.
  - 35–50 Ideate fixes for each *didn't go well* cluster, then dot-vote.
  - 50–60 Commit to 2–3 experiments with owners and signals. Close with a one-word check-out.
- **Prompts to read aloud:**
  - "We're here to improve how we work, not to judge anyone. Assume everyone did their best with what they knew."
  - "Silently, for ten minutes: what went well, what didn't, what might we try? One idea per note."
  - "Here is what users told us this iteration. Which of these did our way of working cause?"
  - "Which of these would make the biggest difference to our users or to our team next iteration?"
  - "Who owns this, and how will we know it worked?"
- **Materials:** sticky notes in three or four colors (one per column), markers for everyone, dot stickers, a timer, and the list of the last retro's experiments.
- **Board layout:** empty `.cols` for *Went well · Didn't go well · Try next*, or four for *Worked well · Needs to change · Questions · New ideas*, plus a parking lot. If the team wants it, add the voice-of-the-user column prefilled from upstream pages with their tags, and the last retro's experiments to review. Leave an empty experiments table.
- **Tips:** everyone participates. The facilitator stays neutral, or the role rotates. Park off-topic issues. Start on time and stay on time.

After the session, read the photos or the Mural export and build the results page, keeping each note's wording and tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/retrospectives-<iteration>.html`. Keep the simulated banner only if the voice-of-the-user column holds simulated items; delete it otherwise.
- **Title:** `<Iteration> Retrospective`, for example "Sprint 14 Retrospective".
- **Header `.meta`:** under Users, give the team's coverage ("7 of 8 teammates") and the users behind the voice-of-the-user column, real and simulated.
- **Sections:**
  1. **Look back:** a lede with the goal, what was delivered, and kickoff hopes and fears that came true. Then a table of the last retro's experiments: experiment, owner, signal, and a result pill (`data-tone="good"` kept, `warn` didn't try, `bad` dropped). Repo signals go in as `evidence` notes with their source.
  2. **The board:** `.cols`, one `.col` per prompt, each holding titled `.cluster`s with counts, such as "Hand-offs (5)", of tagged `.note`s. A cluster that repeats from the last retro gets a `<span class="pill" data-tone="warn">Repeat</span>`. The optional last column, "Voice of the user", holds the upstream user items with their original tags and sources, and its heading gives the tag count.
  3. **Experiments to try next:** a table of experiment, the cluster it addresses, owner, signal it worked, and check-in date.
  4. **Parking lot:** `question` or `assumption` notes.
  5. **Playback:** the takeaways name the strongest themes and the user outcome. "Validate next" lists the causes the team assumed, and any simulated user items the team is acting on.
- **`content` in `#edt-data`:**
  ```json
  { "iteration": "", "dates": { "start": "", "end": "" }, "goal": "", "format": "3-column",
    "participants": [{ "role": "", "count": 1 }], "coverage": "7 of 8 teammates",
    "look_back": { "summary": "",
                   "experiments": [{ "text": "", "owner": "", "signal": "", "result": "kept", "source": "design-thinking/retrospectives-sprint-13.html" }],
                   "hopes_fears": [{ "text": "", "came_true": true }], "signals": ["N1"] },
    "columns": [{ "name": "Went well", "clusters": [{ "title": "", "notes": ["N2", "N3"], "repeat": false }] }],
    "voice_of_user": { "upstream": ["design-thinking/feedback-grid-checkout.html"], "notes": ["U1"],
                       "counts": { "evidence": 3, "simulated": 14 } },
    "experiments": [{ "text": "", "addresses": "", "owner": "", "signal": "", "check_in": "2026-12-09" }],
    "parking_lot": [""] }
  ```
  `items` holds every note, with `group` set to `"<Column> / <cluster>"`.

## Quality checks
- Every board note comes from a participant. Claude only adds context drawn from upstream pages, labeled with its source, and never writes a note as a teammate.
- Voice-of-the-user items keep their original tags and sources. None is retagged, and none is a fresh simulation.
- Notes are specific and observable. "Design specs landed after sprint planning twice" is better than "communication was bad".
- The retro reviewed the last retro's experiments before generating new ones.
- The team commits to 2–3 experiments at most. Each has an owner, a signal and a check-in date.
- At least one theme considers the user. Did our way of working help or hurt what users got? If the iteration's user learning was mostly simulated, the Playback says so.
- Metrics and git stats start conversations. They never rank individuals.
- Pitfalls:
  - Blaming people instead of processes
  - The same complaints every sprint with no follow-through
  - The loudest voice setting the agenda
  - Skipping the retro when the team is busy

## Next
- `/edt-align:hopes-and-fears`: kick off the next iteration and refresh the team's expectations.
- `/edt-align:daily-syncs`: build the chosen experiments into the daily cadence.
- `/edt-align:playbacks`: if the retro surfaced misalignment with stakeholders, plan a Playback.
- `/edt-core:sponsor-users`: if the voice of the user was mostly simulated, recruit real users for next iteration.
- `/edt-core:practice-check`: check how well the team is applying EDT principles overall.

## Source
[IBM Enterprise Design Thinking Toolkit: Retrospectives](https://www.ibm.com/downloads/documents/us-en/137a3e3494bed9b0)
