---
name: intent
description: Runs AI Essentials Intent, step 1 of an IBM AI strategy, as an HTML artifact. Picks 1–2 core AI intents, ideates and clusters, asks simulated users whether they'd say thank you for each shortlisted theme, and records whether AI is the right tool. Use when someone asks "should we use AI for this?", "what's our AI use case?" or "where could AI help our users?", or when an AI idea is driven by the technology instead of a user problem.
argument-hint: "[topic or user problem] [facilitate]"
---

# AI Essentials: Intent

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

AI work should start from a user need, not from the technology. In Intent, the team diverges and then converges on what the business and its users are trying to achieve. The output is an explicit decision on whether AI belongs in the solution and why. It is the first of five AI Essentials activities (intent → data → understanding → reasoning → knowledge), and each later one reads this page's `#edt-data`. Simulated users keep the user's side honest: before the team commits, each persona says, in their own words, whether they'd thank you for the idea.

## When to use it
- After an As-is Scenario Map, when you understand your users' current experience and the business's needs.
- When a stakeholder says "we need AI" and nobody can name the user problem it solves.
- When there are many AI ideas and the team needs one or two directions to pursue.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of `as-is-scenario-map-*`, `empathy-map-*`, `needs-statements-*`, `hills-*` and `stakeholder-map-*` if they exist. Older `.md` versions are fine; read them as text. Carry user pain points over with their original tag and source.
- **Files the user points to,** such as research findings, tickets or analytics. These are real evidence.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** the business goal, if no upstream page states it, and what stakeholders expect from AI.

## Co-create with Claude
1. **Gather and check readiness.** Build a source list: `S1…` for each real source and `SU-…` for each persona who represents the target users. List the user pain points, tagged `evidence` or `simulated`. If there is no research at all, suggest `/edt-gather:interviews` and `/edt-synthesize:as-is-scenario-map` first, or carry on with the panel's goals and pains, tagged `simulated`. Then answer the deck's two gating questions, each with yes, partly or no, a reason, and whether the answer rests on real or simulated users:
   - Do we know enough about our users to decide what we're trying to accomplish?
   - Do we know which problem the business is able and willing to solve for them?
   If either answer is shaky, or rests only on simulated users, say so and recommend more research before going further.
2. **Establish: choose 1–2 core AI intents.** Show the six core intents and ask which best serve both the business and the users' success:
   - **Accelerate research and discovery:** sift large bodies of domain data quickly and surface what matters.
   - **Enrich your interactions:** talk with customers or employees in natural language, with tailored and personal responses.
   - **Anticipate and preempt disruptions:** monitor systems continuously and catch issues before they get expensive.
   - **Recommend with confidence:** weigh a broad set of information against what matters to the user, then give targeted recommendations.
   - **Scale expertise and learning:** combine experts' know-how with current domain documentation so anyone can draw on it when they need it.
   - **Detect liabilities and mitigate risk:** use language understanding to spot risks, for example around regulatory compliance.
