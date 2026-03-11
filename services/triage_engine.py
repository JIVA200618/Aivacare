def triage(symptoms):

    if "chest pain" in symptoms:
        return "HIGH"

    if "fever" in symptoms or "cough" in symptoms:
        return "MEDIUM"

    return "LOW"