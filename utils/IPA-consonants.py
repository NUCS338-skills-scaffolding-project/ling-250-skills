"""
Reference data for English consonants.
Source: Ling 250 Days 1-3 slides (Strori, Spring 2023).
"""

SONORANT_MANNERS = {"nasal", "approximant", "lateral", "tap"}
CONTINUANT_MANNERS = {"fricative", "approximant", "lateral"}

CONSONANTS = {
    # Bilabial
    "p":  {"place": "bilabial",      "manner": "stop",        "voicing": "voiceless",
           "example_word": "pet",        "spellings": ["p", "pp"]},
    "b":  {"place": "bilabial",      "manner": "stop",        "voicing": "voiced",
           "example_word": "bet",        "spellings": ["b", "bb"]},
    "m":  {"place": "bilabial",      "manner": "nasal",       "voicing": "voiced",
           "example_word": "mat",        "spellings": ["m", "mm"]},
    # Labiodental
    "f":  {"place": "labiodental",   "manner": "fricative",   "voicing": "voiceless",
           "example_word": "fat",        "spellings": ["f", "ff", "ph", "gh"]},
    "v":  {"place": "labiodental",   "manner": "fricative",   "voicing": "voiced",
           "example_word": "vat",        "spellings": ["v"]},
    # Dental
    "θ":  {"place": "dental",        "manner": "fricative",   "voicing": "voiceless",
           "example_word": "thing",      "spellings": ["th"]},
    "ð":  {"place": "dental",        "manner": "fricative",   "voicing": "voiced",
           "example_word": "this",       "spellings": ["th"]},
    # Alveolar
    "t":  {"place": "alveolar",      "manner": "stop",        "voicing": "voiceless",
           "example_word": "top",        "spellings": ["t", "tt"]},
    "d":  {"place": "alveolar",      "manner": "stop",        "voicing": "voiced",
           "example_word": "dog",        "spellings": ["d", "dd"]},
    "s":  {"place": "alveolar",      "manner": "fricative",   "voicing": "voiceless",
           "example_word": "sip",        "spellings": ["s", "ss", "c", "sc"]},
    "z":  {"place": "alveolar",      "manner": "fricative",   "voicing": "voiced",
           "example_word": "zip",        "spellings": ["z", "zz", "s"]},
    "n":  {"place": "alveolar",      "manner": "nasal",       "voicing": "voiced",
           "example_word": "nap",        "spellings": ["n", "nn", "kn", "gn"]},
    "ɾ":  {"place": "alveolar",      "manner": "tap",         "voicing": "voiced",
           "example_word": "butter",     "spellings": ["t", "tt", "d"]},
    "ɹ":  {"place": "alveolar",      "manner": "approximant", "voicing": "voiced",
           "example_word": "red",        "spellings": ["r", "rr", "wr"]},
    "l":  {"place": "alveolar",      "manner": "lateral",     "voicing": "voiced",
           "example_word": "lip",        "spellings": ["l", "ll"]},
    # Post-alveolar
    "ʃ":  {"place": "post-alveolar", "manner": "fricative",   "voicing": "voiceless",
           "example_word": "ship",       "spellings": ["sh", "ti", "ci", "ss"]},
    "ʒ":  {"place": "post-alveolar", "manner": "fricative",   "voicing": "voiced",
           "example_word": "measure",    "spellings": ["s", "si", "g"]},
    "tʃ": {"place": "post-alveolar", "manner": "affricate",   "voicing": "voiceless",
           "example_word": "chip",       "spellings": ["ch", "tch"]},
    "dʒ": {"place": "post-alveolar", "manner": "affricate",   "voicing": "voiced",
           "example_word": "jug",        "spellings": ["j", "g", "dg", "dge"]},
    # Palatal
    "j":  {"place": "palatal",       "manner": "approximant", "voicing": "voiced",
           "example_word": "yes",        "spellings": ["y", "i"]},
    # Velar
    "k":  {"place": "velar",         "manner": "stop",        "voicing": "voiceless",
           "example_word": "cat",        "spellings": ["k", "c", "ck", "ch", "q"]},
    "g":  {"place": "velar",         "manner": "stop",        "voicing": "voiced",
           "example_word": "go",         "spellings": ["g", "gg"]},
    "ŋ":  {"place": "velar",         "manner": "nasal",       "voicing": "voiced",
           "example_word": "sing",       "spellings": ["ng", "n"]},
    # Glottal
    "ʔ":  {"place": "glottal",       "manner": "stop",        "voicing": "voiceless",
           "example_word": "uh-oh",      "spellings": ["'"]},
    "h":  {"place": "glottal",       "manner": "fricative",   "voicing": "voiceless",
           "example_word": "hat",        "spellings": ["h"]},
    # Labio-velar
    "w":  {"place": "labio-velar",   "manner": "approximant", "voicing": "voiced",
           "example_word": "wet",        "spellings": ["w", "wh"]},
}