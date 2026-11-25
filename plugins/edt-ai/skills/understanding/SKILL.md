---
name: understanding
description: Runs AI Essentials Understanding, step 3 of an IBM AI strategy, as an HTML artifact. Breaks critical data sources into the raw, derived, inferred and jargon components the AI must learn, checks the jargon against how simulated users describe it, and flags risky proxies. Reads repo schemas read-only. Use when someone asks "what does our AI need to learn?", "what training data or features do we need?" or "how do we break this data down?" after an AI Essentials data map.
argument-hint: "[topic or data source] [facilitate]"
---

# AI Essentials: Understanding

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

An AI only knows a domain if someone teaches it. In Understanding, the team breaks each critical data source into its individual parts: fields, domain terms, and things that can only be inferred. Together these form a curriculum for the AI, which shapes how the model is trained, grounded and evaluated. The team also asks what could go wrong if the AI starts linking those parts together. Simulated users add a jargon check: the team's terms are rarely the words users say, and an AI that only knows the team's words will misread its users.

## When to use it
- After `/edt-ai:data`, once the critical data sources are identified.
- When a team says "we'll just train a model on our data" but can't say what the model needs to learn.
- Before choosing between training, fine-tuning, retrieval or a pretrained model.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - `data-*` (required): `content.sources` where `critical` is true, and `content.minimum`
  - `intent-*` and `big-idea-vignettes-*`, for the intent and big idea
  - `empathy-map-*` and `interviews-*`, for words real users already used

  Older `.md` versions are fine; read them as text. If there's no data page, run `/edt-ai:data` first.
- **Code and data the user points to,** such as schemas, glossaries and sample files. These are real evidence, read read-only.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** who the data expert is, and any domain glossary you can't find in the repo.

## Co-create with Claude
1. **Gather.** Read the data page and list its critical sources. Build a source list: `S1…` for each real source (files, glossaries, the data expert) and `SU-…` for the personas who represent the target users.
2. **Select and place.** The data page is your copy of the data map, so this step can take it apart. Pick the high-level sources that carry domain concepts: jargon, domain-specific content, or inferred data points such as "loyalty profile", "flight data" or "customer intent". Focus on the sources most critical to the AI experience.
3. **Deconstruct.** For each high-level source, list every individual component, one per line, and break components down further where needed. Be exhaustive here, because it pays off later. Classify each component as one of:
   - **Raw:** a field that exists, such as `departure_time`.
   - **Derived:** computed from raw fields, such as "delay minutes".
   - **Inferred:** something the AI must work out, such as "travel purpose".
   - **Jargon:** a domain term the AI must learn, such as "status match".
4. **Ground it in the repo** (if the user points you at code or data). Read schemas, models, API specs and the headers of sample files **read-only** to enumerate real fields and types. Tag each `evidence`, with the file path as its source. Tag components the team expects but the data doesn't contain as `question`. Don't copy raw records or personal data, don't query live systems, and don't read secrets.
5. **Run the jargon check with simulated users.** Take every jargon and inferred component, plus the high-level concepts. Run a short session with each of 3–4 personas, mixing a novice, an expert and the edge case. Run **one persona at a time**, in character, following the role-play rules in `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Don't say the team's term first:
   - Describe the situation and ask: "What do you call this?" and "How would you explain it to someone new?"
   - Then say the team's term: "Does '<term>' mean anything to you? What do you think it means?"
   - For inferred components: "How can you tell when <it's true>? What gives it away?"
   Record each session as a transcript. Each answer is a `simulated` note with the persona ID. Where users' words differ from the team's, the AI must learn both, so add both to the glossary. A persona's answer can't define the domain meaning; that still comes from the data expert or the docs. If a persona's cue for an inference is a stand-in for who someone is, such as "you can tell from their name" or "from the area they live in", carry it into the next step as a risky proxy.
6. **Discuss.** Work through four questions in order:
   - Do any components have their own jargon that needs defining? Add it to the glossary.
   - Are these the right components for each source? Ask the data expert to confirm them.
   - What happens if the AI makes associations between these components? Look for protected attributes such as gender, race, nationality, age or disability, and for proxies that stand in for them, such as postcode, name, language or purchase history. Include the proxies the personas used. For each one, decide whether to allow, restrict, exclude, or test for disparate impact.
   - Who will curate the data and train or tune the models? Are there pretrained models or existing domain models that could save time?
7. **Map the teaching approach.** For each inferred or jargon component, note how the AI would learn it:
   - labelled examples
   - rules or an ontology
   - a retrieval corpus for grounding
   - fine-tuning
   - an existing model

   Also note what ground truth or evaluation set would show that it has learned it, including test phrasings in the users' own words.
8. **Playback.** Tell the curriculum back in a few sentences: what the AI must learn, where users' words diverge from the team's, and which associations are off-limits. Put the simulated vocabulary and the unconfirmed components at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/understanding-<topic>-kit.html`. A data expert must attend. It needs:
- **Agenda table (60 min):**
  - 0–5 Photograph the data map and recap the intent
  - 5–15 Select and place the critical high-level sticky notes
  - 15–40 Deconstruct silently, one component per sticky note, then add to each other's clusters
  - 40–55 Discuss jargon, correctness, association risks, and curation and pretrained options
  - 55–60 Owners and next steps
