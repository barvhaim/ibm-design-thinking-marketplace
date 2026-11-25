---
name: reasoning
description: Run AI Essentials Reasoning, step 4 of an IBM AI strategy. Grounds ambitious AI big ideas in what the system can actually reason on from its data and understanding, scopes them, and ends in a reasoning statement. Use when someone asks "is our AI idea feasible?", "what can our AI actually do?", or "how do we scope this AI idea?", or wants an AI blueprint after the AI Essentials data and understanding work.
argument-hint: "[topic or big idea] [facilitate]"
---

# AI Essentials: Reasoning

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

Big ideas about AI often outrun what the data can support. In Reasoning, the team puts the big idea next to the data and understanding work and asks what the system will really be able to infer, predict or recommend. Then it scopes the idea down to that. The result is a reasoning statement, a one-line blueprint that keeps the team focused as the product grows. Anything scoped out is kept for later.

## When to use it
- After `/edt-ai:understanding`, once critical data sources are broken down into components.
- When a big idea sounds impressive but nobody has checked it against the data.
- Before committing an AI idea to a roadmap or an estimate.

## Inputs
- From `design-thinking/` (all required, so read them together):
  - `intent-*` for the intent and candidate big ideas
  - `data-*` for the minimum data and its gaps
  - `understanding-*` for the curriculum and association risks
- Also useful: `big-idea-vignettes-*` and `hills-*`.
- If any of the three required files is missing, name the missing step (`/edt-ai:intent`, `/edt-ai:data` or `/edt-ai:understanding`), or record the gap as **Question** and carry on with care.
- Ask the user for: which big idea to take forward, and the data expert's view on what's feasible.

## Co-create with Claude
1. **Set up.** Confirm the four prerequisites, one line each, citing the artifact:
   - the AI's intent
   - a big idea that represents it
   - the data needed to make it real
   - what the AI must be taught to understand the domain
   Lay the big idea next to the data and understanding summaries.
2. **Trace capabilities to data.** Split the big idea into the capabilities it implies: infer, predict, recommend, generate, detect, converse. For each one, list the data components from the understanding artifact it depends on. Mark each as **available**, **gap** (data or teaching is missing), or **unknown**.
3. **Brainstorm: re-envision the idea.** Scope the big idea to what the machine can reason on now. For capabilities marked gap or unknown, propose a smaller version, a human-in-the-loop version, or a deferral. Offer 2–3 scoped options and let the user choose. Don't discard what you scope out. Move it to *Parked for later* with what's blocking it.
4. **Weigh value and cost.** The scoped idea must still be valuable to users and to the business. Note the cost to the business: data acquisition and preparation, labelling, compute, human review and maintenance. If the scoped idea no longer delivers user value, say so. Going back to Intent is a valid outcome.
5. **Plan for being wrong.** For each capability, ask:
   - How confident does the AI need to be?
   - What does the user see when it's uncertain or wrong?
   - Who can correct it?
6. **List assumptions and questions** the team is still making, with a follow-up plan: who will find out, how, and by when.
7. **Review: write the reasoning statement:**
   **[Business] can [intent] by [scoped big idea] based on [the AI's data and understanding].**
   Hypothetical example: "A regional clinic network can scale expertise by suggesting triage notes to nurses based on de-identified past cases and the clinical protocol glossary." Draft 2–3 versions and tighten until each bracket is specific.
8. **Write the artifact** and the Playback.

## Facilitate a live session
- **Materials:** the Data and Understanding boards (or their photos), sticky notes, thick markers, and a large blank area. A data expert must attend.
- **Board layout:** one long wall, read left to right: **Data** grid → **Understanding** clusters → **Our big idea**. Under the big idea, leave room for a scoped version, a "Parked for later" lane, and the reasoning statement template written large.
- **Agenda (60 min):**
  - 5 min: recap the intent and the big idea.
  - 10 min: Setup, placing the big idea and walking the wall.
  - 25 min: Brainstorm, re-envisioning and scoping, and capturing assumptions.
  - 15 min: Review, drafting and refining the reasoning statement.
  - 5 min: follow-up owners.
- **Prompts to read aloud:**
  - "Point to the sticky notes on the wall that make this part of the idea possible. If there aren't any, what does that tell us?"
  - "What's the smallest version of this idea our data supports today?"
  - "What are we assuming that we haven't checked?"
  - "Fill in the blanks: [Business] can [intent] by [big idea] based on [data and understanding]."
- **Capture:** photograph the wall and the final statement, then ask Claude to digitize it into the template below.

## Output
Save to `design-thinking/reasoning-<topic>.md`:

```markdown
# AI Essentials: Reasoning: <topic>

## Inputs
- Intent: … (intent-<topic>.md)
- Big idea (original): …
- Minimum data: … (data-<topic>.md)
- Key understanding: … (understanding-<topic>.md)

## What the AI can reason on
| Capability | Depends on (data components) | Status (available / gap / unknown) | When uncertain or wrong | Tag |
| --- | --- | --- | --- | --- |

## Scoped big idea
- Scoped version (v1): …
- What changed and why: …

## Parked for later
| Piece of the idea | Blocked by | Revisit when |
| --- | --- | --- |

## Value and cost
- User value: …
- Business value: …
- Cost and effort: (data, labelling, compute, human review, upkeep)

## Reasoning statement
**<Business> can <intent> by <scoped big idea> based on <the AI's data and understanding>.**

## Assumptions and questions to follow up
| Item | Assumption / Question | How we'll find out | Owner | By when |
| --- | --- | --- | --- | --- |

## Playback
- Key takeaways: (3–5)
- Assumptions and questions to validate: …
- Next activity: …
```
Tags: `Evidence: <source>`, `Assumption`, or `Question`.

## Quality checks
- Every capability in the scoped idea traces to specific data components. If a capability has none, it isn't in v1.
- The reasoning statement fills all four brackets concretely. A statement like "based on AI" or "based on our data" fails.
- The scoped idea still passes the user test from Intent: users would say thank you.
- Every gap ends up somewhere: in the scoped idea, in the parked lane, or in the follow-up plan.
- There's an answer to "what happens when it's wrong" for every capability that affects users.
- Pitfall: scoping by ambition, not by data. Treat v1 as a prototype that you'll revise as data and learning improve.

## Next
- `/edt-ai:knowledge`: explore what this AI could do to people and society before building it.
- `/edt-plan:hills`: rewrite or check the Hill against the scoped idea.
- `/edt-plan:experience-based-roadmap`: place the scoped v1 and the parked pieces on a roadmap.
- `/edt-test:paper-prototypes`: test the scoped experience, including its uncertain and wrong states, with users.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Reasoning](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac2b)