3. **Ideate.** Generate many specific ways to achieve each chosen intent, for example "How might we enrich interactions between the business and its users?" Ask the user for their ideas first. Then add your own, each tied to a pain point note. Aim for 15 or more ideas. An idea with no pain point behind it is tagged `assumption`. Ask what stakeholders want from this, and whether their thinking should be challenged.
4. **Cluster.** Group all ideas by theme, wherever they sit under the intents. Name each cluster and note where the user need and the business need overlap. Place each theme on user value against business value, as the team's judgment. Look for a higher-order theme that ties the clusters together.
5. **Run the thank-you test with simulated users.** Shortlist 2–3 themes. Run a short session with each of 3–4 personas who represent the target users, including the skeptic and the edge case. Run **one persona at a time**, in character, following the role-play rules in `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Describe each theme in the persona's words, never as "AI" or product vocabulary, and ask:
   - "When did you last run into <pain>? What did you do?"
   - "If this had been there, what would have changed for you?"
   - "Would you say thank you for it? What would make you ignore it or switch it off?"
   - "How would you know it was working?"
   Let them shrug, prefer their workaround, or say no. Record each session as a transcript. Turn each answer into a `simulated` note with the persona ID, holding their verdict (yes, maybe or no) and their own measure of success. If every persona thanks you for every theme, rerun with more friction.
6. **Converge.** Recommend the strongest theme, weighing the overlap, the team's votes and the thank-you test, and explain why. If the user wants a vote, give each person 2–3 votes. Simulated users don't vote; report their verdicts as counts, such as "2 of 4 simulated users". Write the chosen intent as a statement, then draft 1–3 candidate big ideas from the theme.
7. **Check AI fit.** For each leading theme, decide whether AI is actually the right tool, using the signals under Quality checks. Name the simpler alternative, such as rules, a UX fix, a process change or better content. A persona who'd rather keep their spreadsheet is often pointing at it. Record one verdict per theme: *AI*, *Hybrid*, *Non-AI fix first* or *Research more*.
8. **Playback.** Tell the decision back in a few sentences: the intent, the theme, the verdict and why. Put the simulated thank-you verdicts the decision leans on at the top of "Validate next", each with a way to check it with real users. Then publish the page.

## Facilitate a live session
Produce `design-thinking/intent-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0–5 Intro and a recap of the as-is pain points
  - 5–15 Establish, choosing 1–2 core intents
  - 15–25 Ideate, silently, one idea per sticky note
  - 25–35 Cluster and name themes
  - 35–50 Converge, with 2–3 dot votes each and a discussion of why
  - 50–60 AI fit check and next steps
- **Prompts to read aloud:**
  - "Which of these intents would most help our users succeed, and which does the business care about most?"
  - "Write, don't talk. One idea per sticky note. Put it on the wall as soon as you have it."
  - "Where do user needs and business needs overlap?"
  - "If we shipped this, would our users say thank you?"
  - "Could we solve this without AI? What would that look like?"
- **Ground rules:** write before you talk, build on ideas with "yes, and", and put off-topic issues in a parking lot. Invite a sponsor user if you can (`/edt-core:sponsor-users`).
- **Materials:** a wall or digital whiteboard, sticky notes, thick markers and dot stickers. Keep the as-is scenario map visible.
- **Board layout:** an empty `.cols` board with the six core intents as column headers and space below for ideas, an empty user value against business value `.plot`, and an empty AI fit table. Keep the board up, because Data and Reasoning build on it. Optionally seed it with the panel's pain points, labeled as simulated.
- **Thank-you cards:** optionally run the simulated thank-you test before the session and bring each persona's reaction as a card, labeled simulated, so the room argues with something concrete.

