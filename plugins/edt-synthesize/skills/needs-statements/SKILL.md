---
name: needs-statements
description: Turns research into Needs Statements in the format "[user] needs a way to [need] so that they [benefit]", diverging on needs and benefits, then converging on a few strong, evidence-backed ones. Use when the user says "needs statements", "user needs", "what does our user actually need?", "problem statements", "reframe these features as needs", "turn research into needs", or after research and before ideation or Hills.
argument-hint: "[user] [facilitate]"
---

# Needs Statements

> IBM Enterprise Design Thinking · Synthesize research · Reflect, leading into Make · ~30 min

Teams jump to features. Needs Statements bring the conversation back to what users actually require to reach their goals, and why it matters to them. Once you've outlined what users need, ideation can focus on ideas that help them get there. The format keeps three things together: a specific **user**, a **need** stated as something they do or achieve (not a feature), and the **benefit** they get from it. Needs Statements are only as reliable as the research behind them. This is Reflect, and it sets up Make: good needs make ideation and Hills much sharper.

## When to use it
- After research, when the team wants to reframe its thinking to be more user-centered. Ask: "What does our user actually need?"
- When a backlog or PRD is a list of features and nobody can say what they're for.
- Before ideation, or before writing Hills.
- When stakeholders are arguing about solutions. Step back to the need.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **Synthesis:** `empathy-map*` (especially the Thinks and Feels clusters and the tensions), `as-is-scenario-map*` (the lows and gaps)
  - **Research:** `interviews*`, `contextual-inquiry*`, `sponsor-users*`
  - **Other files the user points to:** PRDs, backlogs, tickets
- Ask the user for anything still missing:
  - Which user the statements are for. Use the same user as the empathy map.
  - Which research to draw on
- If there is no defensible data from real observation, say so. Offer drafts that are clearly tagged Assumption, and point to `/edt-gather:interviews` or `/edt-synthesize:empathy-map` first.

## Co-create with Claude
1. **Gather.** List `design-thinking/` and read the upstream artifacts. Pull out the raw material: quotes about goals, workarounds, the lows on the as-is map, and the tensions on the empathy map. Invite the user to bring in a Sponsor User if possible.
2. **Set up.** Write the frame, and fill in the user as specifically as you can, by role and context:
   **[Our user] needs a way to [address this need] so that they [benefit in this way].**
3. **Diverge.** Ask the user to write their own candidates first (write before you talk). Then Claude adds more, aiming for 15–30 in total. Each pairs a need with a benefit and cites a source. Then screen out features:
   - **Spot them.** If a note talks about the machine (a dashboard, a button, a click, an app, an alert, "AI"), it's a feature.
   - **Ladder it.** Ask "What would that let them do?" and then "Why does that matter to them?" Keep the answer and drop the feature.
   - **Cover the levels.** Include task needs, relationship and social needs (trust, belonging, looking competent), and emotional needs, wherever the research supports them.
4. **Converge.** Cluster similar candidates and title the clusters, for example *Work to be done*, *Big pain points* or *Key goals*. For each important cluster, write one statement in exactly the frame's format. Aim for **3–5 strong statements**. Run each one through the quality checks, and record how strong its evidence is.
5. **Playback.** Read the converged statements back. Ask what new questions this exercise raised. Recommend going straight into ideation while the needs are fresh.

**Reframing features as needs.** These examples are hypothetical illustrations, not research.

| Feature-shaped | Needs Statement |
|---|---|
| "Managers need an approvals dashboard." | "Finance managers need a way to see which approvals are stuck before month-end so that they can close the books on time without chasing people." |
| "New developers need a Slack bot." | "Developers new to the codebase need a way to find who owns a service so that they can get unblocked the same day." |

## Facilitate a live session
**Agenda (30 min)**
- **0–3:** Intro. Explain why you're doing this and the norms: write before you talk, there are no bad ideas, everyone participates, build with "yes, and…".
- **3–5:** Gather. Post the empathy map, the as-is map and the key research where everyone can see them. Sponsor Users join if possible.
- **5–7:** Setup. Write the frame large across the top of the wall, with the user filled in.
- **7–17:** Diverge. Everyone writes silently: the need on one sticky note and the benefit on another beside it. The facilitator calls out features as they appear.
- **17–27:** Converge. Cluster the notes, label the clusters, and write a few Needs Statements in the exact format.
- **27–30:** Playback. One person reads the converged statements. Capture new questions, and book the ideation session.

**Prompts to read aloud**
- "What does our user actually need? Not what should we build."
- "Need on the left sticky, benefit on the right: 'so that they…'"
- "If your note names a screen, a button or a technology, ask: what would that let them do?"
- "Which research note backs this up? If none, mark it 'Assumption?'"
- "Is this a benefit to the user, or to us?"

**Materials:** markers and sticky notes in two colors, one for needs and one for benefits, plus dots for marking assumptions.

**Board layout (wall or Mural):**
- **Top:** the frame.
- **Middle:** a diverge area that becomes cluster circles.
- **Bottom:** a strip for the converged statements.
- **Corners:** an "Assumption?" corner for notes with no evidence behind them, and a parking lot.

**Afterwards:** give Claude a photo of the wall or the Mural export, and Claude digitizes it into the template below.

## Output
Save to `design-thinking/needs-statements-<user>.md` using this template:

```markdown
# Needs Statements: <user>

**User:** <role and context> (see `empathy-map-<user>.md`) · **Based on:** <source IDs> · **Contributors:** … · **Date:** …

## Needs Statements
1. **<User> needs a way to <need> so that they <benefit>.**
   - Evidence: <source>, <source> · Confidence: high / medium / low · Cluster: <name>
2. **<User> needs a way to <need> so that they <benefit>.**
   - Assumption: <why we believe it> · Validate by: <activity or question>

## Clusters
### <Cluster title>
- Need: … · Benefit: …. Evidence: <source> | Assumption | Question

## Features we reframed
| Original (feature) | Underlying need | Where it went |
|---|---|---|

## Parking lot
- …

## Playback
- **Key takeaways (3–5):** …
- **New questions raised:** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/edt-ideate:big-idea-vignettes`
```

## Quality checks
- Every statement follows the format exactly: "<user> needs a way to <need> so that they <benefit>."
- The user is specific, a role in a context, and matches the empathy map. "Users" or "customers" is too vague.
- The need is solution-agnostic. It names no UI, technology or product, and it is led by a verb such as know, decide, prove or hand off.
- The benefit is the user's outcome. "So that we increase retention" is a business goal, so reframe it or carry it to the Hills discussion.
- The need and benefit aren't the same thing restated. "A way to save time so that they save time" fails.
- Each statement traces to evidence. Statements without evidence are tagged Assumption and come with a way to validate them.
- There are 3–5 statements, not 30, and they cover different clusters rather than variations of one.
- Pitfalls:
  - Writing features in disguise, for example "needs a way to get alerts"
  - Needs too broad to act on, for example "needs a way to be productive"
  - Inventing needs the research never showed

## Next
- `/edt-ideate:big-idea-vignettes`: ideate right away against the strongest needs.
- `/edt-plan:hills`: turn the most important needs into statements of intent (Who / What / Wow).
- `/edt-ideate:to-be-scenario-map`: imagine the future experience that meets these needs.
- `/edt-plan:prioritization-grid`: rank the needs or ideas by importance and feasibility.
- `/edt-plan:assumptions-and-questions`: plan how to validate the statements tagged Assumption.

## Source
[IBM Enterprise Design Thinking Toolkit: Needs Statements](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac0b)
