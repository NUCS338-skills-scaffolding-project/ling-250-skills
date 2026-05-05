"""
logic.py for diagnose-prerequisite-gaps

Two modes:
  - action="get_probes": returns an ordered list of diagnostic
    sub-probes for a prerequisite concept
  - action="summarize": given which sub-probes passed and which failed,
    returns a structured gap report

Design decision (same as validate-pre-knowledge): judgment is the
orchestrator's job. This skill holds the diagnostic structure — the
sequence of sub-probes and remediation hints — but does not score
student answers.
"""

# Diagnostic catalog for HW1 prerequisites (Days 1-3).
# Each concept has an ordered list of sub-probes from foundational to
# specific. The orchestrator asks them in order and stops at the first
# failure — that's the gap.
DIAGNOSTICS = {
    "voicing": [
        {
            "id": "vocal_folds_exist",
            "name": "Awareness of vocal folds as anatomy",
            "probe_question": (
                "Do you know what the vocal folds (or vocal cords) "
                "are, and roughly where they are in your body?"
            ),
            "what_to_listen_for": (
                "Student identifies the vocal folds as structures in "
                "the larynx/throat. Vague gesture toward the throat "
                "is acceptable."
            ),
            "remediation_hint": (
                "Teach the basic anatomy: vocal folds sit in the "
                "larynx ('voice box') at the top of the trachea. "
                "Ground the concept before introducing vibration."
            ),
        },
        {
            "id": "vibration_as_mechanism",
            "name": "Vibration as the voicing mechanism",
            "probe_question": (
                "Put your hand on your throat and say 'zzz' for a few "
                "seconds, then 'sss'. What do you feel that's different?"
            ),
            "what_to_listen_for": (
                "Student reports vibration/buzzing on [z] and not on "
                "[s]. Any phrasing that captures 'something is moving "
                "for one but not the other' counts."
            ),
            "remediation_hint": (
                "Teach vibration as the defining mechanism. Have the "
                "student produce minimal pairs ([s]/[z], [f]/[v], "
                "[p]/[b]) with a hand on the throat until the "
                "difference is reliable."
            ),
        },
        {
            "id": "voiced_voiceless_labels",
            "name": "Applying voiced/voiceless labels",
            "probe_question": (
                "We call [z] 'voiced' and [s] 'voiceless.' Can you "
                "classify [f] and [v] the same way?"
            ),
            "what_to_listen_for": (
                "Student correctly identifies [v] as voiced and [f] "
                "as voiceless, with reasoning tied to vibration."
            ),
            "remediation_hint": (
                "Drill a few more pairs with the label attached. The "
                "vocabulary is the gap, not the concept."
            ),
        },
    ],
    "place_of_articulation": [
        {
            "id": "constriction_concept",
            "name": "Understanding of constriction",
            "probe_question": (
                "When we talk about a consonant being 'constricted,' "
                "what do you think that means?"
            ),
            "what_to_listen_for": (
                "Student conveys that airflow is being narrowed, "
                "blocked, or obstructed in some way."
            ),
            "remediation_hint": (
                "Teach constriction as the foundational idea: "
                "consonants are made by restricting airflow somewhere "
                "in the vocal tract. Contrast with vowels, where "
                "airflow is relatively free."
            ),
        },
        {
            "id": "anatomical_location",
            "name": "Locating constriction anatomically",
            "probe_question": (
                "If I make the sound [p], where in my mouth is the "
                "constriction happening? What's touching what?"
            ),
            "what_to_listen_for": (
                "Student identifies the lips as the site of "
                "constriction for [p]. Any phrasing that gets the "
                "lips involved counts."
            ),
            "remediation_hint": (
                "Walk through the articulators: lips, teeth, alveolar "
                "ridge, hard palate, velum, glottis. Have the student "
                "feel their own mouth while producing a few "
                "consonants to ground the anatomy."
            ),
        },
        {
            "id": "naming_places",
            "name": "Naming specific places of articulation",
            "probe_question": (
                "We call the place of articulation for [p] 'bilabial' "
                "— because both lips are involved. What would you "
                "call the place for [t], where the tongue tip touches "
                "the ridge behind the upper teeth?"
            ),
            "what_to_listen_for": (
                "Student produces 'alveolar' (or close: 'the ridge "
                "one'). If they don't have the term but describe the "
                "anatomy correctly, the gap is vocabulary, not "
                "understanding."
            ),
            "remediation_hint": (
                "Teach the place-of-articulation vocabulary as labels "
                "for anatomy the student already understands. Use the "
                "IPA chart's place column."
            ),
        },
    ],
    "manner_of_articulation": [
        {
            "id": "place_vs_manner",
            "name": "Distinguishing place from manner",
            "probe_question": (
                "If place is *where* the constriction happens, what "
                "other kind of information do you think we need to "
                "fully describe a consonant?"
            ),
            "what_to_listen_for": (
                "Student reaches for the idea of *how* the sound is "
                "produced — the type of constriction, not just the "
                "location."
            ),
            "remediation_hint": (
                "Introduce manner by contrast with place. Same place "
                "can have different manners: [p] and [m] are both "
                "bilabial, but [p] is a stop and [m] is a nasal. "
                "Manner is the second axis."
            ),
        },
        {
            "id": "airflow_types",
            "name": "Recognizing airflow types",
            "probe_question": (
                "When you say [p], the airflow is completely blocked "
                "for a moment. When you say [s], the airflow is "
                "narrow but continuous. Can you describe what the "
                "airflow is doing for [m]?"
            ),
            "what_to_listen_for": (
                "Student identifies that air is flowing through the "
                "nose for [m] (nasal), or at least that it's not "
                "blocked the same way [p] is."
            ),
            "remediation_hint": (
                "Teach the manner inventory by airflow behavior: "
                "complete oral closure (stops), narrow channel "
                "(fricatives), stop+fricative (affricates), nasal "
                "escape (nasals), open passage (approximants)."
            ),
        },
        {
            "id": "naming_manners",
            "name": "Naming specific manners",
            "probe_question": (
                "Given what you just described, what would you call "
                "the manner of [p]? Of [s]? Of [m]?"
            ),
            "what_to_listen_for": (
                "Student produces 'stop' (or 'plosive'), 'fricative,' "
                "and 'nasal.' If terms are missing but the airflow "
                "descriptions are right, the gap is vocabulary."
            ),
            "remediation_hint": (
                "Attach the manner vocabulary to the airflow "
                "descriptions the student already understands."
            ),
        },
    ],
    "orthography_vs_pronunciation": [
        {
            "id": "spelling_as_unreliable",
            "name": "Recognizing that spelling is unreliable",
            "probe_question": (
                "Do you think the way a word is spelled always tells "
                "you exactly how it sounds in English?"
            ),
            "what_to_listen_for": (
                "Student says no (or something equivalent — "
                "'sometimes,' 'not really,' 'it's inconsistent')."
            ),
            "remediation_hint": (
                "Show examples: c in cat vs cell, gh in through vs "
                "cough, the silent b in lamb. The goal is for the "
                "student to feel the unreliability concretely."
            ),
        },
        {
            "id": "concrete_examples",
            "name": "Generating concrete examples",
            "probe_question": (
                "Can you think of two words where the same letter is "
                "pronounced differently, or the same sound is spelled "
                "differently?"
            ),
            "what_to_listen_for": (
                "Student produces any valid example. If they can't, "
                "the concept is abstract for them — they need more "
                "concrete instances."
            ),
            "remediation_hint": (
                "Do a guided example round: you provide one, they "
                "provide one, alternating. Build a small list until "
                "the pattern feels obvious."
            ),
        },
        {
            "id": "implication_for_ipa",
            "name": "Connecting to the need for IPA",
            "probe_question": (
                "Given that spelling is unreliable, why do you think "
                "linguists invented a separate system like the IPA?"
            ),
            "what_to_listen_for": (
                "Student reaches for the idea that IPA gives a "
                "reliable one-symbol-per-sound mapping, solving what "
                "spelling fails at."
            ),
            "remediation_hint": (
                "Teach the IPA principle directly: one symbol per "
                "distinctive sound, same symbol across words and "
                "languages."
            ),
        },
    ],
    "ipa_principle": [
        {
            "id": "ipa_as_representation",
            "name": "Recognizing IPA as a representation of sounds",
            "probe_question": (
                "What is the IPA — what does it represent?"
            ),
            "what_to_listen_for": (
                "Student identifies IPA as a system for representing "
                "sounds (not letters, not meanings)."
            ),
            "remediation_hint": (
                "Define IPA plainly: International Phonetic Alphabet, "
                "a system of symbols for speech sounds. Sounds — not "
                "letters, not words."
            ),
        },
        {
            "id": "one_sound_one_symbol",
            "name": "The one-sound-one-symbol principle",
            "probe_question": (
                "In the IPA, how many different symbols stand for a "
                "single distinctive sound? And how many sounds can "
                "one symbol represent?"
            ),
            "what_to_listen_for": (
                "Student conveys the one-to-one mapping: one symbol "
                "per sound, one sound per symbol. Any paraphrase is "
                "fine."
            ),
            "remediation_hint": (
                "Teach the principle with contrast: in English "
                "spelling, 'sh' spells one sound but is two letters, "
                "and 'c' spells multiple sounds. In IPA, [ʃ] is one "
                "symbol for one sound, always."
            ),
        },
        {
            "id": "cross_language_consistency",
            "name": "Consistency across words and languages",
            "probe_question": (
                "If the same IPA symbol appears in two different "
                "English words, or in an English word and a French "
                "word, does it represent the same sound?"
            ),
            "what_to_listen_for": (
                "Student says yes — the symbol means the same sound "
                "regardless of language or word."
            ),
            "remediation_hint": (
                "Reinforce with an example: [m] in English 'mat,' "
                "French 'mer,' and Spanish 'mar' all represent the "
                "same bilabial nasal."
            ),
        },
    ],
}


