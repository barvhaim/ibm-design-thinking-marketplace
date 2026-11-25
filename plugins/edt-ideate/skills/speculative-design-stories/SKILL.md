---
name: speculative-design-stories
description: Co-write short relay stories about a randomly generated character 10–30 years in the future, to anticipate users' future problems and harvest big ideas for products, services and IP. Use when someone says "think long-term", "what will users need in 2045", "we need bigger ideas", "fill our long-term roadmap", "speculative design", "futures thinking", "patent ideation", or the team keeps producing only incremental ideas.
argument-hint: "[domain, e.g. cloud, AI, finance] [facilitate]"
---

# Speculative Design Stories

> IBM Enterprise Design Thinking · Generate new ideas · Make / Reflect · ~90 min

Most ideation stays anchored in today's constraints, so it produces incremental ideas. Teams also need a point of view on how emerging trends and behaviors could reshape their domain beyond the next few quarters, and nobody can be creative on demand. This activity gives a repeatable process. Roll dice to create a future character and their world, co-write a five-part story in which that world gives them a problem, then mine the stories for new products, services and intellectual property. Speculation is not extrapolation: the aim is to escape today's reality first, then work back to what you can build now.

## When to use it
- To fill a long-term roadmap with new products, features, services or IP.
- When the team struggles to invent big ideas, or every idea is incremental.
- To seed patent brainstorms or strategy discussions about emerging technology.
- It doesn't replace research on today's users. Use it alongside that research.

## Inputs
- **A broad domain**, such as a technology type (cloud, AI, blockchain, IoT, security, analytics), a domain space (education, public policy, insurance) or an industry (aerospace, finance, energy). It should not be a specific product, because a broad domain produces more ideas.
- **What the ideas are for:** a roadmap, patents or strategy.
- **Optional upstream artifacts in `design-thinking/`:** `needs-statements-*`, `hills-*` and `experience-based-roadmap-*`. They're only for connecting ideas back to today at the end, because this activity deliberately starts far from the present.

**Evidence note:** characters, worlds and stories are speculative fiction. Label them that way, and never cite them as user research or merge them into empathy maps. Every harvested idea is an Assumption, and whatever would have to be true for it becomes a Question.

## Co-create with Claude
1. **Open a big-idea parking lot** at the top of the working document right away. Capture any idea either of you has at any step, however big or small.
2. **Agree on the domain.** If the user names a product, widen it: "AI-assisted underwriting", not "our claims app".
3. **Build the main character with dice.** The template fields are Name, Year, Age, Job title, Domain, Values, Context 1 and Context 2.
   - **Year:** 1–2 = today + 10 years · 3–4 = + 20 · 5–6 = + 30.
   - **Age, job title, values, Context 1 and Context 2:** build a table of six options for each. The deck has sample tables. Or propose six deliberately varied options per field and let the user edit them:
     - ages from the 20s to the 80s
     - jobs far outside the team's usual customers
     - values that could be in tension, like privacy, family, influence or the environment
     - world conditions across social, environmental, economic, political and technological shifts
   - **Use real randomness.** Ask the user to roll a die, or run `echo $((RANDOM % 6 + 1))` once per field and show the result. Don't "pick randomly" in your head, because the surprise is the point. Roll the two contexts from two different tables.
4. **Name and picture the character.** The user names them. Write a two- or three-line portrait, or have the user sketch one.
5. **Write the "In a world" sentence:** "In <year>, <name>, a <age>-year-old <job title>, is living in a world where <domain> co-exists with <context 1> and <context 2>."
6. **Choose an emotional arc,** or roll for one. The six basic shapes come from the research the deck cites:
   - rags to riches (rise)
   - tragedy (fall)
   - man in a hole (fall, then rise)
   - Icarus (rise, then fall)
   - Cinderella (rise, fall, rise)
   - Oedipus (fall, rise, fall)
7. **Write the story as a relay.** It has five parts of one or two sentences each, and each part builds on the one before:
   - **Setup:** the story world and what matters to the character.
   - **Rising action:** the conflict appears, and an incident sets things in motion.
   - **Climax:** the turning point that changes the character's fate, as a consequence of the rising action.
   - **Falling action:** the climax's consequences play out, with a moment of doubt about whether the character will escape their fate.
   - **Ending:** the conflict wraps up and a new status quo is set. The ending may flip the arc.

   Alternate authors to recreate passing the page: the user writes the Setup, Claude the Rising action, the user the Climax, Claude the Falling action and the user the Ending. Offer to swap. Better still, run two or three stories in parallel with the same character, so every part builds on someone else's.

   On your turns, write one or two sentences only, and "yes, and" what came before. Let the world's contexts collide with the character's values. Don't steer toward the team's current product or tie things up with a tidy tech fix. Treat the character and contexts as inspiration, not constraints.

   If the user asks Claude to write everything, write three short stories with different arcs, and say that the relay's surprise is lost.
8. **Harvest big ideas.** Read the stories back. The user lists first: every product, service or invention the stories suggest, however abstract. Then add yours. Capture everything, including the parking lot.
9. **Cluster and label** the ideas by category or type, such as "the future of currency" or "food provenance".
10. **Work backward.** For each cluster, describe the "wedding cake" (the full future vision) and then the "cupcake" (the smallest version you could build or test today). These seed an Experience-based Roadmap or patent groups. If `needs-statements-*` exist, note which of today's needs each cluster echoes.
11. **Save and play back** using the template below.

