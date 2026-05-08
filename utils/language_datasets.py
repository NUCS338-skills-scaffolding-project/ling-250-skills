"""
language_datasets.py — cross-linguistic phonological data references.

Every language dataset that appears in the LING 250 slides, HWs, quizzes, or
midterm prep, with the canonical analysis. Used by `analyze_dist`,
`probe_min_pair`, `write_phon_rule`, and `id_natural_class` when they need
example data for instruction or for parallel-problem suggestions.

Data is structured for programmatic lookup by skills, but designed to read
cleanly as documentation.

Source tag legend:
- DAY_N      = Day N slides
- HW_N       = HW_N PDF
- QUIZ_N     = In-class quiz N
- MT1, MT2   = Midterm 1 / 2 study guide or review problems (KEY)
- ZSIGA      = Zsiga textbook practice exercises (KEY)
- PRAC_N     = Practicum N
"""

LANGUAGE_DATASETS = {
    # ──────────────────────────────────────────────────────────────────
    # Phoneme/allophone classics
    # ──────────────────────────────────────────────────────────────────
    "spanish_b_beta": {
        "language": "Spanish",
        "sounds": ["b", "β"],
        "status": "allophones",
        "distribution": "[b] word-initial or after nasal; [β] intervocalic",
        "ur": "/b/",
        "rule": "/b/ → [β] / V _ V",
        "process": "lenition",
        "data": [
            ("[bino]",  "wine"),
            ("[bonito]", "pretty"),
            ("[ambos]",  "both"),
            ("[laβa]",   "lava"),
            ("[saβer]",  "to know"),
        ],
        "sources": ["DAY_11"],
        "use_case": "canonical example of complementary distribution + lenition; introductory analyze_dist case",
    },
    "old_english_f_v": {
        "language": "Old English",
        "sounds": ["f", "v"],
        "status": "allophones",
        "distribution": "[v] between voiced sounds; [f] elsewhere",
        "ur": "/f/",
        "rule": "/f/ → [v] / [+voice] _ [+voice]",
        "process": "voicing assimilation",
        "sources": ["DAY_12"],
    },
    "ganda_r_l": {
        "language": "Ganda",
        "sounds": ["r", "l"],
        "status": "allophones",
        "distribution": "[r] after high front vowels; [l] elsewhere",
        "ur": "/l/",
        "rule": "/l/ → [r] / [+high +front V] _",
        "process": "assimilation",
        "sources": ["DAY_12"],
    },
    "korean_r_l": {
        "language": "Korean",
        "sounds": ["r", "l"],
        "status": "allophones",
        "distribution": "[r] in onset (before vowel); [l] in coda (before C or word-finally)",
        "ur": "/l/",
        "rule": "/l/ → [r] / __ V (in onset position)",
        "process": "n/a (positional)",
        "data": [
            ("[rupi]",   "ruby"),
            ("[kiri]",   "road"),
            ("[saram]",  "person"),
            ("[irumi]",  "name"),
            ("[ratio]",  "radio"),
            ("[mul]",    "water"),
            ("[pal]",    "big"),
            ("[seul]",   "Seoul"),
            ("[ilkop]",  "seven"),
            ("[ipalsa]", "barber"),
        ],
        "key_insight": "Conditioning environment is SYLLABLE POSITION, not adjacent segments. Important pattern.",
        "sources": ["MT2"],
        "use_case": "showcase for syllable-structural conditioning of allophonic distribution",
    },
    "hindi_b_bh": {
        "language": "Hindi",
        "sounds": ["b", "b̤"],
        "status": "separate phonemes",
        "distribution": "Both occur word-initially before vowels (overlapping #__a, #__i)",
        "evidence": "Minimal pairs",
        "data": [
            ("[bara]", "large"),
            ("[b̤ari]", "heavy"),
            ("[bina]", "without"),
            ("[b̤ir]",  "crowd"),
            ("[bori]", "sackcloth"),
            ("[b̤ɛd]",  "disagreement"),
            ("[bais]", "22"),
            ("[b̤əs]",  "buffalo"),
            ("[bap]",  "dad"),
            ("[b̤ag]",  "part"),
        ],
        "key_insight": "Overlapping distribution proves separate phonemes — minimal pairs not strictly required.",
        "sources": ["DAY_13", "MT2"],
        "use_case": "counterexample to 'if I can't tell two sounds apart, they must be allophones'",
    },
    "english_h_ng": {
        "language": "English",
        "sounds": ["h", "ŋ"],
        "status": "separate phonemes (NOT allophones, despite complementary distribution)",
        "distribution": "[h] only word-initial; [ŋ] only word-final",
        "why_not_allophones": "Phonetic similarity test fails — too dissimilar",
        "sources": ["DAY_11"],
        "use_case": "show that complementary distribution alone is insufficient; phonetic similarity required",
    },
    "swampy_cree_p_b": {
        "language": "Swampy Cree",
        "sounds": ["p", "b"],
        "status": "allophones",
        "distribution": "[p] word-initial, word-final, between Cs; [b] intervocalic",
        "ur": "/p/",
        "rule": "/p/ → [b] / V _ V",
        "process": "voicing assimilation (lenition)",
        "sources": ["DAY_13", "QUIZ_4", "HW_4"],
        "use_case": "canonical HW4 example; reused on Quiz 4",
    },
    "isthmus_zapotec_voicing": {
        "language": "Isthmus Zapotec",
        "sounds": ["voiced/voiceless stops"],
        "status": "allophones",
        "distribution": "voiceless after [s-] prefix; voiced elsewhere",
        "process": "neutralization after sibilant",
        "sources": ["DAY_13"],
    },

    # ──────────────────────────────────────────────────────────────────
    # Process-classification examples (from Day 12 + Zsiga key)
    # ──────────────────────────────────────────────────────────────────
    "japanese_s_palatalization": {
        "language": "Japanese",
        "sounds": ["s", "ʃ"],
        "status": "allophones",
        "rule": "/s/ → [ʃ] / __ [i]",
        "process": "place assimilation",
        "sources": ["DAY_12"],
    },
    "japanese_high_v_devoicing": {
        "language": "Japanese",
        "process": "voicing assimilation",
        "rule": "[+high V] → [-voice] / [-voice C] __ [-voice C]",
        "description": "high vowels devoice between voiceless consonants",
        "sources": ["ZSIGA"],
    },
    "hungarian_voicing_assim": {
        "language": "Hungarian",
        "process": "voicing assimilation",
        "rule": "/[+obs]/ → [α voice] / __ [α voice +obs]",
        "data": [("/ræs-bæn/", "[ræzbæn]")],
        "sources": ["DAY_12"],
    },
    "hungarian_dative_harmony": {
        "language": "Hungarian",
        "process": "vowel harmony (assimilation)",
        "description": "dative -nek/-nɑk by frontness of root vowels",
        "sources": ["ZSIGA"],
    },
    "latin_dissimilation": {
        "language": "Latin",
        "process": "dissimilation",
        "rule": "/-alis/ → [-aris] / [l]...# __",
        "data": [("regalis", "no l in stem"), ("popularis", "l in stem")],
        "sources": ["DAY_12"],
    },
    "lardil_w_insertion": {
        "language": "Lardil",
        "process": "epenthesis",
        "description": "[w] inserted between [i] and [u]",
        "sources": ["DAY_12"],
    },
    "ndebele_high_v_deletion": {
        "language": "Ndebele",
        "process": "deletion",
        "description": "high vowel deletion before [o]",
        "sources": ["DAY_12"],
    },
    "porteno_spanish_fortition": {
        "language": "Porteño Spanish",
        "process": "fortition",
        "rule": "/j/ → [ʒ] / σ[ __",
        "data": [("/lej-es/", "[leʒes]")],
        "sources": ["DAY_12"],
    },
    "scottish_gaelic_lenition": {
        "language": "Scottish Gaelic",
        "process": "lenition",
        "rule": "[+stop] → [+fricative] / V _ V",
        "data": [("/kle:-pok/", "[kle:vok]")],
        "sources": ["DAY_12"],
    },
    "hebrew_metathesis": {
        "language": "Hebrew",
        "process": "metathesis",
        "rule": "/hit-CV/ → [hiCt-V] when C is sibilant",
        "data": [("/hit-sakel/", "[histakel]")],
        "sources": ["DAY_12"],
    },

    # ──────────────────────────────────────────────────────────────────
    # Allomorph paradigms (the heart of HW4 and HW5)
    # ──────────────────────────────────────────────────────────────────
    "english_plural": {
        "language": "English",
        "morpheme": "plural -s",
        "allomorphs": ["[-s]", "[-z]", "[-əz]"],
        "ur": "/-z/",
        "rules": [
            "/-z/ → [-s] / [-voice] __  (voicing assimilation)",
            "Ø → [ə] / [+sibilant] __ /-z/  (epenthesis)",
        ],
        "data": [
            ("cat-s [kæts]",       "voiceless"),
            ("dog-s [dɔgz]",       "voiced"),
            ("bus-əz [bʌsəz]",     "after sibilant"),
            ("dish-əz [dɪʃəz]",    "after sibilant"),
        ],
        "sources": ["DAY_13", "HW_4"],
    },
    "english_past_tense": {
        "language": "English",
        "morpheme": "past tense -ed",
        "allomorphs": ["[-d]", "[-t]", "[-əd]"],
        "ur": "/-d/",
        "rules": [
            "/-d/ → [-t] / [-voice] __",
            "Ø → [ə] / [+alveolar +stop] __ /-d/",
        ],
        "data": [
            ("blame-d [bleɪmd]",    "voiced"),
            ("fix-ed [fɪkst]",      "voiceless"),
            ("seat-ed [sitəd]",     "after alveolar stop"),
            ("fade-d [feɪdəd]",     "after alveolar stop"),
        ],
        "sources": ["DAY_13"],
    },
    "english_in_prefix": {
        "language": "English",
        "morpheme": "negative prefix in-",
        "allomorphs": ["[ɪn-]", "[ɪl-]", "[ɪɹ-]", "[ɪm-]"],
        "ur": "/ɪn-/",
        "rules": [
            "/n/ → [α place] / __ [α place]  (place assimilation)",
        ],
        "data": [
            ("inaccessible, inequitable",   "[ɪn-] elsewhere"),
            ("illegal, illogical",           "[ɪl-] before [l]"),
            ("irrelevant, irresistible",     "[ɪɹ-] before [ɹ]"),
            ("impossible, immeasurable",     "[ɪm-] before bilabial"),
        ],
        "sources": ["DAY_13"],
        "use_case": "canonical multi-allomorph case driven by place assimilation",
    },
    "maltese_definite": {
        "language": "Maltese",
        "morpheme": "definite prefix",
        "allomorphs": ["[il-]", "[l-]", "[id-]", "[iz-]", "[in-]", "etc."],
        "ur": "/l-/",
        "rules": [
            "Ø → [i] / # __ /l/ + [+consonantal]  (epenthesis to repair illegal cluster)",
            "/l/ → [α coronal] / __ [α coronal]  (assimilation to following coronal)",
        ],
        "data": [
            ("[il-fellus]",  "the chicken"),
            ("[il-kelb]",    "the dog"),
            ("[l-omm]",      "the mother"),
            ("[l-aria]",     "the air"),
            ("[it-tin]",     "the fig (assim to t)"),
            ("[id-dawl]",    "the light (assim to d)"),
        ],
        "sources": ["HW_5"],
        "use_case": "HW5 anchor problem — phonemic-analysis-style on syllable-driven alternation",
    },
    "farsi_plural": {
        "language": "Farsi (Persian)",
        "morpheme": "plural -an",
        "allomorphs": ["[-an]", "[-gan]"],
        "ur_choice": "/-an/ + [g]-epenthesis IS simpler than /-gan/ + [g]-deletion",
        "rule": "Ø → [g] / V # __ [-an]  (epenthesis to break VV hiatus)",
        "process": "epenthesis",
        "sources": ["MT2"],
        "use_case": "parallel to Maltese for 'competing UR analysis' simplicity reasoning",
    },
    "dutch_diminutive": {
        "language": "Dutch",
        "morpheme": "diminutive -tjə",
        "allomorphs": ["[-jə]", "[-pjə]", "[-kjə]", "[-tjə]"],
        "ur": "/-tjə/",
        "rules": [
            "/-tjə/ → [-jə] / [-voice +obstruent] # __",
            "/-tjə/ → [-pjə] / [m] # __",
            "/-tjə/ → [-kjə] / [ŋ] # __",
            "/-tjə/ → [-tjə]  (elsewhere)",
        ],
        "data": [
            ("lax-jə",    "little laugh ([-jə] after voiceless obstruent)"),
            ("rim-pjə",   "little belt ([-pjə] after [m])"),
            ("konɪŋ-kjə", "little king ([-kjə] after [ŋ])"),
            ("re-tjə",    "little deer ([-tjə] elsewhere)"),
        ],
        "sources": ["ZSIGA"],
        "use_case": "stronger 4-allomorph parallel to Maltese; place assimilation + deletion",
    },

    # ──────────────────────────────────────────────────────────────────
    # Other process examples
    # ──────────────────────────────────────────────────────────────────
    "boston_linking_r": {
        "language": "Boston English",
        "process": "epenthesis",
        "rule": "Ø → [r] / V __ V (across word boundary)",
        "data": [("Cuba is", "Cuba[r] is an island")],
        "sources": ["ZSIGA"],
    },
    "english_th_fortition": {
        "language": "English (some dialects)",
        "process": "fortition",
        "rule": "[+continuant +interdental] → [-continuant +alveolar]",
        "data": [("this", "dis"), ("think", "tink")],
        "sources": ["ZSIGA"],
    },
    "serbo_croatian_epenthesis": {
        "language": "Serbo-Croatian",
        "process": "epenthesis",
        "description": "CVCC adjective stems → CVCaC unless V-initial suffix follows",
        "sources": ["ZSIGA"],
    },
    "moro_voicing_dissim": {
        "language": "Moro",
        "process": "dissimilation",
        "description": "locative prefix [ék-] before voiced C; [ég-] before voiceless C",
        "sources": ["ZSIGA"],
    },
    "english_support_to_sport": {
        "language": "English (casual speech)",
        "process": "deletion",
        "rule": "[ə + p] → Ø / [s] __ [ɔ]",
        "data": [("support", "sport")],
        "sources": ["ZSIGA"],
    },
    "kinyarwanda_u_to_w": {
        "language": "Kinyarwanda",
        "process": "fortition",
        "rule": "/u/ → [w] / __ [i]",
        "sources": ["ZSIGA"],
    },
    "kinyarwanda_b_after_m": {
        "language": "Kinyarwanda",
        "process": "place assimilation",
        "rule": "/β/ → [b] / [m] __",
        "sources": ["ZSIGA"],
    },
    "english_creak_before_glottal": {
        "language": "English (many dialects)",
        "process": "assimilation",
        "description": "sonorants creaky-voiced before glottal stop",
        "sources": ["ZSIGA"],
    },
    "aklanon_one_prefix": {
        "language": "Aklanon",
        "process": "place assimilation",
        "description": "/saŋ-/ 'one' assimilates final-C to stem-initial-C place",
        "data": [
            ("saŋkurot",  "little bit (velar before velar)"),
            ("sambilog",  "one inanimate (bilabial before bilabial)"),
        ],
        "sources": ["ZSIGA"],
    },
    "maga_rukai_v_harmony": {
        "language": "Maga Rukai",
        "process": "vowel harmony",
        "description": "prefix vowel alternates between mid and high",
        "sources": ["ZSIGA"],
    },

    # ──────────────────────────────────────────────────────────────────
    # Loanword / phonotactic repair (HW5)
    # ──────────────────────────────────────────────────────────────────
    "english_to_japanese_loanwords": {
        "language": "English → Japanese",
        "process": "epenthesis (loanword adaptation)",
        "data": [
            ("Christmas",   "kurisumasu"),
            ("control",     "kontorōru"),
            ("Merry Christmas", "mele kelikimaka (Hawaiian)"),
        ],
        "sources": ["DAY_14"],
    },
    "english_to_finnish_loanwords": {
        "language": "English → Finnish",
        "process": "loanword adaptation",
        "data": [("glass", "lasi"), ("strand", "ranta")],
        "sources": ["DAY_14"],
    },
}

