# utils/glossary.py
"""Key terminology for Ling 250 Days 1-3."""

GLOSSARY = {
    "phonetics": "how speech sounds are produced and perceived, and which sounds are possible",
    "phonology": "how the sounds of a language work together as a system",
    "morphology": "how languages build words and indicate relationships between them",
    "syntax": "how words are organized into phrases and sentences",
    "semantics": "how words and sentences convey meaning",
    "pragmatics": "how context affects interpretation beyond literal meanings",
    "prosody": "the 'music of speech' — rhythm, stress, pitch, intonation, tone",
    "voicing": "state of the vocal folds — voiced means vibrating, voiceless means not",
    "place of articulation": "the location in the vocal tract where constriction of airflow occurs",
    "manner of articulation": "the type and degree of constriction that occurs",
    "airstream": "the movement of air that produces speech sound",
    "vowel": "a speech sound produced with little restriction of airflow",
    "consonant": "a speech sound produced with significant constriction or closure in the vocal tract",
    "obstruent": "a consonant with significant obstruction of airflow (stops, fricatives, affricates)",
    "sonorant": "a consonant with unobstructed airflow (nasals, approximants, laterals, taps)",
    "IPA": "International Phonetic Alphabet — one symbol per distinctive sound, same across languages",
    # extend as needed
}

def define(term):
    """Case-insensitive lookup."""
    return GLOSSARY.get(term.lower())