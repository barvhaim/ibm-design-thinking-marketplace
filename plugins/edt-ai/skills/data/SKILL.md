---
name: data
description: Run AI Essentials Data, step 2 of an IBM AI strategy. Maps the data that could power an AI intent on a Public/Private/User × Have/Need/Nice-to-have grid, with feasibility, owners and the minimum viable data. Can read repo schemas, datasets and API specs (read-only). Use when someone asks "what data do we need for this AI?", "do we have enough data?", or "what data is missing?" after an AI intent. Not for general data analysis.
argument-hint: "[topic or big idea] [facilitate]"
---

# AI Essentials: Data

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

Data is the fuel for AI. In this activity the team lists every data source that could make the chosen intent real, sorts each one by who owns it and whether you have it yet, and then faces how hard each source would be to get. The result is the smallest set of data your AI needs to deliver early value, with a named person responsible for every gap.

## When to use it
- After `/edt-ai:intent`, once the team has agreed on an intent and has at least one big idea.
- When an AI idea is moving forward but nobody has checked whether the data exists, is accessible, or may legally be used.
- Before estimating an AI project. Getting and preparing data is often the biggest cost.

## Inputs
- From `design-thinking/`: `intent-*` (the chosen intent and candidate big ideas, required), `big-idea-vignettes-*`, `hills-*`, `stakeholder-map-*` (to find data owners).
- Ask the user for: the big idea, known systems and datasets, data owners or data-savvy teammates, and any constraints on privacy, consent, licensing or residency.
- If there's no intent artifact, run `/edt-ai:intent` first, or record the intent here and tag it **Assumption**.

## Co-create with Claude
1. **Set up the grid.** There are three columns and three rows.
   - Columns:
     - **Public:** anyone can get it, though you may have to pay or accept a license.
     - **Private:** proprietary data behind your firewall that the business owns.
     - **User:** data the user owns or generates, such as contact details, health history or location. You need the user's permission to store or use it.
   - Rows:
     - **Have:** you can access it today.
     - **Need/Want:** you don't have it, but the intent requires it.
     - **Nice to have:** not available yet, but valuable later.
2. **Start with the obvious.** Ask the user to list the data they know they have, then what they need, then what would be nice to have. Moving back and forth between rows is fine. Get everything on the grid before debating where it belongs. Suggest sources they may have missed, tied to the big idea, and tag your suggestions **Assumption** until someone confirms them.
3. **Ground it in the repo** (if the user points you at code or data). Inspect it **read-only** to turn claims into evidence:
   - Look at schemas and migrations (`*.sql`, `schema.prisma`, ORM models), API specs (OpenAPI/Swagger, GraphQL, `.proto`), data dictionaries, dbt `schema.yml`, analytics tracking plans, and the headers of sample CSV, JSON or Parquet files.
   - Record source names, key fields, types, rough volume if visible, and quality notes. Tag each as `Evidence: <file path>`.
   - Don't run migrations, queries against live systems, or write calls. Don't read `.env` or secrets. Don't copy raw records or personal data into the artifact. Ask before connecting to any database or API, and only use describe-only or read-only operations.
4. **Find data experts and check feasibility.** For every source, ask:
   - Who can confirm we really have it?
   - Who would have to get it? Acquisition can mean contracts, legal review and money.
   - What prep work is needed? Even data you have may need digitizing, normalizing, consolidating or de-biasing, and a person has to do that work.
   - Can we use it for this purpose? Check consent for User data, license terms for Public data, and internal policy for Private data.
   Record an owner, the access route and the effort for each source.
5. **Vote on what's critical.** Ask which sources are essential to the AI's early success. Then define the **minimum data** needed to meet the intent. Stay user-first: favor the data that delivers what users value. Drop data collected "just in case".
6. **Write the artifact** and the Playback.

## Facilitate a live session
- **Materials:** a wall or digital whiteboard, sticky notes in one color per data type if possible, thick markers, and dot stickers. Bring a data engineer or analyst. They should lead step 4.
- **Board layout:** draw the 3×3 grid, with Public, Private and User across the top and Have, Need/Want and Nice to have down the side. Place it next to the Intent board so the big idea stays visible.
- **Agenda (60 min):**
  - 5 min: recap the intent and the big idea.
  - 5 min: draw and explain the grid.
  - 20 min: fill it, starting with Have, then Need/Want, then Nice to have.
  - 15 min: feasibility, led by the data experts.
  - 10 min: dot-vote the critical sources and agree on the minimum data.
  - 5 min: owners and next steps.
- **Prompts to read aloud:**
  - "What data do we already have that touches this idea? One source per sticky note."
  - "What's missing that our big idea can't work without?"
  - "For each Need, who would have to get it, and what would it take?"
  - "Which three sources would make our users say thank you soonest?"
- **Capture:** photograph the grid. Understanding will take sticky notes off this board, so capture it first. Then ask Claude to digitize it into the template below.

## Output
Save to `design-thinking/data-<topic>.md`:

```markdown
# AI Essentials: Data: <topic>

## Context
- Intent: … (from intent-<topic>.md)
- Big idea: …

## Data grid
| | Public | Private | User |
| --- | --- | --- | --- |
| **Have** | | | |
| **Need/Want** | | | |
| **Nice to have** | | | |

## Source register
| Source | Type | Row | What it contains (key fields) | Owner / expert | Access route & effort | Prep needed | Consent / license | Bias or quality risk | Critical? | Tag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Minimum data to meet the intent
1. … (why it is essential)

## Gaps and acquisition plan
| Gap | Who acquires | Route (build / buy / partner / ask users) | Blockers | By when |
| --- | --- | --- | --- | --- |

## Playback
- Key takeaways: (3–5)
- Assumptions and questions to validate: …
- Next activity: …
```
Tags: `Evidence: <source or file path>`, `Assumption`, or `Question`.

## Quality checks
- Every **Have** item is backed by a data expert's confirmation or a file path. If not, it's an **Assumption**.
- Every **Need/Want** item has an owner and a route for getting it, or is explicitly flagged as a blocker.
- Every **User** data item has a consent basis. If none exists, raise it now instead of at launch.
- Prep work is counted. "We have it" isn't the same as "it's usable".
- Bias risks are noted per source: who is under-represented, and what past decisions the data encodes.
- The minimum data is small and tied to the intent. A list of everything isn't a plan.
- Pitfall: treating the grid as a data-warehouse inventory. List only data that serves this intent.

## Next
- `/edt-ai:understanding`: break the critical sources into the pieces your AI has to learn.
- `/edt-plan:assumptions-and-questions`: plan how to test the riskiest data assumptions.
- `/edt-synthesize:stakeholder-map`: map the data owners and approvers you depend on.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Data](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac27)
