---
name: paper-prototypes
description: Plans a Paper Prototype, a fast hand-made model of a task flow built from movable paper pieces, as an HTML artifact: purpose, step-by-step flow, an ASCII sketch of every piece, and simulated users trying it while a teammate plays the computer. Photos of real pieces and sessions work too. Use early in an idea, or when someone says "mock it up quickly", "prototype this on paper", "test the concept before we build" or "try the flow with users".
argument-hint: "[idea or flow] [facilitate]"
---

# Paper Prototypes

> IBM Enterprise Design Thinking · Test your ideas · Make, then Observe · ~60 min

Paper is the cheapest way to give an abstract idea a concrete form. Paper, tape and a pen are enough to make a flow that someone can hold, react to and try. A paper prototype costs minutes to make, so nobody is attached to it. That makes people more willing to throw a piece away, and more willing to give honest criticism. The goal is to play and to learn while the stakes are low. Making also teaches the team something on its own: every piece you crumple up is a thing you now know doesn't work.

## When to use it
- In the first stages of an idea, before wireframes or code.
- When a Big Idea, a Storyboard or a To-be Scenario Map needs something tangible people can react to.
- When you want users or teammates to try a flow in person, at a workshop, a Playback or a sponsor user session.
- When the team keeps describing the idea in words and everyone pictures something different.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the idea: `to-be-scenario-map-*`, `storyboards-*`, `big-idea-vignettes-*`
  - the user and outcome: `hills-*`, `needs-statements-*`
  - what to check: `assumptions-and-questions-*`, plus the `assumption` and `simulated` entries in upstream `items`
- **Photos of real paper pieces or session notes,** if the team has already built or shared the prototype. These are real evidence.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** the idea, if no upstream page names it, and who will see the prototype (peers, stakeholders or users). A remote team can use `/edt-test:wireframes` instead, since paper works best in a room.

## Co-create with Claude
Claude can't cut paper, but it can plan the prototype, sketch every piece, run simulated sessions on it, and digitize the real pieces and sessions afterward.

1. **Gather.** Read the upstream pages and build a source list: `S…` for real sources, such as photos and session notes, and `SU-…` for the personas who match the idea's user.
2. **Decide the purpose.** Pick what this prototype is for, because the purpose shapes everything else:
   - **Communicate** the idea to peers or stakeholders and get their reactions.
   - **Test** the idea with users to see whether it works.
   - **Explore** the idea by making it, so the team learns as it builds.

   Write down the Hill or the assumptions it should inform.
3. **Document the task flow.** Break the experience the user will go through into ordered steps, and be meticulous. For each step, record what the user sees, what they do, and what happens next. Include any error, empty or confirmation state that the flow needs. A missing step will stall the test.
4. **Sketch the pieces.** Turn every step into paper pieces:
   - one base sheet per screen or surface
   - separate, movable pieces for anything that changes, such as menus, dialogs, messages, selected states and typed-in text (sticky notes work well for these)

   Label each piece with its step: `2` for the base, `2a`, `2b` for the pieces laid over it. Draw each one as an ASCII frame, with thick-marker detail only: boxes, a few labels, real words from the domain. It's a guide for the build, not a design. Keep each piece within about 28 characters by 9 lines so it fits its frame without scrolling.
5. **Make it.** The team builds from the sketches without skipping a step. If the team won't build it, Claude's sketches are the prototype. Encourage fast attempts: try a layout, crumple it, try another. Log every discarded attempt, including Claude's own, with one line on why it didn't work. These are findings too.
6. **Plan the share.** Choose a mode that fits the purpose:
   - **Demo and ask:** walk peers or stakeholders through the flow, then ask for direct feedback.
   - **Let them drive:** give a user the scenario and have them complete the flow while thinking aloud. One teammate plays the "computer" and swaps pieces in response to taps, without speaking. For the scenario, the script and neutral prompts, use `/edt-test:cognitive-walkthrough`.
7. **Run simulated sessions.** For a Test, run "let them drive" with 3–5 personas, including the novice, a skeptic and the edge case, one at a time. Claude plays three roles and keeps them apart in the transcript:
   - **Facilitator:** reads the scenario and uses only neutral prompts, such as "What are you thinking?" and "What do you expect that will do?". Never explains the paper.
   - **Persona:** in the first person, taps, points and "types" on the pieces in front of them, thinking aloud in their own words. They react only to what's drawn on the current pieces.
   - **Computer:** the teammate role. Silent. Only narrates the piece swaps, in brackets: "[lays 2a over sheet 2: the trip menu opens]". If there's no piece for what the persona did, the computer does nothing. That's a missing piece and a finding.

   Record how far each persona got, where they stalled, and whether they finished alone (Success), with a hint (Assisted), or not at all (Failed). Tag the notes `simulated`, with the persona ID and step in `src`, and keep every transcript. For **Communicate**, demo the flow to each persona instead, then ask what works, what they'd change, what's unclear and what they'd add. For **Explore**, the making log is the main output, and simulated sessions are optional.
8. **Digitize real pieces and sessions.** Ask for photos of each piece and the session notes. Claude reads the images, redraws each piece as ASCII in its frame, records it against its step, and cites the photo as an `S…` source. Real participants are `P…`, and their notes are `evidence`, shown beside the simulated ones, never merged.
9. **Sort the feedback** with `/edt-test:feedback-grid` when there's a lot of it.
10. **Check assumptions.** For each upstream assumption the prototype touched, give a verdict:
    - from real users: **Validated**, **Invalidated** or **Inconclusive**
    - from simulated users only: **Simulated: supported** or **Simulated: contradicted**, never Validated
