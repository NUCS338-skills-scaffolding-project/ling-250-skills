"""
Reference data for English consonants.
Source: Ling 250 Days 1-3 slides (Strori, Spring 2023).
"""

SONORANT_MANNERS = {"nasal", "approximant", "lateral", "tap"}
CONTINUANT_MANNERS = {"fricative", "approximant", "lateral"}

CONSONANTS = {
    # ========== BILABIAL ==========
    "p":  {"place": "bilabial",
           "manner": "stop",
           "voicing": "voiceless",
           "example_word": "pet",
           "spellings": ["p", "pp"]},
    "b":  {"place": "bilabial",
           "manner": "stop",
           "voicing": "voiced",
           "example_word": "bet",
           "spellings": ["b", "bb"]},
    "m":  {"place": "bilabial",
           "manner": "nasal",
           "voicing": "voiced",
           "example_word": "mat",
           "spellings": ["m", "mm"]},

    # ========== LABIODENTAL ==========
    "f":  {"place": "labiodental",
           "manner": "fricative",
           "voicing": "voiceless",
           "example_word": "fat",
           "spellings": ["f", "ff", "ph", "gh"]},
    "v":  {"place": "labiodental",
           "manner": "fricative",
           "voicing": "voiced",
           "example_word": "vat",
           "spellings": ["v"]},

    # ========== DENTAL ==========
    "θ":  {"place": "dental",
           "manner": "fricative",
           "voicing": "voiceless",
           "example_word": "thing",
           "spellings": ["th"]},
    "ð":  {"place": "dental",
           "manner": "fricative",
           "voicing": "voiced",
           "example_word": "this",
           "spellings": ["th"]},

    # ========== ALVEOLAR ==========
    "t":  {"place": "alveolar",
           "manner": "stop",
           "voicing": "voiceless",
           "example_word": "top",
           "spellings": ["t", "tt"]},
    "d":  {"place": "alveolar",
           "manner": "stop",
           "voicing": "voiced",
           "example_word": "dog",
           "spellings": ["d", "dd"]},
    "s":  {"place": "alveolar",
           "manner": "fricative",
           "voicing": "voiceless",
           "example_word": "sip",
           "spellings": ["s", "ss", "c", "sc"]},
    "z":  {"place": "alveolar",
           "manner": "fricative",
           "voicing": "voiced",
           "example_word": "zip",
           "spellings": ["z", "zz", "s"]},
    "n":  {"place": "alveolar",
           "manner": "nasal",
           "voicing": "voiced",
           "example_word": "nap",
           "spellings": ["n", "nn", "kn", "gn"]},
    "ɾ":  {"place": "alveolar",
       "manner": "tap",
       "voicing": "voiced",
       "example_word": "butter",
       "spellings": ["t", "tt", "d"],
       "environment": (
           "Restricted to between vowels where V1 is stressed and "
           "V2 is unstressed — pattern: [V₁ ɾ V₂]. Examples: butter, "
           "water, ladder, batter. Outside this environment the "
           "underlying /t/ or /d/ surfaces as [t] or [d]."
       )},
    "ɹ":  {"place": "alveolar",
           "manner": "approximant",
           "voicing": "voiced",
           "example_word": "red",
           "spellings": ["r", "rr", "wr"],
           "subcategory": "rhotic liquid"},
    "l":  {"place": "alveolar",
           "manner": "lateral",
           "voicing": "voiced",
           "example_word": "lip",
           "spellings": ["l", "ll"],
           "subcategory": "lateral liquid"},

    # ========== POST-ALVEOLAR ==========
    "ʃ":  {"place": "post-alveolar",
           "manner": "fricative",
           "voicing": "voiceless",
           "example_word": "ship",
           "spellings": ["sh", "ti", "ci", "ss"]},
    "ʒ":  {"place": "post-alveolar",
           "manner": "fricative",
           "voicing": "voiced",
           "example_word": "measure",
           "spellings": ["s", "si", "g"]},
    "tʃ": {"place": "post-alveolar",
           "manner": "affricate",
           "voicing": "voiceless",
           "example_word": "chip",
           "spellings": ["ch", "tch"]},
    "dʒ": {"place": "post-alveolar",
           "manner": "affricate",
           "voicing": "voiced",
           "example_word": "jug",
           "spellings": ["j", "g", "dg", "dge"]},

    # ========== PALATAL ==========
    "j":  {"place": "palatal",
           "manner": "approximant",
           "voicing": "voiced",
           "example_word": "yes",
           "spellings": ["y", "i"],
           "subcategory": "glide"},

    # ========== VELAR ==========
    "k":  {"place": "velar",
           "manner": "stop",
           "voicing": "voiceless",
           "example_word": "cat",
           "spellings": ["k", "c", "ck", "ch", "q"]},
    "g":  {"place": "velar",
           "manner": "stop",
           "voicing": "voiced",
           "example_word": "go",
           "spellings": ["g", "gg"]},
    "ŋ":  {"place": "velar",
           "manner": "nasal",
           "voicing": "voiced",
           "example_word": "sing",
           "spellings": ["ng", "n"]},

    # ========== GLOTTAL ==========
    "ʔ":  {"place": "glottal",
           "manner": "stop",
           "voicing": "voiceless",
           "example_word": "uh-oh",
           "spellings": ["'"]},
    "h":  {"place": "glottal",
           "manner": "fricative",
           "voicing": "voiceless",
           "example_word": "hat",
           "spellings": ["h"]},

    # ========== LABIO-VELAR ==========
    "w":  {"place": "labio-velar",
           "manner": "approximant",
           "voicing": "voiced",
           "example_word": "wet",
           "spellings": ["w", "wh"],
           "subcategory": "glide",
           "rounded": True},
}

