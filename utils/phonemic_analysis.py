"""
phonemic_analysis.py — distributional analysis methodology as catalog data.

Reference module for `analyze_dist` (Round 2 skill) and `repair_misconceptions`
(Round 1 skill) when phonemic-analysis questions surface in HW4 / HW5 / Midterm 2.

Data only — no pedagogical logic. Skills implement the Socratic flow.
"""

# ──────────────────────────────────────────────────────────────────────
# The Phonemic Principle — diagnostic procedure
# ──────────────────────────────────────────────────────────────────────
# The five-step methodology the tutor scaffolds when a student must
# determine the phonemic status of two sounds.

PHONEMIC_DIAGNOSTIC_STEPS = [
    {
        "step": 1,
        "name": "Find minimal pairs",
        "what_to_do": "Look for pairs of words differing only in the target sound.",
        "outcome_if_yes": "Strong evidence for phonemic contrast (separate phonemes).",
        "outcome_if_no": "Inconclusive — must check distribution. Absence of minimal pairs does NOT prove allophony.",
        "tutor_prompts": [
            "Can you find a pair of words that differ only in [X] vs [Y]?",
            "What words have you seen with [X]? What words with [Y]?",
            "If you swap [X] for [Y] in one word, does it become a different word?",
        ],
    },
    {
        "step": 2,
        "name": "List environments for each sound",
        "what_to_do": "Write out every left-and-right context where each sound appears.",
        "outcome_if_overlap": "Sounds appear in at least one shared context → OVERLAPPING distribution → separate phonemes.",
        "outcome_if_complementary": "Sounds appear in NO shared context → COMPLEMENTARY distribution → likely allophones (proceed to step 3).",
        "tutor_prompts": [
            "What's to the left and right of [X] in each word? Make a list.",
            "Now make the same list for [Y].",
            "Are any of the contexts the same? Even one?",
        ],
    },
    {
        "step": 3,
        "name": "Check phonetic similarity",
        "what_to_do": "Compare the two sounds' articulatory features (place, manner, voicing for consonants; height, backness, rounding for vowels).",
        "outcome_if_similar": "Allophones confirmed.",
        "outcome_if_dissimilar": "NOT allophones, even if complementary distribution. (English [h] / [ŋ] are the textbook counterexample.)",
        "tutor_prompts": [
            "What features do [X] and [Y] share?",
            "How are they different articulatorily?",
            "Could one be derived from the other by changing only one feature?",
        ],
    },
    {
        "step": 4,
        "name": "Choose the underlying representation (UR)",
        "what_to_do": "Identify which allophone has the broadest/elsewhere distribution. The UR yields the simplest rules (Occam's razor).",
        "guidance": "Test BOTH candidates. Count the rules required for each analysis. Pick the candidate with fewer/simpler rules.",
        "tutor_prompts": [
            "If [X] is the UR, what rule(s) would you need? List them.",
            "If [Y] is the UR, what rule(s) would you need? List them.",
            "Which analysis is simpler?",
        ],
    },
    {
        "step": 5,
        "name": "Write the rule(s)",
        "what_to_do": "Express the alternation in /A/ → [B] / X __ Y notation. Use natural-class features in the environment.",
        "guidance": "Avoid listing specific sounds when a feature describes the same set. /[+voiced stop]/ is preferable to /[b/d/g]/.",
        "tutor_prompts": [
            "What's the structural change? UR slot, surface form?",
            "What's the conditioning environment? Left context, right context?",
            "Is your environment a natural class? Does it include sounds that AREN'T in the data?",
        ],
    },
]

# ──────────────────────────────────────────────────────────────────────
# Three categories of phonological status
# ──────────────────────────────────────────────────────────────────────
# Tested explicitly in Midterm 2 study guide.

