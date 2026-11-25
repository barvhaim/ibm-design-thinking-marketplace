---
name: storyboards
description: Turns one idea into a short comic-strip story, with a character, a setting and a plot, as an HTML artifact whose frames are drawn in ASCII or simple SVG. The main character is a persona from the simulated user panel, and afterward that persona and a skeptic react to the story. Use when someone says "storyboard this", "tell the story of our idea", "show how a user would use it" or "make a comic strip", or needs to share a future idea quickly in a Playback.
argument-hint: "[idea or user] [facilitate]"
---

# Storyboards

> IBM Enterprise Design Thinking · Generate new ideas · Make · ~20 min

Stories help people understand intuitively how an idea fits into a user's world, and giving a story visual form makes it easier for others to grasp, critique and build on. A storyboard is a comic strip of the user's future: a character, a setting, a plot and a handful of scenes. Drawing skill doesn't matter, because stick figures and speech bubbles are enough. Claude can't draw on paper, so it writes the frames and sketches each one roughly in ASCII or line art, which the team can redraw by hand. The character is a real member of the simulated panel, so once the story is told, that persona can say whether it sounds like their life, and a skeptic can say why it wouldn't work for them.

## When to use it
- You know the problem and the user, and you have one or more candidate ideas, for example from Big Idea Vignettes.
- To share a vision of the user's future quickly in a Playback or with Sponsor Users.
- To expose an idea's assumptions, because drawing the story forces you to decide what actually happens.
- To compare ideas: storyboard two or three alternatives, then converge on a shared vision.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - `big-idea-vignettes-*`: the chosen ideas, their vignettes and the simulated reactions
  - `to-be-scenario-map-*`: its phases are a strong spine for the plot, and its breaks are good twists
  - `needs-statements-*` and `hills-*`: the need the story addresses
  - `empathy-map-*` and `simulated-users.html`: the character's context, tools and voice
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:**
  - which idea to show, if several were chosen
  - whether a real Sponsor User has agreed to be the character
- If the problem and the user aren't known yet, it's too early. Suggest `/edt-synthesize:needs-statements` or `/edt-synthesize:empathy-map` first.

## Co-create with Claude
1. **Gather context.** Read the upstream pages. Name the need the story addresses, with its tag and source.
2. **Cast the character.** The main character is a persona from the panel. Pick the one whose life the idea most needs to work in, usually the persona the empathy map or to-be map was built on. Use their name, role, tools, habits and voice exactly as the panel records them, and cite their `SU-` ID. If nobody on the panel fits, add a persona with `/edt-core:simulated-users` (`add …`) rather than inventing a one-off. A real Sponsor User can be the character instead, with their permission; then their known traits are `evidence`. Also pick one skeptic or non-adopter from the panel to react later.
3. **Identify the story.** Propose the other two elements:
   - **Setting:** where and when the story happens, and what's around the character.
   - **Plot:** the problem, then the moment the character meets the idea, then the outcome.
4. **Diverge on storylines first.** Offer two or three one-line storylines before detailing any of them. Vary the idea, first use against repeat use, or a stressful edge case. Let the user choose one, or rough out all of them. Don't polish one favorite before the alternatives are on the table.
5. **Pick the scenes.** Choose 4–8 frames that show the plot developing from start to finish. Include the major events: a shift in setting, a new character arriving, or a twist where something goes wrong. A useful spine is context, trigger or problem, meeting the idea, using it, payoff, and new normal. Start before the idea appears, so the problem is visible in the character's life.
6. **Write the frames like a comic strip.** For each frame, give:
   - what we see, which becomes the sketch
   - a speech bubble and a thought bubble, in the character's own voice from the panel
   - a caption or narration
   - an action burst for key moments ("BUZZ!", "Done.")
   - the character's mood: high, low or mixed

   Show context and feelings. Draw screens only when they're essential, and keep them rough.
7. **Sketch each frame.** Use ASCII (stick figures, about 24 characters wide and 5–8 lines) or a small inline `<svg>` drawn with `stroke="currentColor"` and `fill="none"`, so it works in light and dark themes. Use no colors, images or external files. Rough is fine, and the team can redraw it by hand. [examples.md](examples.md) shows one frame of each kind.
8. **Label assumptions and questions** on the frame where they occur. For example: "She'd trust an automatic assignment" is an `assumption`, and "Who approves exceptions?" is a `question`.
9. **The character and the skeptic react.** Run each one separately, in character, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Tell them the story frame by frame in plain words.
   - **The character:** "Is this your day? What would you actually do at frame 3? Which part doesn't sound like you?"
   - **The skeptic:** "Why wouldn't this work for you? What would you do instead?"

   Let them be indifferent or annoyed, correct details of their own life, and refuse the premise. Record each reaction as a `simulated` note with the persona ID and the frame number, and keep the transcripts. If both of them love the story, rerun it with more friction.
