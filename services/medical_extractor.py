def extract_medical_info(text):

    text = text.lower()

    symptoms = []
    medicines = []

    if "fever" in text:
        symptoms.append("fever")

    if "headache" in text:
        symptoms.append("headache")

    if "cough" in text:
        symptoms.append("cough")

    if "chest pain" in text:
        symptoms.append("chest pain")

    if "paracetamol" in text:
        medicines.append("paracetamol")

    if "aspirin" in text:
        medicines.append("aspirin")

    if "warfarin" in text:
        medicines.append("warfarin")

    return {
        "symptoms": symptoms,
        "medicines": medicines
    }