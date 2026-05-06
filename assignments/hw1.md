# HW1: Consonant Articulation & IPA

## Assignment Name
HW1: Consonant Articulation & IPA

## Assignment Description
A Canvas quiz worth 40 points covering English consonant articulation and
the IPA. Students work through a mix of concept questions, multi-select
feature-based identification, midsagittal-diagram-to-symbol matching,
IPA-symbol-to-description matching, and IPA-to-English transcription.

Students complete the quiz individually, untimed, using course materials
as reference. The assignment is due before class on the first Tuesday of
the consonant unit per the syllabus.

## Unit / Days Covered
Days 2-3 of the course; Zsiga Ch. 2.

Day 1 anatomy and the IPA overview (from Day 1-2) are also prerequisite
and may be probed by `validate_pre_knowledge`.

## Learning Goals
Students should be able to:
- Describe the essential components of speech production: airstream,
  place, and manner
- Describe voicing and map voiced vs. voiceless sounds to vocal fold
  behavior
- Describe place-of-articulation distinctions for English consonants
  (bilabial through labio-velar)
- Describe manner-of-articulation distinctions for English consonants
  (stop, fricative, affricate, nasal, approximant, lateral, tap)
- Recognize IPA symbols for English consonants and their associated
  sounds
- Transcribe short English words into IPA, setting aside English
  orthographic conventions
- Read a midsagittal diagram and identify the consonant it represents
  from voicing, place, and manner cues
- Distinguish IPA symbols that map easily to English letters (p, b, t,
  d, k, m, n, s, z, f, v, l, h) from symbols with more challenging
  mappings (θ, ð, ʃ, ʒ, tʃ, dʒ, ŋ, ɹ, j, ʔ, ɾ, w)

## Concepts Required
- Vocal tract anatomy — larynx, glottis, velum, oral and nasal
  cavities, alveolar ridge, hard palate [Day 1]
- Three subsystems of the vocal tract — sub-laryngeal, laryngeal,
  supra-laryngeal [Day 1]
- Voicing — voiced vs. voiceless as vocal fold vibration vs. no
  vibration [Day 2]
- Place of articulation as the location of constriction [NEW, Day 2]
- Specific places: bilabial, labiodental, dental, alveolar,
  post-alveolar, palatal, velar, glottal, labio-velar [NEW, Day 2-3]
- Manner of articulation as the type/degree of constriction [NEW, Day 2]
- Specific manners: stop, fricative, affricate, nasal, approximant,
  lateral, tap [NEW, Day 2-3]
- Obstruent vs. sonorant as derived categories [NEW, Day 3]
- IPA symbols for the 26 English consonants [NEW, Day 3]
- Formal consonant description format: voicing + POA + manner, with
  predictable features omitted (e.g., [m] = "bilabial nasal") [NEW,
  Day 3 slide 18 — directly tested by Q11]
- IPA chart structure: columns are place, rows are manner, paired
  symbols in a cell differ in voicing (voiceless on the left) [NEW,
  Day 3 slides 19-20]
- One-sound-one-symbol principle of the IPA [Day 1]
- Orthography ≠ pronunciation [Day 1]
- Tap [ɾ] environment: appears between vowels with V1 stressed
  (butter, water, ladder) [NEW, Day 3 slide 30]
- IPA [r] is a trill, NOT the English r — English uses [ɹ] [Day 3
  slide 28]

## Question Types
- **Multiple choice (single answer)** — concept questions
  (Q2: definition of vowel; Q3: which term is a place of articulation;
  Q4: manner of [θ])
- **Multi-select** — "select all that apply" reasoning about spelling
  (Q1) and feature-based word identification (Q12–Q19: words that begin
  with / end with / contain a consonant matching a given feature)
- **Articulatory diagram identification** — student matches a
  midsagittal drawing to the correct IPA symbol using voicing, velum
  position, and constriction location (Q5–Q10)
- **IPA-symbol-to-feature-description matching** — student pairs IPA
  symbols with articulatory descriptions like "velar nasal" or
  "voiceless post-alveolar fricative" (Q11, worth 10 points)