After the session, read the photos or the whiteboard export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/intent-<topic>.html`.
- **Title:** `<Topic> AI Intent`, for example "Claims Triage AI Intent". The `h1` is "AI Essentials: Intent" with the topic in `.topic`.
- **Sections:**
  1. **Grounding:** `.cols` with three columns. *Users and their pains* holds tagged notes with their sources. *Business goal* holds the goal. *Readiness* holds one note per gating question, giving the answer, the reason and whether it rests on real or simulated users.
  2. **Core AI intents:** a table of intent, why it matters to users, why it matters to the business, and a tag pill.
  3. **Ideas and themes:** `.cols` with one `.col` per theme, headed "<Theme> · <n> votes". Each idea is a tagged `.note` whose `.src` names the pain point it answers. Put the higher-order theme in a `note wide` below.
  4. **Where the value overlaps:** a `.plot` with one numbered dot per theme, user value up and business value across. Label the zones "Shared value" (`z-tr`), "Users only" (`z-tl`), "Business only" (`z-br`) and "Neither" (`z-bl`). Tag the dots `assumption`, and give each theme's thank-you count in the key, such as "2 of 4 simulated users".
  5. **Thank-you test:** one `.cluster` per shortlisted theme, holding one `simulated` note per persona with their verdict and their words, followed by a `details.transcript` per persona.
  6. **Chosen intent:** a `.stmts` block with one `.stmt` whose parts are labeled `Intent`, `Theme`, `Users`, `Outcome` and `Business`, for example: "<Intent> through <theme>, so that <users> can <outcome> while <the business gains …>". In `.why`, put source pills and the verdict pill. List the candidate big ideas below as `assumption` notes.
  7. **Is AI the right tool?:** a table of theme, signals for AI, signals against, simpler alternative, and a verdict pill. Use `data-tone="good"` for AI, `"warn"` for Hybrid or Research more, and `"bad"` for Non-AI fix first.
  8. **Stakeholder input:** notes giving what each stakeholder wants and whether to challenge it. Tag them `evidence` when a real stakeholder said it, and `assumption` otherwise.
  9. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "business_goal": "", "target_users": ["SU-1", "SU-2"],
    "readiness": { "users": { "answer": "partly", "why": "", "basis": "simulated" }, "problem": { "answer": "yes", "why": "", "basis": "evidence" } },
    "intents": [{ "name": "Scale expertise and learning", "user_value": "", "business_value": "" }],
    "themes": [{ "id": "T1", "name": "", "ideas": ["I1", "I4"], "overlap": "", "votes": 5, "user_value": 80, "business_value": 65 }],
    "higher_order_theme": "",
    "thank_you": [{ "theme": "T1", "persona": "SU-2", "verdict": "maybe", "success": "", "note": "N14" }],
    "chosen": { "intent": "", "theme": "T1", "statement": "", "big_ideas": [""] },
    "fit": [{ "theme": "T1", "for": [""], "against": [""], "alternative": "", "verdict": "Hybrid" }],
    "stakeholders": [{ "who": "", "wants": "", "challenge": "" }] }
  ```
  `items` holds every pain point, idea (`I…`) and thank-you note, with `group` set to `"Pains"`, `"Ideas / <theme>"` or `"Thank-you / <theme>"`.

## Quality checks
- **AI fit is argued, not assumed.**
  - *Signals for AI:* ambiguous or unstructured inputs such as language, images or messy records. Patterns too complex or changeable to write as rules. Prediction under uncertainty. Personalization at scale. Data exists, or could exist, that reflects what you want the system to do. A wrong answer can be tolerated or caught by a person.
  - *Signals against AI:* the logic fits in clear rules. Users need an exact, repeatable, auditable result. The pain is really findability, too many steps, or missing information. There's no data and no realistic way to get it. Errors would be costly and nothing would catch them.
- Every theme traces back to a pain point note. Ideas without one are tagged `assumption` or dropped.
- Both the user value and the business value are stated. If only one side benefits, the intent isn't aligned yet.
- Converge on one or two intents. A team that picks all six has no direction.
- The simulated personas sound like different people, and at least one of them shrugs or says no. If every persona thanks you for every theme, the simulation is flattering the team, so rerun it with more friction.
- Personas talk about their pain in their own words. If a persona says "AI-powered insights", the team's vocabulary has leaked into the role-play.
- A simulated "thank you" is a hypothesis about demand, not demand. It stays tagged `simulated`, and the Playback names the real-user check that would confirm it.
- Thank-you results are counts of simulated users, never percentages.
- If readiness rests only on simulated users, the Playback says so plainly.
- Pitfall: picking a model or vendor here. Intent is about outcomes, so leave technology choices for later.

## Next
- `/edt-ideate:big-idea-vignettes`: turn the chosen theme into concrete big ideas. Data needs at least one.
- `/edt-ai:data`: take stock of the data you'd need to make the intent real.
- `/edt-plan:hills`: write the intent as a Who/What/Wow user outcome.
- `/edt-synthesize:as-is-scenario-map`: run this first if there's no map of the current experience.
- `/edt-core:sponsor-users`: find real users to confirm the thank-you test.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Intent](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac21)
