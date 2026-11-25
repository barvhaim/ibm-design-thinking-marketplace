---
name: simulated-users
description: Builds and maintains the panel of simulated users that every Enterprise Design Thinking activity role-plays. The panel holds 3–5 distinct, grounded personas per target role, including skeptics and edge cases, and is saved as an HTML artifact. Use when someone says "simulate our users", "create personas", "who would use this", "add a persona", or "talk to a simulated user", or before running research, synthesis or testing activities without access to real users.
argument-hint: "[target users | add <persona> | talk <SU-id>]"
---

# Simulated users

> IBM Enterprise Design Thinking · Framework · Observe · ~20 min

Every activity in this toolkit that needs users can run with simulated ones. Interviews, empathy maps, walkthroughs, feedback grids and AI impact reviews all draw on the same panel. Building the panel once, on purpose, keeps the personas consistent across the Loop and makes the gap between simulated and real users visible. Follow `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md` exactly. This skill is its front door.

## When to use it
- At the start of a project, before the first Observe activity.
- When an activity needs users and `design-thinking/simulated-users.html` doesn't exist yet.
- To add a missing perspective, such as an admin, a buyer, an accessibility edge case or a non-user affected by the product.
- To talk to one persona directly: `talk SU-3`.
- After real research, to recalibrate the panel against what real people said.

## Inputs
- From `design-thinking/`: `simulated-users.html`, if it exists, plus any real research pages (`interviews-*`, `contextual-inquiry-*`, `sponsor-users-*`) and `stakeholder-map-*`. Read their `#edt-data` blocks.
- Real grounding in the repo: the README, docs, a PRD, onboarding copy, support or FAQ content, and the product's user-facing screens.
- Ask the user only if the target users can't be inferred, in one question: "Who are the 1–3 kinds of people this is for?"

## Co-create with Claude
1. **Ground.** List what is known for certain and give each fact a source ID (`S1…`): the domain, the roles, the constraints, and any real quotes or data. Anything that doesn't come from a source is invented, and the panel says so.
2. **Draft the panel.** Make 3–5 personas per target role, following the spread rules in the protocol: a novice and an expert, different contexts, a champion, a pragmatist, at least one skeptic, and at least one edge case. Give each persona an obviously fictional name and an `SU-n` ID.
3. **Stress-test it.** Check the panel for clichés, for personas that sound alike, and for any persona that exists only to like the product. Fix what you find. Show the user the panel as a one-line summary per persona, and ask whether anyone important is missing.
4. **Voice check.** For each persona, write two short answers in character:
   - "Walk me through the last time you did <core task>."
   - "What would make you stop using a tool like this?"

   If two personas sound alike, rewrite one of them.
5. **Save and publish** the panel page (see Output).

**Modes**
- **`add <description>`:** add one persona with the next free ID. Never renumber existing personas, because other pages cite them.
- **`talk <SU-id>`:** role-play that persona live with the user, in character, until the user says stop. Append the transcript to the panel page under "Conversations", with insights as `simulated` notes.
- **Recalibrate:** after real research, compare each persona with the real findings. Note where the simulation was wrong. Adjust the persona and record the change in its `grounded_in` field.

## Facilitate a live session
Produce `design-thinking/simulated-users-kit.html`, a 20-minute session for the team to review and correct the panel:
- **Agenda:**
  - 0–5: read the cards silently
  - 5–12: on sticky notes, write what each persona gets wrong or misses
  - 12–17: write who is missing
  - 17–20: decide on the changes
- **Prompt to read aloud:** "Which of these people have you actually met? Which one would you bet the product on?"
- Afterwards, apply the changes with `add` or by editing the personas.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/simulated-users.html`. There is only one panel per project, and you update it in place.
- **Title:** `<Product> Simulated Users`.
- **Header:** keep the simulated banner. In `.meta`, state the number of personas per role and the real sources the panel is grounded in.
- **Sections:**
  1. **The panel:** one `.personas` grid per target role, with one `.persona` card per person. Each card holds the ID, the name, the role and context, a characteristic quote, and a `dl` of goals, pains, tools and habits, voice, "would never say", and grounded in.
  2. **Coverage:** a table with one row per persona and a column per spread dimension (experience, context, attitude, edge case), so the gaps show at a glance.
  3. **Voice check:** two `.note[data-tag="simulated"]` answers per persona.
  4. **Conversations:** a `details.transcript` for each `talk` session. Include this section only when there are any.
  5. **Playback:** where the panel is weakest, and which real users to recruit first (`/edt-core:sponsor-users`).
- **`content` in `#edt-data`:**
  ```json
  { "roles": ["release engineer"],
    "personas": [{ "id": "SU-1", "name": "", "role": "", "context": "", "goals": [], "pains": [], "tools": [],
                   "voice": "", "never_says": "", "attitude": "champion|pragmatist|skeptic|non-user",
                   "edge_case": "", "grounded_in": { "real": ["S1"], "invented": ["..."] } }],
    "conversations": [{ "persona": "SU-2", "date": "", "turns": 14 }] }
  ```

## Quality checks
- The personas are distinct people with different goals, constraints and voices, not one person with five names.
- Each role has at least one skeptic or non-adopter, and at least one edge case.
- `grounded_in` separates real sources from invention, and invention is the norm until research happens.
- No persona is a stereotype of a group. Check names, jobs and traits for clichés.
- IDs never change once other pages cite them.
- In-character answers are concrete, mention real tools and real days, and include some friction.

## Next
- `/edt-gather:interviews`: interview the panel, and use the results to rehearse real interviews.
- `/edt-synthesize:empathy-map`: map one persona.
- `/edt-core:sponsor-users`: replace simulation with real people, starting where the panel is weakest.

## Source
[IBM Enterprise Design Thinking: The Keys (Sponsor Users)](https://www.ibm.com/training/enterprise-design-thinking/framework)
