---
name: data
description: Runs AI Essentials Data, step 2 of an IBM AI strategy, as an HTML artifact. Maps the data behind an AI intent on a Public/Private/User × Have/Need/Nice-to-have grid, with owners, feasibility and the minimum viable data. Reads repo schemas and specs read-only, and asks simulated users what they'd share and what feels invasive. Use when someone asks "what data do we need for this AI?", "do we have enough data?" or "what's missing?" after an AI intent.
argument-hint: "[topic or big idea] [facilitate]"
---

# AI Essentials: Data

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

Data is the fuel for AI. In this activity the team lists every data source that could make the chosen intent real, sorts each one by who owns it and whether you have it yet, and then faces how hard each source would be to get. The result is the smallest set of data your AI needs to deliver early value, with a named person responsible for every gap. Much of that data is about people, so simulated users react to it before anyone collects it: what they'd happily share, what they'd share only under conditions, and what would feel invasive.

## When to use it
- After `/edt-ai:intent`, once the team has agreed on an intent and has at least one big idea.
- When an AI idea is moving forward but nobody has checked whether the data exists, is accessible, or may legally be used.
- Before estimating an AI project. Getting and preparing data is often the biggest cost.
- Not for general data analysis or a data-warehouse inventory.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - `intent-*` (required): `content.chosen` for the intent and big ideas, and `content.fit` for the AI fit verdict
  - `big-idea-vignettes-*` and `hills-*`, for the big idea in detail
  - `stakeholder-map-*`, to find data owners

  Older `.md` versions are fine; read them as text. If there's no intent page, run `/edt-ai:intent` first, or record the intent here and tag it `assumption`.
- **Code and data the user points to,** such as schemas, API specs and sample files. These are real evidence, read read-only.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** systems and datasets you can't see in the repo, who the data owners or data-savvy teammates are, and any constraints on privacy, consent, licensing or residency that aren't written down.

## Co-create with Claude
1. **Gather.** Read the intent page and state the intent and big idea in one line each. If its verdict was *Non-AI fix first*, say so and ask whether to continue. Build a source list: `S1…` for each real source (files, docs, people who confirmed something) and `SU-…` for the personas whose data is in scope.
2. **Set up the grid.** There are three columns and three rows.
   - Columns:
     - **Public:** anyone can get it, though you may have to pay or accept a license.
     - **Private:** proprietary data behind your firewall that the business owns.
     - **User:** data the user owns or generates, such as contact details, health history or location. You need the user's permission to store or use it.
   - Rows:
     - **Have:** you can access it today.
     - **Need/Want:** you don't have it, but the intent requires it.
     - **Nice to have:** not available yet, but valuable later.
3. **Start with the obvious.** Ask the user to list the data they know they have, then what they need, then what would be nice to have. Moving back and forth between rows is fine. Get everything on the grid before debating where it belongs. Suggest sources they may have missed, tied to the big idea, and tag your suggestions `assumption` until someone confirms them.
4. **Ground it in the repo** (if the user points you at code or data). Inspect it **read-only** to turn claims into evidence:
   - Look at schemas and migrations (`*.sql`, `schema.prisma`, ORM models), API specs (OpenAPI/Swagger, GraphQL, `.proto`), data dictionaries, dbt `schema.yml`, analytics tracking plans, and the headers of sample CSV, JSON or Parquet files.
   - Record source names, key fields, types, rough volume if visible, and quality notes. Tag each `evidence`, with the file path as its source.
   - Don't run migrations, queries against live systems, or write calls. Don't read `.env` or secrets. Don't copy raw records or personal data into the page. Ask before connecting to any database or API, and only use describe-only or read-only operations.
