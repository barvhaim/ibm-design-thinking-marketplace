---
name: speculative-design-stories
description: Co-writes five-part relay stories about a dice-rolled character 10–30 years in the future, then harvests big ideas and works each back from a wedding cake to a cupcake you can build today, as an HTML artifact. The character can come from or join the simulated panel, and the stories are labeled fiction. Use when someone says "think long-term", "what will users need in 2045", "we need bigger ideas", "fill our long-term roadmap", "speculative design", "futures thinking" or "patent ideation".
argument-hint: "[domain, e.g. cloud, AI, finance] [facilitate]"
---

# Speculative Design Stories

> IBM Enterprise Design Thinking · Generate new ideas · Make / Reflect · ~90 min

Most ideation stays anchored in today's constraints, so it produces incremental ideas. Teams also need a point of view on how emerging trends and behaviors could reshape their domain beyond the next few quarters, and nobody can be creative on demand. This activity gives a repeatable process. Roll dice to create a future character and their world, co-write a five-part story in which that world gives them a problem, then mine the stories for new products, services and intellectual property. Speculation is not extrapolation: the aim is to escape today's reality first, then work back to what you can build now. The stories are fiction, and the page says so everywhere.

## When to use it
- To fill a long-term roadmap with new products, features, services or IP.
- When the team struggles to invent big ideas, or every idea is incremental.
- To seed patent brainstorms or strategy discussions about emerging technology.
- It doesn't replace research on today's users. Use it alongside that research.

## Inputs
- **A broad domain,** such as a technology type (cloud, AI, blockchain, IoT, security, analytics), a domain space (education, public policy, insurance) or an industry (aerospace, finance, energy). It should not be a specific product, because a broad domain produces more ideas.
- **What the ideas are for:** a roadmap, patents or strategy.
- **From `design-thinking/`, optional.** Read the `#edt-data` blocks of `needs-statements-*`, `hills-*` and `experience-based-roadmap-*`, but only at the end, to connect ideas back to today. This activity deliberately starts far from the present.
- **The simulated user panel,** `design-thinking/simulated-users.html`, if it exists. It can supply a character option and the personas for the cupcake check. Don't create a panel just for this activity; if there isn't one, skip the cupcake check or build one with `/edt-core:simulated-users`.
- **Ask the user only for** the domain and the purpose, if you can't infer them.

**Fiction, not research.** Characters, worlds and stories are speculative fiction. Label them that way, and never cite them as user research or merge them into empathy maps. Every harvested idea is an `assumption`, and whatever would have to be true for it is a `question`.

## Co-create with Claude
1. **Open a big-idea parking lot** right away. Capture any idea either of you has at any step, however big or small.
2. **Agree on the domain.** If the user names a product, widen it: "AI-assisted underwriting", not "our claims app".
3. **Build the main character with dice.** The fields are Name, Year, Age, Job title, Domain, Values, Context 1 and Context 2.
   - **Year:** 1–2 = today + 10 years · 3–4 = + 20 · 5–6 = + 30.
   - **Age, job title, values, Context 1 and Context 2:** build a table of six options for each. The deck has sample tables. Or propose six deliberately varied options per field and let the user edit them:
     - ages from the 20s to the 80s
     - jobs far outside the team's usual customers
     - values that could be in tension, like privacy, family, influence or the environment
     - world conditions across social, environmental, economic, political and technological shifts
   - **Drawing from the panel (optional).** One of the six job options may be a panel persona's role, aged forward to the rolled year. If the die lands on it, the character is that persona's future self; cite the `SU-` ID, and treat everything about the future as invented.
   - **Use real randomness.** Ask the user to roll a die, or run `echo $((RANDOM % 6 + 1))` once per field, and show each result. Don't "pick randomly" in your head, because the surprise is the point. Roll the two contexts from two different tables.
4. **Name and picture the character.** The user names them. Write a two- or three-line portrait, or have the user sketch one.
5. **Write the "In a world" sentence:** "In <year>, <name>, a <age>-year-old <job title>, is living in a world where <domain> co-exists with <context 1> and <context 2>."
6. **Choose an emotional arc,** or roll for one. The six basic shapes come from the research the deck cites:
   1. rags to riches (rise)
   2. tragedy (fall)
   3. man in a hole (fall, then rise)
   4. Icarus (rise, then fall)
   5. Cinderella (rise, fall, rise)
   6. Oedipus (fall, rise, fall)
