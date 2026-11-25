---
name: big-idea-vignettes
description: Rapidly diverge on many possible solutions to one user need, then cluster and converge on the ideas worth pursuing. Each idea is a single storyboard-style frame with a one- or two-word headline. Use when someone says "let's brainstorm", "we need ideas", "how might we solve this", "we're stuck", "ideate on this need / Hill / pain point", or wants options before committing to a solution.
argument-hint: "[needs statement, Hill or pain point] [facilitate]"
---

# Big Idea Vignettes

> IBM Enterprise Design Thinking · Generate new ideas · Make / Reflect · ~30 min

Teams tend to fall for the first plausible solution. Big Idea Vignettes force breadth first: everyone quickly produces many ideas, each one a single "frame" showing how a user would experience the solution, before anyone judges them. Only then does the team cluster, spot patterns and converge on a set to pursue. Everyone sees the user and the problem differently, so everyone contributes ideas. Ideation is not just the designers' job.

## When to use it
- You have a clear prompt (needs statement, Hill, user story or as-is pain point) and want solution options.
- The team is stuck, circling one idea, or arguing about implementation too early.
- Before a To-be Scenario Map or Storyboards, to choose which ideas to develop.
- Any time you want to improve something. It's quick enough to run often.

## Inputs
- Upstream artifacts in `design-thinking/`: `needs-statements-*`, `hills-*`, `user-stories-*`, `as-is-scenario-map-*` (pain points), `empathy-map-*` (user context).
- If missing, ask: "Who is the user, and which need or pain point are we solving?" Without one, ideas float free of users. Suggest `/edt-synthesize:needs-statements` or `/edt-synthesize:as-is-scenario-map` first, or proceed with the prompt tagged as an Assumption.

## Co-create with Claude
1. **Set up the prompt.** Create `design-thinking/` if missing, list it, and read upstream artifacts. Propose 1–3 candidate prompts, quoting their source and tag. The user picks one. Use one prompt per round (run again for others), and add a "How might we…?" phrasing if it helps.
2. **The user writes before Claude talks.** Ask the user to dump their own ideas first: rough headlines, no judging. This keeps Claude from anchoring the session. If they'd rather skip, proceed and invite additions later.
3. **Diverge.** First "yes, and" each of the user's ideas: push it further, combine it, flip it. Then add your own, aiming for 20+ in total across a wide range. Use lenses to escape the obvious:
   - Remove the step entirely · do it before the user asks · do it for them
   - Make it social or shared · playful · zero-effort
   - 10x bigger, or a tiny low-tech version
   - Borrow from another industry or from everyday life
   - Invert it: how could we make this worse? Then flip each answer
   - Design it for the most novice user, then for the most expert
   - Include at least three deliberately wild ideas

   Write each as a vignette: a **headline** of one or two words, plus one present-tense sentence describing what the user experiences in that moment. Example: *Ready Desk: she walks in and her desk already shows her name.* For ideas worth showing, add an optional three-line ASCII frame.
4. **Ideas, not features.** A big idea describes how a user experiences the solution, and a feature describes how it's built. Rewrite anything that names implementation (a dropdown, an API, a dashboard widget) as the experience it enables. Park feasibility concerns in the parking lot and don't debate them yet.
5. **Converge.** Cluster by affinity and name each cluster after the user outcome it delivers, not the technology behind it. Show the clusters and let the user or their team choose, for example with three votes each. Don't pick a winner yourself. If asked, offer perspectives (user impact, novelty, effort) and suggest `/edt-plan:prioritization-grid`. Keep the unchosen ideas, because they are the team's option backlog.
6. **Tag what the chosen ideas rest on.** Ideas are proposals, not facts. For each chosen cluster, list the Assumptions it depends on and the Questions to answer. Keep the prompt's original Evidence tags and sources.
7. **Save and play back** using the template below.

## Facilitate a live session
**Agenda (30 min)**