def run(input):
    """
    Main entry point.

    :param input: dict with `action` and `concept`. For summarize,
                  also sub_concepts_passed and sub_concept_failed.
    :return: dict shaped per skills.md
    """
    action = input.get("action")
    concept = input.get("concept")

    if action not in ("get_probes", "summarize"):
        return _error(
            action, concept,
            "action must be 'get_probes' or 'summarize'."
        )

    if concept is None:
        return _error(action, concept, "concept is required.")

    sub_probes = DIAGNOSTICS.get(concept)
    if sub_probes is None:
        return _error(
            action, concept,
            f"Unknown concept: {concept!r}. "
            f"Known: {list(DIAGNOSTICS.keys())}"
        )

    if action == "get_probes":
        return {
            "action": "get_probes",
            "concept": concept,
            "sub_probes": [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "probe_question": p["probe_question"],
                    "what_to_listen_for": p["what_to_listen_for"],
                }
                for p in sub_probes
            ],
            "error": None,
        }

    # action == "summarize"
    passed_ids = input.get("sub_concepts_passed", [])
    failed_id = input.get("sub_concept_failed")

    if not isinstance(passed_ids, list):
        return _error(
            action, concept,
            "sub_concepts_passed must be a list of sub-probe IDs."
        )

    valid_ids = {p["id"] for p in sub_probes}
    unknown = [pid for pid in passed_ids if pid not in valid_ids]
    if unknown:
        return _error(
            action, concept,
            f"Unknown sub-probe IDs in sub_concepts_passed: {unknown}"
        )
    if failed_id is not None and failed_id not in valid_ids:
        return _error(
            action, concept,
            f"Unknown sub-probe ID in sub_concept_failed: {failed_id!r}"
        )

    strengths = [
        {"id": p["id"], "name": p["name"]}
        for p in sub_probes if p["id"] in passed_ids
    ]

    if failed_id is None:
        gap = None
    else:
        failed_probe = next(p for p in sub_probes if p["id"] == failed_id)
        gap = {
            "id": failed_probe["id"],
            "name": failed_probe["name"],
            "remediation_hint": failed_probe["remediation_hint"],
        }

    return {
        "action": "summarize",
        "concept": concept,
        "gap": gap,
        "strengths": strengths,
        "error": None,
    }