11. **Play back** what you found and what you learned from making. Put the simulated claims the team leans on most at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/paper-prototypes-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0:00–0:05 Intro: explain the purpose and the Hill or assumption in focus; rough is the point
  - 0:05–0:15 Plan: teams of 2–3 write the task flow as numbered sticky notes in a row
  - 0:15–0:40 Make: build one piece per step, keep the pieces modular, crumple freely
  - 0:40–0:55 Share: swap with another team, or bring in a sponsor user; one person plays the computer and one takes notes
  - 0:55–0:60 Playback: each team shares its top findings and one thing it learned from making
- **Prompts to read aloud:**
  - "What is this prototype for: to show, to test, or to explore?"
  - "Walk the flow step by step. What does the user see, what do they do, and what happens next?"
  - "Use the fewest words and lines that still get the idea across."
  - "If it isn't working, crumple it up and write down why."
  - When sharing: "Don't explain it. Hand it over and watch."
- **A computer role card:** stay silent, swap pieces only in response to a tap, and do nothing when there's no piece for it.
- **Materials:** colored paper, tape, pens and thick markers (they stop people from drawing too much detail), sticky notes, scissors, index cards, a cardboard base or clipboard, and transparency sheets for text fields (optional).
- **Board layout:** the task flow as a row of numbered steps across the top, with empty frames for each step's pieces beneath it, a "crumpled" column for discarded attempts and their reasons, and a Feedback Grid at the end. Optionally seed the frames with Claude's sketches, labeled Assumption.

After the session, read the photos and notes and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/paper-prototypes-<topic>.html`.
- **Title:** `<Idea> Paper Prototype`, for example "Trip Receipts Paper Prototype".
- **Sections:**
  1. **Purpose:** a `.board` with the purpose, the Hill or assumptions it informs, the audience and the share mode.
  2. **Task flow:** a table of step, what the user sees, what they do, and what happens next.
  3. **The pieces:** `.frames`, one frame per piece, in step order. `frame-n` reads `Step 2a · Overlay`, and the caption says what the piece shows and what makes the computer lay it down. Cite the photo source when there is one.
  4. **Learned from making:** a "Crumpled" `.cluster` with one note per discarded attempt: what was tried and why it was dropped. Tag it `assumption` for the team's judgment, `simulated` or `evidence` when a session caused it.
  5. **Share sessions:** a table of who (ID and group), mode, the furthest step reached, where they stalled, and the outcome pill (`data-tone` `good` Success, `warn` Assisted, `bad` Failed). Then one `.cluster` per step with the tagged observation notes, and a "Missing pieces" cluster.
  6. **Assumptions checked:** a table of assumption, where it came from, verdict pill and note IDs. Real verdicts use `data-tone` (`good` Validated, `bad` Invalidated, `warn` Inconclusive). Simulated verdicts use a `data-tag="simulated"` pill reading "Simulated: supported" or "Simulated: contradicted".
  7. **Session transcripts:** a `details.transcript` per simulated session, with persona turns as `turn sim` and `Computer` turns for the piece swaps.
  8. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "purpose": "communicate|test|explore", "hill": "", "audience": "", "share_mode": "demo|drive",
    "flow": [{ "step": 1, "sees": "", "does": "", "next": "" }],
    "pieces": [{ "id": "2a", "step": 2, "type": "base|overlay|sticky", "shows": "", "trigger": "", "photo": "S2" }],
    "discarded": [{ "tried": "", "why": "", "tag": "assumption" }],
    "sessions": [{ "who": "SU-2", "kind": "simulated|real", "mode": "demo|drive", "reached_step": 4, "stalled_at": "3",
                   "outcome": "success|assisted|failed", "notes": ["N5"] }],
    "missing_pieces": [{ "step": 3, "what": "", "found_by": "SU-4" }],
    "assumptions": [{ "text": "", "from": "", "verdict": "validated|invalidated|inconclusive|simulated-supported|simulated-contradicted|untested", "notes": ["N5"] }] }
  ```
  `items` holds every note, with `group` set to `"Step <n> / <participant>"`, `"Crumpled"` or `"Missing pieces"`.

## Quality checks
- The purpose is stated, and the share mode matches it. You can't "test" a prototype you only demonstrated, and simulated demo sessions don't count as tests.
- The task flow is complete enough that someone can reach the end without the maker narrating.
- Pieces are modular and rough, with no polished visuals. If people comment on color or font, it's too refined.
- Discarded attempts are logged with reasons. Making is learning.
- The computer never explains or helps, and personas react only to what's drawn on the pieces in front of them.
- The personas stall where they realistically would. If every persona finishes without a hitch, rerun them with more friction. If two sound alike, rewrite one.
- Feedback from users and feedback from teammates are kept apart, and only real user feedback validates assumptions about users. No simulated note is tagged `evidence`.
- Simulated results are counts ("2 of 4 simulated users stalled at step 3"), never percentages.
- Common pitfalls:
  - building only the happy path
  - spending the whole hour on one screen
  - explaining the prototype while someone is trying it
  - keeping the prototype to yourself instead of playing it back

## Next
- `/edt-test:cognitive-walkthrough`: run a full walkthrough on the paper prototype, simulated or real.
- `/edt-test:feedback-grid`: sort the feedback and decide what changes.
- `/edt-test:wireframes`: move the surviving flow to digital low fidelity.
- `/edt-core:sponsor-users`: find real users to try the paper flow.
- `/edt-align:playbacks`: share the findings and what you learned with stakeholders.

## Source
[IBM Enterprise Design Thinking Toolkit: Paper Prototypes](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac09)