7. **Write the story as a relay.** It has five parts of one or two sentences each, and each part builds on the one before:
   - **Setup:** the story world and what matters to the character.
   - **Rising action:** the conflict appears, and an incident sets things in motion.
   - **Climax:** the turning point that changes the character's fate, as a consequence of the rising action.
   - **Falling action:** the climax's consequences play out, with a moment of doubt about whether the character will escape their fate.
   - **Ending:** the conflict wraps up and a new status quo is set. The ending may flip the arc.

   Alternate authors to recreate passing the page: the user writes the Setup, Claude the Rising action, the user the Climax, Claude the Falling action and the user the Ending. Offer to swap. Better still, run two or three stories in parallel with the same character, so every part builds on someone else's.

   On your turns, write one or two sentences only, and "yes, and" what came before. You're the author, not the character, so don't role-play them. Let the world's contexts collide with the character's values. Don't steer toward the team's current product or tie things up with a tidy tech fix. Treat the character and contexts as inspiration, not constraints.

   If the user asks Claude to write everything, write three short stories with different arcs, and say that the relay's surprise is lost.
8. **Harvest big ideas.** Read the stories back. The user lists first: every product, service or invention the stories suggest, however abstract. Then add yours. Capture everything, including the parking lot.
9. **Cluster and label** the ideas by category or type, such as "the future of currency" or "food provenance".
10. **Work backward.** For each cluster, describe the **wedding cake**, the full future vision, and then the **cupcake**, the smallest version you could build or test today. These seed an Experience-based Roadmap or patent groups. If `needs-statements-*` exist, note which of today's needs each cluster echoes, with that need's tag.
11. **Cupcake check (optional, simulated).** If there's a panel, take 2 present-day personas, one of them a skeptic. One persona at a time, in character, describe each cupcake in plain words and ask: "Would this matter to you this year? What would you use instead?" Expect indifference, because these ideas come from the future. Record each answer as a `simulated` note on the cupcake. The answers sharpen the cupcake, but they don't rank the clusters.
12. **Keep the character, if the user wants to.** Add them to the panel with `/edt-core:simulated-users` (`add …`), with the year in their role and every trait listed as invented, so later activities know they're a speculative future persona, not a present-day user. If the character came from the panel, don't carry their future traits back into the present-day persona.
13. **Playback.** Name the future problems you anticipated, the strongest clusters and the cupcake worth trying first. Then publish the page.

## Facilitate a live session
Produce `design-thinking/speculative-design-stories-<domain>-kit.html`. It needs:
- **Agenda table (90 min, in story teams of 3–5):**

  | Time | Step | Notes |
  |---|---|---|
  | 0–10 | Intro and norms | Why we're here, story arcs, and the big-idea parking lot · write before you talk · yes, and · stay focused on the character · everyone participates |
  | 10–15 | Domain | Agree on one broad domain |
  | 15–30 | Character | Roll for year, age, job, values and two contexts. Name and draw the character, then write the "In a world" sentence |
  | 30–60 | Relay writing | Five rounds of about six minutes: write one or two sentences, stop, then pass the page to your right |
  | 60–70 | Read aloud | Each member reads the story they ended up with to their group |
  | 70–80 | Silent ideation | Hang the stories, then put sticky-note ideas next to each one |
  | 80–90 | Cluster and seed | Cluster and label the ideas, name wedding cakes and cupcakes, and agree next steps |
- **Prompts to read aloud:**
  - "Trust the process. Speculation isn't extrapolation, so don't drag today into <year>."
  - "Keep it human. This is <name>'s story, not the technology's."
  - Setup: "In one or two sentences, drop us into <name>'s world. Then stop and wait."
  - Rising action: "Read what you received, then introduce the conflict. What happens that sets things in motion?"
  - Climax: "Write the turning point that changes <name>'s fate."
  - Falling action: "Resolve the climax's consequences, but leave us doubting whether <name> will make it."
  - Ending: "Wrap it up and set the new normal. You can flip the emotional arc."
  - Harvest: "What products, services or inventions does this story suggest? Capture every one."
- **Materials:** an 11×17 sheet per person, divided into five labeled sections. Also markers, large paper pads, whiteboard markers, a six-sided die (or a random number generator, with a vote as the last resort), and sticky notes.
- **Option tables:** six filled-in options per field, prepared by Claude, as tables in the kit.
- **The board:** a blank character card and "In a world" `.stmt`, an empty five-frame `.frames` strip per story, empty wedding cake and cupcake `.cols`, and a parking lot.

