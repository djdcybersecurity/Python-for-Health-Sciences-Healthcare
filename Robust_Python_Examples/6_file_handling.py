# Chapter 6: File Handling in Python
# Demonstrating file reading, writing, and appending

file_name = "patient_data.txt"

# Writing to a file
with open(file_name, "w") as file:
    file.write("Patient Name, Age, Diagnosis\n")
    file.write("John Doe, 45, Diabetes\n")

# Reading the file content
with open(file_name, "r") as file:
    content = file.readlines()

# Print file content
print("File Content:")
for line in content:
    print(line.strip())
