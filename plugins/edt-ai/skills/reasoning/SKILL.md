---
name: reasoning
description: Runs AI Essentials Reasoning, step 4 of an IBM AI strategy, as an HTML artifact. Traces each AI capability to its data, scopes the big idea to what the AI can reason on, plans for wrong answers with simulated users reacting to one, and ends in a reasoning statement. Use when someone asks "is our AI idea feasible?", "what can our AI actually do?" or "how do we scope this AI idea?", or wants an AI blueprint after the AI Essentials data and understanding work.
argument-hint: "[topic or big idea] [facilitate]"
---

# AI Essentials: Reasoning

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

Big ideas about AI often outrun what the data can support. In Reasoning, the team puts the big idea next to the data and understanding work and asks what the system will really be able to infer, predict or recommend. Then it scopes the idea down to that. The result is a reasoning statement, a one-line blueprint that keeps the team focused as the product grows. Anything scoped out is kept for later. Every AI is sometimes wrong, so before the statement is final, simulated users meet a wrong answer and show the team whether they'd notice, what it would cost them, and whether they'd trust it again.

## When to use it
- After `/edt-ai:understanding`, once critical data sources are broken down into components.
- When a big idea sounds impressive but nobody has checked it against the data.
- Before committing an AI idea to a roadmap or an estimate.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of all three, together:
  - `intent-*`: `content.chosen` for the intent and candidate big ideas
  - `data-*`: `content.minimum` and `content.gaps`
  - `understanding-*`: `content.components` and `content.risks`

  Also useful: `big-idea-vignettes-*` and `hills-*`. Older `.md` versions are fine; read them as text. If any of the three is missing, name the missing step (`/edt-ai:intent`, `/edt-ai:data` or `/edt-ai:understanding`), or record the gap as a `question` and carry on with care.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** which big idea to take forward, if the intent page lists several, and the data expert's view on what's feasible.

## Co-create with Claude
1. **Set up.** Confirm the four prerequisites, one line each, citing the upstream page:
   - the AI's intent
   - a big idea that represents it
   - the data needed to make it real
   - what the AI must be taught to understand the domain

   Lay the big idea next to the data and understanding summaries. Build a source list: `S1…` for real sources and `SU-…` for the personas who represent the target users.
2. **Trace capabilities to data.** Split the big idea into the capabilities it implies: infer, predict, recommend, generate, detect, converse. For each one, list the components from the understanding page it depends on, by ID. Mark each capability **available**, **gap** (data or teaching is missing) or **unknown**.
3. **Brainstorm: re-envision the idea.** Scope the big idea to what the machine can reason on now. For capabilities marked gap or unknown, propose a smaller version, a human-in-the-loop version, or a deferral. Offer 2–3 scoped options and let the user choose. Don't discard what you scope out. Move it to *Parked for later* with what's blocking it.
4. **Weigh value and cost.** The scoped idea must still be valuable to users and to the business. Note the cost to the business: data acquisition and preparation, labelling, compute, human review and maintenance. If the scoped idea no longer delivers user value, say so. Going back to Intent is a valid outcome.
5. **Plan for being wrong.** For each capability, ask:
   - How confident does the AI need to be?
   - What does the user see when it's uncertain or wrong?
   - Who can correct it?
6. **Rehearse a wrong answer with simulated users.** Pick the 1–2 user-facing capabilities where a wrong answer would hurt most. For each, write a concrete scenario: what the user asked, the confidently wrong answer the AI gives, and exactly what the user sees. Play it to each of 3–4 personas, including a novice who may over-trust it, an expert who may catch it, the skeptic and the edge case. Run **one persona at a time**, in character, following the role-play rules in `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Don't tell them it's wrong at first:
   - "Here's what you see. What do you do next?"
   - Then reveal it: "It turned out to be wrong. When would you have found out? What would it have cost you?"
   - "What would you have needed to see to catch it?"
   - "Would you use it again tomorrow?"
   Record each session as a transcript. Turn each reaction into a `simulated` note with the persona ID, saying whether they noticed, what they did, and how their trust changed. If your recovery plan depends on users noticing and a persona didn't, change the plan in step 5. The personas inform the design; the team still sets the confidence thresholds.
7. **List assumptions and questions** the team is still making, with a follow-up plan: who will find out, how, and by when.
8. **Review: write the reasoning statement:**
   **[Business] can [intent] by [scoped big idea] based on [the AI's data and understanding].**
   Hypothetical example: "A regional clinic network can scale expertise by suggesting triage notes to nurses based on de-identified past cases and the clinical protocol glossary." Draft 2–3 versions and tighten until each bracket is specific.
9. **Playback.** Read the final statement aloud and tell the story of v1: what it does, what it leaves for later, and what happens when it's wrong. Put the simulated wrong-answer reactions and the unconfirmed capabilities at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/reasoning-<topic>-kit.html`. A data expert must attend. It needs:
- **Agenda table (60 min):**
  - 0–5 Recap the intent and the big idea
  - 5–15 Setup, placing the big idea and walking the wall
  - 15–40 Brainstorm, re-envisioning and scoping, capturing assumptions, and planning for wrong answers
  - 40–55 Review, drafting and refining the reasoning statement
  - 55–60 Follow-up owners