# Non-English reference symbols students might confuse with English ones.
# These are NOT in the English consonant inventory but are mentioned in
# Day 3 slides (e.g., the trill [r] is contrasted with English's [ɹ]).
# Kept separate from CONSONANTS so feature lookups for English don't
# return false positives.
NON_ENGLISH_REFERENCE = {
    "r":  {"place": "alveolar",
           "manner": "trill",
           "voicing": "voiced",
           "example_languages": ["Spanish (rico)", "Italian (rosso)",
                                 "Scottish English (bright red)"],
           "english_counterpart": "ɹ",
           "note": (
               "[r] in IPA is a trill — a series of rapid taps from the "
               "tongue tip against the alveolar ridge. English does NOT "
               "use the trill. The English r in red, run, very is the "
               "rhotic approximant [ɹ], a single approximation without "
               "any tongue contact. When transcribing English, use [ɹ]."
           )},
}
# Place-of-articulation descriptions.
PLACES = {
    "bilabial": {
        "description": "upper and lower lip",
        "examples": ["m", "p", "b"],
    },
    "labiodental": {
        "description": "lower lip, upper teeth",
        "examples": ["f", "v"],
    },
    "dental": {
        "description": "tongue tip and upper front teeth (also called interdental)",
        "examples": ["θ", "ð"],
    },
    "alveolar": {
        "description": "tongue tip or blade and the alveolar ridge",
        "examples": ["t", "d", "s", "z", "n", "ɾ", "ɹ", "l"],
    },
    "post-alveolar": {
        "description": "tongue blade (and front of tongue) and post-alveolar ridge / front palatal region (also called palato-alveolar)",
        "examples": ["ʃ", "ʒ", "tʃ", "dʒ"],
    },
    "palatal": {
        "description": "front of tongue, hard palate",
        "examples": ["j"],
    },
    "velar": {
        "description": "back of tongue against velum",
        "examples": ["k", "g", "ŋ"],
    },
    "glottal": {
        "description": "at the glottis — either neutral vocal tract with open glottis ([h]) or a brief complete closure between the vocal folds ([ʔ])",
        "examples": ["h", "ʔ"],
    },
    "labio-velar": {
        "description": "rounded lips and back of tongue against velum",
        "examples": ["w"],
    },
}

# Manner-of-articulation descriptions.
MANNERS = {
    "stop": {
        "description": "complete closure in the oral cavity — air cannot escape (also called plosive)",
        "examples": ["p", "b", "t", "d", "k", "g", "ʔ"],
        "category": "obstruent",
    },
    "fricative": {
        "description": "narrow constriction creating turbulent airflow and friction",
        "examples": ["f", "v", "θ", "ð", "s", "z", "ʃ", "ʒ", "h"],
        "category": "obstruent",
    },
    "affricate": {
        "description": "a stop closure followed by a fricative release",
        "examples": ["tʃ", "dʒ"],
        "category": "obstruent",
    },
    "nasal": {
        "description": "complete oral closure but velum lowered so air escapes through the nose",
        "examples": ["m", "n", "ŋ"],
        "category": "sonorant",
    },
    "approximant": {
        "description": "weak closure — articulators approach but don't create friction (includes glides and rhotic liquids)",
        "examples": ["ɹ", "j", "w"],
        "category": "sonorant",
    },
    "lateral": {
        "description": "constriction in center of oral cavity but air passes over the sides of the tongue",
        "examples": ["l"],
        "category": "sonorant",
    },
    "tap": {
        "description": "brief single contact between tongue blade and alveolar ridge (also called flap)",
        "examples": ["ɾ"],
        "category": "sonorant",
    },
    "trill": {
        "description": "rapid repeated taps of an articulator (NOT used in English; see Spanish 'rico', Scottish 'red')",
        "examples": [],  # No English consonants are trills; [r] lives in NON_ENGLISH_REFERENCE
        "category": "sonorant",
        "english": False,
    },
}

