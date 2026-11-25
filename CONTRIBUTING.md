# Authoring skills for this marketplace

Each IBM Enterprise Design Thinking (EDT) toolkit activity is one Claude Code skill. Every skill follows the same shape, so the skills read as one toolkit and can hand work to each other.

## Layout

```
shared/                       # source of truth, copied into every plugin
├── artifact-template.html    # the HTML page every activity produces
├── artifacts.md              # how to build, save, publish and read artifacts, plus a component catalog
└── simulated-users.md        # the simulated user protocol
plugins/<plugin>/
├── .claude-plugin/plugin.json
├── shared/                   # copy of /shared; don't edit it here
└── skills/<skill-name>/
    ├── SKILL.md              # required; keep it under ~200 lines
    └── examples.md           # optional worked example, loaded only when needed
```

- **Skill names.** `<skill-name>` is the activity's name in kebab-case, such as `empathy-map` or `as-is-scenario-map`. The frontmatter `name` matches the folder name. Users invoke a skill as `/<plugin>:<skill-name>`, for example `/edt-synthesize:empathy-map`.
- **Shared files.** Edit files in `/shared`, then run `scripts/sync-shared.sh`. Skills reference their plugin's copy as `${CLAUDE_PLUGIN_ROOT}/shared/…`.
- **New plugins.** When you add a plugin, add its entry to `.claude-plugin/marketplace.json`. Keep the entry's `name` the same as the `name` in `plugin.json`.
- **Checks.** After every change, run `claude plugin validate .` and `scripts/sync-shared.sh --check`.
- **Docs site.** `scripts/build-site.py` generates the GitHub Pages site from the SKILL.md files, so a new skill gets its page automatically. It takes plugin labels and skill order from the Plugins table in README.md, so add every new skill there.

## Conventions every skill follows

1. **HTML artifacts.** Every activity's output is a self-contained HTML page built from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`.
   - Save it to `design-thinking/<skill-name>-<topic-slug>.html` at the user's project root.
   - Publish it as an artifact when the session has an Artifact tool.
   - Use the template's components and don't restyle it.
   - Every page embeds an `#edt-data` JSON block. The next activity reads that block, not the HTML.
2. **Simulated users.** When an activity needs users, Claude simulates them. It follows `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`, using or creating the shared panel at `design-thinking/simulated-users.html`, and runs the activity's user-facing steps with those personas. Real research the user provides always comes first, and simulation fills the gaps.
3. **Provenance on every item.** Each note, dot or pill carries a `data-tag`:
   - `evidence`: real and observed, with its source
   - `simulated`: from a simulated user, with the persona ID
   - `assumption`: something the team believes
   - `question`: an open unknown

   Simulated items never become evidence. The simulated banner stays on any page that contains them.
4. **Two modes.**
   - **Co-create** is the default. Claude runs the whole activity with the user, using the workspace, the files the user points to, and simulated users.
   - **Facilitate** applies when the user mentions a workshop or session, or passes `facilitate`. Claude produces a facilitator kit page with an agenda, prompts, materials and an empty board. After the session, it turns photos or exports into the results page.
5. **End with a Playback.** Every page ends with three parts: key takeaways, what to validate next (simulated and assumed claims first), and the recommended next activity.
6. **Respect the source.** Paraphrase the IBM toolkit decks instead of pasting them, and link the deck in the skill and on the page.
7. **Cross-reference by command.** Point to other activities by their slash command, such as `/edt-plan:hills`.

## SKILL.md template

````markdown
---
name: <skill-name>
description: <One or two sentences: what the activity produces (an HTML artifact), then "Use when …" with concrete triggers. 500 characters or fewer.>
argument-hint: "[topic or user] [facilitate]"
---

# <Activity Name>

> IBM Enterprise Design Thinking · <Toolkit category> · <Loop phase(s)> · ~<N> min

<Why this activity exists, in one paragraph.>

## When to use it
- …

## Inputs
- From `design-thinking/`: … (read their `#edt-data` blocks)
- The simulated user panel, `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- Ask the user only for what you can't infer or simulate: …

## Co-create with Claude
1. … (numbered steps that follow the deck's phases, including where and how simulated users take part)

## Facilitate a live session
- Agenda with timings · prompts to read aloud · materials · board layout → a kit page

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/<skill-name>-<topic>.html`.
- **Title:** …
- **Sections:** … (which components each uses)
- **`content` in `#edt-data`:** … (the activity's own data shape)

## Quality checks
- … (what good looks like, plus common pitfalls, including simulation pitfalls)

## Next
- `/<plugin>:<skill>`: why it comes next

## Source
[IBM Enterprise Design Thinking Toolkit: <Activity>](<deck URL>)
````
