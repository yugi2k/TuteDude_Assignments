# Task 1: Create a Dictionary of Student Marks


# 1.   Creates a dictionary where student names are keys and their marks are values.
students = {
    "Arun": 45,
    "Balbir": 95,
    "Chinna": 70,
    "Anjali": 85,
    "Nikita": 50
}

stu_name = input("Enter the student's name: ") # Asks the user to input a student's name.

# output
if stu_name in students:
    print(f"{stu_name}'s marks: {students[stu_name]}")
else:
    print(f"Student not found.")