# Spelling-to-IPA trap inventory. Used by repair-misconceptions and by
# the orthography_vs_pronunciation refresher when the orchestrator
# wants concrete examples of how English spelling misleads transcription.
# Each entry pairs a spelling pattern with the sounds it can represent
# in English, plus example words and the gist of the trap.
# Source: Day 3 slides 21-31 plus standard examples from Days 1-3.
SPELLING_TRAPS = {
    "th": {
        "represents": ["θ", "ð"],
        "examples": [("thing", "θ"), ("this", "ð"), ("path", "θ"),
                     ("smooth", "ð")],
        "trap": (
            "Two different sounds spelled identically. Voiceless [θ] and "
            "voiced [ð] differ only in voicing. Most words use one or "
            "the other; the spelling never tells you which."
        ),
    },
    "ph": {
        "represents": ["f"],
        "examples": [("phone", "f"), ("graph", "f"), ("photograph", "f")],
        "trap": "One sound: [f]. Not [p] + [h], even though it looks that way.",
    },
    "ch": {
        "represents": ["tʃ", "k", "ʃ"],
        "examples": [("chip", "tʃ"), ("character", "k"), ("chic", "ʃ"),
                     ("ache", "k")],
        "trap": (
            "Three different sounds depending on the word. Default [tʃ] "
            "(chip), but [k] in Greek-derived words (character, ache) "
            "and [ʃ] in French-derived words (chic, machine)."
        ),
    },
    "sh": {
        "represents": ["ʃ"],
        "examples": [("ship", "ʃ"), ("crash", "ʃ"), ("fashion", "ʃ")],
        "trap": "Two letters, one sound: [ʃ]. Reliable.",
    },
    "ng": {
        "represents": ["ŋ", "ŋg", "ndʒ"],
        "examples": [("sing", "ŋ"), ("finger", "ŋg"), ("change", "ndʒ"),
                     ("ringer", "ŋ")],
        "trap": (
            "Often one sound [ŋ], but in 'finger' both [ŋ] and [g]; in "
            "'change' it's something else entirely. The pattern is "
            "morphological: 'sing-er' = [ŋ], 'fing-er' = [ŋg]."
        ),
    },
    "tt": {
        "represents": ["t", "ɾ"],
        "examples": [("attic", "t"), ("butter", "ɾ"), ("matters", "ɾ"),
                     ("attest", "t")],
        "trap": (
            "[t] in many positions, but [ɾ] (tap) when between a "
            "stressed and unstressed vowel — butter, water, ladder. The "
            "spelling 'tt' doesn't change; the environment does."
        ),
    },
    "c": {
        "represents": ["k", "s", "ʃ"],
        "examples": [("cat", "k"), ("cell", "s"), ("ocean", "ʃ"),
                     ("cup", "k"), ("cycle", "s")],
        "trap": (
            "Hard [k] before a/o/u, soft [s] before e/i/y, and "
            "occasionally [ʃ] in -cean / -cious. One letter, three "
            "sounds — students who transcribe by spelling lose this."
        ),
    },
    "s": {
        "represents": ["s", "z", "ʃ", "ʒ"],
        "examples": [("sip", "s"), ("dogs", "z"), ("sure", "ʃ"),
                     ("measure", "ʒ"), ("rose", "z")],
        "trap": (
            "Most often [s] or [z] depending on voicing context, but "
            "also [ʃ] (sure, sugar) and [ʒ] (measure, vision, leisure). "
            "Plural -s is [z] after voiced sounds, [s] after voiceless."
        ),
    },
    "ti": {
        "represents": ["ʃ", "ti", "tʃ"],
        "examples": [("nation", "ʃ"), ("tiger", "ti"), ("question", "tʃ")],
        "trap": (
            "[ʃ] in -tion / -tia, plain [ti] in most other positions, "
            "and [tʃ] in -stion."
        ),
    },
    "wh": {
        "represents": ["w", "h"],
        "examples": [("what", "w"), ("who", "h"), ("whose", "h"),
                     ("when", "w")],
        "trap": (
            "Usually [w] (the h is silent), but in a small set "
            "(who, whose, whole, whore) the w is silent and it's [h]."
        ),
    },
    "gh": {
        "represents": ["", "f", "g"],
        "examples": [("through", "(silent)"), ("rough", "f"),
                     ("ghost", "g"), ("though", "(silent)"),
                     ("laugh", "f")],
        "trap": (
            "Usually silent (through, though, neighbor), sometimes [f] "
            "(rough, laugh, cough), sometimes [g] in initial position "
            "(ghost). Among English's worst spelling-sound mismatches."
        ),
    },
    "silent_letters": {
        "represents": [""],
        "examples": [("knee", "n"), ("knight", "naɪt"), ("psalm", "sɑm"),
                     ("comb", "kom"), ("lamb", "læm"), ("write", "ɹ"),
                     ("whole", "h"), ("hour", "aʊɹ")],
        "trap": (
            "Initial k before n, p before s/n, w before r, and silent "
            "h in some words. Final b after m. The IPA reflects what "
            "you say, not what's written."
        ),
    },
    "j_as_y": {
        "represents": ["j"],
        "examples": [("yes", "j"), ("yellow", "j"), ("you", "j")],
        "trap": (
            "The IPA symbol [j] is the y-glide sound at the start of "
            "'yes' — NOT the [dʒ] sound at the start of 'jug'. Looks "
            "like English 'j' but isn't."
        ),
    },
    "english_r": {
        "represents": ["ɹ"],
        "examples": [("red", "ɹ"), ("right", "ɹ"), ("very", "ɹ")],
        "trap": (
            "English 'r' is [ɹ] (rhotic approximant), NOT IPA [r] "
            "(which is the trill in Spanish, Italian, Scottish). Use "
            "[ɹ] when transcribing English."
        ),
    },
}