10. **Iterate.** Read the story and the reactions back to the user, and ask: "Could this actually happen? What would make a real user doubt it?" The user decides which frames change. Record each change and the reaction that prompted it. The reactions sharpen the story, but they don't validate it.
11. **Playback.** Tell the story in under a minute, then say where it feels fragile. Put the riskiest labels and reactions at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/storyboards-<topic>-kit.html`. It needs:
- **Agenda table (20 min, plus about 2 min of Playback per person):**

  | Time | Step | Notes |
  |---|---|---|
  | 0–2 | Intro and norms | Read the problem and the user aloud · write before you talk · stay focused on the user |
  | 2–7 | Identify | Each person picks a character, a setting and a plot, then lists scenes on stickies |
  | 7–15 | Illustrate | Each person sketches their own storyboard, with bubbles, captions and bursts |
  | 15–20 | Label and iterate | Add assumption and question stickies, swap with a neighbor and ask "could this come true?", then refine |
  | then | Playback | Everyone plays back their storyboard, then the group converges |
- **Prompts to read aloud:**
  - "Who is our character, where are they, and what's happening in their day before our idea shows up?"
  - "Sketch it like a comic strip with stick figures, speech and thought bubbles, and captions. No art skills needed."
  - "Where's the twist? What could go wrong, and what happens next?"
  - "Put a sticky on anything you aren't sure is true."
  - Playback: "What elements show up across several stories? How might we combine our stories into one shared vision of the user's future? Which assumptions do we still need to validate?"
- **Materials:** printed six-frame sheets (or a storyboard frame per person in Mural), markers, sticky notes in a distinct color for assumptions and questions, and a timer. Print the character's persona card from the panel for every table.
- **The board:** the need as a `.stmts` banner, the character's `.persona` card, an empty six-frame `.frames` sheet with only the frame numbers, and `.cols` for common elements, shared vision, assumptions to validate, and the parking lot.

After the session, read the photos or the Mural export. Transcribe each storyboard frame by frame, redrawing the sketches as ASCII or SVG, and keep the labels. Record the common elements and the converged vision. Then run step 9 on the converged story before you build the results page.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/storyboards-<topic>.html`. [examples.md](examples.md) shows finished frames, reactions and a data block.
- **Title:** `<Idea> Storyboard`, for example "Ready Desk Storyboard".
- **Sections:**
  1. **The story:** the character's `.persona` card, copied from the panel with its `SU-` ID; a `.stmt` with the need it addresses and its source pills; and a lede with the setting and plot.
  2. **Storyboard:** one `.frames` grid, with one `figure.frame` per frame.
     - `.frame-art`: the ASCII or SVG sketch.
     - `.frame-n`: `Frame 3 · Twist`.
     - Caption: a `.mood`, the narration, the speech in quotes, the thought in parentheses, the burst in capitals, and a pill for each label on that frame.
  3. **Reactions:** `.cols` with one column for the character and one for the skeptic. Each holds `.note[data-tag="simulated"]` notes that start with the frame number, with `.src` set to `SU-2 · reaction`.
  4. **Assumptions and questions:** `.notes` tagged `assumption` or `question`, each naming its frame, followed by a table of the frame, the label, and how we might validate it.
  5. **What changed:** a table of the frame, the change, and the reaction that prompted it.
  6. **Alternatives considered:** the other storylines, one line each, with why they weren't chosen.
  7. **Reaction sessions:** a `details.transcript` per persona.
  8. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "idea": { "id": "I7", "headline": "", "source": "design-thinking/big-idea-vignettes-<topic>.html" },
    "need": { "text": "", "tag": "evidence", "source": "design-thinking/needs-statements-<user>.html" },
    "character": { "persona": "SU-2", "name": "", "role": "" }, "skeptic": "SU-4",
    "setting": "", "plot": { "problem": "", "encounter": "", "outcome": "" },
    "storylines": [{ "text": "", "chosen": true, "why": "" }],
    "frames": [{ "n": 1, "title": "", "art": "ascii|svg", "sees": "", "says": "", "thinks": "",
                 "caption": "", "burst": "", "mood": "high|low|mixed", "labels": ["N5"] }],
    "reactions": [{ "persona": "SU-2", "as": "character|skeptic", "frame": 3, "note": "N8" }],
    "changes": [{ "frame": 3, "change": "", "prompted_by": "N8" }] }
  ```
  `items` holds every note, with `group` set to `"Reactions / <persona>"` or `"Labels / Frame <n>"`.

## Quality checks
- The character, setting and plot are explicit, and the character is a panel persona with an `SU-` ID or a consenting Sponsor User.
- The story starts before the idea appears, and ends with the outcome for the user, not with a product launch.
- Every frame moves the plot forward, and there is at least one major event or twist. The mood dips somewhere.
- It shows experience, feelings and context. It isn't a UI walkthrough.
- Every frame has a sketch, and the SVGs use `currentColor` only.
- Assumptions and questions are labeled on their frames, and the user believes the story could come true.
- Someone outside the team understands it in under a minute.
- Simulation pitfalls:
  - a character and a skeptic who both love the story; the skeptic should object to something specific
  - a character who acts out of step with their own panel card, or who sounds like the skeptic
  - a reaction tagged `evidence`, or the story called validated because the character agreed
  - percentages from simulated counts
- Other pitfalls: a hero story where everything works perfectly, and treating one storyboard as the decision.

## Next
- `/edt-align:playbacks`: share the storyboard with stakeholders and Sponsor Users.
- `/edt-test:feedback-grid`: capture reactions, questions and new ideas from more users, real or simulated.
- `/edt-plan:assumptions-and-questions`: prioritize the labels and reactions for validation.
- `/edt-test:paper-prototypes`: make the key frame testable.
- `/edt-ideate:to-be-scenario-map`: expand the story into a full future experience.

## Source
[IBM Enterprise Design Thinking Toolkit: Storyboards](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9ac)
