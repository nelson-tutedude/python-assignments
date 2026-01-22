
# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Ramesh": 85,
    "Nelson": 92,
    "Jay": 78,
    "Abdul": 90,
    "Narayan": 88,
    "Suresh": 76,
    "Aditya": 95,
    "Priya": 89,
    "Kavita": 91,
    "Anita": 84
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found.")