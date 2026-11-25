---
name: knowledge
description: Runs AI Essentials Knowledge, step 5 of an IBM AI strategy, as an HTML artifact. Maps who an AI could affect, adds simulated decision subjects, bystanders and non-users who describe impacts in their own words, runs six ethics lenses over three horizons, ranks risks and makes a Go/Go with conditions/Rework/Stop call. Use when someone asks "what could go wrong with this AI?", "is our AI fair?", "who could this AI harm?" or wants an AI impact or responsible-AI review.
argument-hint: "[topic or reasoning statement] [facilitate]"
---

# AI Essentials: Knowledge

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

An AI's knowledge doesn't stay inside the product. What it learns, infers and recommends reaches users, the people its decisions are about, the organization and wider society, and it keeps changing as the system learns from use. In Knowledge, the team looks past the intended benefits to the unintended effects. It decides who could be harmed and what to do about it before building, while changing course is still cheap. The people most affected are rarely in the room, so Claude simulates them: decision subjects, bystanders, non-users and the people in the training data each describe, in their own words, what the AI would do to their lives. Those voices sharpen the review, and they are prompts for real consultation, not a substitute for it.

## When to use it
- After `/edt-ai:reasoning`, once there is a scoped big idea and a reasoning statement.
- Before a pilot, launch or scale-up of any AI feature that makes or shapes decisions about people.
- When a stakeholder, regulator or user raises a concern about fairness, privacy or trust.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - `reasoning-*` (required): `content.statement`, `content.capabilities` and `content.wrong_answer_tests`
  - `understanding-*`: `content.risks` and the components marked `protected` or `proxy`
  - `data-*`: User sources, their consent basis, and `content.comfort`
  - `intent-*`, `stakeholder-map-*` and `empathy-map-*`

  Older `.md` versions are fine; read them as text. If there's no reasoning statement, write a provisional one with the user and tag it `assumption`, or run `/edt-ai:reasoning` first.
- **Files the user points to,** such as policies, regulations, incident reports or complaints. These are real evidence.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. This activity adds affected people to it.
- **Ask the user only for:** who the AI makes decisions *about*, the deployment context, and applicable policies or regulations, when the upstream pages don't say.

## Co-create with Claude
1. **Set up.** State the reasoning statement at the top. Give the team a mandate to look for harm, not just benefit. Build a source list: `S1…` for real sources and `SU-…` for every persona who speaks in this review.
2. **Map who is affected.** List every group:
   - **direct users**
   - **decision subjects:** people the AI judges or recommends about
   - **operators:** workers whose job changes
   - **bystanders and non-users**
   - **people represented in the training data**
   - **society**

   For each group, record its voice in the room: real people, simulated only, or none. Consider vulnerable groups explicitly: minors, people with disabilities, low digital literacy, marginalized communities.
3. **Add the affected people to the panel.** For every group except society that has no real voice, add 1–2 personas to `design-thinking/simulated-users.html`, following the panel protocol (or use `/edt-core:simulated-users`). Give each one a `relationship` field (`decision subject`, `operator`, `bystander`, `non-user` or `in training data`) and the group it speaks for, and show the relationship on its card. Build each from specific circumstances and constraints, not from a stereotype of the group. Some affected people don't know the AI exists, and some don't care; include them. Republish the panel.
4. **Brainstorm impacts.** For each group, list positive and negative effects, intended and unintended, on three horizons:
   - **now:** at launch
   - **at scale:** with millions of uses
   - **over time:** as the AI learns from use

   Ask the user first, then add effects they missed, tagged `assumption`. Useful provocations:
   - "What if it's wrong?"
   - "What if it works too well?"
   - "What if someone uses it in a way we didn't intend?"
   - "What do people stop doing because the AI does it?"
