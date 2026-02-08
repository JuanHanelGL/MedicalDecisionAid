# ============================================================
#  Decision aid v1
# ============================================================

DEFAULT_LIKELIHOOD = 0.01  # fallback for symptom|diagnosis not defined


# ------------------------------------------------------------
#  Full symptom list
# ------------------------------------------------------------
SYMPTOMS = [
    # Cardiopulmonary / Vascular / Respiratory
    "chest_pain_pressure", "chest_pain_pleuritic", "chest_tightness", "jaw_pain",
    "shortness_of_breath", "dyspnea_on_exertion", "palpitations",
    "feeling_of_impending_doom", "syncope", "near_syncope", "tachycardia",
    "bradycardia", "cyanosis", "tripoding", "sudden_onset_dyspnea",
    "unilateral_leg_swelling", "bilateral_leg_swelling", "calf_pain_tenderness",

    # Neurologic / Mental Status
    "disorientation", "confusion", "decreased_loc", "severe_headache_sudden",
    "progressive_headache", "dizziness", "vertigo", "photophobia",
    "cranial_nerve_deficit", "left_ue_weakness", "right_ue_weakness",
    "left_le_weakness", "right_le_weakness", "amnesia_surrounding_event",

    # Environmental / EVA-Specific
    "joint_pain", "skin_mottling_marbling", "neuropathy", "excessive_thirst",
    "heat_intolerance", "cold_intolerance",

    # Gastrointestinal / Abdominal
    "abdominal_pain_diffuse", "rlq_pain", "ruq_pain", "epigastric_pain",
    "pain_radiating_to_back_midline", "flank_pain", "nausea", "vomiting",
    "food_intolerance", "watery_diarrhea", "bloody_diarrhea", "anorexia",
    "abdominal_tenderness", "rebound_tenderness", "abdominal_distension",

    # Genitourinary
    "flank_pain_gu", "dysuria", "urinary_urgency", "urinary_frequency",
    "inability_to_urinate", "decreased_urine_output", "dark_colored_urine",
    "suprapubic_pain", "hematuria",

    # Musculoskeletal / Trauma
    "localized_bone_pain", "deformity_of_limb", "generalized_swelling",
    "limited_rom", "pain_with_movement", "joint_instability",
    "neck_muscle_tenderness", "midline_spinal_tenderness", "joint_catching",
    "pain_relieved_by_rest", "pain_worsened_with_activity", "pain_at_rest",

    # Skin / Soft Tissue / Eye
    "skin_redness", "skin_warmth", "laceration", "purulent_drainage",
    "foul_smelling_drainage", "burning_skin_pain", "blistering", "ulceration",
    "itchiness", "vision_loss", "blurred_vision", "eye_pain", "photopsia",

    # Infectious / Systemic
    "fever", "chills", "malaise", "fatigue", "myalgias", "productive_cough",
    "non_productive_cough", "pleuritic_cough", "sore_throat",
    "inspiratory_stridor", "expiratory_stridor",

    # Radiation / Hematologic / General
    "easy_bruising", "unexplained_bleeding",
]


# ------------------------------------------------------------
# Diagnosis, priors, likelihoods (need to get real values)
# ------------------------------------------------------------
# Likelihoods are currently just placeholders

LIKELIHOOD_MAP = {
    "always": 0.9,
    "usually": 0.7,
    "sometimes": 0.5,
    "might": 0.3,
}

