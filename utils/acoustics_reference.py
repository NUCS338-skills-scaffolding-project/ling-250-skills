"""
acoustics_reference.py — F0 ranges, VOT, fricative energy, formant transitions,
and source-filter facts for HW3 / read_acoustic_trace.

Reference module. Data drawn from Day 5-7 slides + F0-Formants explainer
(instructor's own document) + standard phonetics references.
"""

# ──────────────────────────────────────────────────────────────────────
# Source-filter theory — the conceptual core
# ──────────────────────────────────────────────────────────────────────
SOURCE_FILTER_THEORY = {
    "source": {
        "anatomical_location": "vocal folds (glottis)",
        "produces": "complex periodic wave (F0 + harmonics)",
        "F0_perceived_as": "pitch",
        "F0_unit": "Hz (Hertz)",
        "harmonics": "integer multiples of F0",
        "harmonic_amplitude": "decreases as frequency increases (in source signal)",
    },
    "filter": {
        "anatomical_location": "supralaryngeal vocal tract",
        "function": "selectively amplifies harmonics matching its resonance shape",
        "resonance_shape_determined_by": "tongue position, lip rounding, jaw opening, velum position",
        "amplified_harmonics_called": "formants",
        "formant_naming": "F1 lowest, then F2, F3, ... (count up from bottom)",
    },
    "key_independence": {
        "claim": "F0 and formants are INDEPENDENT properties",
        "implication": "Same vowel at different F0 = same formant frequencies, different harmonic spacing",
        "proof": "A male and female speaker producing 'beat' [bit] both have low F1 and high F2 (formant pattern), but different F0s",
        "common_misconception": "Students conflate F0 (source) with F1 (filter). HIGH PRIORITY.",
    },
}

# ──────────────────────────────────────────────────────────────────────
# F0 ranges by speaker type (Hz)
# ──────────────────────────────────────────────────────────────────────
F0_RANGES = {
    "adult_male":   (85, 180),
    "adult_female": (165, 255),
    "child":        (250, 400),
}

# Concrete harmonic-spacing examples for the tutor to reference
# (Higher F0 → wider spacing — counterintuitive direction)
HARMONIC_SPACING_EXAMPLES = {
    "low_F0": {
        "F0_Hz": 150,
        "harmonics_Hz": [150, 300, 450, 600, 750, 900, 1050, 1200],
        "spacing_Hz": 150,
        "speaker_typical": "adult male, lower-pitched",
    },
    "high_F0": {
        "F0_Hz": 300,
        "harmonics_Hz": [300, 600, 900, 1200, 1500, 1800, 2100, 2400],
        "spacing_Hz": 300,
        "speaker_typical": "adult female or child",
    },
}

def nth_harmonic(n, f0):
    """Return Nth harmonic of fundamental F0. (5th harmonic of 110 Hz = 550 Hz.)"""
    return n * f0

# ──────────────────────────────────────────────────────────────────────
# Voice Onset Time (VOT) ranges in milliseconds
# ──────────────────────────────────────────────────────────────────────
# IMPORTANT: phrase-initial English voiced stops are typically zero/short-lag,
# NOT negative. Prevoicing is more reliable INTERVOCALICALLY. (Quiz 3 Q1.)
VOT_RANGES_MS = {
    "negative":  {
        "range":   (-150, -10),
        "label":   "prevoiced",
        "context": "intervocalic voiced stops in English; word-initial voiced stops in Spanish, French, etc.",
    },
    "zero_short_lag": {
        "range":   (0, 30),
        "label":   "unaspirated voiced or voiceless",
        "context": "English /b d g/ word-initial; English /p t k/ after [s] (e.g., 'spy', 'sty', 'sky')",
    },
    "long_lag": {
        "range":   (30, 100),
        "label":   "aspirated voiceless",
        "context": "English /pʰ tʰ kʰ/ word-initial / stressed-syllable-initial",
    },
}

