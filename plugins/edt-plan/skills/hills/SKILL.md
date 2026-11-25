---
name: hills
description: Writes up to three Hills (Who / What / Wow statements of meaningful user outcomes) plus a Foundation as an HTML artifact. Each Hill traces to needs and is checked with simulated sponsor users. Use when a team says "write our Hills", "define the mission or north star", "turn these needs into goals" or "what are we really trying to do for users", or is kicking off a project or release. Also use to review or tighten existing Hills.
argument-hint: "[project or user] [facilitate]"
---

# Hills

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~60 min

A team that doesn't agree where it's going rarely gets there. Hills are statements of intent written as meaningful user outcomes. Each one says **who** gets the outcome, **what** they can now do, and the **wow**: why that's remarkable, which is the user and market value. Hills describe what a user is enabled to do, never how the team will build it. That leaves room for breakthrough ideas and gives stakeholders one sentence to rally behind. The classic example is JFK's 1961 goal: land a man on the Moon and return him safely to Earth before the decade is out. It names a who and a measurable what and wow, and says nothing about the rocket.

## When to use it
- At the start of a project, release or initiative, once you understand the users' real problems.
- When the team has needs statements and must turn them into goals it can commit to.
- When a roadmap or backlog has drifted into a feature list and nobody can say which user outcome it serves.
- To review existing Hills before a Hills Playback.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of `needs-statements-*` (the main input), `empathy-map-*`, `as-is-scenario-map-*`, `sponsor-users-*`, `stakeholder-map-*` and any earlier `hills-*`.
- **The simulated user panel,** `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the scope (one product, release or initiative), the business and market context (competitors, targets, deadlines), and who the real sponsor users are. None of these can be simulated.
- With no needs statements, suggest `/edt-synthesize:needs-statements` first. If the user wants to go ahead anyway, tag every Who and What `assumption`.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream data. Restate the user, their top needs and their pain points as a short list. Keep each item's tag and source as you found it: `evidence` with `S…`, `simulated` with `SU-…`, `assumption` or `question`. Confirm the scope.
2. **Set up Who / What / Wow.** Make three columns and explain them briefly:
   - **Who:** a specific user or user group, described by role and situation.
   - **What:** what they'll be able to do that they can't do today. It's an outcome, not a feature.
   - **Wow:** what makes it remarkable, measurable and different from what the market offers today.
3. **Diverge on each column separately.** Propose 5–8 options per column, drawn from the needs, and ask the user to add theirs. Go for quantity over quality. If an option names a technology, a screen or a component, rewrite it as an outcome and point out the change.
4. **Build sentences.** Mix and match options into 3–6 draft Hills using the pattern *Who* can *What* *Wow*. Try unexpected combinations as well as the obvious ones.
5. **Stress-test each draft** against the Quality checks. Be blunt. Give a short verdict per draft, such as "What is an implementation" or "Wow isn't measurable", with a suggested rewrite.
6. **Converge.** Keep no more than three Hills. Move the technical groundwork, platform work and fixes the Hills depend on into a **Foundation**. A Foundation isn't a fourth Hill. Split any Hill that's too big to deliver or test into Sub-Hills that share its Who. Record every rejected draft and why.
7. **Check with simulated sponsor users.** For each Hill, pick 2–3 personas from the panel who match its Who, and include the skeptic. Run each one separately, in character:
   - Describe the outcome in the persona's words, not the team's, and ask about the last time they faced this: "What did you do? What did it cost you?"
   - Ask: "If you could do this, would it matter to you? What would you stop doing?"
   - Ask: "What would make you say 'wow'? What would make you shrug?"

   Record each session as a transcript, and each reaction as a `simulated` note with the persona's ID. Use the answers to sharpen the Who and to find candidate Wow measures. A persona who shrugs is a finding, not a failure; keep it. If every persona loves every Hill, the simulation is too polite, so rerun it with more friction. Simulated reactions show whether an outcome *might* matter to people like this. They are never proof that the Wow beats the market.
8. **Define the Wow measure and name sponsor users.** For each Hill, record a metric, a baseline and a target. Tag the baseline `evidence` only if someone measured it, and `assumption` otherwise. A threshold a persona named ("under ten minutes would be wow") stays `simulated`. Name at least one *real* sponsor user per Hill. A simulated persona can stand in for now, labeled simulated, but also record a `question` and suggest `/edt-core:sponsor-users`.
9. **Refine with fresh eyes.** Do a cold read: restate each Hill as an outsider would, including what you'd assume the team is building, and ask whether that matches the intent. Recommend that someone outside the team reads the Hills too. Hills evolve as understanding grows, so set the status to draft.
10. **Play back.** Label anything in a Hill that is a belief rather than a fact; being in a Hill doesn't make it true. Put the simulated reactions and assumed baselines each Hill leans on at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/hills-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0:00–0:05 Intro: why Hills, the JFK example, and the rules (write before you talk, yes-and, parking lot)
  - 0:05–0:10 Set up: draw Who / What / Wow and post the needs statements where everyone can see them
  - 0:10–0:25 Ideate: 4 min of silent writing per column, then a quick share. Quantity over quality
  - 0:25–0:40 Build: small groups mix and match stickies into 2–3 Hill sentences each
  - 0:40–0:50 Refine: groups swap drafts and critique them against the quality checks
  - 0:50–1:00 Playback: read each Hill aloud, dot-vote down to no more than three, name sponsor users and Foundation items, flag assumptions
- **Prompts to read aloud:**
  - Who: "Who exactly are we doing this for? Give me a role and a situation, not 'users'."
  - What: "What will they be able to do that they can't do today? Say it without naming a feature."
  - Wow: "How will we know it's remarkable? What number would change, and why would the market notice?"
  - Refine: "If you'd never seen this project, what would you think this Hill asks us to build?"
- **Materials:** sticky notes in three colors (one per column) plus a fourth for assumptions, markers, dot stickers, a timer, and printed needs statements.
- **An empty board:** three `.cols` labeled Who, What and Wow, a wide "Hill drafts" strip below them, and a Foundation box and a Parking lot. Optionally seed the columns with the needs statements, keeping their tags.

After the session, read the photos or the board export and build the results page. Ask which drafts were rejected and why. Offer to run the simulated sponsor-user check (step 7) on the Hills the room chose.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/hills-<topic>.html`.
- **Title:** `<Topic> Hills`, for example "Claims Intake Hills".
- **Sections:**
  1. **Context:** `.cluster`s of tagged `.note`s for the user, the needs addressed (each with its needs-statement ID and source) and the market context. Market claims with no source are `assumption`.
  2. **Hills:** `.stmts`, one `.stmt` per Hill. The `.say` line wraps its parts as `<span class="part" data-label="Who">`, `data-label="What"` and `data-label="Wow"`. The `.why` line holds pills for the needs it serves, its sponsor users (real, or simulated with a `question` pill) and the Wow measure. Put each Sub-Hill's `.stmt` right after its parent, and start its `.why` with "Sub-Hill of Hill 1".
  3. **Sponsor-user check:** per Hill, a `.cols` with one `.col` per persona, holding that persona's `simulated` notes: would it matter, what would be a wow, what would make them shrug. Then a `details.transcript` per session.
  4. **Wow measures:** a table of Hill, metric, baseline with its tag pill, target, and how it will be measured.
  5. **Foundation:** a table of each item and the Hill that needs it.
  6. **Drafts we rejected:** a table of each draft and its verdict.
  7. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "scope": "", "status": "draft",
    "hills": [{ "id": "H1", "name": "", "who": "", "what": "", "wow": "", "statement": "",
      "needs": ["NS1"], "parent": null,
      "sponsor_users": { "real": [], "simulated": ["SU-2"] },
      "wow_measure": { "metric": "", "baseline": "", "baseline_tag": "assumption", "target": "" },
      "sponsor_check": [{ "persona": "SU-2", "matters": "yes|somewhat|no", "wow": "", "shrug": "", "notes": ["N7"] }] }],
    "foundation": [{ "text": "", "for": ["H1"] }],
    "rejected": [{ "draft": "", "why": "" }] }
  ```
  Sub-Hills are entries in `hills` with `parent` set. `items` holds every tagged note, with `group` set to `"<Hill id> / <section>"`.

## Quality checks
- **Who is specific.** "Users", "customers" or "everyone" fails. A good Who reads like "a first-time claims adjuster at a mid-size insurer".
- **What is an outcome, not an implementation.** Reject anything that names a UI, a technology or a component, such as "via a dashboard", "using AI" or "a mobile app". Ask whether three very different solutions could satisfy it. If only one could, it's an implementation.
- **Wow is measurable and differentiating.** Vague adjectives like "easily", "seamlessly" or "intuitively" fail. A good Wow has a number, a time or a before/after, and it beats what users can get today. If a competitor already delivers it, it's not a Wow.
- **Every Hill traces to at least one needs statement.** A Hill with no need behind it is the team's wish, not the user's outcome.
- **No more than three Hills plus a Foundation.** More than three means the team hasn't chosen. Foundation items are enablers, not user outcomes.
- **Each Hill names a real sponsor user** who can tell the team whether it was met, or carries an open `question` until one is recruited. A simulated persona is never the sponsor user of record.
- **It fits in a sentence that a stakeholder can repeat** from memory after hearing it once.
- **The sponsor-user check has friction.** It includes a skeptic, the personas sound like different people, and at least one of them is lukewarm about something. If all of them love every Hill, rerun it.
- **Simulated stays simulated.** Persona reactions are tagged `simulated`, never `evidence`. They don't count as a baseline or as proof of market differentiation. Counts read "2 of 3 simulated users", never as percentages.
- Hypothetical rewrites, for calibration only:
  - Weak: "Admins can manage users through a new React console." This is an implementation, the Who is vague, and there's no Wow.
  - Strong: "An IT admin at a 500-person company can onboard a new hire to every tool they need in under 10 minutes, without filing a ticket."

## Next
- `/edt-align:playbacks`: run a Hills Playback with stakeholders and sponsor users.
- `/edt-plan:assumptions-and-questions`: find out which assumptions and simulated claims in your Hills carry the most risk.
- `/edt-ideate:big-idea-vignettes` or `/edt-ideate:to-be-scenario-map`: generate ways to reach each Hill.
- `/edt-plan:experience-based-roadmap`: stage the Hills into near-term and long-term user outcomes.
- `/edt-plan:user-stories`: break a Hill into user tasks.
- `/edt-core:sponsor-users`: recruit a real sponsor user for any Hill that has none.

## Source
[IBM Enterprise Design Thinking Toolkit: Hills](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac11)
