"""
phonological_processes.py — the five-family taxonomy of phonological processes
(assimilation, dissimilation, fortition/lenition, epenthesis/deletion, metathesis)
with cross-linguistic examples.

Reference module. Drawn from Day 12 slides + Zsiga Ch. 11 + Zsiga textbook
practice exercises (KEY).

Used by `write_phon_rule`, `analyze_dist`, and `repair_misconceptions` (when
students mis-classify processes).
"""

# ──────────────────────────────────────────────────────────────────────
# The five families (canonical taxonomy)
# ──────────────────────────────────────────────────────────────────────

PHONOLOGICAL_PROCESSES = {
    "assimilation": {
        "definition": "making adjacent sounds more similar",
        "intuition": "the most common process cross-linguistically",
        "examples": [
            {
                "name": "English vowel nasalization",
                "rule": "V → [+nasal] / __ [+nasal]",
                "data": "can [kæ̃n], cat [kæt]",
                "type": "manner assimilation",
            },
            {
                "name": "English plural voicing",
                "rule": "/-z/ → [-s] / [-voice] __",
                "data": "cats [kæts], dogs [dɔgz]",
                "type": "voicing assimilation",
            },
            {
                "name": "English negative prefix",
                "rule": "/n/ → [α place] / __ [α place]",
                "data": "im-possible (bilabial), il-legal (alveolar lateral), ir-relevant (alveolar approximant)",
                "type": "place assimilation",
            },
            {
                "name": "Japanese /s/ palatalization",
                "rule": "/s/ → [ʃ] / __ [i]",
                "data": "/sushi/ → [ʃushi] (in some dialects)",
                "type": "place assimilation",
            },
            {
                "name": "Hungarian dative suffix vowel harmony",
                "rule": "suffix V → [α back] / [α back-V root] __",
                "data": "[-nek] after front-V words, [-nɑk] after back-V words",
                "type": "feature assimilation (vowel harmony)",
            },
            {
                "name": "Hungarian obstruent voicing assimilation",
                "rule": "/[+obs]/ → [α voice] / __ [α voice +obs]",
                "data": "/ræs-bæn/ → [ræzbæn]",
                "type": "voicing assimilation",
            },
            {
                "name": "Maltese coronal assimilation (HW5 Part B)",
                "rule": "/l/ → [α coronal] / __ [α coronal]",
                "data": "tin → ittin, dawl → iddawl",
                "type": "place assimilation (full assimilation)",
            },
            {
                "name": "Aklanon prefix",
                "rule": "/saŋ-/ → [sam-/saŋ-] / __ [α place]",
                "data": "saŋ-kurot, sam-bilog (place of stem-initial C)",
                "type": "place assimilation",
            },
            {
                "name": "Japanese high vowel devoicing",
                "rule": "[+high V] → [-voice] / [-voice C] __ [-voice C]",
                "data": "high vowels devoiced between voiceless Cs",
                "type": "voicing assimilation",
            },
            {
                "name": "Kinyarwanda place assimilation",
                "rule": "[β] → [b] / [m] __",
                "data": "fricative becomes stop after nasal (place to bilabial)",
                "type": "place assimilation",
            },
        ],
    },
    "dissimilation": {
        "definition": "making sounds less similar (the opposite of assimilation)",
        "intuition": "rare; often historical/lexicalized rather than productive",
        "examples": [
            {
                "name": "Latin -alis → -aris",
                "rule": "/l/ → [r] / [l]...# __",
                "data": "regalis (no l in stem), popularis (l in stem)",
                "type": "manner dissimilation",
            },
            {
                "name": "Moro locative prefix",
                "rule": "/k/ → [g] / __ [-voice C-stem]",
                "data": "[ék-] before voiced C; [ég-] before voiceless C",
                "type": "voicing dissimilation",
            },
        ],
    },
    "fortition": {
        "definition": "making consonants stronger (more obstruent / less sonorous)",
        "intuition": "less common than lenition; usually positionally triggered",
        "examples": [
            {
                "name": "Porteño Spanish [j] → [ʒ]",
                "rule": "/j/ → [ʒ] / σ[__",
                "data": "/lej-es/ → [leʒes]",
                "type": "syllable-onset fortition",
            },
            {
                "name": "Some English dialects [ð]/[θ] → [d]/[t]",
                "rule": "[+continuant +interdental] → [-continuant +alveolar]",
                "data": "this → dis, think → tink",
                "type": "manner fortition",
            },
            {
                "name": "Kinyarwanda [u] → [w]",
                "rule": "/u/ → [w] / __ [i]",
                "data": "vowel becomes glide (less sonorant) before another vowel",
                "type": "sonority-decreasing",
            },
        ],
    },
    "lenition": {
        "definition": "making consonants weaker (more sonorant / less obstruent)",
        "intuition": "very common, especially intervocalically",
        "examples": [
            {
                "name": "English flapping",
                "rule": "/[+alveolar +stop]/ → [ɾ] / V[+stress] __ V[-stress]",
                "data": "butter [bʌɾəɹ], water [wɑɾəɹ], ladder [læɾəɹ]",
                "type": "intervocalic lenition",
            },
            {
                "name": "Spanish stop lenition",
                "rule": "/[+voiced stop]/ → [+fricative] / V __ V",
                "data": "/abido/ → [aβiðo] (Spanish 'aware')",
                "type": "intervocalic lenition",
            },
            {
                "name": "Scottish Gaelic stop weakening",
                "rule": "[+stop] → [+fricative] / V __ V",
                "data": "/kle:-pok/ → [kle:vok]",
                "type": "intervocalic lenition",
            },
        ],
    },
    "epenthesis": {
        "definition": "inserting a sound to repair an illegal sequence",
        "intuition": "constrained by phonotactics — never random",
        "examples": [
            {
                "name": "English plural -əz",
                "rule": "Ø → [ə] / [+sibilant] __ [-z]",
                "data": "wishes [wɪʃəz], buses [bʌsəz], churches [tʃɝtʃəz]",
                "type": "vowel epenthesis to break sibilant cluster",
            },
            {
                "name": "English warmth",
                "rule": "Ø → [+stop] / [+nasal] __ [+fricative]",
                "data": "warmth [wɔɹmpθ], length [lɛŋkθ]",
                "type": "consonant epenthesis",
            },
            {
                "name": "Loanword cluster repair (English → Japanese)",
                "rule": "Ø → V / between illegal C clusters",
                "data": "Christmas → kurisumasu, control → kontorōru",
                "type": "vowel epenthesis (loanword adaptation)",
            },
            {
                "name": "Loanword cluster repair (Arabic → English)",
                "rule": "Ø → V / between illegal C clusters",
                "data": "al-jabr → algebra",
                "type": "vowel epenthesis",
            },
            {
                "name": "Boston English linking-r",
                "rule": "Ø → [r] / V __ V (across word boundary)",
                "data": "Cuba is → Cuba[r]is",
                "type": "consonant epenthesis to break vowel hiatus",
            },
            {
                "name": "Serbo-Croatian CVCC → CVCaC",
                "rule": "Ø → [a] / C __ C# (when no V-suffix follows)",
                "data": "adjective stem repair before consonants",
                "type": "vowel epenthesis",
            },
            {
                "name": "Maltese definite prefix /l-/ (HW5 Part A)",
                "rule": "Ø → [i] / # __ /l/ + [+consonantal]",
                "data": "/l-fellus/ → [il-fellus]; /l-omm/ → [l-omm]",
                "type": "vowel epenthesis (syllable repair)",
            },
            {
                "name": "Farsi pluralization",
                "rule": "Ø → [g] / [-V] # __ [-an]",
                "data": "[-gan] after V-final stems, [-an] elsewhere",
                "type": "consonant epenthesis (hiatus repair)",
            },
        ],
    },
    "deletion": {
        "definition": "removing a sound",
        "intuition": "common in casual speech; structurally repairs illegal sequences",
        "examples": [
            {
                "name": "English t/d deletion",
                "rule": "[+stop +alveolar] → Ø / [+consonantal] __ # [+consonantal]",
                "data": "best game → bes' game, sand paper → san' paper",
                "type": "consonant deletion",
            },
            {
                "name": "English support → sport",
                "rule": "[+V][+stop] → Ø / [+consonantal] __ [+stop]",
                "data": "support [səpɔɹt] → sport [spɔɹt] (casual speech)",
                "type": "vowel + consonant deletion",
            },
            {
                "name": "Ndebele high vowel deletion",
                "rule": "[+high V] → Ø / __ [o]",
                "data": "high vowels deleted before [o]",
                "type": "vowel deletion",
            },
        ],
    },
    "metathesis": {
        "definition": "exchanging the order of two sounds",
        "intuition": "rare productively; often lexicalized",
        "examples": [
            {
                "name": "Spanish miraculum → milagro",
                "rule": "[r]...[l] → [l]...[r]",
                "data": "Latin miraculum → Spanish milagro ('miracle')",
                "type": "consonant metathesis (historical)",
            },
            {
                "name": "Hebrew hit- prefix",
                "rule": "/hit-CV.../ → [hiCt-V...] when C is sibilant",
                "data": "/hit-sakel/ → [histakel]",
                "type": "productive metathesis",
            },
        ],
    },
}