- **IPA-to-English transcription** — given an IPA sequence, student
  writes the English word (Q20–Q31)

## Common Misconceptions

Course-wide misconceptions from `context/misconceptions.md` that are
especially relevant to HW1:

- **Spelling reflects pronunciation** — core to Q1 and to every IPA
  transcription question. Students often write the IPA symbol that
  matches the English *letter* rather than the *sound* (e.g., writing
  [c] instead of [s] for the first sound of *cell*, or [s] instead of
  [z] for the final sound of *raised*).
- **"Th" is one sound** — relevant to Q11 where both [θ] and [ð] appear
  and to any transcription with *th*.
- **"Ch" is a simple consonant, not an affricate** — Q4 tests this
  exact distinction; also relevant to Q18 (words ending in an affricate)
  and Q30 (transcription of *reached* → [ritʃt]).
- **"Y" is always a vowel** — relevant to Q22 (*yellow* → [jɛlo]) and
  to identifying [j] as a consonant.
- **Nasals involve only the nose** — relevant to Q5-Q10 midsagittal
  matching, especially Q7 ([m], bilabial nasal) where the student must
  recognize both the oral closure AND the lowered velum.
- **Voiceless sounds are silent** — relevant to every voicing question
  and to midsagittal questions where voicing is shown by the wavy vs.
  straight line.
- **[ŋ] is two sounds** — relevant to Q11 (velar nasal → [ŋ]) and any
  transcription of word-final *ng*.
- **English r is the IPA [r]** [NEW, Day 3] — relevant to any
  transcription with the English r sound. Students who write [r]
  instead of [ɹ] are using the trill notation; flag and redirect to [ɹ].