| Time | Step | Notes |
|---|---|---|
| 0–3 | Intro & norms | Write before you talk · no bad ideas · ideas, not features · yes, and · parking lot |
| 3–5 | Prompt | Read it aloud and post it where everyone can see it |
| 5–15 | Silent diverge | One idea per sticky: quick sketch plus a 1–2 word headline |
| 15–20 | Share & build | Each person posts and explains in ≤30 s; others build on new stickies |
| 20–26 | Cluster & name | Silently move similar ideas together, then name the clusters |
| 26–28 | Converge | Dot vote, three dots each |
| 28–30 | Playback | One person plays back each cluster; add ideas as they come |

**Prompts to read aloud**
- "Our prompt is: … For ten minutes, silently sketch as many ideas as you can, one per sticky. Draw what the user would experience, then give it a one- or two-word headline."
- "Quantity beats quality right now. If it feels too wild, write it anyway."
- "If you catch yourself drawing a button or a database, ask what the user experiences, and draw that instead."
- "Building on someone else's idea counts. It's encouraged."
- Converge: "Without talking, move ideas that feel related closer together. Then we'll name the groups."

**Materials:** large sticky notes you can sketch on, a marker for everyone, dot stickers and a timer.

**Board layout (physical wall or Mural)**
```
+---------------------------------------------------------------+
| PROMPT: <needs statement / Hill / pain point>                 |
+-----------------------------------------------+---------------+
| DIVERGE: open space or one column per person  |  PARKING LOT  |
+-----------------------------------------------+               |
| CLUSTERS: named groups + dot votes            |               |
+-----------------------------------------------+---------------+
```

**After the session:** ask for photos or a Mural export. Transcribe every sticky, including unvoted ideas and the parking lot. Keep who wrote what and record the vote counts. Mark any ideas Claude adds afterward as "Claude, post-session".

## Output
Save to `design-thinking/big-idea-vignettes-<topic>.md` using this template:

```markdown
# Big Idea Vignettes: <topic>
_Date · Participants · Mode: co-create | facilitated_

## Prompt
> <needs statement / Hill / user story / pain point>

Source: <artifact or person> · Evidence | Assumption

## Vignettes
| # | Headline | What the user experiences | Origin | Builds on |
|---|----------|---------------------------|--------|-----------|
| 1 | <1–2 words> | <one present-tense sentence> | user / Claude / <name> | – |

## Clusters
### <Cluster name, phrased as a user outcome>
- Ideas: #1, #4, #9 · Votes: <n>
- Why it matters to the user: …

## Chosen direction(s)
| Cluster | Assumptions it depends on | Questions to answer |
|---------|---------------------------|---------------------|
| | Assumption: … | Question: … |

## Parking lot
- …

## Playback
- **Key takeaways:** 3–5 bullets (range explored, the strongest clusters, surprises)
- **Assumptions and questions to validate:** the riskiest few from the table above
- **Recommended next activity:** for example `/edt-ideate:storyboards` for <cluster>
```

## Quality checks
- There is one prompt, and it traces to a real need. It is not a solution in disguise, like "users need a dashboard".
- Volume and range: 20+ ideas from safe to wild, not 20 variations on one idea.
- Each vignette is an experience a user would notice, with a headline. Features and implementation details don't count.
- The user's own ideas come first and are credited. Claude built on them instead of replacing them.
- Nobody evaluated during the diverge. Cluster names describe user outcomes.
- The user or team chose the direction, and unchosen ideas are kept.
- Pitfalls: converging on whatever is easiest to build, and Claude presenting one polished favorite.

## Next
- `/edt-ideate:storyboards`: show how a chosen idea fits into the user's life.
- `/edt-ideate:to-be-scenario-map`: envision the end-to-end future experience with the chosen ideas.
- `/edt-plan:prioritization-grid`: rank clusters by user value and feasibility.
- `/edt-plan:hills`: turn a winning direction into a Hill.

## Source
[IBM Enterprise Design Thinking Toolkit: Big Idea Vignettes](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac1f)
