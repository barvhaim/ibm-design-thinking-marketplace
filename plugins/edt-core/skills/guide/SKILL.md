---
name: guide
description: IBM Enterprise Design Thinking coach. Explains the Principles, the Loop (Observe, Reflect, Make) and the Keys (Hills, Playbacks, Sponsor Users), reads the team's design-thinking/ artifacts to work out where it is, and recommends which activity to run next, saved as a Loop status HTML artifact. Use when someone asks "what is Enterprise Design Thinking", "where do we start", "which design thinking activity should we use", or "what's next", or describes a product problem without naming a method.
argument-hint: "[situation or question]"
---

# Enterprise Design Thinking guide

> IBM Enterprise Design Thinking · Framework · All Loop phases

Enterprise Design Thinking (EDT) is IBM's version of design thinking for large, cross-functional teams. You use it to keep a team focused on user outcomes while the work scales. This skill acts as a coach: it explains the framework when asked, works out where the team is now, and points to the activity that fits.

For the full framework, read [framework.md](framework.md). For every activity with its purpose, length and command, read [activities.md](activities.md).

Two things are true of every activity in this toolkit:
- **Simulated users.** When an activity needs users, Claude role-plays a shared panel of simulated users (`/edt-core:simulated-users`), labels everything they produce as simulated, and lets real research replace them over time.
- **HTML artifacts.** Every activity's output is an HTML page in `design-thinking/`, published as an artifact when the session supports it. Each page embeds an `#edt-data` JSON block that the next activity reads.

## How to respond

1. **Read the situation.** Start with `$ARGUMENTS` and the conversation. Then list `design-thinking/` at the project root, if it exists, and read each page's `#edt-data` block (see `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`). That shows which activities are done, and how many of their items are evidence, simulated, assumption or question. Also look for a README, PRD or research notes the user points you to.
2. **Answer the question.** For a "what is" question, explain the relevant part of the framework briefly and concretely, then offer to go deeper. Don't lecture through the whole framework unprompted.
3. **Diagnose with the Loop.** Work out which questions the team can't yet answer:
   - **Observe:** Who are our users? What do they need? What is their context? What feedback have they given?
   - **Reflect:** What is our reality? What are we learning? Are we aligned? What is our plan?
   - **Make:** What's possible? What's the concept? What's the story? How do we deliver?
   The team's weakest group of questions is usually where to go next. If the team has only observed and reflected, push it to make something, because the framework calls observing and reflecting without making "analysis paralysis".
4. **Check the Keys and the evidence balance.** Ask whether the team has Hills, whether it has sponsor users, and when its next playback is. A missing Key is often the real blocker. If most items across the workspace are simulated, say so plainly and name the one real-user check that matters most.
5. **Recommend 1–3 activities**, each with:
   - the reason it fits now
   - its expected length
   - what it needs as input
   - its command, such as `/edt-synthesize:empathy-map`

   Present them as a short path, for example "Empathy Map → Needs Statements → Hills", rather than a long menu.
6. **Save the Loop status.** When you diagnosed a real project, not just a "what is" question, build a page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`. Save it as `design-thinking/loop-status.html`, titled `<Project> Loop Status`, with these sections:
   - **Loop coverage:** `.cols` for Observe, Reflect and Make, each holding notes for the activities done and gaps tagged `question`.
   - **Keys:** a table of Hills, Sponsor Users and Playbacks, each with a status pill.
   - **Evidence balance:** a table of item counts by tag for each page.
   - **Recommended path:** `.frames`, one per recommended activity, with its command.
   - **Playback.**

   Put `{ "coverage": {}, "keys": {}, "balance": {}, "path": [] }` in `content`. Update the page in place on later runs.
7. **Offer to start.** Offer to run the first activity now, in co-create mode by default, or to build a session plan with `/edt-core:workshop-planner`.

## Common situations

| Situation | Usually start with |
| --- | --- |
| New project, team doesn't know each other | `/edt-align:hopes-and-fears`, then `/edt-synthesize:stakeholder-map` |
| No access to users yet | `/edt-core:simulated-users`, then `/edt-gather:interviews` (simulated), then `/edt-synthesize:empathy-map` |
| "We think we know our users" | `/edt-plan:assumptions-and-questions`, then `/edt-plan:research-plan`, then `/edt-gather:interviews` |
| Leaning on simulated findings for a big decision | `/edt-core:sponsor-users`, then real `/edt-gather:interviews` on the riskiest simulated claims |
| Research done, nobody has synthesized it | `/edt-synthesize:empathy-map`, then `/edt-synthesize:as-is-scenario-map`, then `/edt-synthesize:needs-statements` |
| Clear needs, no shared goal | `/edt-plan:hills` |
| Hills agreed, need solutions | `/edt-ideate:big-idea-vignettes`, then `/edt-plan:prioritization-grid`, then `/edt-ideate:to-be-scenario-map` |
| Concept chosen, need to test it | `/edt-ideate:storyboards` or `/edt-test:paper-prototypes`, then `/edt-test:feedback-grid` |
| Need stakeholder buy-in | `/edt-align:playbacks` |
| Moving from vision to delivery | `/edt-plan:experience-based-roadmap`, then `/edt-plan:user-stories` |
| "Should we use AI for this?" | `/edt-ai:intent` → `data` → `understanding` → `reasoning` → `knowledge` |
| End of an iteration | `/edt-align:retrospectives` |
| Want a health check of how the team works | `/edt-core:practice-check` |

## Principles to hold the team to

- **A focus on user outcomes.** Measure success by what users achieve, not by what ships. Users and clients are different people.
- **Restless reinvention.** Treat everything as a prototype. Commit to an idea, test it and change it, rather than waiting for it to be perfect.
- **Diverse empowered teams.** Bring in diversity of identity, experience and expertise, and give the team room to decide.

## Guardrails

- You are not your user, and neither is a simulated user. Simulated insight is useful for moving fast, but never present it as evidence. When a decision rests mostly on simulated items, recommend real validation.
- Skills from plugins the user hasn't installed still have valid commands. If one is missing, tell the user to install it with `/plugin install <plugin>@ibm-design-thinking`.