## Facilitate a live session
**Agenda (90 min, in story teams of 3–5)**

| Time | Step | Notes |
|---|---|---|
| 0–10 | Intro & norms | Why we're here, story arcs, and the big-idea parking lot · write before you talk · yes, and · stay focused on the character · everyone participates |
| 10–15 | Domain | Agree on one broad domain |
| 15–30 | Character | Roll for year, age, job, values and two contexts. Name and draw the character, then write the "In a world" sentence |
| 30–60 | Relay writing | Five rounds of about six minutes: write one or two sentences, stop, then pass the page to your right |
| 60–70 | Read aloud | Each member reads the story they ended up with to their group |
| 70–80 | Silent ideation | Hang the stories, then put sticky-note ideas next to each one |
| 80–90 | Cluster & seed | Cluster and label the ideas, name wedding cakes and cupcakes, and agree next steps |

**Prompts to read aloud**
- "Trust the process. Speculation isn't extrapolation, so don't drag today into <year>."
- "Keep it human. This is <name>'s story, not the technology's."
- Setup: "In one or two sentences, drop us into <name>'s world. Then stop and wait."
- Rising action: "Read what you received, then introduce the conflict. What happens that sets things in motion?"
- Climax: "Write the turning point that changes <name>'s fate."
- Falling action: "Resolve the climax's consequences, but leave us doubting whether <name> will make it."
- Ending: "Wrap it up and set the new normal. You can flip the emotional arc."
- Harvest: "What products, services or inventions does this story suggest? Capture every one."

**Materials:** an 11×17 sheet per person, divided into five labeled sections. Also markers, large paper pads, whiteboard markers, a six-sided die (or a random number generator, with a vote as the last resort), sticky notes and the prepared option tables.

**Board layout (physical wall or Mural)**
```
+-------------------------------------------------------------+--------------+
| MAIN CHARACTER: Name | Year | Age | Job | Domain | Values   |  BIG IDEA    |
|                 Context 1 | Context 2 | (drawing)           |  PARKING LOT |
| "In <year>, <name>, a <age> <job>, is living in a world..." |              |
+-------------------------------------------------------------+              |
| STORY WALL: story 1 | story 2 | story 3 ... (stickies beside each)         |
+----------------------------------------------------------------------------+
| CLUSTERS: label -> wedding cake -> cupcake                                 |
+----------------------------------------------------------------------------+
```

**After the session:** ask for photos or a Mural export. Transcribe the stories word for word with each part's author, every sticky and the parking lot, then build the clusters table.

## Output
Save to `design-thinking/speculative-design-stories-<domain>.md` using this template:

```markdown
# Speculative Design Stories: <domain>
_Date · Participants · Mode: co-create | facilitated · Purpose: roadmap | patents | strategy_

> Speculative fiction. The characters and worlds below are invented to provoke ideas. They are not user research.

## Main character
| Name | Year | Age | Job title | Domain | Values | Context 1 | Context 2 |
|------|------|-----|-----------|--------|--------|-----------|-----------|

In <year>, <name>, a <age>-year-old <job title>, is living in a world where <domain> co-exists with <context 1> and <context 2>.

## Story <n>: <title> · Arc: <arc>
1. **Setup** (<author>): …
2. **Rising action** (<author>): …
3. **Climax** (<author>): …
4. **Falling action** (<author>): …
5. **Ending** (<author>): …

## Big ideas harvested
| # | Idea | Type: product / service / IP | From story | Cluster |
|---|------|------------------------------|------------|---------|

## Clusters: wedding cake to cupcake
| Cluster | Wedding cake (future vision) | Cupcake (build or test today) | Today's need it echoes | Questions |
|---------|------------------------------|-------------------------------|------------------------|-----------|

## Parking lot
- …

## Playback
- **Key takeaways:** 3–5 bullets (future problems we anticipated, the strongest clusters)
- **Assumptions and questions to validate:** what would have to be true, and what early signals we could look for today
- **Recommended next activity:** for example `/edt-plan:experience-based-roadmap` to place the cupcakes
```

## Quality checks
- The domain is broad, not a product. The year is at least 10 years out, and the world feels truly different.
- The attributes were actually rolled, not chosen to resemble today's customers.
- The story is human-centered: the conflict comes from the character's life and values, with technology in the background.
- Each part has one or two sentences and builds on the previous part. The climax changes the character's fate.
- The stories are labeled as fiction, and every idea is tagged as an Assumption.
- Every idea is captured, including abstract ones, and each cluster has at least one cupcake.
- Pitfalls: writing a product ad set in the future, and dismissing wild ideas during the harvest.

## Next
- `/edt-plan:experience-based-roadmap`: place the wedding cakes and work back to cupcakes.
- `/edt-ideate:big-idea-vignettes`: diverge further on a promising cluster with today's users in mind.
- `/edt-ideate:storyboards`: make a cupcake concrete as a visual story.
- `/edt-plan:research-plan`: look for early signals of these futures among today's users.
- `/edt-plan:assumptions-and-questions`: sort the riskiest assumptions behind the clusters.

## Source
[IBM Enterprise Design Thinking Toolkit: Speculative Design Stories](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac25)
