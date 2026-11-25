---
name: hills
description: Write IBM Enterprise Design Thinking Hills, which are up to three Who / What / Wow statements of meaningful user outcomes plus a Foundation, each traced to user needs and a sponsor user. Use when a team says "write our Hills", "define the mission or north star", "turn these needs into goals", "what are we really trying to do for users", or is kicking off a project or release. Also use to review or tighten existing Hills.
argument-hint: "[project or user] [facilitate]"
---

# Hills

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~60 min

A team that doesn't agree where it's going rarely gets there. Hills are statements of intent written as meaningful user outcomes. Each one says who gets the outcome, what they can now do, and why that's remarkable, which is the user and market value. Hills describe what a user is enabled to do, never how the team will build it. That leaves the team room to find breakthrough ideas and gives stakeholders one sentence to rally behind. The classic example is JFK's 1961 goal: land a man on the Moon and return him safely to Earth before the decade is out. It names a who and a measurable what and wow, and says nothing about the rocket.

## When to use it
- At the start of a project, release or initiative, once you understand the users' real problems.
- When the team has needs statements and must turn them into goals it can commit to.
- When a roadmap or backlog has drifted into a feature list and nobody can say which user outcome it serves.
- To review existing Hills before a Hills Playback.

## Inputs
- Upstream artifacts in `design-thinking/`: `needs-statements-*` (the main input), `empathy-map-*`, `as-is-scenario-map-*`, `sponsor-users-*`, `stakeholder-map-*`, and any earlier `hills-*`.
- What to ask the user for if missing: the target user, the problem as users experience it, any business or market context such as competitors, targets or deadlines, and who the sponsor users are. If there are no needs statements, suggest `/edt-synthesize:needs-statements` first. If the user wants to go ahead anyway, tag every Who and What as an **Assumption**.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream artifacts. Restate the user, their top needs and the pain points in a short list, and tag each item as **Evidence** (with its source file), **Assumption** or **Question**. Confirm the scope with the user: one product, one release or one initiative.
2. **Set up Who / What / Wow.** Make three columns. Explain them briefly:
   - **Who:** a specific user or user group, described by role and situation.
   - **What:** what they'll be able to do that they can't do today. It's an outcome, not a feature.
   - **Wow:** what makes it remarkable, measurable and different from what the market offers today.
3. **Diverge on each column separately.** Propose 5–8 options per column, drawn from the evidence, and ask the user to add theirs. Go for quantity over quality. If an option names a technology, a screen or a component, rewrite it as an outcome and point out the change.
4. **Build sentences.** Mix and match options into 3–6 draft Hills using the pattern *Who* can *What* *Wow*. Try unexpected combinations as well as the obvious ones.
5. **Stress-test each draft** against the Quality checks. Be blunt. Show a short verdict per draft, such as "What is an implementation" or "Wow isn't measurable", with a suggested rewrite.
6. **Converge.** Keep no more than three Hills. Move technical groundwork, platform work and fixes the Hills depend on into a **Foundation**. A Foundation isn't a fourth Hill. Split any Hill that's too big to deliver or test into Sub-Hills that share its Who. Name at least one sponsor user per Hill, or record a Question and suggest `/edt-core:sponsor-users`.
7. **Define the Wow measure.** For each Hill, record a metric, a baseline and a target. Mark the baseline as Evidence only if someone measured it. Otherwise it's an Assumption.
8. **Refine with fresh eyes.** Do a cold read: restate each Hill in your own words as an outsider would, including what you'd assume the team is building, and ask whether that matches the intent. Recommend that someone outside the team reads the Hills too. Hills evolve as understanding grows, so set the status to draft.
9. **Tag and play back.** Label anything in a Hill that is a belief rather than a fact. Being in a Hill doesn't make it true. Write the Playback section, then save the artifact.

## Facilitate a live session
**Agenda (60 min)**
| Time | Step | What happens |
| --- | --- | --- |
| 0:00 | Intro | Why Hills, the JFK example, the rules: write before you talk, yes-and, parking lot |
| 0:05 | Set up | Draw Who / What / Wow. Post the needs statements where everyone can see them |
| 0:10 | Ideate | 4 min of silent writing per column, then a quick share. Quantity over quality |
| 0:25 | Build | Small groups mix and match stickies into 2–3 Hill sentences each |
| 0:40 | Refine | Groups swap drafts and critique them against the quality checks |
| 0:50 | Playback | Read each Hill aloud, dot-vote down to no more than three, name sponsor users and Foundation items, flag assumptions |

