---
name: understanding
description: Run AI Essentials Understanding, step 3 of an IBM AI strategy. Breaks each critical data source into the components, jargon and inferences your AI must learn, a "curriculum" for the AI, and flags risky associations. Can read repo schemas and datasets (read-only). Use when someone asks "what does our AI need to learn?", "how do we break down this data for the model?", or "what features or training data do we need?" after an AI Essentials data map.
argument-hint: "[topic or data source] [facilitate]"
---

# AI Essentials: Understanding

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

An AI only knows a domain if someone teaches it. In Understanding, the team breaks each critical data source into its individual parts: fields, domain terms, and things that can only be inferred. Together these form a curriculum for the AI, which shapes how the model is trained, grounded and evaluated. The team also asks what could go wrong if the AI starts linking those parts together.

## When to use it
- After `/edt-ai:data`, once the critical data sources are identified.
- When a team says "we'll just train a model on our data" but can't say what the model needs to learn.
- Before choosing between training, fine-tuning, retrieval or a pretrained model.

## Inputs
- From `design-thinking/`: `data-*` (critical sources and the minimum data list, required), `intent-*`, `big-idea-vignettes-*`.
- Ask the user for: which sources are most critical, who the data expert is, domain glossaries, and any schemas or sample data they can point you to.
- If there's no data artifact, run `/edt-ai:data` first.

## Co-create with Claude
1. **Select and place.** Copy the data map first (the facilitator photographs the board), because this step takes it apart. From the data map, pick the high-level sticky notes that carry domain concepts: jargon, domain-specific content, or inferred data points such as "loyalty profile", "flight data" or "customer intent". Focus on the sources most critical to the AI experience.
2. **Deconstruct.** For each high-level source, list every individual component, one per line, and break components down further where needed. Be exhaustive here, because it pays off later. Classify each component as one of:
   - **Raw:** a field that exists, such as `departure_time`.
   - **Derived:** computed from raw fields, such as "delay minutes".
   - **Inferred:** something the AI must work out, such as "travel purpose".
   - **Jargon:** a domain term the AI must learn, such as "status match".
3. **Ground it in the repo** (if the user points you at code or data). Read schemas, models, API specs and the headers of sample files **read-only** to enumerate real fields and types. Tag each as `Evidence: <file path>`. Mark components the team expects but the data doesn't contain as **Question**. Don't copy raw records or personal data, don't query live systems, and don't read secrets.
4. **Discuss.** Work through four questions in order:
   - Do any components have their own jargon that needs defining? Add it to the glossary.
   - Are these the right components for each source? Ask the data expert to confirm them.
   - What happens if the AI makes associations between these components? Look for protected attributes such as gender, race, nationality, age or disability, and for proxies that stand in for them, such as postcode, name, language or purchase history. For each one, decide whether to allow, restrict, exclude, or test for disparate impact.
   - Who will curate the data and train or tune the models? Are there pretrained models or existing domain models that could save time?
5. **Map the teaching approach.** For each inferred or jargon component, note how the AI would learn it:
   - labelled examples
   - rules or an ontology
   - a retrieval corpus for grounding
   - fine-tuning
   - an existing model
   Also note what ground truth or evaluation set would show that it has learned it.
6. **Write the artifact** and the Playback.

## Facilitate a live session
- **Materials:** the photographed data map, sticky notes in a second color for components, thick markers, and dot stickers. A data expert must attend.
- **Board layout:** an "Understanding" area next to the data grid. Move each critical high-level sticky note there and cluster its component sticky notes around it, like spokes. Leave room to break components down further.
- **Agenda (60 min):**
  - 5 min: photograph the data map and recap the intent.
  - 10 min: Select and place the critical high-level sticky notes.
  - 25 min: Deconstruct silently, one component per sticky note, then add to each other's clusters.
  - 15 min: Discuss jargon, correctness, association risks, and curation and pretrained options.
  - 5 min: owners and next steps.
- **Prompts to read aloud:**
  - "What is this source actually made of? One component per sticky note."
  - "Which of these would a new hire need explained? That's jargon our AI must learn too."
  - "If the AI connected these two sticky notes, could it treat people differently because of who they are?"
  - "Who will curate this data, and has someone already trained a model on it?"
- **Capture:** photograph each cluster up close, then ask Claude to digitize it into the template below.

## Output
Save to `design-thinking/understanding-<topic>.md`:

```markdown
# AI Essentials: Understanding: <topic>

## Context
- Intent: … · Big idea: …
- Critical sources (from data-<topic>.md): …

## Curriculum
### <High-level source>
| Component | Sub-components | Kind (raw / derived / inferred / jargon) | Sensitive or proxy? | How the AI learns it | Tag |
| --- | --- | --- | --- | --- | --- |

## Glossary
| Term | Meaning in our domain | Where it appears | Tag |
| --- | --- | --- | --- |

## Association risks
| Components linked | What the AI could infer | Who could be affected | Decision (allow / restrict / exclude / test) | Tag |
| --- | --- | --- | --- | --- |

## Curation and training
- Data curator(s): …
- Labels or ground truth needed: …
- Evaluation: how we'll know it learned each inferred component: …
- Pretrained or existing models to evaluate: …

## Playback
- Key takeaways: (3–5)
- Assumptions and questions to validate: …
- Next activity: …
```
Tags: `Evidence: <source or file path>`, `Assumption`, or `Question`.

## Quality checks
- Every critical source from the data map is broken down, or deliberately deferred with a reason.
- Inferred components are clearly separated from raw fields. Inferences are where models fail and where bias enters.
- Every protected attribute and likely proxy is flagged, and each has a decision.
- Every inferred component has a way to learn it and a way to evaluate it.
- Components claimed to exist are backed by a file path or a data expert's confirmation.
- Pitfall: stopping at table names. "Customer record" isn't a component, but `membership_level` is.

## Next
- `/edt-ai:reasoning`: use this curriculum to ground the big idea in what the AI can actually reason on.
- `/edt-ai:knowledge`: take the association risks into a full review of effects on people and society.
- `/edt-plan:research-plan`: plan how to confirm the components and glossary with domain experts.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Understanding](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac2d)
