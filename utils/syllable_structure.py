"""
syllable_structure.py — sonority hierarchy, English syllable templates, mora
rules, syllable typology, and SSP-violation patterns.

Reference module for HW5 / id_natural_class / write_phon_rule (when rules
reference syllable structure).

Drawn from Day 14-15 slides + Quiz 5 + Midterm 2 review problem D.
"""

# ──────────────────────────────────────────────────────────────────────
# Sonority hierarchy (Day 14, Quiz 5 Q3 confirmed)
# ──────────────────────────────────────────────────────────────────────
# 8 ranks. Higher = more sonorant.

SONORITY_HIERARCHY = [
    ("vowels",                8),  # most sonorant
    ("glides",                7),  # [w, j]
    ("liquids",               6),  # [l, ɹ, r]
    ("nasals",                5),  # [m, n, ŋ]
    ("voiced_fricatives",     4),  # [v, z, ʒ, ð]
    ("voiceless_fricatives",  3),  # [f, s, ʃ, θ, h]
    ("voiced_stops",          2),  # [b, d, g]
    ("voiceless_stops",       1),  # [p, t, k]  least sonorant
]

# Reverse lookup
SONORITY_RANK = {name: rank for name, rank in SONORITY_HIERARCHY}

# Map IPA segments to sonority class. Used by sonority_of().
SEGMENT_TO_SONORITY_CLASS = {
    # Vowels
    **{v: "vowels" for v in ["i", "ɪ", "e", "ɛ", "æ", "ə", "ʌ", "u", "ʊ", "o", "ɔ", "ɑ", "a"]},
    # Glides
    **{g: "glides" for g in ["w", "j"]},
    # Liquids
    **{l: "liquids" for l in ["l", "ɹ", "r", "ɫ"]},
    # Nasals
    **{n: "nasals" for n in ["m", "n", "ŋ"]},
    # Voiced fricatives
    **{f: "voiced_fricatives" for f in ["v", "z", "ʒ", "ð"]},
    # Voiceless fricatives
    **{f: "voiceless_fricatives" for f in ["f", "s", "ʃ", "θ", "h"]},
    # Voiced stops
    **{s: "voiced_stops" for s in ["b", "d", "g"]},
    # Voiceless stops
    **{s: "voiceless_stops" for s in ["p", "t", "k"]},
}


def sonority_class(segment):
    """Return the sonority class of an IPA segment, or None."""
    return SEGMENT_TO_SONORITY_CLASS.get(segment)


def sonority_of(segment):
    """Return the sonority rank (1-8) of an IPA segment, or None."""
    cls = sonority_class(segment)
    if cls is None:
        return None
    return SONORITY_RANK[cls]


def sort_by_sonority(segments, descending=True):
    """Sort a list of segments by sonority rank.
    Default: descending (most-to-least sonorant)."""
    return sorted(segments, key=lambda s: sonority_of(s) or 0, reverse=descending)


# ──────────────────────────────────────────────────────────────────────
# English syllable templates
# ──────────────────────────────────────────────────────────────────────

ENGLISH_ONSET_TEMPLATES = {
    "empty":  {"description": "no onset (English allows V-initial syllables)", "examples": ["egg [ɛg]", "I [aɪ]"]},
    "C":      {"description": "single C; any consonant", "examples": ["pat", "bat"]},
    "CC": {
        "description": "obstruent + liquid; stop + glide; /s/ + obstruent",
        "examples": [
            "play, pray, clay (obstruent + liquid)",
            "twin, pure [pjʊɹ] (stop + glide)",
            "spy, sty, ski, smell, snow, slow (/s/ + C — SSG-violating but legal)",
        ],
    },
    "CCC": {
        "description": "/s/ + obstruent + liquid",
        "examples": ["splay, spray, stray, screw"],
        "note": "All English CCC onsets begin with /s/.",
    },
}

ENGLISH_CODA_TEMPLATES = {
    "empty":  {"description": "no coda (English allows V-final syllables)", "examples": ["pie, see, blue"]},
    "C":      {"description": "single C; any consonant", "examples": ["cat, dog, ship"]},
    "CC": {
        "description": "liquid + obstruent; nasal + obstruent; fricative + stop",
        "examples": [
            "part, milk, hearth (liquid + obstruent)",
            "hand, lens, lump (nasal + obstruent)",
            "soft, mask, lost (fricative + stop)",
        ],
    },
    "CCC_plus": {
        "description": "coda + suffix C(s)",
        "examples": ["parts, sixths, twelfths, hulks, forced"],
        "note": "English CCCC codas usually involve morphological -s, -ed, -t suffix",
    },
}