DIAGNOSES = {
    "Acute Coronary Syndrome": {
        "prior": 0.05,
        "likelihoods": {
            "chest_pain_pressure": "always",
            "jaw_pain": "might",
            "shortness_of_breath": "sometimes",
            "nausea": "might",
            "tachycardia": "sometimes",
            "dizziness": "might",
        },
    },

    "Atrial Fibrillation / Atrial Flutter": {
        "prior": 0.03,
        "likelihoods": {
            "palpitations": "usually",
            "tachycardia": "usually",
            "dizziness": "might",
            "fatigue": "might",
            "shortness_of_breath": "sometimes",
        },
    },

    "Venous Thromboembolism": {
        "prior": 0.02,
        "likelihoods": {
            "unilateral_leg_swelling": "usually",
            "calf_pain_tenderness": "usually",
            "sudden_onset_dyspnea": "sometimes",
            "pleuritic_cough": "might",
        },
    },

    "Trauma - Chest Injury (blunt)": {
        "prior": 0.01,
        "likelihoods": {
            "chest_pain_pleuritic": "sometimes",
            "pain_with_movement": "sometimes",
            "high_mechanism": "usually",
        },
    },

    "Respiratory Tract Infection – Lower": {
        "prior": 0.06,
        "likelihoods": {
            "fever": "usually",
            "productive_cough": "usually",
            "pleuritic_cough": "sometimes",
            "fatigue": "sometimes",
            "chills": "might",
        },
    },

    "Trauma – Severe Head": {
        "prior": 0.01,
        "likelihoods": {
            "severe_headache_sudden": "sometimes",
            "decreased_loc": "usually",
            "amnesia_surrounding_event": "sometimes",
            "confusion": "might",
            "high_mechanism": "usually",
        },
    },

    "Headache": {
        "prior": 0.04,
        "likelihoods": {
            "progressive_headache": "usually",
            "photophobia": "might",
            "nausea": "might",
        },
    },

    "Headache – CO2 Induced": {
        "prior": 0.02,
        "likelihoods": {
            "progressive_headache": "sometimes",
            "fatigue": "might",
            "dizziness": "might",
        },
    },

    "EVA Related Decompression Sickness": {
        "prior": 0.01,
        "likelihoods": {
            "joint_pain": "usually",
            "skin_mottling_marbling": "sometimes",
            "neuropathy": "might",
        },
    },

    "EVA Related Dehydration": {
        "prior": 0.03,
        "likelihoods": {
            "excessive_thirst": "always",
            "dizziness": "sometimes",
            "fatigue": "sometimes",
            "decreased_urine_output": "usually",
        },
    },

    "Gravity Well – Entry Motion Sickness": {
        "prior": 0.02,
        "likelihoods": {
            "nausea": "usually",
            "vomiting": "sometimes",
            "dizziness": "sometimes",
        },
    },

    "Acute Radiation Syndrome": {
        "prior": 0.005,
        "likelihoods": {
            "nausea": "sometimes",
            "vomiting": "sometimes",
            "fatigue": "sometimes",
            "skin_redness": "might",
        },
    },

    "Appendicitis": {
        "prior": 0.03,
        "likelihoods": {
            "rlq_pain": "usually",
            "abdominal_tenderness": "usually",
            "rebound_tenderness": "sometimes",
            "anorexia": "might",
            "fever": "might",
        },
    },

    "Cholelithiasis / Biliary Colic": {
        "prior": 0.02,
        "likelihoods": {
            "ruq_pain": "usually",
            "epigastric_pain": "might",
            "pain_radiating_to_back_midline": "might",
        },
    },

    "Pancreatitis, Acute": {
        "prior": 0.01,
        "likelihoods": {
            "epigastric_pain": "usually",
            "pain_radiating_to_back_midline": "usually",
            "nausea": "sometimes",
            "vomiting": "sometimes",
        },
    },

    "Acute Gastroenteritis / Acute Diarrhea": {
        "prior": 0.05,
        "likelihoods": {
            "watery_diarrhea": "usually",
            "bloody_diarrhea": "might",
            "abdominal_pain_diffuse": "sometimes",
            "nausea": "sometimes",
            "vomiting": "might",
        },
    },

    "Nephrolithiasis": {
        "prior": 0.02,
        "likelihoods": {
            "flank_pain_gu": "usually",
            "hematuria": "sometimes",
            "nausea": "might",
        },
    },

    "Urinary Tract Infection": {
        "prior": 0.04,
        "likelihoods": {
            "dysuria": "usually",
            "urinary_urgency": "usually",
            "urinary_frequency": "usually",
            "suprapubic_pain": "sometimes",
            "fever": "might",
        },
    },

    "Space Adaptation – Urinary Retention": {
        "prior": 0.01,
        "likelihoods": {
            "inability_to_urinate": "usually",
            "suprapubic_pain": "sometimes",
            "decreased_urine_output": "usually",
        },
    },

    "Fracture – Arm": {
        "prior": 0.01,
        "likelihoods": {
            "localized_bone_pain": "usually",
            "deformity_of_limb": "usually",
            "pain_with_movement": "sometimes",
            "high_mechanism": "might",
        },
    },

    "Fracture – Hand": {
        "prior": 0.01,
        "likelihoods": {
            "localized_bone_pain": "usually",
            "deformity_of_limb": "might",
            "pain_with_movement": "sometimes",
        },
    },

    "Fracture – Lower Extremity": {
        "prior": 0.01,
        "likelihoods": {
            "localized_bone_pain": "usually",
            "deformity_of_limb": "usually",
            "generalized_swelling": "sometimes",
        },
    },

    "Dislocation – Shoulder": {
        "prior": 0.01,
        "likelihoods": {
            "joint_instability": "usually",
            "limited_rom": "sometimes",
            "pain_with_movement": "sometimes",
        },
    },

    "Sprain / Strain – Neck": {
        "prior": 0.02,
        "likelihoods": {
            "neck_muscle_tenderness": "usually",
            "pain_with_movement": "sometimes",
        },
    },

    "Sprain / Strain – Upper Extremity": {
        "prior": 0.02,
        "likelihoods": {
            "pain_with_movement": "sometimes",
            "limited_rom": "might",
        },
    },

    "Tendinopathy / Enthesopathy / Bursitis": {
        "prior": 0.02,
        "likelihoods": {
            "pain_worsened_with_activity": "usually",
            "pain_relieved_by_rest": "sometimes",
        },
    },

    "Trauma – Abdominal Injury (Blunt)": {
        "prior": 0.01,
        "likelihoods": {
            "abdominal_pain_diffuse": "sometimes",
            "abdominal_tenderness": "usually",
            "abdominal_distension": "might",
            "high_mechanism": "usually",
        },
    },

    "Burn – Chemical Skin": {
        "prior": 0.005,
        "likelihoods": {
            "burning_skin_pain": "usually",
            "blistering": "sometimes",
            "skin_redness": "sometimes",
        },
    },

    "Skin Infection – Bacterial": {
        "prior": 0.03,
        "likelihoods": {
            "skin_redness": "usually",
            "skin_warmth": "usually",
            "purulent_drainage": "usually",
            "foul_smelling_drainage": "sometimes",
            "fever": "might",
        },
    },

    "Eye – Retinal Injury": {
        "prior": 0.005,
        "likelihoods": {
            "vision_loss": "usually",
            "photopsia": "usually",
            "eye_pain": "sometimes",
        },
    },

    "Anaphylaxis": {
        "prior": 0.01,
        "likelihoods": {
            "shortness_of_breath": "usually",
            "itchiness": "usually",
            "skin_redness": "might",
        },
    },
}