# ──────────────────────────────────────────────────────────────────────
# Fricative energy patterns
# ──────────────────────────────────────────────────────────────────────
# Frequency ranges where each fricative's noise concentrates.
FRICATIVE_ENERGY = {
    "f":  {"distribution": "diffuse",       "concentration_Hz": None,         "place": "labiodental"},
    "v":  {"distribution": "diffuse",       "concentration_Hz": None,         "place": "labiodental"},
    "θ":  {"distribution": "diffuse",       "concentration_Hz": None,         "place": "interdental"},
    "ð":  {"distribution": "diffuse",       "concentration_Hz": None,         "place": "interdental"},
    "s":  {"distribution": "concentrated",  "concentration_Hz": (5000, 6000), "place": "alveolar"},
    "z":  {"distribution": "concentrated",  "concentration_Hz": (5000, 6000), "place": "alveolar"},
    "ʃ":  {"distribution": "concentrated",  "concentration_Hz": (2500, 3500), "place": "post-alveolar"},
    "ʒ":  {"distribution": "concentrated",  "concentration_Hz": (2500, 3500), "place": "post-alveolar"},
    "h":  {"distribution": "follows_vowel_formants", "concentration_Hz": None, "place": "glottal"},
}

# ──────────────────────────────────────────────────────────────────────
# Stop place of articulation diagnostics from formant transitions
# ──────────────────────────────────────────────────────────────────────
# Read formant transitions of the ADJACENT vowel to determine consonant POA.
STOP_FORMANT_TRANSITIONS = {
    "labial": {
        "stops": ["p", "b", "m"],
        "diagnostic": "ALL formant edges point DOWN going INTO the consonant",
        "intuition": "labial closure lowers all resonance frequencies",
    },
    "alveolar": {
        "stops": ["t", "d", "n"],
        "diagnostic": "F2 points UP toward ~1700 Hz (the 'alveolar locus')",
        "intuition": "alveolar tongue position raises F2 to a fairly fixed value",
    },
    "velar": {
        "stops": ["k", "g", "ŋ"],
        "diagnostic": "F2 and F3 converge ('velar pinch')",
        "intuition": "velar closure brings F2 and F3 toward each other",
    },
}

# ──────────────────────────────────────────────────────────────────────
# Nasal acoustic signature
# ──────────────────────────────────────────────────────────────────────
NASAL_FORMANTS_HZ = {
    "low_nasal_formant":  200,
    "high_nasal_formant": 2000,
    "diagnostic": "abrupt amplitude drop at nasal onset; place read from adjacent vowel formants",
}

# ──────────────────────────────────────────────────────────────────────
# Approximant signatures
# ──────────────────────────────────────────────────────────────────────
APPROXIMANT_SIGNATURES = {
    "l": {"diagnostic": "low F2; abrupt intensity change at boundary"},
    "ɹ": {"diagnostic": "very low F3 (this is THE diagnostic for English r)"},
    "w": {"diagnostic": "very similar to vowel [u] but lower amplitude"},
    "j": {"diagnostic": "very similar to vowel [i] but lower amplitude"},
}

# ──────────────────────────────────────────────────────────────────────
# Spectrogram axes and conventions
# ──────────────────────────────────────────────────────────────────────
SPECTROGRAM_AXES = {
    "x_axis": "time (left to right, in seconds or ms)",
    "y_axis": "frequency (bottom to top, in Hz)",
    "darkness": "amplitude / intensity (darker = louder at that frequency at that time)",
    "common_bandwidth": {
        "wide_band": "emphasizes formants (good for vowel identification)",
        "narrow_band": "shows individual harmonics (good for F0 estimation)",
    },
}

# ──────────────────────────────────────────────────────────────────────
# Hearing & speech frequency ranges
# ──────────────────────────────────────────────────────────────────────
HUMAN_HEARING_RANGE_HZ = (20, 20000)
SPEECH_FREQ_RANGE_HZ   = (50, 8000)  # most speech energy in the lower half

# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────

def vot_category(ms):
    """Given a VOT in ms, return the category label."""
    if ms < 0:
        return "negative"
    if ms < 30:
        return "zero_short_lag"
    return "long_lag"

def fricative_concentration(symbol):
    """Return concentration tuple (low_Hz, high_Hz) or None if diffuse."""
    f = FRICATIVE_ENERGY.get(symbol)
    if f is None:
        return None
    return f["concentration_Hz"]


# ──────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert nth_harmonic(5, 110) == 550
    assert vot_category(-50) == "negative"
    assert vot_category(15) == "zero_short_lag"
    assert vot_category(60) == "long_lag"
    assert fricative_concentration("s") == (5000, 6000)
    assert fricative_concentration("f") is None  # diffuse
    print("acoustics_reference.py self-test passed.")