# ──────────────────────────────────────────────────────────────────────
# Process classification helpers
# ──────────────────────────────────────────────────────────────────────

PROCESS_FAMILIES = list(PHONOLOGICAL_PROCESSES.keys())

# Heuristic patterns that indicate each process — useful when student
# describes an alternation in prose and the tutor needs to classify.
PROCESS_INDICATORS = {
    "assimilation": [
        "becomes more similar to",
        "matches the place of",
        "matches the voicing of",
        "matches the feature of",
        "agrees with",
        "becomes identical to",
    ],
    "dissimilation": [
        "becomes different from",
        "diverges from",
        "no longer matches",
    ],
    "fortition": [
        "becomes more obstruent",
        "becomes a stop from a fricative",
        "becomes a fricative from an approximant",
        "becomes stronger",
    ],
    "lenition": [
        "becomes more sonorant",
        "becomes a fricative from a stop",
        "becomes a flap from a stop",
        "becomes weaker",
    ],
    "epenthesis": [
        "is inserted",
        "appears between",
        "breaks up the cluster",
        "repairs the illegal sequence",
        "ø →",
        "Ø →",
        "ø \u2192",
        "Ø \u2192",
    ],
    "deletion": [
        "is deleted",
        "drops out",
        "disappears between",
        "→ Ø",
    ],
    "metathesis": [
        "switches places",
        "swaps with",
        "is reordered",
        "the order changes",
    ],
}