5. **Hear from the affected people.** Run a short session with each affected persona, and with 1–2 user personas. Run **one persona at a time**, in character, following the role-play rules in `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Describe the AI in plain words and let them tell it their way:
   - Decision subjects: "Last time a decision like this was made about you, what happened? Now a system makes it. What happens next in your life?"
   - Bystanders and non-users: "You never use it, but <how it reaches you>. What changes for you?"
   - People in the training data: "Your <records, calls or posts> were used to teach it. How do you feel about that?"
   - Everyone: "What would you want to know? If it got it wrong about you, what would you do, and who would you go to?"
   Let them be angry, resigned, indifferent or unaware. Record each session as a transcript. Each impact they describe is a `simulated` note with the persona ID, placed on its horizon.
6. **Stress-test with ethics lenses.** These are drawn from IBM's AI ethics focus areas and pillars of trust:
   - **Fairness and bias:** Does it perform equally well across groups? Could the data or proxies flagged in Understanding produce unequal outcomes? How will you measure that?
   - **Explainability and transparency:** Can users and decision subjects tell that AI is involved, why it produced an output, and how confident it is?
   - **Privacy and user data rights:** Is data used only with consent and only for this purpose? Can people see, correct or delete their data, or opt out?
   - **Robustness and misuse:** How does it fail under unusual inputs, manipulation or adversarial use? Who could weaponize it, and how?
   - **Accountability and oversight:** Who owns its outcomes? Can a person review, override or appeal a decision? Who is told when something goes wrong?
   - **Value alignment and wider effects:** Does it reflect the values of the users and communities it serves? What does it do to jobs, skills, dependence and the environment?
7. **Examine how its knowledge changes.** What does the AI learn from use? Could feedback loops reinforce bias, for example by recommending more of what it already recommended? Who reviews model or knowledge updates, and how will you detect drift?
8. **Prioritize.** Rate each negative impact from 1 to 3 on **severity**, **likelihood** and **reversibility** (1 easily undone, 3 irreversible), and rank by their product. Irreversible harm to vulnerable groups ranks first, however unlikely it is. Likelihood is the team's estimate, never the number of personas who raised it.
9. **Commit.** For each top risk, record:
   - a mitigation: design change, data change, human review, guardrail, disclosure, or not building that part
   - an owner
   - a signal to monitor after launch

   Plan real consultation for every group voiced only by simulation: who to talk to (people from the group, advocacy groups, sponsor users), how, and before which milestone. Then make the call: **Go**, **Go with conditions**, **Rework** (back to Reasoning or Intent), or **Stop**. If the top risks rest only on simulated voices, the call is at most Go with conditions, and that consultation is one of the conditions. Set any red lines, meaning uses the team won't support.
10. **Playback.** State the call and the two or three risks that drove it. Put the harms that rest only on simulated voices at the top of "Validate next", each with its consultation step. Then publish the page.

## Facilitate a live session
Produce `design-thinking/knowledge-<topic>-kit.html`. It needs:
- **Team:** diverse, empowered teams catch more harms. Include people with different backgrounds and roles, plus a sponsor user or an advocate for affected groups, and someone from legal, privacy or ethics if possible.
- **Agenda table (60 min):**
  - 0–5 Read the reasoning statement aloud and set the mandate
  - 5–10 Map who is affected
  - 10–25 Brainstorm impacts silently, then post them in the rings
  - 25–40 Lens pass, with pairs taking one or two lenses each
  - 40–50 Dot-vote the top risks
  - 50–60 Mitigations, owners and the call
- **Prompts to read aloud:**
  - "Who is affected by this AI but not in this room?"
  - "Imagine the headline if this goes wrong. What does it say?"
  - "Who gets a worse answer from this system than everyone else?"
  - "If a person disagrees with the AI's decision about them, what can they do?"
  - "What would we refuse to let this be used for?"
- **Materials:** a wall or digital whiteboard, sticky notes in two colors (positive and negative), thick markers and dot stickers.
- **Board layout:** the reasoning statement at the center, with concentric rings outward: Users → Decision subjects and operators → Organization → Society. Beside it, an empty *Now / At scale / Over time* `.cols` board, a panel with the six lenses, and an empty risk table.
- **Affected voices:** optionally run the simulated sessions before the workshop and bring each affected persona's words as a card, labeled simulated, to put the absent groups on the wall. Say aloud that they stand in for people the team still has to consult.

After the session, read the photos or the whiteboard export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/knowledge-<topic>.html`.
- **Title:** `<Topic> AI Knowledge`, for example "Claims Triage AI Knowledge". The `h1` is "AI Essentials: Knowledge" with the topic in `.topic`.
- **Sections:**
  1. **Under review:** the reasoning statement as a `.stmts` block with its labeled parts, and a source pill for the reasoning page.
  2. **Who is affected:** a table of group, relationship, vulnerable or not, voice in the room, and persona IDs. Show the voice as a pill: `evidence` for real people, `simulated` for simulated only, `question` for none. Follow it with a `.personas` block holding a card for each affected person added in this activity, with the relationship in `.role`.
  3. **Impacts over time:** `.cols` with *Now*, *At scale* and *Over time*. Each impact is a tagged note whose text starts with the group and sign, such as "Decision subjects · −". Quote the affected personas in their own words, with the persona ID in `.src`.
  4. **Ethics lens review:** a table with one row per lens: finding, a risk pill (`data-tone="good"` low, `"warn"` medium, `"bad"` high) and a tag pill.
  5. **How its knowledge changes:** `.cols` with *Learns from*, *Feedback-loop or drift risk* and *Update review by*, holding tagged notes.
  6. **Risk ranking:** a table of rank, risk, who is harmed, severity, likelihood, reversibility, score (`td.num` for the numbers), mitigation, owner, signal to monitor, and a tag pill.
  7. **Decision:** the call as a verdict pill (`data-tone="good"` Go, `"warn"` Go with conditions, `"bad"` Rework or Stop) with the reason, the conditions, the red lines as a list, and the human oversight and appeal path. Then a consultation plan table of group, voiced by, who to consult, how, before which milestone, and owner.
  8. **Simulated sessions:** a `details.transcript` per persona.
  9. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "statement": { "text": "", "source": "design-thinking/reasoning-<topic>.html" },
    "groups": [{ "id": "G1", "name": "", "relationship": "decision subject", "vulnerable": true, "voice": "simulated", "personas": ["SU-7"] }],
    "impacts": [{ "note": "N12", "group": "G1", "sign": "-", "intended": false, "horizon": "scale" }],
    "lenses": [{ "lens": "fairness", "finding": "", "risk": "high", "tag": "assumption" }],
    "knowledge_change": { "learns_from": "", "loop_risk": "", "review_by": "" },
    "risks": [{ "rank": 1, "text": "", "groups": ["G1"], "severity": 3, "likelihood": 2, "reversibility": 3, "score": 18, "mitigation": "", "owner": "", "signal": "", "impacts": ["N12"] }],
    "decision": { "call": "Go with conditions", "why": "", "conditions": [""], "red_lines": [""], "oversight": "" },
    "consultation": [{ "group": "G1", "voiced_by": ["SU-7"], "consult": "", "how": "", "before": "pilot", "owner": "" }] }
  ```
  `relationship` is `user`, `decision subject`, `operator`, `bystander`, `non-user`, `in training data` or `society`. `voice` is `real`, `simulated` or `none`. `horizon` is `now`, `scale` or `over_time`. `items` holds every impact and lens note, with `group` set to `"<Horizon> / <group>"` or `"Lens / <lens>"`.

## Quality checks
- Decision subjects and non-users are listed, not only the people who use the product.
- Every lens has a real finding. "N/A" needs a reason.
- Every sensitive or proxy component from Understanding shows up in the fairness review.
- Every top risk has a mitigation, an owner and a post-launch signal. "We'll be careful" is not a mitigation.
- There's a path for a person to contest or override decisions that matter to them.
- Simulated harm voices are prompts for real consultation, not a substitute for it. Every group voiced only by simulation has a line in the consultation plan, and no simulated harm is tagged `evidence`. Harms stay `simulated` or `assumption` until the people affected confirm them.
- Affected personas are specific people in specific circumstances, not stereotypes of a vulnerable group. Check them for clichés, and don't write personas who exist only to suffer.
- The affected personas sound different from each other and from the users. If they all object in the same words, or none of them objects at all, rerun the sessions with more realistic variety.
- Likelihood comes from the team's judgment and real data, not from how many personas raised a harm. Persona counts are never percentages.
- Pitfall: a review that only lists benefits, or one held after the build when changing course is expensive.

## Next
- `/edt-ideate:speculative-design-stories`: explore longer-term futures this AI could create, for better or worse.
- `/edt-plan:assumptions-and-questions`: turn the riskiest impact assumptions into tests.
- `/edt-core:sponsor-users`: recruit real people from the affected groups for the consultation plan.
- `/edt-align:playbacks`: play the AI strategy and its risks back to stakeholders and sponsor users.
- `/edt-ai:intent`: revisit the intent if the call was Rework or Stop.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Knowledge](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac23). The toolkit describes this activity as brainstorming the impact your AI can have on people and the world. When this skill was written, that link served the Understanding deck, so the steps here are adapted from that description and IBM's published AI ethics guidance.
