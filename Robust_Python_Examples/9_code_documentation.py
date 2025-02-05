# Chapter 9: Code Documentation in Python
# Properly documenting code with comments and docstrings

def diagnose_patient(symptoms):
    """Determines the likely condition based on symptoms"""
    if "fever" in symptoms:
        return "Possible Infection"
    return "Consult a specialist"

# Example usage
print(diagnose_patient(["cough", "fever", "fatigue"]))
