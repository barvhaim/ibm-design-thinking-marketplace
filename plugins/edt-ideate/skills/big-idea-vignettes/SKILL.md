---
name: big-idea-vignettes
description: Diverges on many ideas for one user need, then clusters and converges, as an HTML artifact of sketched vignettes, each with a one- or two-word headline. You write your ideas first, simulated users react to the shortlist, and the team decides. Use when someone says "let's brainstorm", "we need ideas", "how might we…", "we're stuck", "ideate on this need, Hill or pain point", or wants options before committing to a solution.
argument-hint: "[needs statement, Hill or pain point] [facilitate]"
---

# Big Idea Vignettes

> IBM Enterprise Design Thinking · Generate new ideas · Make / Reflect · ~30 min

Teams tend to fall for the first plausible solution. Big Idea Vignettes force breadth first. Everyone quickly produces many ideas, each one a single frame showing how a user would experience the solution, before anyone judges them. Only then does the team cluster, spot patterns and converge on a set to pursue. Everyone sees the user and the problem differently, so everyone contributes ideas; ideation is not just the designers' job. Simulated users then react to the shortlist, so the team hears "I wouldn't notice that" before it commits. The team still makes the call.

## When to use it
- You have a clear prompt, such as a needs statement, a Hill, a user story or an as-is pain point, and you want solution options.
- The team is stuck, circling one idea, or arguing about implementation too early.
- Before a To-be Scenario Map or Storyboards, to choose which ideas to develop.
- Any time you want to improve something. It's quick enough to run often.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - prompts: `needs-statements-*` (statements and their tags), `hills-*` (Who, What, Wow), `user-stories-*`, and the lows and gaps of `as-is-scenario-map-*`
  - user context: `empathy-map-*` and `simulated-users.html`
  - earlier `big-idea-vignettes-*` pages, so you don't repeat a round
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:**
  - which prompt to use, if there are several
  - their own ideas, before you show any of yours
- If there's no need, Hill or pain point at all, ideas float free of users. Suggest `/edt-synthesize:needs-statements` or `/edt-synthesize:as-is-scenario-map` first, or proceed with the prompt tagged `assumption`.

## Co-create with Claude
1. **Set up the prompt.** Propose 1–3 candidate prompts from the upstream pages, quoting each one with its tag and source. The user picks one. Use one prompt per round, and run again for others. Add a "How might we…?" phrasing if it helps.
2. **The user writes before Claude talks.** Ask the user to dump their own ideas first: rough headlines, no judging. This keeps Claude from anchoring the session. If they'd rather skip, proceed and invite additions later.
3. **Diverge.** First, "yes, and" each of the user's ideas: push it further, combine it, flip it. Then add your own, aiming for 20+ in total across a wide range. Use lenses to escape the obvious:
   - remove the step entirely · do it before the user asks · do it for them
   - make it social or shared · playful · zero-effort
   - 10x bigger, or a tiny low-tech version
   - borrow from another industry or from everyday life
   - invert it: how could we make this worse? Then flip each answer
   - design it for the most novice persona on the panel, then for the most expert
   - include at least three deliberately wild ideas

   Write each idea as a vignette: a **headline** of one or two words, plus one present-tense sentence describing what the user experiences in that moment. For example: *Ready Desk: she walks in and her desk already shows her name.* Give each one a rough sketch for its frame.
4. **Ideas, not features.** A big idea describes how a user experiences the solution, and a feature describes how it's built. Rewrite anything that names implementation, such as a dropdown, an API or a dashboard widget, as the experience it enables. Put feasibility concerns in the parking lot and don't debate them yet.
5. **Converge.** Cluster by affinity, and name each cluster after the user outcome it delivers, not the technology behind it. Show the clusters and let the user or their team vote, for example with three votes each. Don't pick a winner yourself. The 3–5 most-voted vignettes or clusters form the shortlist. Keep the unchosen ideas, because they are the team's option backlog.
6. **Simulated users react to the shortlist.** Choose 2–4 personas from the panel for spread: the persona the prompt is about, a skeptic or non-adopter, and an edge case. Run them one persona at a time, in character, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
   - Describe each vignette in the persona's words, not the team's. Don't use the headline as a sales pitch.
   - Ask about their real life: "When would this have come up for you last week?" "What would you have to stop doing?" "What would make you ignore it?"
   - Let them be honestly indifferent ("I'd never notice that"), confused, or opposed. Most people don't care about most ideas.
   - Record one `simulated` note per persona per vignette, with the persona ID and a stance: wants it, indifferent, objects or confused. Keep the transcript.

   If every persona likes every vignette, the simulation is broken. Rerun it with more friction.
7. **The team decides.** Show the votes and the reactions side by side. The user or the team chooses the direction or directions, and can change the shortlist in light of the reactions, but reactions never outvote the team. If asked, offer perspectives (user impact, novelty, effort) and suggest `/edt-plan:prioritization-grid`.
8. **Tag what the chosen ideas rest on.** Ideas are proposals, not facts. For each chosen cluster, list the `assumption`s it depends on and the `question`s to answer, including what the simulated reactions raised. Keep the prompt's original `evidence` tags and sources.
9. **Playback.** Tell back the range explored, the chosen direction and why, and the reaction that surprised you most. Put the simulated reactions the choice leans on at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/big-idea-vignettes-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**

  | Time | Step | Notes |
  |---|---|---|
  | 0–3 | Intro and norms | Write before you talk · no bad ideas · ideas, not features · yes, and · parking lot |
  | 3–5 | Prompt | Read it aloud and post it where everyone can see it |
  | 5–15 | Silent diverge | One idea per sticky: a quick sketch plus a one- or two-word headline |
  | 15–20 | Share and build | Each person posts and explains in 30 seconds or less; others build on new stickies |
  | 20–26 | Cluster and name | Silently move similar ideas together, then name the clusters |
  | 26–28 | Converge | Dot vote, three dots each |
  | 28–30 | Playback | One person plays back each cluster; add ideas as they come |