PHONOLOGICAL_STATUS_CATEGORIES = {
    "separate_phonemes": {
        "definition": "Two sounds that contrast lexically (different sounds yield different words).",
        "evidence": [
            "Minimal pairs (clear evidence)",
            "Overlapping distribution (one or more shared contexts)",
        ],
        "examples": [
            ("English /p/ vs /b/",      "pat vs bat"),
            ("Hindi /b/ vs /b̤/",        "overlapping environments #__a, #__i"),
            ("English /i/ vs /ɪ/",      "beat vs bit"),
        ],
    },
    "allophones": {
        "definition": "Predictable variants of a single phoneme; positionally restricted.",
        "evidence": [
            "Complementary distribution (NO shared contexts)",
            "Phonetic similarity",
        ],
        "examples": [
            ("English [pʰ] vs [p]",     "[pʰ] in pie, [p] in spy — both are /p/"),
            ("Spanish [b] vs [β]",      "[b] word-initial / after nasal; [β] intervocalic"),
            ("Korean [r] vs [l]",       "[r] in onset, [l] in coda — both are /l/ or /r/"),
        ],
    },
    "free_variation": {
        "definition": "Variants that are interchangeable in the same context — speakers can use either.",
        "evidence": [
            "Same context allows both pronunciations",
            "No predictable pattern",
        ],
        "examples": [
            ("English word-final [t] vs [t˺]", "released vs unreleased — same context"),
            ("English /r/ vs uvular [ʁ]",      "some speakers free-vary in casual speech"),
        ],
        "note": "Often confused with allophony. Allophones are PREDICTABLE; free variants are INTERCHANGEABLE.",
    },
}

# ──────────────────────────────────────────────────────────────────────
# Cross-linguistic phonemic analysis classics
# ──────────────────────────────────────────────────────────────────────
# Compact references for analyze_dist examples. Full data sets live in
# language_datasets.py; this is the methodological summary.

CLASSIC_ANALYSES = {
    "spanish_b_beta": {
        "language": "Spanish",
        "sounds": ("b", "β"),
        "status": "allophones",
        "distribution": "[b] word-initial or after nasal; [β] intervocalic",
        "ur_choice": "/b/",
        "rule": "/b/ → [β] / V _ V",
        "process": "lenition",
        "why_b_is_ur": "Two analyses considered: (a) /b/ + lenition rule (1 rule), (b) /β/ + fortition rules (2 rules). /b/ is simpler.",
    },
    "korean_r_l": {
        "language": "Korean",
        "sounds": ("r", "l"),
        "status": "allophones",
        "distribution": "[r] in onset (before vowel); [l] in coda (before consonant or word-finally)",
        "ur_choice": "/l/ (broader 'elsewhere' distribution)",
        "rule": "/l/ → [r] / __ V (in onset position)",
        "process": "n/a (positional alternation)",
        "note": "The conditioning environment is SYLLABLE POSITION, not adjacent segments. Important pattern.",
    },
    "hindi_b_bh": {
        "language": "Hindi",
        "sounds": ("b", "b̤"),
        "status": "separate phonemes",
        "distribution": "Both occur word-initially before vowels (overlapping at #__a, #__i)",
        "evidence": "Minimal pairs (e.g., bara 'large' vs b̤ari 'heavy')",
        "note": "Counterexample to 'if I can't tell two sounds apart, they must be allophones.' English speakers don't distinguish breathy from non-breathy voicing, but Hindi does.",
    },
    "english_h_ng": {
        "language": "English",
        "sounds": ("h", "ŋ"),
        "status": "separate phonemes (NOT allophones, despite complementary distribution)",
        "distribution": "[h] only word-initially; [ŋ] only word-finally — NEVER overlap",
        "why_not_allophones": "Phonetic similarity test fails. [h] is a glottal voiceless fricative; [ŋ] is a velar voiced nasal. Too different to be variants of the same phoneme.",
        "lesson": "Complementary distribution alone is not enough — phonetic similarity is required.",
    },
    "swampy_cree_p_b": {
        "language": "Swampy Cree",
        "sounds": ("p", "b"),
        "status": "allophones",
        "distribution": "[p] word-initial, word-final, between consonants; [b] between vowels",
        "ur_choice": "/p/",
        "rule": "/p/ → [b] / V _ V",
        "process": "voicing assimilation (lenition)",
        "tested_in": "HW4, Quiz 4, Day 13 slides",
    },
}

