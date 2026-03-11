from services.medical_extractor import extract_medical_info
from services.triage_engine import triage
from services.summary_generator import generate_summary
from services.drug_checker import check_interactions


def process_consultation(text):

    # Extract medical information
    info = extract_medical_info(text)

    symptoms = info["symptoms"]
    medicines = info["medicines"]

    # Determine risk level
    risk = triage(symptoms)

    # Check medicine conflicts
    drug_check = check_interactions(medicines)

    # Generate summary
    summary = generate_summary(info)

    return {
        "medical_info": info,
        "risk_level": risk,
        "drug_check": drug_check,
        "summary": summary
    }