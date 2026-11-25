---
name: as-is-scenario-map
description: Maps a user's current end-to-end experience as an HTML artifact, with named phases, Doing, Thinking and Feeling rows, and the highs, lows and gaps in team knowledge. It builds on research and on 2–3 simulated users walking through their last real attempt. Use when the user says "as-is scenario", "current-state journey", "journey map", "map the current experience", "where are the pain points?" or "how does it work today?", or at the start of new work.
argument-hint: "[user and scenario] [facilitate]"
---

# As-is Scenario Map

> IBM Enterprise Design Thinking · Synthesize research · Reflect · ~30 min

Before you can improve an experience, the team has to agree on what it is today. An as-is scenario map lays out a user's present experience phase by phase: what they're doing, thinking and feeling at each step. The team can then see where things work, where they break, and where nobody actually knows. It turns scattered research into one shared picture of current reality and points to opportunities for improvement. When research is thin, simulated users walk the team through their last real attempt, so the map starts from a told story rather than the official process. This is Reflect. The future experience belongs on a to-be map, where you Make.

## When to use it
- As the team starts a new body of work, to surface what it collectively knows and doesn't know.
- After research, to make sense of interview and observation data.
- When stakeholders disagree about where the real problem is.
- Before writing Hills or a to-be scenario.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the user: `empathy-map-*` (use the same user) and `simulated-users.html`
  - research: `interviews-*`, `contextual-inquiry-*`, `sponsor-users-*`
  - context: `stakeholder-map-*`, for the other people in the experience
  - history: earlier `as-is-scenario-map-*` pages
- **Files the user points to,** such as transcripts, support tickets, process docs or analytics. These are real evidence. A process doc shows the official path, not necessarily what people do.
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** which *one* user the map is for and which scenario, with a clear start and end, if you can't infer them. For example: "from noticing a billing error to seeing it corrected".

## Co-create with Claude
1. **Gather.** List `design-thinking/` and read the research. Build a source list: `S1…` for each real source and `SU-…` for each simulated user who represents this user.
2. **Set up.** Agree on the user and the scenario, including the trigger that starts it and the outcome that ends it. Create the rows **Doing**, **Thinking** and **Feeling** under a header of phases. Add a row for tools or people involved only if the user wants it.
3. **Simulate the walk-throughs.** Pick 2–3 personas from the panel who are this user, in different contexts and with different attitudes, including a skeptic or the edge case. Interview them one at a time, in character. Ask each to walk through the *last time* they went from the start to the end: "Start from the moment you noticed… What did you do next? What was going through your head? How did that feel?" Each persona tells it as it happened, including other tools, other people, paper, waiting, the step they skipped, and where they gave up and came back later. Probe for one high and one low. Keep the transcripts. If real research already covers the journey, simulate only the phases it leaves thin.
4. **Brainstorm.** From the research and the walk-throughs, write one item per note in its row, and tag it:
   - `evidence`: from a real source, with its `S…` ID.
   - `simulated`: from a walk-through, with its `SU-…` ID.
   - `assumption`: what the team believes. Ask the user what the team knows beyond the documents, and add it with this tag.
   - `question`: what nobody knows.

   Include the steps outside your product: other tools, other people, paper and waiting.
5. **Review and cluster.** Put the items in time order and group them into phases. Name each phase from the user's point of view with a verb, for example "Find a flight", not "Search module". Most scenarios have 4–8 phases. Where the personas differ within a phase, keep both notes side by side with their sources. If they follow different phases altogether, they're different users, so split the map. Mark an empty cell with a `question` note instead of filling it with a guess.
6. **Identify highs, lows and gaps.** Mark the especially positive moments, the especially negative ones, and the areas where the team needs to learn more. Annotate each one with why it matters, for example "Critical moment for trust", "Missed opportunity" or "Works well today, so protect it". Start each Feeling cell with a `.mood` of high, low or mixed, and use mixed where the personas disagree. Optionally score each phase's emotion from −2 to +2 per persona to show the curve. Never average the scores into one "user score".
7. **Playback.** Answer two questions. Which parts are we certain are true, and on what evidence? Where are the gaps in the team's knowledge? If most of the map is simulated, say so plainly. List the top lows as candidate opportunities, put the simulated lows the team leans on most at the top of "Validate next", and recommend what comes next. Then publish the page.

