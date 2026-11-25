---
name: knowledge
description: Run AI Essentials Knowledge, step 5 of an IBM AI strategy. Explores the effects an AI could have on people and society, intended and unintended, including bias, fairness, explainability, privacy and misuse, and who could be harmed. Ends in mitigations and a go/adjust/stop call. Use when someone asks "what could go wrong with this AI?", "is our AI ethical or fair?", "who could this AI harm?", or wants an AI impact or responsible-AI review.
argument-hint: "[topic or reasoning statement] [facilitate]"
---

# AI Essentials: Knowledge

> IBM Enterprise Design Thinking · Define your AI strategy · Reflect · ~60 min

An AI's knowledge doesn't stay inside the product. What it learns, infers and recommends reaches users, the people its decisions are about, the organization and wider society, and it keeps changing as the system learns from use. In Knowledge, the team looks past the intended benefits to the unintended effects. It decides who could be harmed and what to do about it before building, while changing course is still cheap. A focus on user outcomes includes the outcomes nobody intended.

## When to use it
- After `/edt-ai:reasoning`, once there is a scoped big idea and a reasoning statement.
- Before a pilot, launch or scale-up of any AI feature that makes or shapes decisions about people.
- When a stakeholder, regulator or user raises a concern about fairness, privacy or trust.

## Inputs
- From `design-thinking/`: `reasoning-*` (required), `understanding-*` (association risks and sensitive components), `data-*` (User data and consent), `intent-*`, `stakeholder-map-*`, `empathy-map-*`.
- Ask the user for: who uses the AI, who it makes decisions *about*, the deployment context, applicable policies or regulations, and any incidents or complaints so far.
- If there's no reasoning statement, write a provisional one with the user and tag it **Assumption**, or run `/edt-ai:reasoning` first.

## Co-create with Claude
1. **Set up.** State the reasoning statement at the top. Give the team a mandate to look for harm, not just benefit.
2. **Map who is affected.** List every group:
   - **direct users**
   - **decision subjects:** people the AI judges or recommends about
   - **operators:** workers whose job changes
   - **bystanders and non-users**
   - **people represented in the training data**
   - **society**
   Mark which groups have a voice in the room. Groups without one need a proxy or outreach. Consider vulnerable groups explicitly: minors, people with disabilities, low digital literacy, marginalized communities.
3. **Brainstorm impacts.** For each group, list positive and negative effects, intended and unintended. Think on three horizons:
   - **now:** at launch
   - **at scale:** with millions of uses
   - **over time:** as the AI learns from use
   Ask the user first, then add effects they missed and tag them **Assumption**. Useful provocations:
   - "What if it's wrong?"
   - "What if it works too well?"
   - "What if someone uses it in a way we didn't intend?"
   - "What do people stop doing because the AI does it?"
4. **Stress-test with ethics lenses.** These are drawn from IBM's AI ethics focus areas and pillars of trust:
   - **Fairness and bias:** Does it perform equally well across groups? Could the data or proxies flagged in Understanding produce unequal outcomes? How will you measure that?
   - **Explainability and transparency:** Can users and decision subjects tell that AI is involved, why it produced an output, and how confident it is?
   - **Privacy and user data rights:** Is data used only with consent and only for this purpose? Can people see, correct or delete their data, or opt out?
   - **Robustness and misuse:** How does it fail under unusual inputs, manipulation or adversarial use? Who could weaponize it, and how?
   - **Accountability and oversight:** Who owns its outcomes? Can a person review, override or appeal a decision? Who is told when something goes wrong?
   - **Value alignment and wider effects:** Does it reflect the values of the users and communities it serves? What does it do to jobs, skills, dependence and the environment?
5. **Examine how its knowledge changes.** What does the AI learn from use? Could feedback loops reinforce bias, for example by recommending more of what it already recommended? Who reviews model or knowledge updates, and how will you detect drift?
6. **Prioritize.** Rate each negative impact on severity, likelihood and reversibility. Name the top risks. Irreversible harm to vulnerable groups ranks first, however unlikely it is.
7. **Commit.** For each top risk, record:
   - a mitigation: design change, data change, human review, guardrail, disclosure, or not building that part
   - an owner
   - a signal to monitor after launch
   Then make the call: **Go**, **Go with conditions**, **Rework** (back to Reasoning or Intent), or **Stop**. Set any red lines, meaning uses the team won't support.
