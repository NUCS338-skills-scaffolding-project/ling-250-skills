---
assignment_id: ""
assignment_name: ""
course: ""
unit: ""
due_date: ""
total_points: 0
canvas_quiz: true
---

# Assignment Template

This is a reusable template for documenting a Ling 250 assignment in a
format the orchestrating tutor can read at session start. Copy this file,
rename it to `assignment.md` at the repo root (or inside an assignment-
specific folder), and fill in each section.

Sections marked **required** must be filled in for the tutor to function.
Sections marked *optional* improve the tutor's behavior but won't break it
if left empty.

---

## Assignment Name *(required)*
The student-facing name of the assignment (e.g., "HW1: Consonant
Articulation & IPA").

## Assignment Description *(required)*
One or two paragraphs describing what the student is being asked to do,
at the level of detail a student would get from the Canvas handout.
Include the deliverable format (Canvas quiz, written worksheet, etc.)
and any high-level constraints (no calculators, open-book, etc.).

## Unit / Days Covered *(required)*
Which class days and textbook chapters this assignment is assessing.
Example: "Days 2-3; Zsiga Ch. 2." This tells the tutor which slice of
the course material to draw on and which to stay out of.

## Learning Goals *(required)*
The concepts and skills this assignment is specifically designed to
develop. Write these as "students should be able to ___" statements.
The tutor keeps these in focus throughout a session.

Example (HW1):
- Recognize and describe the articulatory characteristics of English
  consonants in terms of place, manner, and voicing
- Recognize IPA symbols for English consonants and their associated
  sounds
- Transcribe short English words into IPA
- Distinguish IPA symbols that map easily to English letters from
  symbols with more challenging mappings

## Concepts Required *(required)*
Every concept a student needs to understand to complete this assignment.
This is the gating list used by `validate_pre_knowledge` and
`diagnose_prerequisite_gaps`: the tutor will not write or scaffold code
involving a concept that isn't in the student's profile.

List each concept on its own line. Mark concepts that are new for this
assignment with `[NEW]` and concepts from prior assignments with the
assignment where they were introduced.

Example (HW1):
- Vocal tract anatomy (larynx, glottis, cavities) [Day 1]
- Voicing: voiced vs. voiceless [Day 2]
- Place of articulation: bilabial, labiodental, dental, alveolar,
  post-alveolar, palatal, velar, glottal, labio-velar [NEW, Day 2]
- Manner of articulation: stop, fricative, affricate, nasal,
  approximant, lateral, tap [NEW, Day 2-3]
- IPA symbols for English consonants [NEW, Day 3]
- Orthography ≠ pronunciation [Day 1]

## Question Types *(required)*
The shapes of questions on the assignment. The tutor uses this to
anticipate what the student is working on. Add as many types as the
assignment contains.

Standard types (pick the ones that apply):
- **Multiple choice (single answer)**: student picks one option
- **Multi-select**: student picks all that apply ("select all the words
  that begin with a voiceless fricative")
- **Matching**: student pairs items from two lists (e.g., IPA symbols
  with their articulatory descriptions)
- **Articulatory diagram identification**: student matches a
  midsagittal drawing to the correct IPA symbol
- **IPA-to-English transcription**: given an IPA sequence, student
  writes the English word
- **English-to-IPA transcription**: given an English word, student
  produces the IPA
- **Feature manipulation**: given a sound and a feature change,
  student produces the resulting sound (e.g., "make [i] back and round
  → [u]")
- **Free-response short answer**: open-ended written response
- **True/false**: binary judgment with optional justification
- **Waveform / spectrogram reading**: student interprets a
  visualization

## Common Misconceptions *(required)*
Wrong mental models students typically bring to this assignment. The
tutor watches for these and addresses them through questioning rather
than direct correction. This section feeds the
`repair_misconceptions` skill.

For each, give:
- the misconception in one sentence
- a brief why-it's-wrong
- (optional) a Socratic prompt that surfaces the error

Pull from `context/misconceptions.md` for course-wide misconceptions
and add assignment-specific ones here.

## What Success Looks Like *(required)*
A conceptual description of a correct solution — not the answer key.
Helps the tutor recognize when the student is on track without
giving away the answer. For a Canvas quiz, this can be a short
description of the reasoning a correct student goes through, not the
specific answers they produce.

## What the Tutor Should NOT Do *(required)*
Assignment-specific constraints on the tutor. This section is the
tutor's guardrail. Be explicit.

Examples:
- Do not produce full IPA transcriptions of entire words for the
  student. The student must produce each symbol themselves.
- Do not explain acoustic concepts (waveforms, frequency) on this
  assignment — that's a later unit.
- Do not reference the Day 4 vowel chart when the student is working
  on consonants.

## Skills Relevant to This Assignment *(optional)*
A list of the skills from the skill catalog that are particularly
applicable to this assignment, with a one-line rationale for each.
Lets the orchestrator prioritize which skills to draw from.

Example (HW1):
- `give-contrastive-hint` — for Q5-10 (midsagittal matching) and
  Q11 (feature-based matching) when the student confuses two
  neighboring consonants
- `repair_misconceptions` — for Q1 (spelling vs. sound) and any
  mis-transcription driven by orthography
- `escalate_hint_level_gradually` — any question where a student is
  stuck
- `validate_pre_knowledge` — before starting the assignment
- `diagnose_prerequisite_gaps` — when the student is blocked

## Reference Materials *(optional)*
Links or paths to any course materials the tutor should draw on:
- Lecture slides (file paths or URLs)
- Readings (chapter + page ranges)
- Relevant context files in this repo
- External references (IPA chart, demo recordings)

## Notes for the Instructor *(optional)*
Anything else about this assignment that the tutor or a future team
should know — known gotchas, student patterns from past semesters,
edge cases to watch for.