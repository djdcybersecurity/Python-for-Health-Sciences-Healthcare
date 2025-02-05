# Codepad Coding Challenges
# Codepad is an interactive coding environment for solving programming challenges.

# Example: A simple challenge - Checking for even or odd numbers

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = 7
print(f"{num} is {check_even_odd(num)}.")
