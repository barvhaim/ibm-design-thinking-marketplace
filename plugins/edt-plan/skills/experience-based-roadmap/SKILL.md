---
name: experience-based-roadmap
description: Turns a long-term vision into a three-stage roadmap of user outcomes ("Our user can…") as an HTML artifact. Stage 1 is what we know we'll build, Stage 2 what we think, Stage 3 what we might, and each is a complete, usable slice checked with simulated users. Use when a team asks "build our roadmap", "what's our MVP", "what goes in v1 versus later" or "slice this vision into releases", or when a feature-list roadmap needs reframing around users.
argument-hint: "[product, Hill or vision] [facilitate]"
---

# Experience-based Roadmap

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~60 min

Feature roadmaps say what the team will ship. Experience-based roadmaps say what users will be able to do, and when. In this activity the team reflects together to scope a long-term experience into stages, each giving users at least one complete task they can achieve. That matches what a minimum viable product really is: delivering just enough to learn how to move forward. A true MVP is a full experience that works, so it's functional, reliable, usable and even delightful. Think of a thin slice of pizza that still has crust, sauce and toppings, not a crust with no toppings. The result gives the team clarity for near-term action and a vision for the long-term outcome.

## When to use it
- Once the team has identified users' real problems and needs and has ideas for addressing them.
- When defining an MVP or a first release, so it delivers a complete experience rather than one layer of the stack.
- When an existing roadmap is a list of features and nobody can say what a user gets at each step.
- After prioritizing, to turn "what matters" into "what comes when".

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of `hills-*` (the long-term vision), `to-be-scenario-map-*`, `big-idea-vignettes-*`, `prioritization-grid-*`, `needs-statements-*`, `user-stories-*` and `assumptions-and-questions-*`.
- **The simulated user panel,** `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the release horizon in calendar terms (for example, quarters) and the hard constraints, such as commitments, dependencies and capacity. Ask for the vision only if there are no Hills.
- If there are no needs statements and no ideas yet, this activity is premature. Suggest `/edt-synthesize:needs-statements` or `/edt-ideate:big-idea-vignettes`.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream data. Restate the vision and the Hills it serves, the target user and the candidate ideas, keeping each one's tag. Confirm what "short term" and "long term" mean for this team.
2. **Set up the frame.** Head the roadmap "Our <user> can… / will be able to…". Short term goes on the left and long term on the right.
3. **Ideate user tasks.** Finish the sentence with as many user tasks as possible, drawing on the to-be scenario, the grid and the stories. Ask the user to add more.
   - Convert feature language into experience language as you go. For example, "SSO integration" becomes "Our user can sign in with their work account". Point out each conversion.
   - Infrastructure that doesn't map to a user task goes in a separate Enablers list. It isn't a roadmap item.
4. **Sort.** Place each task on the continuum from short term to long term, relative to the others. For each task, ask:
   - Does it depend on another task?
   - How important is it? Use the prioritization grid if one exists.
   - How confident are we that users need it? Check its tag: `evidence`, `simulated` or `assumption`.
   - Does it need to happen soon, or can it wait?
5. **Establish three stages.** Draw two lines that divide the continuum:
   - **Stage 1, we know we'll build this.** It's committed and rests on the strongest basis the team has.
   - **Stage 2, we think we'll build this.** It's likely, but it depends on what Stage 1 teaches.
   - **Stage 3, we might build this.** It's the vision, still open.
6. **Check each stage is a slice.** Every stage must let the user complete at least one end-to-end task. Walk through that task and check it against the pyramid: functional, reliable, usable, delightful. If Stage 1 is "the backend" or "the data model", it's a layer, not a slice, so rework it.
7. **Check the near term with simulated users.** For Stage 1, and Stage 2 if time allows, pick 2–3 personas from the panel who match the user, including the skeptic. Run each one separately, in character:
   - Describe the stage's end-to-end task in plain words, never as a feature list, and ask about their last week: "What did you do instead? What did it cost you?"
   - Ask: "If you could do this, would it change your week? What would you stop doing?"
   - Walk them through the task step by step and ask what's missing that would stop them using it at all. A missing step means the stage is a layer for this person, not a slice.

   Record each session as a transcript, and each reaction as a `simulated` note on the item it concerns. An item that changes nobody's week is a candidate to move later. If every persona says every item would change their week, the simulation is too polite, so rerun it with more friction. Simulated reactions inform the order; they never count as the evidence that puts an item in Stage 1.
8. **Write the promotion criteria.** For Stage 2 and Stage 3 items, note what real evidence or result would move each one forward a stage. This links the roadmap to learning instead of dates. A simulated reaction alone never promotes an item.
9. **Play back.** Narrate each stage as a short story: "In Stage 1, <user> can…". Stage 1 feeds the next planning session. Put the Stage 1 items that rest only on simulated or assumed reactions at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/experience-based-roadmap-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0:00–0:07 Intro: why experiences beat features, the MVP pizza slice, the rules
  - 0:07–0:10 Set up: write "Our user can…" across the top of the sheet, with Short term on the left and Long term on the right
  - 0:10–0:22 Ideate: silent writing of user tasks, one per sticky, finishing the sentence
  - 0:22–0:37 Sort: post the stickies and reposition them relative to each other. Now or later?
  - 0:37–0:50 Establish: draw two lines to make three stages, and check each holds at least one complete task
  - 0:50–1:00 Playback: one person plays back each stage. Pull the Stage 1 stickies for the next planning session
- **Prompts to read aloud:**
  - "Finish the sentence: our user can… Start each sticky with a verb the user does."
  - "If we shipped only this stage, could a user finish a real task end to end?"
  - "Is this a slice of the pizza, or just the crust?"
  - "What would we need to learn to move this from 'we think' to 'we know'?"
- **Materials:** a large sheet or a Mural canvas, sticky notes, markers, a timer, and the Hills and prioritization grid posted nearby.
- **An empty board:** "Our user can… / will be able to…" across the top, three empty `.cols` for Stage 1 "We know", Stage 2 "We think" and Stage 3 "We might" running short term to long term, and a strip for Enablers and a Parking lot.

After the session, read the photos or the board export and build the results page stage by stage, keeping each sticky's wording. Offer to run the simulated check (step 7) on the Stage 1 items.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/experience-based-roadmap-<topic>.html`.
- **Title:** `<Product> Experience-based Roadmap`, for example "Claims Intake Experience-based Roadmap".
- **Sections:**
  1. **Our <user> can…:** `.cols` with one `.col` per stage, headed with the stage label and its timeframe. Each `.col` starts with its end-to-end task and the slice check as four pills (functional, reliable, usable, delightful) with `data-tone`. Then come its items as tagged `.note`s starting "Our user can…", each `src` naming its Hill and source.
  2. **Each stage as a story:** `.frames`, one frame per stage, with an ASCII or `<svg>` sketch of the end-to-end task and a caption "In Stage 1, <user> can…".
  3. **Near-term check:** a table of item, persona, "would this change your week?" as a `data-tone` pill next to a `simulated` pill, and what's missing. Then a `details.transcript` per session.
  4. **Stage details:** a table of item, Hill, basis (tag pill), depends on, and moves forward if….
  5. **Enablers and parked:** `.cols` with Enablers (each with the stage that needs it) and Parked (each with why).
  6. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "vision": "", "user": "", "hills": ["H1"], "horizon": "",
    "stages": [{ "n": 1, "label": "We know", "timeframe": "", "end_to_end_task": "",
      "slice_check": { "functional": true, "reliable": true, "usable": false, "delightful": false },
      "items": [{ "id": "R1", "text": "Our user can …", "hill": "H1", "tag": "evidence", "source": "S2",
        "depends_on": [], "promote_if": "",
        "sim_check": [{ "persona": "SU-2", "changes_week": "yes|somewhat|no", "missing": "", "note": "N9" }] }] }],
    "enablers": [{ "text": "", "for_stage": 1 }],
    "parked": [{ "text": "", "why": "" }] }
  ```
  `items` holds every roadmap item and every check note, with `group` set to `"Stage <n>"`.

## Quality checks
- **Experiences, not features.** Every item starts "Our user can…" followed by a user action and outcome. Reject component names like "API v2", "dashboard" or "ML model".
- **The items are written from the user's point of view.** You should be able to read any item to a sponsor user and have them nod or object.
- **Each stage contains at least one complete task,** usable end to end. A stage that only makes sense after the next one ships is a layer, not a slice.
- **Confidence falls honestly from left to right.** Stage 1 items carry the strongest basis available, ideally `evidence`. If a Stage 1 item rests only on simulated or assumed reactions, the page says so plainly and names the real check needed before committing.
- **The near-term check has friction.** It includes a skeptic, the personas sound like different people, and at least one shrugs at something. Simulated reactions stay tagged `simulated`, and counts read "1 of 3 simulated users", never as percentages.
- **Stage 1 is concrete enough to write user stories from tomorrow.** Stage 3 is still ambitious enough to inspire.
- **No firm dates are promised for Stage 3,** and Stage 2 dates depend on what Stage 1 teaches.
- **Every item traces to a Hill.** Items that don't are challenged or parked.

## Next
- `/edt-plan:user-stories`: break the Stage 1 items into stories with acceptance criteria.
- `/edt-plan:assumptions-and-questions`: list what must be learned to promote Stage 2 items.
- `/edt-plan:research-plan`: schedule that learning ahead of the next iteration.
- `/edt-align:playbacks`: play the roadmap back to stakeholders and sponsor users.

## Source
[IBM Enterprise Design Thinking Toolkit: Experience-based Roadmap](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac15)