- **Doubled consonant letters spell doubled sounds** [NEW, Day 3] —
  relevant to Q26 (*wouldn't*) and to any transcription with medial
  *tt*, *dd* between vowels (*butter*, *water*, *ladder*). The student
  needs the tap [ɾ], not [t]/[d].
- **The IPA chart is just a list** [NEW, Day 3] — relevant to Q11
  (matching), where students who try to memorize symbols flat will
  struggle compared to students who navigate by feature.
- **Formal descriptions name all three features** [NEW, Day 3] —
  relevant to Q11 if the description in the prompt has a feature
  omitted (e.g., "bilabial nasal" without "voiced") and the student
  doesn't recognize it as a complete description.

Assignment-specific patterns to watch for:

- Students often confuse [θ] and [f] because they share voicing and
  manner — the only difference is place (dental vs. labiodental).
  Q4 probes this, and it's a prime target for `give-contrastive-hint`.
- Students often confuse [ʃ] and [s] because of spelling overlap
  (*ship*, *nation*, *special* all use [ʃ] but look different in
  spelling).
- In Q11 (the feature-to-symbol matching), students sometimes
  mis-match "glottal stop" — either forgetting [ʔ] exists or assigning
  it to a wrong symbol.
- In Q26 (*wouldn't* → [wʊdnʔ]), students typically miss the glottal
  stop at the end and write [t] instead.

## What Success Looks Like

A correct student:
- Treats each IPA symbol as a label for a sound, not for a letter
- When given an English word for transcription, speaks the word slowly
  and writes down what they *hear themselves saying*, not how they
  would spell it
- When reading a midsagittal diagram, works through the three features
  in order — voicing (wavy vs. straight line at the larynx), place
  (where the constriction is), manner (how complete the constriction
  is, velum position) — and arrives at the symbol that matches all three
- For feature-based "select all that begin/end/contain" questions,
  pronounces each word aloud (internally or externally) and checks the
  relevant feature for the target sound rather than relying on spelling
- For the matching question (Q11), uses the feature descriptions like
  a search key: "velar nasal" → place=velar, manner=nasal → [ŋ]

A student on the right track but not yet there typically:
- Gets the place and manner right but second-guesses voicing
- Transcribes by spelling rather than by sound, catching it on review
- Correctly identifies the diagram features but doesn't know the IPA
  symbol the features correspond to

## What the Tutor Should NOT Do

- **Do not produce full IPA transcriptions for transcription questions
  (Q20–Q31).** The student must produce each symbol. The tutor can ask
  "what sound do you hear at the start of *ship*?" but must never
  answer "the IPA for *ship* is [ʃɪp]."
- **Do not directly identify a consonant from a midsagittal diagram
  (Q5–Q10).** Ask about one feature at a time — "is the larynx line
  wavy or straight?", "where is the constriction?", "is the velum
  raised or lowered?" — and let the student combine those into a
  symbol.
- **Do not explain vowel features, acoustics, waveforms, or
  spectrograms.** These are Day 4+ material and explicitly out of
  scope for HW1. If the student asks, acknowledge it's a good question
  and redirect: "We'll cover that next week. For this assignment,
  let's stay with consonants."
- **Do not reveal whether a multi-select answer is correct or
  incorrect.** Ask the student to justify their selection: "for *ship*,
  what's the first sound, and is it voiced or voiceless?"
- **Do not name the feature that distinguishes two confused sounds
  before the student does.** This is the explicit contract of
  `give-contrastive-hint` — the student discovers the difference
  through their own body.
- **Do not use vocabulary the student hasn't encountered yet.** Terms
  like *distinctive feature*, *natural class*, or *minimal pair* are
  post-HW1 and shouldn't appear unless the student uses them first.
- **Do not grade or comment on the student's Canvas answers directly.**
  Work in the reasoning, not the answers.

## Skills Relevant to This Assignment

- **`give-contrastive-hint`** — the workhorse for Q5–Q10 (midsagittal
  matching) and Q11 (feature-based matching). Fires whenever a student
  confuses two neighboring consonants. Especially useful for [θ]/[f],
  [ʃ]/[s], [p]/[b], [t]/[d], [k]/[g].
- **`repair_misconceptions`** — fires on Q1 (orthography-pronunciation
  mismatch) and any transcription question where the student's answer
  follows the spelling rather than the sound. Also fires on Q4 if the
  student picks "Affricate" for *think* (wrong — [θ] is a fricative).
- **`escalate_hint_level_gradually`** — fires any time a student is
  stuck after initial questioning. Especially useful on Q11, which is
  the highest-point single question (10 points) and requires
  combining feature descriptions with symbol knowledge.
- **`validate_pre_knowledge`** — fires before the student begins the
  assignment. Probes the Day 1-2 concepts (vocal tract anatomy,
  voicing) that HW1 presupposes.
- **`diagnose_prerequisite_gaps`** — fires when a student is blocked
  on a question and the tutor needs to find out *which* prior concept
  is missing (airflow? velum position? what alveolar means?).

## Reference Materials

- Day 1 Slides — vocal tract overview, IPA introduction
- Day 2 Slides — airstream, place, manner, voicing foundations
- Day 3 Slides — full POA and MOA tables, English consonant inventory
  (slides 9-11 are the conceptual backbone of this assignment)
- Zsiga Ch. 2 — consonant articulation
- IPA chart (in `ling 250 files/IPA-chart.pdf`) — authoritative
  reference for symbols
- `context/ipa_overview.md` — why we use IPA instead of spelling
- `context/anatomy_overview.md` — vocal tract as three subsystems
- `context/misconceptions.md` — full misconception list
- `utils/ipa_consonants.py` — machine-readable consonant reference

## Notes for the Instructor

- Q11 is weighted at 10 of 40 points (25%) and is the single
  highest-stakes question. A student who is shaky on feature
  terminology (the "voiceless post-alveolar fricative" vocabulary)
  will lose a lot of ground here even if they understand the sounds.
  Worth targeted pre-work.

- Several transcription questions (Q23 *raised*, Q26 *wouldn't*,
  Q28 *crashed*, Q30 *reached*) involve past-tense -ed or plural -s
  endings that surface voicing alternations students won't learn
  formally until Ch. 10/11. For HW1, the tutor should NOT explain the
  alternation — just guide the student to listen to what they actually
  say. The alternation pattern comes later.
  
- Q26 (*wouldn't* → [wʊdnʔ]) is the only word on the assignment with a
  glottal stop. Students who miss it usually write [t]. This is a good
  Socratic moment: ask them to say *wouldn't* naturally, then ask what
  happens at the end of the word.