After the session, read the photos or the Mural export. Transcribe the stories word for word with each part's author, every sticky and the parking lot. Then build the clusters, and run the cupcake check if there's a panel.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/speculative-design-stories-<domain>.html`.
- **Title:** `<Domain> Speculative Design Stories`, for example "Insurance Speculative Design Stories".
- **Header:** in `.meta`, give the purpose and the rolled year. Keep the simulated banner if the character came from the panel or a cupcake check ran. Open `<main>` with a lede: "Speculative fiction. The characters and worlds below are invented to provoke ideas. They are not user research."
- **Sections:**
  1. **Main character:** a `.persona` card with the name, a pill reading "Fiction" (and the `SU-` ID if they came from or joined the panel), the portrait, and a `dl` of year, age, job, values and the two contexts. Then a `.stmt` with the "In a world" sentence, its parts labeled Year, Character, Domain, Context 1 and Context 2. Then a table of the dice rolls: field, roll, result, and the six options.
  2. **Stories:** one `h3` per story, with its title and arc, followed by a `.frames` strip of five frames. Each frame has a rough scene sketch in ASCII or `currentColor` SVG, a `.frame-n` like `Part 3 · Climax · user`, a `.mood` that follows the arc, and the part's text.
  3. **Big ideas:** one `.cluster` per cluster, its `h4` the label, holding `assumption` notes. Each note's `.src` names the story and part that suggested it, and who spotted it.
  4. **Wedding cake to cupcake:** for each cluster, an `h3` and a `.cols` with two columns. The wedding cake column holds the future vision as `assumption` notes and what would have to be true as `question` notes. The cupcake column holds what to build or test today, the cupcake check's `simulated` notes, and a pill for any of today's needs it echoes.
  5. **Parking lot:** `.notes` tagged `assumption` or `question`.
  6. **Cupcake check:** a `details.transcript` per persona. Include this only when you ran one.
  7. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "domain": "", "purpose": "roadmap|patents|strategy", "fiction": true,
    "character": { "name": "", "year": 2046, "age": 0, "job": "", "values": "", "context1": "", "context2": "",
                   "in_a_world": "", "from_persona": null, "added_as": null,
                   "rolls": { "year": 4, "age": 2, "job": 6, "values": 1, "context1": 3, "context2": 5 } },
    "options": { "age": ["", "", "", "", "", ""], "job": [], "values": [], "context1": [], "context2": [] },
    "stories": [{ "id": "ST1", "title": "", "arc": "man-in-a-hole",
                  "parts": [{ "part": "setup|rising|climax|falling|ending", "author": "user|claude|<name>", "text": "" }] }],
    "ideas": [{ "id": "I1", "text": "", "type": "product|service|ip", "story": "ST1", "part": "climax",
                "by": "user|claude", "cluster": "C1", "note": "N4" }],
    "clusters": [{ "id": "C1", "label": "", "wedding_cake": "", "cupcake": "", "must_be_true": ["N12"],
                   "echoes": [{ "need": "", "source": "design-thinking/needs-statements-<user>.html", "tag": "evidence" }],
                   "cupcake_check": [{ "persona": "SU-3", "note": "N18" }] }],
    "parking_lot": ["N20"] }
  ```
  `items` holds every note, with `group` set to `"Ideas / <cluster>"`, `"Cake / <cluster>"`, `"Cupcake / <cluster>"` or `"Parking lot"`.

## Quality checks
- The domain is broad, not a product. The year is at least 10 years out, and the world feels truly different.
- The attributes were actually rolled, with the results shown, not chosen to resemble today's customers.
- The story is human-centered: the conflict comes from the character's life and values, with technology in the background.
- Each part has one or two sentences and builds on the previous part. The climax changes the character's fate.
- The stories are labeled fiction on the page and in `#edt-data`. Every idea is tagged `assumption`, and nothing from a story is tagged `evidence` or `simulated`.
- Every idea is captured, including abstract ones, and each cluster has at least one cupcake.
- Simulation pitfalls:
  - present-day personas who are excited by every cupcake; most should shrug at most of them
  - a future character added to the panel without being marked speculative, or future traits leaking into a present-day persona
  - a cupcake check tagged `evidence`, or used to rank the clusters
  - percentages from simulated counts
- Other pitfalls: writing a product ad set in the future, and dismissing wild ideas during the harvest.

## Next
- `/edt-plan:experience-based-roadmap`: place the wedding cakes and work back to cupcakes.
- `/edt-ideate:big-idea-vignettes`: diverge further on a promising cluster with today's users in mind.
- `/edt-ideate:storyboards`: make a cupcake concrete as a visual story.
- `/edt-plan:research-plan`: look for early signals of these futures among today's users.
- `/edt-plan:assumptions-and-questions`: sort the riskiest assumptions behind the clusters.

## Source
[IBM Enterprise Design Thinking Toolkit: Speculative Design Stories](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac25)
