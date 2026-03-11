def check_interactions(medicines):

    if "aspirin" in medicines and "warfarin" in medicines:
        return "Warning: Aspirin and Warfarin combination increases bleeding risk."

    if len(medicines) == 0:
        return "No medicines detected."

    return "No dangerous drug interaction detected."