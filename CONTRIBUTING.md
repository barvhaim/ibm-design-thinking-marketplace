# Authoring skills for this marketplace

Each IBM Enterprise Design Thinking (EDT) toolkit activity is one Claude Code skill. Every skill follows the same shape so they read as one toolkit and can hand work to each other.

## Layout

```
plugins/<plugin>/
├── .claude-plugin/plugin.json
└── skills/<skill-name>/
    ├── SKILL.md          # required, keep under ~200 lines
    └── examples.md       # optional: a worked example, loaded only when needed
```

- `<skill-name>` is the activity name in kebab-case (`empathy-map`, `as-is-scenario-map`). The frontmatter `name` matches the folder name.
- Users invoke a skill as `/<plugin>:<skill-name>`, for example `/edt-synthesize:empathy-map`.
- When you add a plugin, add its entry to `.claude-plugin/marketplace.json`, and keep the entry `name` the same as the `name` in `plugin.json`.
- After every change, run `claude plugin validate .`.

## Conventions every skill follows

1. **Shared workspace.** Skills read and write artifacts in `design-thinking/` at the user's project root. Create the folder if it's missing. Name each artifact `design-thinking/<skill-name>[-<topic-slug>].md`. Before starting, list `design-thinking/` and read any upstream artifacts the activity builds on. For example, Needs Statements reads empathy maps and as-is scenario maps. This shared folder is how activities from different plugins chain together.
2. **Evidence over invention.** Never invent user research. Tag every item as one of:
   - **Evidence:** observed or quoted, with its source.
   - **Assumption:** something the team believes.
   - **Question:** an open unknown.

   If inputs are missing, ask for them, or point the user to the activity that would produce them. Write hypothetical examples only when the user asks for them, and label them as hypothetical. You are not your user.
3. **Two modes.**
   - **Co-create** (the default): Claude works through the activity with the user in conversation. It draws on workspace artifacts and on any files the user points to, such as transcripts, notes, tickets, analytics or PRDs, and writes the artifact.
   - **Facilitate:** the user is running a live session with a team. Use this mode when the user mentions a workshop, session or facilitation, or passes `facilitate` as an argument. Claude produces a facilitator kit: an agenda with timings, prompts to read aloud, materials, a board layout that works on a physical wall or a digital whiteboard such as Mural, and a capture template. After the session, Claude digitizes the results into the artifact.
4. **End with a Playback.** Every artifact ends with a short Playback section. It holds 3–5 key takeaways, the assumptions and questions to validate, and the recommended next activity.
5. **Respect the source.** Paraphrase the IBM toolkit decks instead of pasting their text, and link the source deck in each skill.
6. **Cross-reference by command.** Point to related activities by their slash command (`/edt-plan:hills`), so users can see they exist even if they haven't installed that plugin yet.

## SKILL.md template

````markdown
---
name: <skill-name>
description: <One or two sentences. What the activity produces, then "Use when …" with concrete triggers, phrases and situations. ≤ 500 characters.>
argument-hint: "[topic or user] [facilitate]"
---

# <Activity Name>

> IBM Enterprise Design Thinking · <Toolkit category> · <Loop phase(s): Observe / Reflect / Make> · ~<N> min

<Why this activity exists, in one paragraph.>

## When to use it
- …

## Inputs
- Upstream artifacts in `design-thinking/`: …
- What to ask the user for if missing: …

## Co-create with Claude
1. … (numbered steps that follow the deck's phases, adapted to working with Claude)

## Facilitate a live session
- Agenda with timings · prompts to read aloud · materials · board layout

## Output
Save to `design-thinking/<skill-name>-<topic>.md` using this template:

```markdown
… (the artifact template, ending with a ## Playback section)
```

## Quality checks
- … (what good looks like, plus common pitfalls)

## Next
- `/<plugin>:<skill>`: why it comes next

## Source
[IBM Enterprise Design Thinking Toolkit: <Activity>](<deck URL>)
````