- **Prompts to read aloud:**
  - "Our prompt is: … For ten minutes, silently sketch as many ideas as you can, one per sticky. Draw what the user would experience, then give it a one- or two-word headline."
  - "Quantity beats quality right now. If it feels too wild, write it anyway."
  - "If you catch yourself drawing a button or a database, ask what the user experiences, and draw that instead."
  - "Building on someone else's idea counts. It's encouraged."
  - Converge: "Without talking, move ideas that feel related closer together. Then we'll name the groups."
- **Materials:** large sticky notes you can sketch on, a marker for everyone, dot stickers and a timer.
- **The board:** the prompt as a `.stmts` banner, an empty `.frames` grid for the diverge, and `.cols` for the clusters and the parking lot. Leave it empty, or seed two or three example vignettes labeled Assumption.

After the session, read the photos or the Mural export. Transcribe every sticky, including unvoted ideas and the parking lot. Keep who wrote what, record the vote counts, and mark any ideas Claude adds afterward as "Claude, post-session". Then run step 6 on the shortlist and bring the reactions to the next sync, so the team decides with them in view.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/big-idea-vignettes-<topic>.html`.
- **Title:** `<Topic> Big Idea Vignettes`, for example "New Hire Desk Big Idea Vignettes".
- **Sections:**
  1. **Prompt:** one `.stmt` holding the chosen prompt, with pills for its tag and source, and the "How might we" phrasing in `.why`.
  2. **Vignettes:** one `h3` per cluster, named as a user outcome, with its vote count, followed by a `.frames` grid. Each `.frame` holds:
     - `.frame-art`: a rough sketch, either ASCII (about 24 characters wide and 4–6 lines) or an inline `<svg>` drawn in `currentColor`
     - `.frame-n`: `Idea 7 · Ready Desk`
     - `.frame-cap` text: the experience sentence, then its origin (the user, Claude or a name) and the idea it builds on
  3. **Simulated reactions:** one `.cluster` per shortlisted vignette, its `h4` the headline, holding one `.note[data-tag="simulated"]` per persona. Each note's `.src` reads `SU-3 · indifferent`. Follow it with a table of vignette, votes, and the number of simulated users who want it, are indifferent, object or are confused, written as counts, never percentages.
  4. **Chosen direction:** a table of the cluster, why the team chose it, the assumptions it depends on and the questions to answer, each with a tag pill.
  5. **Parking lot:** `.notes` tagged `assumption` or `question`.
  6. **Reaction sessions:** a `details.transcript` per persona.
  7. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "prompt": { "text": "", "type": "needs-statement|hill|user-story|pain-point", "how_might_we": "",
                "source": "design-thinking/needs-statements-<user>.html", "tag": "evidence" },
    "ideas": [{ "id": "I7", "headline": "Ready Desk", "experience": "", "origin": "user|claude|<name>",
                "builds_on": ["I2"], "cluster": "C1", "wild": false }],
    "clusters": [{ "id": "C1", "name": "", "ideas": ["I7"], "votes": 5 }],
    "shortlist": ["I7"],
    "reactions": [{ "idea": "I7", "persona": "SU-3", "stance": "wants|indifferent|objects|confused", "note": "N12" }],
    "chosen": [{ "cluster": "C1", "why": "", "assumptions": ["N20"], "questions": ["N21"] }],
    "parking_lot": ["N30"] }
  ```
  `items` holds every tagged note, with `group` set to `"Reactions / <headline>"`, `"Chosen / <cluster>"` or `"Parking lot"`.

## Quality checks
- There is one prompt, and it traces to a real need. It is not a solution in disguise, like "users need a dashboard".
- Volume and range: 20+ ideas from safe to wild, not 20 variations on one idea.
- Each vignette is an experience a user would notice, with a headline. Features and implementation details don't count.
- The user's own ideas come first and are credited. Claude built on them instead of replacing them.
- Nobody evaluated during the diverge. Cluster names describe user outcomes.
- Simulated users reacted only after the team voted, one persona at a time, and the team made the choice. Unchosen ideas are kept.
- Simulation pitfalls:
  - personas who love every idea; most shortlisted ideas should draw at least one shrug or objection
  - personas who sound alike, or who use the team's vocabulary and headlines
  - a reaction tagged `evidence`, or a choice justified by "the users liked it"
  - percentages from simulated counts, such as "75% want it"
- Other pitfalls: converging on whatever is easiest to build, and Claude presenting one polished favorite.

## Next
- `/edt-ideate:storyboards`: show how a chosen idea fits into a persona's life.
- `/edt-ideate:to-be-scenario-map`: envision the end-to-end future experience with the chosen ideas.
- `/edt-plan:prioritization-grid`: rank clusters by user value and feasibility.
- `/edt-plan:hills`: turn a winning direction into a Hill.
- `/edt-core:sponsor-users`: show the shortlist to real users and check the simulated reactions.

## Source
[IBM Enterprise Design Thinking Toolkit: Big Idea Vignettes](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac1f)
