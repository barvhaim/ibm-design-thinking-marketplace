---
name: to-be-scenario-map
description: Maps a future experience in which your ideas already exist, with what the user does, thinks and feels in each phase, as an HTML artifact. It compares the map with the as-is map to show which pain points it resolves, then walks 2–3 simulated users through it to find where it still breaks. Use when someone says "to-be map", "future-state journey", "what would the future look like" or "how would our idea change their day", or right after ideating.
argument-hint: "[user, scenario or idea] [facilitate]"
---

# To-be Scenario Map

> IBM Enterprise Design Thinking · Generate new ideas · Reflect / Make · ~60 min

An as-is scenario map shows what users struggle with today. A to-be map imagines your ideas already exist and walks the same user through the same goal again, phase by phase: what they do, think and feel. The team can then reflect honestly on whether its ideas address current needs, or only look good on a sticky note. Walking a few simulated users through the future, each with their own tools, habits and doubts, shows where it would still break for them before anyone builds it. The result is a coherent story to put in front of stakeholders and Sponsor Users, so everyone aligns on intent.

## When to use it
- After Big Idea Vignettes or any ideation, to see how the chosen ideas fit together end to end.
- To check that the ideas resolve the as-is pain points and needs statements.
- To prepare a Playback, because a to-be map is a strong artifact for aligning stakeholders and users.
- To compare competing directions: sketch two or three rough alternative futures instead of debating in the abstract.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - `as-is-scenario-map-*`, the essential baseline: its user, scenario, phases, the Doing, Thinking and Feeling notes, and every low and gap with its tag and source
  - `needs-statements-*` and `hills-*`: what this future must answer
  - `big-idea-vignettes-*`: the chosen clusters, plus the simulated reactions to them
  - `empathy-map-*` and `storyboards-*`, for the user's context
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:**
  - which ideas this future contains, if there's no vignettes page (or suggest `/edt-ideate:big-idea-vignettes`)
  - whether any real users have seen the ideas yet
- If there's no as-is map, recommend `/edt-synthesize:as-is-scenario-map` first. If the user wants to continue anyway, ask them to describe today's experience briefly and tag it `assumption`.

## Co-create with Claude
1. **Anchor.** Restate the user, the goal and the ideas in scope. Use the same user and goal as the as-is map, for example "assign a workstation to a new employee". List the as-is pain points and needs statements this map must answer, each keeping its tag and source.
2. **Set up the rows:** Doing, Thinking and Feeling, with phases across the top. Leave the phases blank for now, because they emerge from clustering.
3. **Brainstorm.** Imagine the ideas are real today, and walk the user's journey from trigger to goal. At each moment, what does the user do, think and feel? Ask the user to go first, then add your own. Write one item per note, and write Thinking and Feeling in the user's voice. Revisit each as-is pain point and ask what happens at that moment now. Some steps should disappear, and that's often the biggest win.
4. **Cluster into phases.** Group similar items, refine their order, and name each phase from the user's point of view ("Getting set up", not "Provisioning"). Phases don't have to match the as-is map.
5. **Mark highs and lows.** Give each phase a mood: high, low or mixed. Be honest. A credible future still has lows, such as waiting, learning something new, deciding whether to trust it, and new failure modes the idea introduces. Compare each as-is pain point with its to-be moment and mark it resolved, improved, unchanged or worse.
6. **Walk simulated users through it.** Choose 2–3 personas from the panel: the persona the as-is map was built on, a skeptic or non-adopter, and an edge case, such as an accessibility need, low bandwidth or a regulated workflow. Run them one persona at a time, in character, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
   - Narrate the future one phase at a time, in plain words. Then ask: "What would you actually do here?" "What would you keep doing the old way?" "Where would you get stuck, or give up?"
   - The persona answers from their own context: their tools, constraints, habits and trust. They don't help the team make the map work.
   - Capture each place where the future still breaks for them, such as a step they'd skip, a workaround they'd keep, a trust gap or a new cost, as a `simulated` note in that phase, with the persona ID. "I'd keep my spreadsheet" counts.
   - Keep the transcripts.

   If a persona breezes through every phase, rerun them with more friction.
7. **Find the gaps.** Which needs are still unaddressed? Which lows and breaks need new ideas? Loop those back to `/edt-ideate:big-idea-vignettes`. What must be true for this future to work?
8. **Tag.** A to-be map is envisioned, so the team's Doing, Thinking and Feeling notes are `assumption`s until tested with real users. What the personas said during the walk-through is `simulated`. Pain points carried over from the as-is map keep their `evidence` or `simulated` tags and sources. Open unknowns are `question`s. When a break contradicts an envisioned note, keep both side by side. Don't rewrite the assumption to agree.
9. **Playback.** Tell the future as a two-minute story: the biggest improvement, the lows that remain, and where it still breaks for each persona. Put the riskiest assumptions and breaks at the top of "Validate next". Then publish the page.

Describe the user's experience, not the system's: "Sam sees her desk on her phone", not "the API syncs records". Keep UI detail out, because that comes later in `/edt-test:wireframes`.

