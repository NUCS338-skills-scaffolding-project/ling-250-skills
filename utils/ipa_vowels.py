"""
ipa_vowels.py — English vowel inventory with articulatory features and formants.

Reference module for skills that need vowel-feature lookup, vowel-pair contrast,
or formant-based identification. Parallel to ipa_consonants.py.

Data sources:
- Day 4 slides (LING 250 Spring 2026)
- Hillenbrand et al. 1995 (formant means for adult male/female)
- Make-up HW + practica reference values

This module is data-only — it does not implement pedagogical logic. Skills
that USE this module (e.g., id_natural_class, read_acoustic_trace) implement
the Socratic flow.
"""

# ──────────────────────────────────────────────────────────────────────
# English vowel inventory: 12 monophthongs + 5 diphthongs
# ──────────────────────────────────────────────────────────────────────

# Each vowel's feature dict. Backward-compatible: callers can do
#   ENGLISH_VOWELS["i"]["height"] == "high"
# Notes:
#   - "stressed" is True/False/None — None = not relevant (only schwa/wedge
#     differ on this dimension)
#   - "diphthong" is the digraph IPA for vowels that are realized as
#     diphthongs in standard American English (e.g., "e" -> "eɪ")
ENGLISH_VOWELS = {
    "i":  {"height": "high",  "backness": "front",   "rounding": "unrounded", "tense": True,  "type": "monophthong", "example": "beat",   "stressed": None},
    "ɪ":  {"height": "high",  "backness": "front",   "rounding": "unrounded", "tense": False, "type": "monophthong", "example": "bit",    "stressed": None},
    "e":  {"height": "mid",   "backness": "front",   "rounding": "unrounded", "tense": True,  "type": "diphthong",   "example": "bait",   "stressed": None, "diphthong": "eɪ"},
    "ɛ":  {"height": "mid",   "backness": "front",   "rounding": "unrounded", "tense": False, "type": "monophthong", "example": "bet",    "stressed": None},
    "æ":  {"height": "low",   "backness": "front",   "rounding": "unrounded", "tense": False, "type": "monophthong", "example": "bat",    "stressed": None},
    "ə":  {"height": "mid",   "backness": "central", "rounding": "unrounded", "tense": False, "type": "monophthong", "example": "about",  "stressed": False},
    "ʌ":  {"height": "mid",   "backness": "central", "rounding": "unrounded", "tense": False, "type": "monophthong", "example": "fun",    "stressed": True},
    "ɜ˞": {"height": "mid",   "backness": "central", "rounding": "unrounded", "tense": False, "type": "monophthong", "example": "heard",  "stressed": True,  "rhotacized": True},
    "u":  {"height": "high",  "backness": "back",    "rounding": "rounded",   "tense": True,  "type": "monophthong", "example": "boot",   "stressed": None},
    "ʊ":  {"height": "high",  "backness": "back",    "rounding": "rounded",   "tense": False, "type": "monophthong", "example": "look",   "stressed": None},
    "o":  {"height": "mid",   "backness": "back",    "rounding": "rounded",   "tense": True,  "type": "diphthong",   "example": "boat",   "stressed": None, "diphthong": "oʊ"},
    "ɔ":  {"height": "mid",   "backness": "back",    "rounding": "rounded",   "tense": False, "type": "monophthong", "example": "law",    "stressed": None},
    "ɑ":  {"height": "low",   "backness": "back",    "rounding": "unrounded", "tense": True,  "type": "monophthong", "example": "father", "stressed": None},
}

DIPHTHONGS = {
    "aɪ": {"start": "a", "end": "ɪ", "example": "bite"},
    "ɔɪ": {"start": "ɔ", "end": "ɪ", "example": "boy"},
    "eɪ": {"start": "e", "end": "ɪ", "example": "bait"},
    "oʊ": {"start": "o", "end": "ʊ", "example": "boat"},
    "aʊ": {"start": "a", "end": "ʊ", "example": "bout"},
}

# Daniel Jones cardinal vowels — REFERENCE POINTS, not English vowels.
# Auditorily equidistant. NOT typological universals.
# Tested on HW2 Q23-Q25, Quiz 1 Q3, Quiz 1 Q5.
CARDINAL_VOWELS = {
    1: {"symbol": "i", "description": "high front unrounded"},
    2: {"symbol": "e", "description": "mid-high front unrounded"},
    3: {"symbol": "ɛ", "description": "mid-low front unrounded"},
    4: {"symbol": "a", "description": "low front unrounded"},
    5: {"symbol": "ɑ", "description": "low back unrounded"},
    6: {"symbol": "ɔ", "description": "mid-low back rounded"},
    7: {"symbol": "o", "description": "mid-high back rounded"},
    8: {"symbol": "u", "description": "high back rounded"},
}

