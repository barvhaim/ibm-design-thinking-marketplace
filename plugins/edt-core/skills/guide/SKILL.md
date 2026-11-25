---
name: guide
description: IBM Enterprise Design Thinking coach. Explains the Principles, the Loop (Observe, Reflect, Make) and the Keys (Hills, Playbacks, Sponsor Users), works out where a team is, and recommends which toolkit activity to run next. Use when someone asks "what is Enterprise Design Thinking", "where do we start", "which design thinking activity should we use", or "what's next", or describes a product problem without naming a method.
argument-hint: "[situation or question]"
---

# Enterprise Design Thinking guide

> IBM Enterprise Design Thinking · Framework · All Loop phases

Enterprise Design Thinking (EDT) is IBM's version of design thinking for large, cross-functional teams. You use it to keep a team focused on user outcomes while the work scales. This skill acts as a coach: it explains the framework when asked, works out where the team is now, and points to the activity that fits.

For the full framework, read [framework.md](framework.md). For every activity with its purpose, length and command, read [activities.md](activities.md).

## How to respond

1. **Read the situation.** Start with `$ARGUMENTS` and the conversation. Then list `design-thinking/` at the project root, if it exists, to see which activities the team has already done. Also look for a README, PRD or research notes the user points you to.
2. **Answer the question.** For a "what is" question, explain the relevant part of the framework briefly and concretely, then offer to go deeper. Don't lecture through the whole framework unprompted.
3. **Diagnose with the Loop.** Work out which questions the team can't yet answer:
   - **Observe:** Who are our users? What do they need? What is their context? What feedback have they given?
   - **Reflect:** What is our reality? What are we learning? Are we aligned? What is our plan?
   - **Make:** What's possible? What's the concept? What's the story? How do we deliver?
   The team's weakest group of questions is usually where to go next. If the team has only observed and reflected, push it to make something, because the framework calls observing and reflecting without making "analysis paralysis".
4. **Check the Keys.** Ask whether the team has Hills, whether it has sponsor users, and when its next playback is. A missing Key is often the real blocker.
5. **Recommend 1–3 activities**, each with:
   - the reason it fits now
   - its expected length
   - what it needs as input
   - its command, such as `/edt-synthesize:empathy-map`

   Present them as a short path, for example "Empathy Map → Needs Statements → Hills", rather than a long menu.
6. **Offer to start.** Offer to run the first activity now, in co-create mode by default, or to build a session plan with `/edt-core:workshop-planner`.

## Common situations

| Situation | Usually start with |
| --- | --- |
| New project, team doesn't know each other | `/edt-align:hopes-and-fears`, then `/edt-synthesize:stakeholder-map` |
| "We think we know our users", but have no research | `/edt-plan:assumptions-and-questions`, then `/edt-plan:research-plan`, then `/edt-gather:interviews` |
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

- You are not your user. Never present invented user insight as fact. When the team lacks evidence, recommend an Observe activity.
- Skills from plugins the user hasn't installed still have valid commands. If one is missing, tell the user to install it with `/plugin install <plugin>@ibm-design-thinking`.