## Facilitate a live session
Produce `design-thinking/to-be-scenario-map-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**

  | Time | Step | Notes |
  |---|---|---|
  | 0–5 | Intro and norms | Hang the as-is map above the new board and recap its pain points · write before you talk · yes, and · parking lot |
  | 5–8 | Setup | Draw rows for Doing, Thinking and Feeling. Read the scenario aloud |
  | 8–25 | Brainstorm | Write silently, one sticky per answer, one color per row, then share |
  | 25–37 | Cluster phases | Group, reorder, draw rough columns and name each phase |
  | 37–50 | Highs and lows | Circle highs and lows, compare with the as-is map and list gaps |
  | 50–60 | Playback | One or two people present the map, and the group discusses |
- **Prompts to read aloud:**
  - "Imagine our ideas exist today. <User> is trying to <goal>. What's the first thing they do?"
  - "What are they thinking at this moment? Write it as a quote."
  - "How do they feel here, and is it better or worse than on the as-is map?"
  - "Find that pain point on the as-is map above. What happens at that moment now?"
  - Playback: "How does our idea change this user's experience? Where are there still gaps?"
- **Materials:** the as-is map, sticky notes in three colors (Doing, Thinking, Feeling), markers, tape for the phase columns, and red and green markers for lows and highs.
- **The board:** the as-is map's phases and lows, read from its `#edt-data`, as a reference `.map` at the top, then an empty `.map` with Doing, Thinking and Feeling rows below it, and a parking lot.

After the session, read the photos or the Mural export. Transcribe the phases and notes word for word and record the highs and lows. Then fill in the pain point comparison with the user, and run step 6 on the transcribed map before you build the results page.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/to-be-scenario-map-<topic>.html`.
- **Title:** `<User> To-be Scenario Map`, for example "New Hire To-be Scenario Map".
- **Sections:**
  1. **Scenario:** the user, the goal and the ideas in this future, then a table of what the map must answer: the pain point or need, its as-is phase, and a tag pill with its source.
  2. **The map:** `.scroll` > `.map`, with `--cols` set to the number of phases and one `.ch` per phase.
     - Rows: Doing, Thinking and Feeling, then a "Still breaks" row.
     - Doing, Thinking and Feeling cells hold `assumption` notes. Thinking notes are quotes.
     - Each Feeling cell opens with a `.mood` of high, low or mixed.
     - "Still breaks" cells hold the walk-through's `simulated` notes, with `.src` set to `SU-4 · walk-through`.
  3. **Pain points resolved:** a table with the pain point or need, its as-is moment, its to-be moment, and a status pill (`data-tone="good"` for resolved, `"warn"` for improved or unchanged, `"bad"` for worse). Keep the original tag pill on each row.
  4. **Where it still breaks:** a table of phase, persona, what breaks, why it breaks in their context, and the follow-up, which is a new idea or a question.
  5. **Gaps and new risks:** `.notes` tagged `question` or `assumption`.
  6. **Walk-throughs:** a `details.transcript` per persona.
  7. **Playback.**

  A map with many phases scrolls sideways inside its frame, so keep it as one map rather than splitting it.
- **`content` in `#edt-data`:**
  ```json
  { "user": { "name": "", "role": "", "persona": "SU-2" }, "goal": "",
    "ideas": [{ "id": "I7", "headline": "", "source": "design-thinking/big-idea-vignettes-<topic>.html" }],
    "baseline": "design-thinking/as-is-scenario-map-<topic>.html",
    "phases": [{ "id": "P1", "name": "", "mood": "high|low|mixed",
                 "doing": ["N1"], "thinking": ["N2"], "feeling": ["N3"], "breaks": ["N9"] }],
    "pain_points": [{ "text": "", "as_is_phase": "", "to_be_phase": "P2", "status": "resolved|improved|unchanged|worse",
                      "tag": "evidence", "source": "S2" }],
    "breaks": [{ "phase": "P2", "persona": "SU-4", "what": "", "why": "", "follow_up": "", "note": "N9" }],
    "gaps": ["N14"] }
  ```
  `items` holds every note, with `group` set to `"<Phase> / Doing"` (or Thinking, Feeling, Still breaks), or `"Gaps"`.

## Quality checks
- **It relates back to the as-is map:** the same user and goal, and every key pain point is accounted for in the table.
- **It resolves pain points or fulfills needs statements.** An idea that addresses nothing is questioned.
- **It tells an engaging story** that someone outside the team can follow in a couple of minutes.
- The language is user-centric. Thinking notes are quotes, and Feeling notes name specific emotions like "relieved" or "uneasy" instead of "good".
- It has honest lows and named gaps. An all-highs map isn't credible.
- It isn't a feature spec, and it has no UI detail.
- Envisioned notes are tagged `assumption`, and nothing is presented as if it were observed.
- Simulation pitfalls:
  - personas who glide through the future and love it; each walk-through should find at least one real break or a reason to keep the old way
  - personas who sound alike, or who know the product's vocabulary
  - a break or reaction tagged `evidence`, or an assumption retagged because a persona agreed with it
  - percentages from simulated counts, such as "67% would adopt"

## Next
- `/edt-ideate:storyboards`: turn this future into a visual story with one persona.
- `/edt-ideate:big-idea-vignettes`: generate ideas for the lows and breaks that remain.
- `/edt-plan:hills`: capture the intended outcome as a Hill (Who, What, Wow).
- `/edt-plan:assumptions-and-questions`: plan how to validate the riskiest assumptions and breaks.
- `/edt-align:playbacks`: present the to-be map to stakeholders and Sponsor Users.
- `/edt-test:paper-prototypes`: make the highest-value phase testable.

## Source
[IBM Enterprise Design Thinking Toolkit: To-be Scenario Map](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9aa)
