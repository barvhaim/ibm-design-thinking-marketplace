---
name: sponsor-users
description: Find, recruit and work with Sponsor Users, one of the three Keys of IBM Enterprise Design Thinking. Produces a sponsor user profile, a recruiting screener, an outreach message and an engagement plan across the Loop. Use when a team asks "who should our sponsor users be", "how do we recruit users to work with us", or "how do we involve users throughout the project", or has Hills with no real user attached.
argument-hint: "[target user or Hill]"
---

# Sponsor Users

> IBM Enterprise Design Thinking · The Keys · Observe, Reflect and Make · ~45 min to plan, then ongoing

A sponsor user is a real-world user who regularly contributes their domain expertise to the team. This makes them a collaborator who comes back throughout the project, not a test subject you see once. With sponsor users involved, the team's work stays tied to the users' reality instead of the team's guesses about it.

## When to use it
- At project kickoff, before the first research.
- When Hills exist but no real user stands behind them. Aim for at least one sponsor user per Hill.
- When the team keeps saying "we think users want…" and nobody can check.

## Inputs
- From `design-thinking/`: any `hills-*`, `stakeholder-map-*`, `empathy-map-*` or `needs-statements-*` files.
- Ask the user for: the target user role(s), the domain, any access constraints (NDA, client approval, internal-only), and how often the team can engage.

## Co-create with Claude
1. **Define who.** Draft a profile for each Hill or primary user role covering role, context, experience level, tools, and the decisions they make. Separate the **user** (who does the work) from the **client** or buyer (who pays).
2. **Apply the three criteria** to each candidate profile:
   - Do they represent the target user?
   - Are they personally invested in the outcome?
   - Are they available to collaborate on a regular cadence?
   Reject candidates who are "close enough", such as an internal colleague who used to do the job years ago, unless you label them as a stopgap.
3. **Write a screener** of 5–8 questions. The answers should confirm that someone matches the profile, without revealing which answer qualifies.
4. **Draft outreach.** Write a short message that explains:
   - why the team wants this person
   - the time commitment, for example 1 hour every 2 weeks
   - what they get in return: influence, early access, recognition
   - confidentiality terms
5. **Plan the engagement across the Loop:**
   - **Observe through their eyes:** contextual inquiry, interviews, shadowing.
   - **Reflect together:** invite them to synthesis sessions and to Hills and Playbacks.
   - **Make collaboratively:** co-sketch with them, test prototypes, review stories.
6. **Set up ethics and logistics:** consent, NDAs, who keeps the relationship, how the team closes the loop by telling sponsor users what changed because of them, and when to rotate in new people.

## Facilitate a live session
- **Recruiting workshop (45 min):**
  - 10 min: list target roles.
  - 15 min: everyone writes candidate names or sources on sticky notes, then clusters them.
  - 10 min: score each candidate on the three criteria.
  - 10 min: assign an owner and a first contact date to each.
- **Prompt to read aloud:** "Who would be upset if we got this wrong, and could we talk to them every two weeks?"

## Output
Save to `design-thinking/sponsor-users-<topic>.md`:

```markdown
# Sponsor Users: <project>

## Profiles
| Hill / role | Profile (role, context, experience) | Must have | Nice to have |
| --- | --- | --- | --- |

## Candidates
| Name / source | Representative? | Invested? | Available? | Owner | Status |
| --- | --- | --- | --- | --- | --- |

## Screener
1. …

## Outreach message
…

## Engagement plan
| Loop phase | Activity | Cadence | Next date |
| --- | --- | --- | --- |
| Observe | … | | |
| Reflect | … | | |
| Make | … | | |

## Logistics and ethics
- Consent / NDA:
- Relationship owner:
- How we close the loop:

## Playback
- Key takeaways:
- Assumptions to validate:
- Next activity:
```

## Quality checks
- Every Hill has at least one named sponsor user, or a dated plan to recruit one.
- Sponsor users are real people. Personas don't count.
- The engagement recurs. A single interview makes someone a research participant, not a sponsor user.
- The team has said what it gives back to the sponsor user, not only what it takes.

## Next
- `/edt-gather:interviews` or `/edt-gather:contextual-inquiry`: hold your first session with each sponsor user.
- `/edt-plan:hills`: check your Hills with your sponsor users.
- `/edt-align:playbacks`: invite sponsor users to your next playback.

## Source
[IBM Enterprise Design Thinking: The Keys](https://www.ibm.com/training/enterprise-design-thinking/framework)