**Prompts to read aloud**
- Who: "Who exactly are we doing this for? Give me a role and a situation, not 'users'."
- What: "What will they be able to do that they can't do today? Say it without naming a feature."
- Wow: "How will we know it's remarkable? What number would change, and why would the market notice?"
- Refine: "If you'd never seen this project, what would you think this Hill asks us to build?"

**Materials:** sticky notes in three colors (one per column) plus a fourth color for assumptions, markers, dot stickers, a timer, and printed needs statements.

**Board layout** (wall or a Mural frame per group): three tall columns labelled Who | What | Wow. Below them, a wide "Hill drafts" strip. On the right, a "Foundation" box and a "Parking lot".

**After the session:** ask for photos or a board export, then digitize the results into the Output template. Ask which drafts were rejected and why, and record them in the template.

## Output
Save to `design-thinking/hills-<topic>.md` using this template:

```markdown
# Hills: <project>
Status: draft | played back on <date> · Team: <names>

## Context
- Users: <who, with source>
- Needs addressed: <needs statements, each tagged Evidence / Assumption, with source file>
- Market context: <what users get today, competitors, constraints>

## Hill 1: <short name>
- **Who:** …
- **What:** …
- **Wow:** …
> <Who> can <What> <Wow>.
- Needs it serves: …
- Sponsor user(s): <name or "Question: not yet recruited">
- Wow measure: metric · baseline (Evidence / Assumption) · target
- Sub-Hills (optional): …
- Assumptions: … · Questions: …

## Hill 2: <short name>
…

## Hill 3: <short name>
…

## Foundation
- <technical groundwork or fix the Hills depend on, and which Hill needs it>

## Drafts we rejected
- <draft>: <why, for example "describes an implementation">

## Playback
- Key takeaways: <3–5 bullets>
- Assumptions and questions to validate: …
- Next activity: …
```

## Quality checks
- **Who is specific.** "Users", "customers" or "everyone" fails. A good Who reads like "a first-time claims adjuster at a mid-size insurer".
- **What is an outcome, not an implementation.** Reject anything that names a UI, a technology or a component, such as "via a dashboard", "using AI" or "a mobile app". Test it by asking whether three very different solutions could satisfy it. If only one could, it's an implementation.
- **Wow is measurable and differentiating.** Vague adjectives like "easily", "seamlessly" or "intuitively" fail. A good Wow has a number, a time or a before/after, and it beats what users can get today. If a competitor already delivers it, it's not a Wow.
- **Every Hill traces to at least one needs statement.** A Hill with no need behind it is the team's wish, not the user's outcome.
- **No more than three Hills plus a Foundation.** More than three means the team hasn't chosen. Foundation items are enablers, not user outcomes.
- **Each Hill has at least one sponsor user** who can tell the team whether the Hill was met.
- **It fits in a sentence that a stakeholder can repeat** from memory after hearing it once.
- Hypothetical rewrites, for calibration only:
  - Weak: "Admins can manage users through a new React console." This is an implementation, the Who is vague, and there's no Wow.
  - Strong: "An IT admin at a 500-person company can onboard a new hire to every tool they need in under 10 minutes, without filing a ticket."

## Next
- `/edt-align:playbacks`: run a Hills Playback with stakeholders and sponsor users.
- `/edt-plan:assumptions-and-questions`: find out which assumptions in your Hills carry the most risk.
- `/edt-ideate:big-idea-vignettes` or `/edt-ideate:to-be-scenario-map`: generate ways to reach each Hill.
- `/edt-plan:experience-based-roadmap`: stage the Hills into near-term and long-term user outcomes.
- `/edt-plan:user-stories`: break a Hill into user tasks.
- `/edt-core:sponsor-users`: recruit a sponsor user for any Hill that has none.

## Source
[IBM Enterprise Design Thinking Toolkit: Hills](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac11)