8. **Write the artifact** and the Playback.

## Facilitate a live session
- **Team:** diverse, empowered teams catch more harms. Include people with different backgrounds and roles, plus a sponsor user or an advocate for affected groups, and someone from legal, privacy or ethics if possible.
- **Materials:** a wall or digital whiteboard, sticky notes in two colors (positive and negative), thick markers, and dot stickers.
- **Board layout:** write the reasoning statement at the center. Draw concentric rings outward: Users → Decision subjects and operators → Organization → Society. Post impacts in the ring where they land. Set aside a side panel with the six lenses, and a "Top risks → Mitigation → Owner" table.
- **Agenda (60 min):**
  - 5 min: read the reasoning statement aloud and set the mandate.
  - 5 min: map who is affected.
  - 15 min: brainstorm impacts silently, then post them in the rings.
  - 15 min: lens pass, with pairs taking one or two lenses each.
  - 10 min: dot-vote the top risks.
  - 10 min: mitigations, owners and the go/adjust/stop call.
- **Prompts to read aloud:**
  - "Who is affected by this AI but not in this room?"
  - "Imagine the headline if this goes wrong. What does it say?"
  - "Who gets a worse answer from this system than everyone else?"
  - "If a person disagrees with the AI's decision about them, what can they do?"
  - "What would we refuse to let this be used for?"
- **Capture:** photograph the rings and the risk table, then ask Claude to digitize them into the template below.

## Output
Save to `design-thinking/knowledge-<topic>.md`:

```markdown
# AI Essentials: Knowledge: <topic>

## Reasoning statement under review
**…** (reasoning-<topic>.md)

## Who is affected
| Group | Relationship (user / decision subject / operator / bystander / in training data / society) | Vulnerable? | Voice in the room? | Tag |
| --- | --- | --- | --- | --- |

## Impact map
| Impact | Group | + / − | Intended? | Horizon (now / scale / over time) | Tag |
| --- | --- | --- | --- | --- | --- |

## Ethics lens review
| Lens | Finding | Risk (low / med / high) | Tag |
| --- | --- | --- | --- |
| Fairness and bias | | | |
| Explainability and transparency | | | |
| Privacy and user data rights | | | |
| Robustness and misuse | | | |
| Accountability and oversight | | | |
| Value alignment and wider effects | | | |

## How the AI's knowledge changes over time
- Learns from: … · Feedback-loop or drift risk: … · Update review by: …

## Top risks and mitigations
| Risk | Who is harmed | Severity | Likelihood | Reversible? | Mitigation | Owner | Signal to monitor |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Decision
- Call: Go / Go with conditions / Rework / Stop, because …
- Red lines: …
- Human oversight and appeal path: …

## Playback
- Key takeaways: (3–5)
- Assumptions and questions to validate: …
- Next activity: …
```
Tags: `Evidence: <source>`, `Assumption`, or `Question`.

## Quality checks
- Decision subjects and non-users are listed, not only the people who use the product.
- Every lens has a real finding. "N/A" needs a reason.
- Every sensitive or proxy component from Understanding shows up in the fairness review.
- Every top risk has a mitigation, an owner and a post-launch signal. "We'll be careful" is not a mitigation.
- There's a path for a person to contest or override decisions that matter to them.
- Harms to affected groups are **Assumptions** until checked with those people. Plan to validate them.
- Pitfall: a review that only lists benefits, or one held after the build when changing course is expensive.

## Next
- `/edt-ideate:speculative-design-stories`: explore longer-term futures this AI could create, for better or worse.
- `/edt-plan:assumptions-and-questions`: turn the riskiest impact assumptions into tests.
- `/edt-align:playbacks`: play the AI strategy and its risks back to stakeholders and sponsor users.
- `/edt-ai:intent`: revisit the intent if the call was Rework or Stop.

## Source
[IBM Enterprise Design Thinking Toolkit: AI Essentials: Knowledge](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac23). The toolkit describes this activity as brainstorming the impact your AI can have on people and the world. When this skill was written, that link served the Understanding deck, so the steps here are adapted from that description and IBM's published AI ethics guidance.