def list_concepts():
    """Return all concept IDs with sub-probe counts."""
    return [
        {"concept": c, "sub_probe_count": len(probes)}
        for c, probes in DIAGNOSTICS.items()
    ]


def _error(action, concept, msg):
    return {
        "action": action,
        "concept": concept,
        "error": msg,
    }


if __name__ == "__main__":
    # --- get_probes mode ---
    r = run({"action": "get_probes", "concept": "place_of_articulation"})
    assert r["action"] == "get_probes"
    assert r["concept"] == "place_of_articulation"
    assert len(r["sub_probes"]) == 3
    assert r["sub_probes"][0]["id"] == "constriction_concept"
    assert r["sub_probes"][1]["id"] == "anatomical_location"
    assert r["sub_probes"][2]["id"] == "naming_places"
    assert all("probe_question" in p and "what_to_listen_for" in p
               for p in r["sub_probes"])
    assert r["error"] is None

    # sub_probes returned do NOT include remediation_hint (orchestrator
    # doesn't need it until summarize)
    assert all("remediation_hint" not in p for p in r["sub_probes"])

    # Each of the 5 concepts works
    for cid in DIAGNOSTICS.keys():
        r = run({"action": "get_probes", "concept": cid})
        assert r["error"] is None
        assert len(r["sub_probes"]) >= 2

    # Unknown concept
    r = run({"action": "get_probes", "concept": "vowel_harmony"})
    assert r["error"] is not None

    # --- summarize mode: gap identified partway through ---
    r = run({
        "action": "summarize",
        "concept": "place_of_articulation",
        "sub_concepts_passed": ["constriction_concept"],
        "sub_concept_failed": "anatomical_location",
    })
    assert r["action"] == "summarize"
    assert r["gap"] is not None
    assert r["gap"]["id"] == "anatomical_location"
    assert "articulators" in r["gap"]["remediation_hint"].lower()
    assert len(r["strengths"]) == 1
    assert r["strengths"][0]["id"] == "constriction_concept"
    assert r["error"] is None

    # --- summarize mode: all passed, no gap ---
    r = run({
        "action": "summarize",
        "concept": "voicing",
        "sub_concepts_passed": ["vocal_folds_exist",
                                "vibration_as_mechanism",
                                "voiced_voiceless_labels"],
        "sub_concept_failed": None,
    })
    assert r["gap"] is None
    assert len(r["strengths"]) == 3
    assert r["error"] is None

    # --- summarize mode: first sub-probe failed ---
    r = run({
        "action": "summarize",
        "concept": "voicing",
        "sub_concepts_passed": [],
        "sub_concept_failed": "vocal_folds_exist",
    })
    assert r["gap"]["id"] == "vocal_folds_exist"
    assert r["strengths"] == []

    # --- summarize mode: invalid sub-probe id in passed list ---
    r = run({
        "action": "summarize",
        "concept": "voicing",
        "sub_concepts_passed": ["not_a_real_id"],
    })
    assert r["error"] is not None

    # --- summarize mode: invalid failed id ---
    r = run({
        "action": "summarize",
        "concept": "voicing",
        "sub_concepts_passed": [],
        "sub_concept_failed": "bogus",
    })
    assert r["error"] is not None

    # --- summarize mode: sub_concepts_passed not a list ---
    r = run({
        "action": "summarize",
        "concept": "voicing",
        "sub_concepts_passed": "vocal_folds_exist",
    })
    assert r["error"] is not None

    # --- invalid action ---
    r = run({"action": "teleport", "concept": "voicing"})
    assert r["error"] is not None

    # --- missing action ---
    r = run({"concept": "voicing"})
    assert r["error"] is not None

    # --- missing concept ---
    r = run({"action": "get_probes"})
    assert r["error"] is not None

    # --- list_concepts returns all 5 ---
    all_c = list_concepts()
    assert len(all_c) == 5
    assert all("concept" in c and "sub_probe_count" in c for c in all_c)

    print("diagnose-prerequisite-gaps/logic.py: all checks passed ✓")