# ──────────────────────────────────────────────────────────────────────
# SSP — Sonority Sequencing Generalization
# ──────────────────────────────────────────────────────────────────────
# The nucleus is the sonority peak; sonority decreases outward.
# English /s/ + obstruent is the canonical SSG-violating but legal onset.

SSP_VIOLATIONS_ENGLISH = [
    {"word": "spa",    "syllable": [("s", 3), ("p", 1), ("ɑ", 8)],
     "violation": "Onset [sp]: s (3) > p (1), but the path from edge to nucleus should rise monotonically"},
    {"word": "ski",    "syllable": [("s", 3), ("k", 1), ("i", 8)],
     "violation": "Same as spa — sibilant onset rule is the SSG exception"},
    {"word": "fox",    "syllable": [("f", 3), ("ɑ", 8), ("k", 1), ("s", 3)],
     "violation": "Coda [ks]: k (1) < s (3) — sonority should decrease toward edge but rises"},
    {"word": "twelfths", "syllable": [("t",1),("w",7),("ɛ",8),("l",6),("f",3),("θ",3),("s",3)],
     "violation": "Multiple coda violations across consonants"},
]

SSP_CONFORMING_ENGLISH = [
    {"word": "peak",  "syllable": [("p", 1), ("i", 8), ("k", 1)]},
    {"word": "blink", "syllable": [("b", 2), ("l", 6), ("i", 8), ("ŋ", 5), ("k", 1)]},
    {"word": "tramp", "syllable": [("t", 1), ("ɹ", 6), ("æ", 8), ("m", 5), ("p", 1)]},
    {"word": "fish",  "syllable": [("f", 3), ("ɪ", 8), ("ʃ", 3)]},
]


def is_ssp_conforming(syllable):
    """Given an ordered list of (segment, rank) tuples, check whether sonority
    rises monotonically to the nucleus (the peak) and falls monotonically away.
    Returns (bool, reason_if_violation)."""
    if not syllable:
        return True, "empty syllable"
    ranks = [r for _, r in syllable]
    peak_idx = ranks.index(max(ranks))
    # Check rise
    for i in range(peak_idx):
        if ranks[i] >= ranks[i+1]:
            return False, f"Sonority does not rise at position {i}: {syllable[i][0]}({ranks[i]}) → {syllable[i+1][0]}({ranks[i+1]})"
    # Check fall
    for i in range(peak_idx, len(ranks) - 1):
        if ranks[i] <= ranks[i+1]:
            return False, f"Sonority does not fall at position {i}: {syllable[i][0]}({ranks[i]}) → {syllable[i+1][0]}({ranks[i+1]})"
    return True, None


# ──────────────────────────────────────────────────────────────────────
# Cross-linguistic syllable typology
# ──────────────────────────────────────────────────────────────────────

SYLLABLE_TYPOLOGY = {
    "hawaiian":  {"onset_max": 1, "coda_max": 0, "nucleus": "(C)V(:)",
                  "note": "No codas, no clusters; CV is the only universal type"},
    "japanese":  {"onset_max": 1, "coda_max": 1, "nucleus": "V, CV, CVN",
                  "note": "Coda only allowed if it's a nasal or geminate"},
    "finnish":   {"onset_max": 1, "coda_max": 1, "nucleus": "CV mostly",
                  "note": "Limited clusters"},
    "english":   {"onset_max": 3, "coda_max": 4, "nucleus": "V, V:, VV",
                  "note": "Up to CCCVCCCC (with morphology)"},
    "german":    {"onset_max": 3, "coda_max": 3, "nucleus": "varied",
                  "note": "Similar to English, slightly more restricted"},
}

# Implicational universal (Quiz 5 Q1)
IMPLICATIONAL_UNIVERSALS = [
    "If a language allows syllables with codas, it also allows syllables without codas.",
    "Every language allows CV syllables (no exceptions known).",
    "Languages with coda clusters always allow simple codas.",
]


# ──────────────────────────────────────────────────────────────────────
# Mora rules
# ──────────────────────────────────────────────────────────────────────