- **Prompts to read aloud:**
  - "Point to the sticky notes on the wall that make this part of the idea possible. If there aren't any, what does that tell us?"
  - "What's the smallest version of this idea our data supports today?"
  - "When it's wrong, what does the user see, and who notices?"
  - "What are we assuming that we haven't checked?"
  - "Fill in the blanks: [Business] can [intent] by [big idea] based on [data and understanding]."
- **Materials:** the Data and Understanding boards or their pages, sticky notes, thick markers and a large blank area.
- **Board layout:** one long wall, read left to right: **Data** grid → **Understanding** clusters → **Our big idea**. Under the big idea, an empty capability table, a "Parked for later" lane, and an empty `.stmts` block with the four labeled parts written large.
- **Wrong-answer cards:** optionally run the simulated wrong-answer test before the session and bring each persona's reaction as a card, labeled simulated, for the "when it's wrong" discussion.

After the session, read the photos or the whiteboard export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/reasoning-<topic>.html`.
- **Title:** `<Topic> AI Reasoning`, for example "Claims Triage AI Reasoning". The `h1` is "AI Essentials: Reasoning" with the topic in `.topic`.
- **Sections:**
  1. **Reasoning statement:** a `.stmts` block, final statement first, then the earlier drafts. Label the parts `Business`, `Intent`, `Big idea` and `Based on`. In each `.why`, name the data (`D…`) and components (`C…`) the "based on" part rests on, with source pills.
  2. **Prerequisites:** a table of the four prerequisites, a one-line summary of each, the upstream page, and a tag pill.
  3. **What the AI can reason on:** a table of capability, the components it depends on, a status pill and a tag pill. Use `data-tone="good"` for available, `"warn"` for unknown and `"bad"` for gap.
  4. **Scoped big idea:** `.cols` with one column per scoped option, holding tagged notes. Start the chosen option's heading with "Chosen ·". Below it, a *Parked for later* table of piece, blocked by, and revisit when.
  5. **Value and cost:** a table of user value, business value, and each cost (data, labelling, compute, human review, upkeep), with tag pills.
  6. **When the AI is wrong:** a table of capability, confidence needed, what the user sees when it's uncertain, what they see when it's wrong, and who corrects it. For each rehearsed scenario, optionally add a `.frames` frame showing what the user sees, then a `.cluster` holding one `simulated` note per persona, then a `details.transcript` per persona.
  7. **Follow-up:** a table of assumption or question, a tag pill, how you'll find out, owner, and by when.
  8. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "prerequisites": { "intent": "", "big_idea": "", "data": ["D1", "D4"], "understanding": ["C3", "C7"] },
    "capabilities": [{ "id": "CAP1", "verb": "recommend", "text": "", "depends_on": ["C3", "C7"], "status": "gap", "confidence": "", "uncertain_ux": "", "wrong_ux": "", "corrector": "" }],
    "options": [{ "id": "O1", "text": "", "chosen": true, "why": "" }],
    "parked": [{ "piece": "", "blocked_by": "", "revisit": "" }],
    "value": { "user": "", "business": "", "cost": { "data": "", "labelling": "", "compute": "", "review": "", "upkeep": "" } },
    "wrong_answer_tests": [{ "capability": "CAP1", "scenario": "", "persona": "SU-3", "noticed": false, "did": "", "trust_after": "", "note": "N21" }],
    "statement": { "business": "", "intent": "", "big_idea": "", "based_on": "", "text": "", "drafts": [""] },
    "follow_up": [{ "text": "", "tag": "question", "how": "", "owner": "", "by": "" }] }
  ```
  `status` is `available`, `gap` or `unknown`. `items` holds every option, wrong-answer reaction and follow-up note, with `group` set to `"Options"`, `"Wrong answer / <capability>"` or `"Follow-up"`.

## Quality checks
- Every capability in the scoped idea traces to specific components. If a capability has none, it isn't in v1.
- The reasoning statement fills all four parts concretely. A statement like "based on AI" or "based on our data" fails.
- The scoped idea still passes the thank-you test from Intent: users would say thank you.
- Every gap ends up somewhere: in the scoped idea, in the parked lane, or in the follow-up plan.
- There's an answer to "what happens when it's wrong" for every capability that affects users.
- The wrong-answer test has at least one persona who misses the error. Real users over-trust confident systems. If every persona catches every wrong answer, the scenario was too obvious or the role-play too generous, so rerun it.
- The personas react differently: the novice and the expert don't notice the same things.
- Wrong-answer results are counts of simulated users, such as "1 of 4 simulated users noticed", never percentages. They stay tagged `simulated`, and the Playback names the real-user test that would confirm them.
- Pitfall: scoping by ambition, not by data. Treat v1 as a prototype that you'll revise as data and learning improve.

## Next
- `/edt-ai:knowledge`: explore what this AI could do to people and society before building it.
- `/edt-plan:hills`: rewrite or check the Hill against the scoped idea.
- `/edt-plan:experience-based-roadmap`: place the scoped v1 and the parked pieces on a roadmap.
- `/edt-test:paper-prototypes`: test the scoped experience, including its uncertain and wrong states, with real users.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Reasoning](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac2b)
