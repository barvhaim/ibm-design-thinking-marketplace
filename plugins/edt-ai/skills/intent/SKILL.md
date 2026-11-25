---
name: intent
description: Run AI Essentials Intent, the first step of an IBM AI strategy. Aligns the team on the business and user intent for an AI solution, and decides whether AI is the right tool at all. Use when someone asks "should we use AI for this?", "where could AI help our users?", "what's our AI use case?", or wants to start an AI strategy, or when an AI idea is being driven by the technology instead of a user problem.
argument-hint: "[topic or user problem] [facilitate]"
---

# AI Essentials: Intent

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

AI work should start from a user need, not from the technology. In Intent, the team diverges and then converges on what the business and its users are trying to achieve. The output is an explicit decision on whether AI belongs in the solution and why. It is the first of five AI Essentials activities (intent → data → understanding → reasoning → knowledge), and each later one builds on this artifact.

## When to use it
- After an As-is Scenario Map, when you understand your users' current experience and the business's needs.
- When a stakeholder says "we need AI" and nobody can name the user problem it solves.
- When there are many AI ideas and the team needs one or two directions to pursue.

## Inputs
- From `design-thinking/`: read `as-is-scenario-map-*`, `empathy-map-*`, `needs-statements-*`, `hills-*` and `stakeholder-map-*` if they exist. Pull user pain points as **Evidence** and cite the file.
- Ask the user for: the target users, the business goal, any research findings (transcripts, tickets, analytics), and what stakeholders expect from AI.
- If there is no user research, don't invent it. Suggest `/edt-gather:interviews` and `/edt-synthesize:as-is-scenario-map` first, or carry on with every user claim tagged **Assumption**.

## Co-create with Claude
1. **Check readiness.** Ask the two gating questions from the deck:
   - Do we know enough about our users to decide what we're trying to accomplish?
   - Do we know which problem the business is able and willing to solve for them?
   If either answer is shaky, say so and recommend more research before going further.
2. **Establish: choose 1–2 core AI intents.** Show the six core intents and ask which ones best serve both the business and the users' success:
   - **Accelerate research and discovery:** sift large bodies of domain data quickly and surface what matters.
   - **Enrich your interactions:** talk with customers or employees in natural language, with tailored and personal responses.
   - **Anticipate and preempt disruptions:** monitor systems continuously and catch issues before they get expensive.
   - **Recommend with confidence:** weigh a broad set of information against what matters to the user, then give targeted recommendations.
   - **Scale expertise and learning:** combine experts' know-how with current domain documentation so anyone can draw on it when they need it.
   - **Detect liabilities and mitigate risk:** use language understanding to spot risks, for example around regulatory compliance.
3. **Ideate.** Generate many specific ways to achieve each chosen intent, for example "How might we enrich interactions between the business and its users?" Ask the user for their ideas first. Then add your own, each tied to a user pain point from the research. Aim for 15 or more ideas. Ask what stakeholders want from this, and whether their thinking should be challenged.
4. **Cluster.** Group all ideas by theme, wherever they sit under the intents. Name each cluster. For each one, note where the user need and the business need overlap. Look for a higher-order theme that ties the clusters together.
5. **Converge.** Recommend the strongest theme and explain why. If the user wants a vote, give each person 2–3 votes. Test the theme from the user's side: would users say "thank you" for this? How would they define success? From the chosen theme, draft 1–3 candidate big ideas.
6. **AI fit check.** For each leading theme, decide whether AI is actually the right tool. Use the table under Quality checks. Name the simpler alternative, such as rules, a UX fix, a process change or better content, and record a verdict: *AI*, *Hybrid*, *Non-AI fix first*, or *Research more*.
7. **Write the artifact** and the Playback.

## Facilitate a live session
- **Materials:** a wall or digital whiteboard, sticky notes, and thick markers. Have the as-is scenario map visible.
- **Board layout:** the six core intents as header stickies across the top, with open space below for ideas and clusters. Keep the board up, because Data and Reasoning build on it.
- **Agenda (60 min):**
  - 5 min: intro and a recap of the as-is pain points.
  - 10 min: Establish, choosing 1–2 core intents.
  - 10 min: Ideate, silently, one idea per sticky note.
  - 10 min: Cluster and name themes.
  - 15 min: Converge, with 2–3 dot votes each and a discussion of why.
  - 10 min: AI fit check and next steps.
- **Prompts to read aloud:**
  - "Which of these intents would most help our users succeed, and which does the business care about most?"
  - "Write, don't talk. One idea per sticky note. Put it on the wall as soon as you have it."
  - "Where do user needs and business needs overlap?"
  - "If we shipped this, would our users say thank you?"
  - "Could we solve this without AI? What would that look like?"
- **Ground rules:** write before you talk, build on ideas with "yes, and", and put off-topic issues in a parking lot. Invite a sponsor user if you can (`/edt-core:sponsor-users`).
- **Capture:** photograph the board, then ask Claude to digitize it into the template below.

## Output
Save to `design-thinking/intent-<topic>.md`:

```markdown
# AI Essentials: Intent: <topic>

## Grounding
- Users and their problem: … (Evidence: as-is-scenario-map-<topic>.md)
- Business goal: …
- Readiness: Know enough about users? <yes/no, why> · Know the problem we can and will solve? <yes/no, why>

## Core AI intents chosen
| Intent | Why it matters to users | Why it matters to the business | Tag |
| --- | --- | --- | --- |

## Ideas
| # | Idea | User pain point it addresses | Tag |
| --- | --- | --- | --- |

## Clusters
| Theme | Ideas (#) | User need ↔ business need | Votes |
| --- | --- | --- | --- |
- Higher-order theme: …

## Converged direction
- Chosen theme: …
- Why users would say "thank you": …
- Candidate big ideas: 1. … 2. …

## Is AI the right tool?
| Theme | Signals for AI | Simpler alternative | Verdict | Tag |
| --- | --- | --- | --- | --- |

## Stakeholder input
- <stakeholder>: <what they want> · Challenge? …

## Playback
- Key takeaways: (3–5)
- Assumptions and questions to validate: …
- Next activity: …
```
Tags: `Evidence: <source>`, `Assumption`, or `Question`.

## Quality checks
- **AI fit is argued, not assumed.**
  - *Signals for AI:* ambiguous or unstructured inputs such as language, images or messy records. Patterns too complex or changeable to write as rules. Prediction under uncertainty. Personalization at scale. Data exists, or could exist, that reflects what you want the system to do. A wrong answer can be tolerated or caught by a person.
  - *Signals against AI:* the logic fits in clear rules. Users need an exact, repeatable, auditable result. The pain is really findability, too many steps, or missing information. There's no data and no realistic way to get it. Errors would be costly and nothing would catch them.
- Every theme traces back to a real user pain point. Ideas without one get tagged **Assumption** or dropped.
- Both the user value and the business value are stated. If only one side benefits, the intent isn't aligned yet.
- Converge on one or two intents. A team that picks all six has no direction.
- Pitfall: picking a model or vendor here. Intent is about outcomes, so leave technology choices for later.

## Next
- `/edt-ideate:big-idea-vignettes`: turn the chosen theme into concrete big ideas. Data needs at least one.
- `/edt-ai:data`: take stock of the data you'd need to make the intent real.
- `/edt-plan:hills`: write the intent as a Who/What/Wow user outcome.
- `/edt-synthesize:as-is-scenario-map`: run this first if there's no map of the current experience.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Intent](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac21)