# ------------------------------------------------------------
# Naive bayes
# ------------------------------------------------------------
def compute_probabilities(selected_symptoms):
    unnormalized = {}

    for diagnosis, info in DIAGNOSES.items():
        prob = info["prior"]

        for symptom in selected_symptoms:
            value = info["likelihoods"].get(symptom, DEFAULT_LIKELIHOOD)

            if isinstance(value, str):
                value = LIKELIHOOD_MAP[value]

            prob *= value

        unnormalized[diagnosis] = prob

    total = sum(unnormalized.values())
    if total == 0:
        return {d: info["prior"] for d, info in DIAGNOSES.items()}

    return {d: p / total for d, p in unnormalized.items()}


# ------------------------------------------------------------
# User input
# would it be better to start with a list of general symptoms?
# ------------------------------------------------------------
def main():
    print("Enter symptoms separated by commas (e.g., fever, dizziness):")
    # for testing purposes, will be changed to app UI
    user_input = input("> ")

    raw = [s.strip() for s in user_input.split(",") if s.strip()]
    selected = [s.lower().replace(" ", "_") for s in raw]

    valid = [s for s in selected if s in SYMPTOMS]
    invalid = [s for s in selected if s not in SYMPTOMS]

    if invalid:
        print("\nUnrecognized symptoms (ignored):", invalid)

    if not valid:
        print("\nNo valid symptoms entered. Using priors only.")

    print("\nUsing symptoms:", valid)

    probs = compute_probabilities(valid)
    sorted_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)

    print("\nDiagnosis probabilities:")
    for diag, p in sorted_probs:
        print(f"{diag}: {p*100:.1f}%")


if __name__ == "__main__":
    main()
