# ============================================================
#  Decision aid v3
# ============================================================

import json

# ============================================================
#  LOAD JSON FILES
# ============================================================

with open("symptoms.json") as f:
    symptom_data = json.load(f)

with open("diagnosis.json") as f:
    diagnosis_data = json.load(f)

# Symptom categories and flat list
SYMPTOM_CATEGORIES = symptom_data["symptoms"]

SYMPTOMS = []
for category, items in SYMPTOM_CATEGORIES.items():
    SYMPTOMS.extend(items)

DIAGNOSES = diagnosis_data["diagnoses"]
MODIFIERS = diagnosis_data.get("modifiers", {})
DEFAULTS = diagnosis_data.get("defaults", {})

DEFAULT_ABSENT_LIKELIHOOD = DEFAULTS.get("absent_symptom_likelihood", 0.01)


# ============================================================
#  FULL NAIVE BAYES ENGINE
# ============================================================

def compute_posterior(selected_symptoms, age_group, sex):
    selected = set(selected_symptoms)
    all_symptoms = set(SYMPTOMS)
    absent = all_symptoms - selected

    unnormalized = {}

    for diagnosis, info in DIAGNOSES.items():
        prior = info["prior"]

        # Apply age/sex modifiers
        prior *= MODIFIERS.get("age", {}).get(age_group, 1.0)
        prior *= MODIFIERS.get("sex", {}).get(sex, 1.0)

        likelihoods = info["likelihoods"]

        prob = prior

        # Present symptoms
        for s in selected:
            p = likelihoods.get(s, DEFAULT_ABSENT_LIKELIHOOD)
            prob *= p

        # Absent symptoms
        for s in absent:
            p = likelihoods.get(s, DEFAULT_ABSENT_LIKELIHOOD)
            prob *= (1 - p)

        unnormalized[diagnosis] = prob

    total = sum(unnormalized.values())
    if total == 0:
        return {d: 0.0 for d in unnormalized}

    return {d: p / total for d, p in unnormalized.items()}


# ============================================================
#  CATEGORY-DRIVEN SYMPTOM SELECTION (Version 2 UI)
# ============================================================

def choose_symptoms():
    selected = []

    while True:
        print("\nSelect a symptom category:")
        categories = list(SYMPTOM_CATEGORIES.keys())

        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        print(f"{len(categories)+1}. Done selecting symptoms")

        choice = input("> ").strip()

        if not choice.isdigit():
            print("Invalid input.")
            continue

        choice = int(choice)

        if choice == len(categories) + 1:
            break

        if choice < 1 or choice > len(categories):
            print("Invalid category.")
            continue

        category = categories[choice - 1]
        symptoms = SYMPTOM_CATEGORIES[category]

        print(f"\nSelect a symptom from {category}:")
        for i, s in enumerate(symptoms, 1):
            print(f"{i}. {s}")

        symptom_choice = input("> ").strip()

        if not symptom_choice.isdigit():
            print("Invalid input.")
            continue

        symptom_choice = int(symptom_choice)

        if symptom_choice < 1 or symptom_choice > len(symptoms):
            print("Invalid symptom.")
            continue

        selected_symptom = symptoms[symptom_choice - 1]
        selected.append(selected_symptom)

        print(f"Added: {selected_symptom}")

    return selected


# ============================================================
#  USER INTERFACE
# ============================================================

def main():
    print("=== Symptom Selection ===")
    selected = choose_symptoms()

    print("\nSelected symptoms:", selected)

    # Age group
    print("\nSelect age group (young, adult, older):")
    age_group = input("> ").strip().lower()
    if age_group not in MODIFIERS.get("age", {}):
        print("Invalid age group. Defaulting to 'adult'.")
        age_group = "adult"

    # Sex
    print("\nSelect sex (male, female):")
    sex = input("> ").strip().lower()
    if sex not in MODIFIERS.get("sex", {}):
        print("Invalid sex. Defaulting to 'male'.")
        sex = "male"

    # Compute posterior
    probs = compute_posterior(selected, age_group, sex)

    sorted_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    top5 = sorted_probs[:5]

    print("\nTop 5 diagnosis probabilities:")
    for diag, p in top5:
        print(f"{diag}: {p*100:.2f}%")


if __name__ == "__main__":
    main()