def get_features(symbol):
    """Return the full feature dict for a symbol, including derived fields, or None."""
    base = CONSONANTS.get(symbol)
    if not base:
        return None
    return {
        **base,
        "sonorant": base["manner"] in SONORANT_MANNERS,
        "obstruent": base["manner"] not in SONORANT_MANNERS,
        "continuant": base["manner"] in CONTINUANT_MANNERS,
    }


def features_that_differ(sym1, sym2):
    """Return a list of feature names where two consonants differ."""
    f1, f2 = get_features(sym1), get_features(sym2)
    if not f1 or not f2:
        return []
    return [feat for feat in ["place", "manner", "voicing"] if f1[feat] != f2[feat]]


def consonants_with(feature, value):
    """Return all consonant symbols whose feature matches the given value."""
    return [sym for sym in CONSONANTS if get_features(sym).get(feature) == value]


def describe_place(place):
    """Return the description for a place of articulation, or None."""
    entry = PLACES.get(place)
    return entry["description"] if entry else None


def describe_manner(manner):
    """Return the description for a manner of articulation, or None."""
    entry = MANNERS.get(manner)
    return entry["description"] if entry else None

if __name__ == "__main__":
    # Basic feature lookups
    assert get_features("p")["voicing"] == "voiceless"
    assert get_features("m")["sonorant"] is True
    assert get_features("s")["obstruent"] is True
    assert get_features("s")["continuant"] is True
    assert get_features("p")["continuant"] is False
    assert get_features("xyz") is None  # unknown symbol

    # Contrasts
    assert features_that_differ("p", "b") == ["voicing"]
    assert features_that_differ("s", "ʃ") == ["place"]

    # Lookups by feature
    assert set(consonants_with("manner", "nasal")) == {"m", "n", "ŋ"}
    assert "ŋ" in consonants_with("sonorant", True)

    # Descriptions
    assert describe_place("bilabial") == "upper and lower lip"
    assert describe_manner("stop").startswith("complete closure")

    # Cross-check: every consonant's place and manner exist in PLACES and MANNERS
    for sym, feats in CONSONANTS.items():
        assert feats["place"] in PLACES, f"Missing place entry: {feats['place']}"
        assert feats["manner"] in MANNERS, f"Missing manner entry: {feats['manner']}"

    print("ipa_consonants.py: all checks passed ✓")