## Facilitate a live session
Produce `design-thinking/as-is-scenario-map-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0–3 Intro: why you're doing this, and the norms (write before you talk, there are no bad ideas, stay focused on users, use a parking lot)
  - 3–5 Setup: write the scenario, with its start and end, across the top and the row labels down the left side
  - 5–15 Brainstorm: everyone writes silently, one note each, placing each note in its row
  - 15–22 Review and cluster: order the notes left to right, draw rough column lines, and name the phases
  - 22–27 Identify: circle and label the highs and lows, and put a "?" on blank areas
  - 27–30 Playback: one or two people tell the story, then ask what we're certain of and where the gaps are
- **Prompts to read aloud:** "What is our user doing, thinking and feeling throughout this experience? One idea per sticky." "What happens *before* they ever touch our product? What happens after?" "Where would they say 'this part is great'? Where would they give up?" "Which of these notes did we actually see or hear? Which are we guessing?" "Where on this map are we least sure what happens?"
- **Materials:** a long wall or a wide Mural canvas, sticky notes in three colors (one each for Doing, Thinking and Feeling), markers, and symbols for highs (+), lows (−) and gaps (?).
- **An empty map board:** the `.map` component with the scenario's start and end in the lede, blank phase headers, the Doing, Thinking and Feeling rows, and a parking lot. Optionally seed it with the simulated walk-throughs' notes so the team can react to them, labeled as simulated.

After the session, read the photo of the wall or the Mural export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/as-is-scenario-map-<topic>.html`. `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows a finished page.
- **Title:** `<User or scenario> As-is Scenario Map`, for example "Billing Correction As-is Scenario Map".
- **Sections:**
  1. **Scenario:** the user and the scenario's start and end in the lede, with `.personas` cards for the simulated users who walked it, copied from the panel.
  2. **The map:** `.scroll` > `.map`, with `--cols` set to the number of phases. Use one `.ch` per phase, named with a verb, with `<small>Phase n</small>`. Add `.rh` rows for Doing, Thinking and Feeling, plus Tools and people if used. Each Feeling cell starts with a `.mood`. Every item is a tagged `.note` with its source in `.src`.
  3. **Highs, lows and gaps:** a table of phase, moment, why it matters, emotion per persona (if scored), sources and a tag pill. Show the moment as a pill: `data-tone="good"` for a high, `data-tone="bad"` for a low, `data-tag="question"` for a gap.
  4. **Confidence:** `.cols` with three columns of notes: *Certain (evidence)*, *Simulated only* and *Gaps in team knowledge*.
  5. **Opportunities:** `assumption` notes, each naming its phase, to carry into Needs Statements and Hills.
  6. **Simulated walk-throughs:** a `details.transcript` per persona. Include this only when you ran any.
  7. **Parking lot,** if anything landed there, then the **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "user": { "name": "", "role": "", "empathy_map": "design-thinking/empathy-map-<user>.html" },
    "scenario": { "start": "", "end": "" },
    "phases": [{ "id": "P1", "name": "", "doing": ["N1"], "thinking": ["N2"], "feeling": ["N3"], "mood": "low",
                 "emotion": { "SU-1": -1, "SU-3": -2 },
                 "moments": [{ "type": "low", "why": "", "notes": ["N3"], "tag": "simulated" }] }],
    "opportunities": [{ "text": "", "phase": "P3", "tag": "assumption" }],
    "confidence": { "certain": ["N4"], "simulated_only": ["N2"], "gaps": ["N9"] },
    "parking_lot": [""] }
  ```
  `mood` is `high`, `low` or `mixed`, and `moments[].type` is `high`, `low` or `gap`. `items` holds every note, with `group` set to `"<Phase> / <Row>"`.

## Quality checks
- The map covers one user and one scenario, with an explicit start and end.
- Phases are named from the user's point of view, in their words. They are not system components or departments.
- It shows today's reality, including the workarounds, not the official process or a fixed version. Solutions and features belong on the to-be map.
- Each phase has Doing, Thinking and Feeling filled in, or an explicit `question` note.
- Feeling names emotions with causes, and they vary across phases. If every phase says "frustrated", dig deeper.
- Highs are marked as well as lows, because what works today has to survive into the to-be.
- Every note is tagged and sourced, and gaps are named, not filled with guesses. No simulated note is tagged `evidence`.
- Each walk-through is a specific past event with its own detours. If every persona moves through the same tidy steps, or the steps match your product's screens, rerun them with more friction.
- Personas' feelings differ where their contexts differ. Counts read "2 of 3 simulated users stalled here", never as percentages, and emotion scores are never averaged.
- Pitfalls:
  - Mapping only your product's screens instead of the whole experience
  - Going click-level detailed, or so coarse that there are only three phases
  - Blending several users into one journey

## Next
- `/edt-synthesize:needs-statements`: turn the lows and gaps into needs.
- `/edt-plan:hills`: write intent around the moments that matter most.
- `/edt-ideate:to-be-scenario-map`: reimagine the same scenario as it could be.
- `/edt-ideate:big-idea-vignettes`: generate ideas for the biggest lows.
- `/edt-gather:contextual-inquiry`: go and observe the phases marked as gaps.
- `/edt-plan:assumptions-and-questions`: prioritize what the map left uncertain.

## Source
[IBM Enterprise Design Thinking Toolkit: As-is Scenario Map](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac29)