# ──────────────────────────────────────────────────────────────────────
# Quick lookups
# ──────────────────────────────────────────────────────────────────────

def family_of(rule_or_description):
    """Best-effort guess at process family from a rule or prose description.
    Returns a list of plausible families (often just one)."""
    text = rule_or_description.lower()
    candidates = []
    for family, indicators in PROCESS_INDICATORS.items():
        if any(ind in text for ind in indicators):
            candidates.append(family)
    return candidates

def examples_for(family):
    """Return the list of example dicts for a process family."""
    p = PHONOLOGICAL_PROCESSES.get(family)
    if p is None:
        return []
    return p["examples"]

def all_examples():
    """Return all examples across all families, with family annotation."""
    result = []
    for family, data in PHONOLOGICAL_PROCESSES.items():
        for ex in data["examples"]:
            result.append({**ex, "family": family})
    return result


# ──────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert "assimilation" in PROCESS_FAMILIES
    assert len(PROCESS_FAMILIES) == 7  # the five families, with fortition+lenition split
    assert len(examples_for("assimilation")) >= 5
    candidates = family_of("the [l] becomes identical to the following coronal")
    assert "assimilation" in candidates
    candidates2 = family_of("Ø → [i] / # __ [l]")
    assert "epenthesis" in candidates2
    print("phonological_processes.py self-test passed.")
    print(f"  {len(PROCESS_FAMILIES)} process families")
    print(f"  {len(all_examples())} total examples across all families")