# ──────────────────────────────────────────────────────────────────────
# Common errors to anticipate (catalog for repair_misconceptions)
# ──────────────────────────────────────────────────────────────────────

PHONEMIC_ANALYSIS_ERRORS = [
    {
        "id": "PA1",
        "error": "Projecting English categorizations onto another language",
        "example": "Concluding that [i]/[ɪ] are allophones in Language X because they're 'similar' in English",
        "fix": "Each language's phonemic structure is determined by its OWN data. Listen to the data given, not to English intuition.",
    },
    {
        "id": "PA2",
        "error": "Skipping the distributional analysis step",
        "example": "Jumping to 'these are allophones' without writing out the environments",
        "fix": "List EVERY left-and-right environment for both sounds. Compare. Only then conclude.",
    },
    {
        "id": "PA3",
        "error": "Confusing complementary and overlapping distribution",
        "example": "Calling 'they appear in different positions sometimes' complementary distribution",
        "fix": "Complementary = NEVER the same context. Overlapping = at least ONE shared context.",
    },
    {
        "id": "PA4",
        "error": "Skipping the phonetic similarity check",
        "example": "Concluding [h]/[ŋ] are allophones in English because they're complementary",
        "fix": "Even with complementary distribution, the sounds must be phonetically similar to qualify as allophones.",
    },
    {
        "id": "PA5",
        "error": "Picking the wrong UR (most-frequent rather than broadest)",
        "example": "Choosing the form that appears most in the data, regardless of distribution width",
        "fix": "The UR is the form with the BROADEST/ELSEWHERE distribution, which yields the SIMPLEST rules. Walk through both candidates.",
    },
    {
        "id": "PA6",
        "error": "Confusing slashes and brackets in rules",
        "example": "Writing /[X] → /Y/ / __ [Z]/ — mixing levels",
        "fix": "/X/ = phoneme/UR. [X] = surface. Maintain the distinction faithfully.",
    },
    {
        "id": "PA7",
        "error": "Listing sounds where features should be used",
        "example": "Writing /[b,d,g]/ → [β,ð,ɣ] / V_V instead of /[+voiced stop]/ → [+fricative] / V_V",
        "fix": "Use natural-class features in rule environments. The whole point of natural classes.",
    },
]

# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────

def step(n):
    """Return the diagnostic step dict for step number N."""
    return next((s for s in PHONEMIC_DIAGNOSTIC_STEPS if s["step"] == n), None)

def status_definition(category):
    """Get the definition of a phonological status category.
    category: 'separate_phonemes', 'allophones', or 'free_variation'."""
    return PHONOLOGICAL_STATUS_CATEGORIES.get(category, {}).get("definition")

def example_analysis(name):
    """Return a classic phonemic analysis by name (e.g., 'korean_r_l')."""
    return CLASSIC_ANALYSES.get(name)


# ──────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert step(1)["name"] == "Find minimal pairs"
    assert "predictable" in PHONOLOGICAL_STATUS_CATEGORIES["allophones"]["definition"].lower() or \
           "variant" in PHONOLOGICAL_STATUS_CATEGORIES["allophones"]["definition"].lower()
    assert example_analysis("korean_r_l")["status"] == "allophones"
    assert len(PHONEMIC_DIAGNOSTIC_STEPS) == 5
    print(f"phonemic_analysis.py self-test passed.")
    print(f"  {len(PHONEMIC_DIAGNOSTIC_STEPS)} diagnostic steps")
    print(f"  {len(PHONOLOGICAL_STATUS_CATEGORIES)} status categories")
    print(f"  {len(CLASSIC_ANALYSES)} classic analyses")
    print(f"  {len(PHONEMIC_ANALYSIS_ERRORS)} cataloged error patterns")