MORA_RULES = {
    "english": {
        "light":      "CV (1 mora)",
        "heavy":      "CV: or CVC (2 moras) — CVC only counts when stressed",
        "superheavy": "CV:C (3 moras) — only in stressed monosyllables",
        "key_rule":   "In English, coda Cs contribute moras ONLY in stressed syllables",
    },
    "japanese": {
        "light":      "CV (1 mora)",
        "heavy":      "CV:, CVN, CVQ (geminate) — all 2 moras",
        "key_rule":   "Every C and V can be moraic; geminates and codas are mora-bearing",
    },
    "latin": {
        "light":      "CV (1 mora)",
        "heavy":      "CV: or CVC (2 moras)",
        "key_rule":   "Both V length and coda C contribute moras",
    },
    "greek": {
        "light":      "CV (1 mora)",
        "heavy":      "CV: or CVC (2 moras)",
        "superheavy": "CV:C (3 moras)",
        "key_rule":   "Same as Latin (Classical Greek)",
        "note":       "Tested in HW5 Q17-Q18 (Odyssey line)",
    },
}


# ──────────────────────────────────────────────────────────────────────
# Speech-error patterns (syllable-position evidence)
# ──────────────────────────────────────────────────────────────────────
# Spoonerisms preserve syllable position. Onsets swap with onsets, etc.

SPEECH_ERROR_PATTERNS = [
    {"intended": "weak link",     "error": "leak wink",      "swap": "onsets"},
    {"intended": "heap of junk",  "error": "hunk of jeep",   "swap": "rhymes"},
    {"intended": "cup of coffee", "error": "cop of cuffee",  "swap": "nuclei"},
    {"intended": "stiff neck",    "error": "stik nef",       "swap": "codas"},
    {"intended": "figgy pudding", "error": "piggy fudding",  "swap": "onsets"},
    {"intended": "bed bugs",      "error": "bud begz",       "swap": "nuclei"},
]

UNLIKELY_SPEECH_ERROR = {
    "intended": "stick in the mud",
    "error":    "skit in the dum",
    "why_unlikely": "Would require swapping the coda of one word with the onset of the next, violating syllable position.",
}


# ──────────────────────────────────────────────────────────────────────
# Maximal Onset Principle (MOP)
# ──────────────────────────────────────────────────────────────────────
# When syllabifying a word with intervocalic consonant clusters, put as many
# Cs as possible into the onset of the FOLLOWING syllable, subject to
# language-specific phonotactic constraints.

MOP_EXAMPLES = [
    {"word": "market",    "syllabification": "[mɑr.kət]",  "rationale": "Single intervocalic [k] → onset of σ2"},
    {"word": "limit",     "syllabification": "[lɪ.mɪt]",   "rationale": "Single intervocalic [m] → onset of σ2"},
    {"word": "empty",     "syllabification": "[ɛmp.ti]",   "rationale": "[mpt] not a legal onset → split: [mp] coda, [t] onset"},
    {"word": "instruct",  "syllabification": "[ɪn.stɹəkt]", "rationale": "[nstr] not a legal onset; [str] is → coda [n], onset [str]"},
    {"word": "papaya",    "syllabification": "[pə.paɪ.ə]", "rationale": "Intervocalic [p] → onset of σ2; final V is its own σ"},
]


# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────

def shared_features_summary(symbols):
    """Wrapper helper: classify the natural class of a segment list by sonority.
    Useful for id_natural_class when sonority is the relevant feature."""
    classes = {sonority_class(s) for s in symbols if sonority_class(s)}
    if len(classes) == 1:
        return classes.pop()
    return None


# ──────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert sonority_of("i") == 8
    assert sonority_of("p") == 1
    assert sonority_of("l") == 6
    # Sonority sort
    assert sort_by_sonority(["s", "r", "e", "t", "j"], descending=True) == ["e", "j", "r", "s", "t"]
    # SSP check
    ok, _ = is_ssp_conforming([("p", 1), ("i", 8), ("k", 1)])
    assert ok
    bad, why = is_ssp_conforming([("s", 3), ("p", 1), ("ɑ", 8)])
    assert not bad
    print("syllable_structure.py self-test passed.")
    print(f"  {len(SYLLABLE_TYPOLOGY)} languages in typology")
    print(f"  {len(MORA_RULES)} mora-rule systems")
    print(f"  {len(SSP_VIOLATIONS_ENGLISH)} SSP-violating English examples")
    print(f"  {len(SSP_CONFORMING_ENGLISH)} SSP-conforming English examples")
