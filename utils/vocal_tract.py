# utils/vocal_tract.py
"""
Anatomical reference for the vocal tract.
Source: Ling 250 Days 1-3 slides, instructor-provided overview.
"""

SUBSYSTEMS = {
    "sub-laryngeal": {
        "description": "lungs and trachea — provides the airstream",
        "components": ["lungs", "trachea"],
        "function": "supplies the airflow that becomes speech",
    },
    "laryngeal": {
        "description": "the larynx — where voicing and pitch are controlled",
        "components": ["larynx", "vocal cords", "glottis", "epiglottis"],
        "function": "controls voicing, pitch, and airstream modifications",
    },
    "supra-laryngeal": {
        "description": "three cavities above the larynx where sounds are shaped",
        "components": ["pharynx", "oral cavity", "nasal cavity"],
        "function": "shapes airflow into distinct speech sounds via constrictions",
    },
}

SUPRA_LARYNGEAL_CAVITIES = ["pharynx", "oral cavity", "nasal cavity"]

VOCAL_TRACT_PARTS = {
    "glottis": "the opening between the vocal cords",
    "larynx": "the 'voice box' where voicing is produced",
    "pharynx": "tubular part of the throat above the larynx",
    "oral cavity": "the mouth",
    "nasal cavity": "the nose and the passages connecting it to the throat and sinuses",
    "velum": "the soft palate; when lowered, air flows through the nasal cavity",
    "alveolar ridge": "the bony ridge just behind the upper teeth",
    "hard palate": "the hard roof of the mouth",
    "vocal cords": "the folds in the larynx that vibrate to produce voicing",
}

def get_subsystem(name):
    return SUBSYSTEMS.get(name)

def which_subsystem(component):
    """Given a component, return which subsystem it belongs to."""
    for subsystem, data in SUBSYSTEMS.items():
        if component in data["components"]:
            return subsystem
    return None

if __name__ == "__main__":
    assert which_subsystem("larynx") == "laryngeal"
    assert which_subsystem("lungs") == "sub-laryngeal"
    assert which_subsystem("pharynx") == "supra-laryngeal"
    assert len(SUPRA_LARYNGEAL_CAVITIES) == 3
    print("vocal_tract.py: all checks passed ✓")