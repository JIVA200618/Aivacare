def generate_summary(data):

    symptoms = ", ".join(data["symptoms"])
    medicines = ", ".join(data["medicines"])

    summary = f"""
Patient Symptoms: {symptoms}

Current Medicines: {medicines}
"""

    return summary