5. **Ask the people whose data it is.** For every User source, and every Private source that describes people, run a short session with each of 3–4 personas, including the skeptic and the edge case. Run **one persona at a time**, in character, following the role-play rules in `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Describe the data in plain words, never as field names: "To <benefit>, it would use <what it would know about you>." Then ask:
   - "Would you be OK with that? Why, or why not?"
   - "What would feel like too much?"
   - "Who should be able to see it, and for how long?"
   - "What would you do if you found out it was being used this way?"
   Let them be inconsistent, as real people are: happy to share location for one thing and furious about it for another. Record each session as a transcript. Sort each reaction into *Comfortable*, *Only if…* (with the condition) or *Invasive*, as a `simulated` note with the persona ID.
6. **Find data experts and check feasibility.** Only real people can confirm data, so never simulate a data owner or expert. A confirmation is `evidence`, with the person's role and the date; an unconfirmed claim is a `question`. For every source, ask:
   - Who can confirm we really have it?
   - Who would have to get it? Acquisition can mean contracts, legal review and money.
   - What prep work is needed? Even data you have may need digitizing, normalizing, consolidating or de-biasing, and a person has to do that work.
   - Can we use it for this purpose? Check consent for User data, license terms for Public data, and internal policy for Private data.
   Record an owner, the access route and the effort for each source.
7. **Vote on what's critical.** Ask which sources are essential to the AI's early success. Then define the **minimum data** needed to meet the intent. Stay user-first: favor the data that delivers what users value. Drop data collected "just in case". If a source felt invasive to the personas and isn't essential, drop it or find a less invasive substitute.
8. **Playback.** Tell the data story back in a few sentences: what you have, what blocks you, and what the minimum is. Put unconfirmed Have items and the simulated comfort reactions at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/data-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0–5 Recap the intent and the big idea
  - 5–10 Draw and explain the grid
  - 10–30 Fill it, starting with Have, then Need/Want, then Nice to have
  - 30–45 Feasibility, led by the data experts
  - 45–55 Dot-vote the critical sources and agree on the minimum data
  - 55–60 Owners and next steps
- **Prompts to read aloud:**
  - "What data do we already have that touches this idea? One source per sticky note."
  - "What's missing that our big idea can't work without?"
  - "For each Need, who would have to get it, and what would it take?"
  - "Whose data is this, and would they be OK with us using it this way?"
  - "Which three sources would make our users say thank you soonest?"
- **Materials:** a wall or digital whiteboard, sticky notes in one color per data type if possible, thick markers and dot stickers. Bring a data engineer or analyst to lead feasibility.
- **Board layout:** an empty 3×3 `.map` grid, with Public, Private and User across the top and Have, Need/Want and Nice to have down the side, next to the Intent board so the big idea stays visible. Beside it, an empty *Comfortable / Only if… / Invasive* `.cols` board, optionally seeded with the personas' reactions, labeled as simulated.
- **Capture:** Understanding will take sticky notes off this board, so photograph the grid first.

After the session, read the photos or the whiteboard export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/data-<topic>.html`.
- **Title:** `<Topic> AI Data`, for example "Claims Triage AI Data". The `h1` is "AI Essentials: Data" with the topic in `.topic`.
- **Sections:**
  1. **Context:** the chosen intent and big idea from the Intent page, in a `.stmts` block, with its verdict pill and a source pill for the upstream page.
  2. **Data grid:** a `.scroll` wrapping a `.map` with `--cols: 3`. The `.ch` headers are Public, Private and User, each with its definition in `<small>`; the `.rh` rows are Have, Need/Want and Nice to have. Each cell holds one note per source: `evidence` with the file path or confirming person as its `.src`, `assumption` for unconfirmed suggestions, `question` for unknowns. Start a critical source's text with "Critical ·".
  3. **Source register:** a table of source, type, row, key fields, owner or expert, access route and effort, prep needed, consent or license basis, bias or quality risk, critical, and a tag pill.
  4. **Comfort and consent:** `.cols` with *Comfortable*, *Only if…* and *Invasive*, holding `simulated` notes that name the data source and quote the persona, with the persona ID in `.src`. Follow it with a `details.transcript` per persona.
  5. **Minimum data:** a table of source, why it's essential, and a tag pill.
  6. **Gaps and acquisition plan:** a table of gap, who acquires it, route (build, buy, partner or ask users), blockers, and by when.
  7. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "intent": "", "big_idea": "", "intent_verdict": "Hybrid",
    "sources": [{ "id": "D1", "name": "", "type": "user", "row": "have", "fields": ["membership_level"], "owner": "", "access": "", "effort": "med", "prep": "", "basis": "consent", "bias_risk": "", "critical": true, "tag": "evidence", "source": "S2" }],
    "comfort": [{ "data": "D3", "persona": "SU-2", "reaction": "only_if", "condition": "", "note": "N11" }],
    "minimum": [{ "data": "D1", "why": "" }],
    "gaps": [{ "data": "D5", "who": "", "route": "partner", "blockers": "", "by": "" }] }
  ```
  `type` is `public`, `private` or `user`. `row` is `have`, `need` or `nice`. `reaction` is `comfortable`, `only_if` or `invasive`. `items` holds every grid note and comfort note, with `group` set to `"<Column> / <Row>"` or `"Comfort / <reaction>"`.

## Quality checks
- Every **Have** item is backed by a file path or a real data expert's confirmation. If not, it's an `assumption` or a `question`. A simulated user never confirms that data exists.
- Every **Need/Want** item has an owner and a route for getting it, or is explicitly flagged as a blocker.
- Every **User** data item has a consent basis. If none exists, raise it now instead of at launch. Simulated comfort is not consent: it shows where to look first, and the basis still comes from policy and real users.
- Prep work is counted. "We have it" isn't the same as "it's usable".
- Bias risks are noted per source: who is under-represented, and what past decisions the data encodes.
- The minimum data is small and tied to the intent. A list of everything isn't a plan.
- The personas differ in what they'd share. If every persona is fine with everything, the simulation is too agreeable, so rerun it with the skeptic and the edge case pushing back.
- Personas react to data described in plain words. If they're reacting to field names, the question was too technical or leading.
- Comfort results are counts of simulated users, such as "3 of 4 simulated users found it invasive", never percentages.
- No raw records, personal data or secrets appear on the page.
- Pitfall: treating the grid as a data-warehouse inventory. List only data that serves this intent.

## Next
- `/edt-ai:understanding`: break the critical sources into the pieces your AI has to learn.
- `/edt-plan:assumptions-and-questions`: plan how to test the riskiest data and comfort assumptions.
- `/edt-synthesize:stakeholder-map`: map the data owners and approvers you depend on.
- `/edt-core:sponsor-users`: check the comfort reactions with real users before you collect anything.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Data](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac27)