- **Prompts to read aloud:**
  - "What is this source actually made of? One component per sticky note."
  - "Which of these would a new hire need explained? That's jargon our AI must learn too."
  - "Would our users use this word? What would they say instead?"
  - "If the AI connected these two sticky notes, could it treat people differently because of who they are?"
  - "Who will curate this data, and has someone already trained a model on it?"
- **Materials:** the photographed data map, sticky notes in a second color for components, thick markers and dot stickers.
- **Board layout:** an empty `.cols` board with one column per critical high-level source, where component sticky notes cluster like spokes, leaving room to break them down further. Beside it, an empty glossary table with a "Users' words" column, optionally seeded with the personas' words, labeled as simulated.
- **Capture:** photograph each cluster up close.

After the session, read the photos or the whiteboard export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/understanding-<topic>.html`.
- **Title:** `<Topic> AI Understanding`, for example "Claims Triage AI Understanding". The `h1` is "AI Essentials: Understanding" with the topic in `.topic`.
- **Sections:**
  1. **Critical sources:** a table of source, why it's critical (from the data page), and whether it's broken down here or deferred, with the reason.
  2. **Curriculum:** `.cols` with one `.col` per high-level source. Each component is a tagged note whose text starts with its kind, such as "Inferred · travel purpose". Use `evidence` with the file path, `assumption` for the team's expectations, and `question` for components the data doesn't contain. Below it, a table of component, sub-components, kind, sensitive or proxy, how the AI learns it, how you'll evaluate it, and a tag pill.
  3. **Glossary and jargon check:** a table of term, meaning in our domain (with its source), where it appears, users' words, and a match pill. Put each persona's words in quotes with a `simulated` pill naming the persona. Use `data-tone="good"` when users share the term, `"warn"` when they use different words, and `"bad"` when they misread it.
  4. **Association risks:** a table of components linked, what the AI could infer, who could be affected, a decision pill, and a tag pill. Use `data-tone="good"` for allow, `"warn"` for restrict or test, and `"bad"` for exclude. Mark the proxies the personas used.
  5. **Curation and training:** `.cols` with *Curators*, *Ground truth and labels* and *Pretrained or existing models*, holding tagged notes.
  6. **Simulated sessions:** a `details.transcript` per persona.
  7. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "intent": "", "big_idea": "",
    "sources": [{ "data": "D1", "name": "", "status": "deconstructed", "reason": "" }],
    "components": [{ "id": "C1", "data": "D1", "name": "membership_level", "parent": null, "kind": "raw", "sensitive": "none", "learn": "", "evaluate": "", "tag": "evidence", "source": "S3" }],
    "glossary": [{ "term": "", "meaning": "", "meaning_source": "S4", "appears_in": "", "user_words": [{ "persona": "SU-1", "words": "", "note": "N7" }], "match": "different" }],
    "risks": [{ "components": ["C4", "C9"], "inference": "", "affected": "", "decision": "test", "from_persona": "SU-3", "tag": "assumption" }],
    "curation": { "curators": [""], "ground_truth": [""], "pretrained": [""] } }
  ```
  `kind` is `raw`, `derived`, `inferred` or `jargon`. `sensitive` is `none`, `protected` or `proxy`. `match` is `same`, `different` or `misread`. `decision` is `allow`, `restrict`, `exclude` or `test`. `items` holds every component and jargon-check note, with `group` set to `"Curriculum / <source>"` or `"Jargon / <term>"`.

## Quality checks
- Every critical source from the data page is broken down, or deliberately deferred with a reason.
- Inferred components are clearly separated from raw fields. Inferences are where models fail and where bias enters.
- Every protected attribute and likely proxy is flagged, and each has a decision.
- Every inferred component has a way to learn it and a way to evaluate it.
- Components claimed to exist are backed by a file path or a data expert's confirmation.
- The personas' words stay in the users' words column. A simulated user never supplies the domain meaning, and no simulated note is tagged `evidence`.
- The personas sound different: the novice and the expert don't use the same vocabulary. If every persona already knows the team's terms, the role-play is echoing the team, so rerun it without saying the term first.
- Mismatches are counts of simulated users, such as "2 of 4 simulated users misread 'status match'", never percentages.
- Pitfall: stopping at table names. "Customer record" isn't a component, but `membership_level` is.

## Next
- `/edt-ai:reasoning`: use this curriculum to ground the big idea in what the AI can actually reason on.
- `/edt-ai:knowledge`: take the association risks into a full review of effects on people and society.
- `/edt-plan:research-plan`: plan how to confirm the components and glossary with domain experts.
- `/edt-gather:interviews`: check the users' words with real users.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Understanding](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac2d)
