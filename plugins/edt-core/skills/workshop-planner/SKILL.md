---
name: workshop-planner
description: Plan an IBM Enterprise Design Thinking workshop that chains several toolkit activities, from a 90-minute session to a multi-day event. Produces an agenda with timings, goals, a participant and role plan, materials, a board setup (wall or Mural) and a pre-work and follow-up checklist. Use when someone says "plan a design thinking workshop", "build an agenda", "we have a day with the team", "run a kickoff", or "facilitate a design jam".
argument-hint: "[goal] [duration] [in-person|remote]"
---

# Workshop planner

> IBM Enterprise Design Thinking · Framework · All Loop phases · 30–60 min to plan

A good EDT workshop moves through the Loop with a purpose: it observes or brings in evidence, reflects together, and makes something concrete before it ends. This skill combines toolkit activities into a realistic agenda and hands you facilitator kits for each one.

## Inputs
- From `design-thinking/`: whatever already exists, so the workshop builds on earlier work instead of repeating it.
- Ask the user for:
  - the outcome they need by the end, for example "agreed Hills", "a concept to test" or "a prioritized backlog"
  - the duration
  - in-person or remote, and which whiteboard tool for remote
  - the participants: number and roles
  - whether users or sponsor users can join
  - the evidence the team already has

## Co-create with Claude
1. **Pin the outcome.** Write a single line: "By the end, we will have ___." Every agenda block must serve it.
2. **Choose the activity chain.** Use [activities.md](../guide/activities.md) and the patterns below. Each activity's output should be the next one's input. Don't plan more activities than the time allows. Teams always run long.
3. **Size the time.** Start from each activity's suggested duration. Then add:
   - 10–15 min for the opening, norms and hopes and fears
   - a 10-minute break every 90 minutes
   - 5 min of transition between activities
   - a 15–30 min closing playback

   Remote sessions need about 25% more time and shorter blocks.
4. **Plan roles:**
   - **Facilitator:** keeps time and stays neutral.
   - **Co-facilitator:** captures notes and runs the parking lot.
   - **Decision-maker:** a sponsor or product owner who must be in the room for converge steps.
   - **Users or sponsor users:** join where the work needs evidence.
5. **Plan materials and the board.**
   - **In person:** sticky notes, Sharpies, dot stickers, large paper, painter's tape, a timer.
   - **Remote:** one board, with a frame per activity laid out left to right in agenda order. Also prepare a parking lot frame and a norms frame.
6. **Write pre-work and follow-up.**
   - **Pre-work:** research readouts, invitations, any homework.
   - **Follow-up:** digitize the walls into `design-thinking/`, assign owners, and schedule the next playback.
7. **Generate the kits.** For each activity, offer to run its skill in `facilitate` mode, for example `/edt-synthesize:empathy-map facilitate`, to get prompts and detailed steps.

## Typical chains

| Outcome | Chain |
| --- | --- |
| Kickoff and alignment (½ day) | Hopes and Fears → Stakeholder Map → Assumptions and Questions → Research Plan |
| From research to intent (1 day) | Empathy Map → As-is Scenario Map → Needs Statements → Hills → Hills Playback |
| From intent to concept (1 day) | Big Idea Vignettes → Prioritization Grid → To-be Scenario Map → Storyboards → Playback |
| Test and iterate (½ day) | Paper Prototypes or Wireframes → Cognitive Walkthrough with users → Feedback Grid |
| Vision to delivery (½ day) | Experience-based Roadmap → User Stories → Playback |
| AI strategy (1 day) | AI Essentials: Intent → Data → Understanding → Reasoning → Knowledge |
| Full design jam (3 days) | Day 1: from research to intent · Day 2: from intent to concept · Day 3: test and iterate, then roadmap |

## Output
Save to `design-thinking/workshop-plan-<topic>.md`:

```markdown
# Workshop: <title>
**Outcome:** By the end, we will have …
**When / where:** … · **Format:** in-person | remote (<tool>)
**Participants:** … · **Facilitator:** … · **Decision-maker:** …

## Agenda
| Time | Block | Activity / command | Output | Owner |
| --- | --- | --- | --- | --- |
| 09:00 | Opening | Norms, Hopes and Fears (`/edt-align:hopes-and-fears`) | Shared expectations | |

## Norms
Write before you talk · There are no bad ideas: diverge, then converge · Stay focused on users · Everyone participates · Use the parking lot · Yes, and…

## Materials and board
- …

## Pre-work
- [ ] …

## Follow-up
- [ ] Digitize outputs into `design-thinking/`
- [ ] Next playback: <date>

## Playback
- What the workshop should prove:
- Risks (time, missing people, missing evidence):
- Next activity after the workshop:
```

## Quality checks
- The agenda includes Observe or evidence, Reflect, and Make. If it's all discussion, add a Make activity.
- Converge steps happen while the decision-maker is in the room.
- Times add up, and the agenda includes buffer.
- Each block names the output it produces.

## Next
- Run each activity's skill in `facilitate` mode for its kit.
- `/edt-align:playbacks`: plan the closing playback story.

## Source
[IBM Enterprise Design Thinking Toolkit](https://www.ibm.com/training/enterprise-design-thinking/toolkit)