# ──────────────────────────────────────────────────────────────────────
# Formant data (Hillenbrand et al. 1995 means)
# ──────────────────────────────────────────────────────────────────────
# Format: (F1_male, F2_male, F1_female, F2_female) in Hz.
# Used by read_acoustic_trace for spectrogram/spectrum reading.
ENGLISH_VOWEL_FORMANTS = {
    "i":  {"male": (342, 2322), "female": (437, 2761), "child": (452, 3081)},
    "ɪ":  {"male": (427, 2034), "female": (483, 2365), "child": (511, 2552)},
    "ɛ":  {"male": (580, 1799), "female": (731, 2058), "child": (749, 2267)},
    "æ":  {"male": (588, 1952), "female": (669, 2349), "child": (717, 2501)},
    "ɑ":  {"male": (768, 1333), "female": (936, 1551), "child": (1002, 1688)},
    "ɔ":  {"male": (652,  997), "female": (781, 1136), "child": (803, 1210)},
    "ʊ":  {"male": (469, 1122), "female": (519, 1225), "child": (568, 1490)},
    "u":  {"male": (378,  997), "female": (459, 1105), "child": (494, 1345)},
    "ʌ":  {"male": (623, 1200), "female": (753, 1426), "child": (749, 1546)},
    # Schwa, ɜ˞, e, o omitted from Hillenbrand — measure in context if needed
}

# ──────────────────────────────────────────────────────────────────────
# Helper functions
# ──────────────────────────────────────────────────────────────────────

def lookup_vowel(symbol):
    """Return feature dict for the given IPA vowel symbol, or None."""
    return ENGLISH_VOWELS.get(symbol)

def vowels_with_feature(feature, value):
    """Return list of IPA symbols for vowels matching feature=value.

    Example:
        vowels_with_feature("height", "high") -> ["i", "ɪ", "u", "ʊ"]
        vowels_with_feature("tense", True)    -> ["i", "e", "u", "o", "ɑ"]
    """
    return [s for s, v in ENGLISH_VOWELS.items() if v.get(feature) == value]

def is_lax(symbol):
    """Return True if the vowel is lax (tense=False). Returns None if unknown."""
    v = ENGLISH_VOWELS.get(symbol)
    if v is None:
        return None
    return not v["tense"]

def is_lax_word_final_legal(symbol):
    """In English, lax vowels can't occur word-finally — except schwa.
    Returns True if the vowel CAN appear word-finally."""
    if symbol == "ə":
        return True
    if is_lax(symbol):
        return False
    return True

def shared_features(symbols):
    """Return dict of {feature: value} for features shared across all the
    given vowel symbols. Useful for natural-class reasoning.

    Example:
        shared_features(["i", "ɪ"])
        -> {"height": "high", "backness": "front", "rounding": "unrounded"}
    """
    if not symbols:
        return {}
    first = ENGLISH_VOWELS.get(symbols[0])
    if first is None:
        return {}
    shared = dict(first)
    for s in symbols[1:]:
        v = ENGLISH_VOWELS.get(s)
        if v is None:
            continue
        shared = {f: val for f, val in shared.items() if v.get(f) == val}
    return shared

def differing_feature(s1, s2):
    """Return the feature(s) that distinguish two vowels, ignoring shared.
    Useful for give_contrastive_hint.

    Example:
        differing_feature("i", "ɪ") -> ["tense"]   (both high front unrounded)
        differing_feature("i", "u") -> ["backness", "rounding"]
    """
    v1 = ENGLISH_VOWELS.get(s1)
    v2 = ENGLISH_VOWELS.get(s2)
    if v1 is None or v2 is None:
        return []
    return [f for f in v1 if v1.get(f) != v2.get(f) and f in v2]

def transform(symbol, **changes):
    """Find the vowel that results from changing one or more features.
    Used by id_natural_class for HW2 Q18-Q22 ('Make [i] mid' -> [e]).

    Example:
        transform("i", height="mid")           -> "e"
        transform("i", tense=False)            -> "ɪ"
        transform("ɑ", height="mid", tense=False) -> "ʌ"

    Returns None if no English vowel matches the resulting feature set,
    or a single matching symbol if there's exactly one match. If multiple
    candidates match, returns the list.
    """
    base = ENGLISH_VOWELS.get(symbol)
    if base is None:
        return None
    target = {**base, **changes}
    matches = []
    # Only match on the four core articulatory features; "type" (monophthong
    # vs diphthong) is a surface-level distinction that shouldn't block a
    # feature-space transformation. E.g., HW2 Q18 'Make [i] mid' expects [e]
    # even though [e] surfaces as a diphthong [eɪ].
    for s, v in ENGLISH_VOWELS.items():
        if all(v.get(f) == target.get(f) for f in ("height", "backness", "rounding", "tense")):
            matches.append(s)
    if len(matches) == 1:
        return matches[0]
    return matches if matches else None

def formant_for(symbol, speaker_type="male"):
    """Return (F1, F2) tuple for a vowel symbol and speaker type.
    speaker_type: 'male', 'female', or 'child'."""
    data = ENGLISH_VOWEL_FORMANTS.get(symbol)
    if data is None:
        return None
    return data.get(speaker_type)


# ──────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Quick assertions to sanity-check the data
    assert lookup_vowel("i")["height"] == "high"
    assert lookup_vowel("ɪ")["tense"] is False
    assert is_lax("i") is False
    assert is_lax("ɪ") is True
    assert is_lax_word_final_legal("ɪ") is False
    assert is_lax_word_final_legal("ə") is True
    assert is_lax_word_final_legal("i") is True
    assert "tense" in differing_feature("i", "ɪ")
    assert transform("i", height="mid") == "e"
    assert transform("i", tense=False) == "ɪ"
    print("ipa_vowels.py self-test passed.")
    print(f"Inventory size: {len(ENGLISH_VOWELS)} monophthongs + {len(DIPHTHONGS)} diphthongs")
