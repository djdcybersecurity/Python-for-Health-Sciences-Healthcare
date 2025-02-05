# Chapter 7: Python Functions and Statements
# Demonstrating function usage, conditionals, and loops

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)"""
    return weight / (height ** 2)

# Using Loops
patients = {"John": (70, 1.75), "Jane": (55, 1.60), "Alex": (80, 1.85)}

for patient, (weight, height) in patients.items():
    bmi = calculate_bmi(weight, height)
    print(f"{patient}'s BMI: {bmi:.2f}")