# ──────────────────────────────────────────────────────────────────────
# Quick lookups
# ──────────────────────────────────────────────────────────────────────

def by_status(status):
    """Return dataset names where status matches.
    status: 'allophones', 'separate phonemes', etc."""
    return [name for name, d in LANGUAGE_DATASETS.items() if d.get("status") == status]

def by_process(process):
    """Return dataset names where process matches."""
    return [name for name, d in LANGUAGE_DATASETS.items()
            if d.get("process") == process or process in d.get("rules", [""])]

def by_source(source_tag):
    """Return dataset names that include the given source tag."""
    return [name for name, d in LANGUAGE_DATASETS.items()
            if source_tag in d.get("sources", [])]

def parallels_for(name):
    """Suggest parallel datasets for a given name (loose: same status or process)."""
    base = LANGUAGE_DATASETS.get(name)
    if base is None:
        return []
    candidates = set()
    if base.get("status"):
        candidates.update(by_status(base["status"]))
    if base.get("process"):
        candidates.update(by_process(base["process"]))
    candidates.discard(name)
    return list(candidates)


# ──────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert "spanish_b_beta" in LANGUAGE_DATASETS
    assert LANGUAGE_DATASETS["korean_r_l"]["status"] == "allophones"
    assert "hindi_b_bh" in by_status("separate phonemes")
    assert len(by_source("ZSIGA")) >= 5
    assert "spanish_b_beta" in parallels_for("swampy_cree_p_b")  # both lenition allophones
    print("language_datasets.py self-test passed.")
    print(f"  {len(LANGUAGE_DATASETS)} datasets")
    print(f"  Allophone examples: {len(by_status('allophones'))}")
    print(f"  Phoneme examples: {len(by_status('separate phonemes'))}")
    print(f"  Zsiga-sourced: {len(by_source('ZSIGA'))}")
