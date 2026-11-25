# IBM Design Thinking marketplace for Claude Code

This [Claude Code](https://code.claude.com) plugin marketplace turns [IBM Enterprise Design Thinking](https://www.ibm.com/training/enterprise-design-thinking/framework) into skills. It covers the framework (the Principles, the Loop and the Keys) and all 29 activities in the [EDT toolkit](https://www.ibm.com/training/enterprise-design-thinking/toolkit).

Every skill works in two modes:

- **Co-create** (the default): Claude works through the activity with you, using your research notes, transcripts, PRDs or code, and writes the resulting artifact.
- **Facilitate**: add `facilitate` to the command, and Claude prepares a kit for a live team session. The kit has an agenda with timings, prompts to read aloud, a board layout for a wall or Mural, and a capture template.

The skills share a `design-thinking/` folder in your project, so they build on each other. For example, `/edt-synthesize:needs-statements` reads your empathy maps, and `/edt-plan:hills` reads your needs statements.

## Install

```bash
claude plugin marketplace add barvhaim/ibm-design-thinking-marketplace

# Install the framework guide first, then the activity plugins you want:
claude plugin install edt-core@ibm-design-thinking
claude plugin install edt-synthesize@ibm-design-thinking
```

Or install all eight plugins at once:

```bash
for p in core gather synthesize plan ideate test align ai; do
  claude plugin install "edt-$p@ibm-design-thinking"
done
```

You can also browse and install from inside a session with `/plugin`.

## Plugins

| Plugin | Skills |
| --- | --- |
| **edt-core**: the framework | `guide` · `sponsor-users` · `workshop-planner` · `practice-check` |
| **edt-gather**: gather user data | `contextual-inquiry` · `interviews` |
| **edt-synthesize**: synthesize research | `empathy-map` · `as-is-scenario-map` · `needs-statements` · `stakeholder-map` |
| **edt-plan**: plan your work | `hills` · `assumptions-and-questions` · `prioritization-grid` · `experience-based-roadmap` · `research-plan` · `user-stories` |
| **edt-ideate**: generate new ideas | `big-idea-vignettes` · `to-be-scenario-map` · `storyboards` · `speculative-design-stories` |
| **edt-test**: test your ideas | `feedback-grid` · `cognitive-walkthrough` · `paper-prototypes` · `wireframes` |
| **edt-align**: align your team | `playbacks` · `hopes-and-fears` · `daily-syncs` · `retrospectives` |
| **edt-ai**: AI Essentials | `intent` · `data` · `understanding` · `reasoning` · `knowledge` |

You run a skill as `/<plugin>:<skill>`, for example `/edt-plan:hills`. You don't have to call skills by name, though. Claude also picks the right one when you describe what you need, for example "help me turn these interview notes into an empathy map".

## Where to start

```
/edt-core:guide we're kicking off a new onboarding experience for data scientists
```

The guide works out where you are in the Loop, checks which Keys you're missing, and recommends the next 1–3 activities.

Common paths:

- **From research to intent:** `empathy-map` → `as-is-scenario-map` → `needs-statements` → `hills` → `playbacks`
- **From intent to concept:** `big-idea-vignettes` → `prioritization-grid` → `to-be-scenario-map` → `storyboards`
- **Test:** `paper-prototypes` or `wireframes` → `cognitive-walkthrough` → `feedback-grid`
- **Delivery:** `experience-based-roadmap` → `user-stories`

## Develop

```bash
claude plugin validate .                      # validate the marketplace and every plugin
claude plugin marketplace add ./              # test locally
claude plugin install edt-core@ibm-design-thinking
```

Run `/reload-plugins` in a session to pick up your edits. For skill conventions and the SKILL.md template, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Attribution

Enterprise Design Thinking, its framework and its toolkit are © IBM Corporation. These skills paraphrase IBM's public materials and link to the original toolkit decks.

The skill files in this repository are licensed under [Apache-2.0](LICENSE). That license does not cover IBM's toolkit materials, which remain IBM's.
