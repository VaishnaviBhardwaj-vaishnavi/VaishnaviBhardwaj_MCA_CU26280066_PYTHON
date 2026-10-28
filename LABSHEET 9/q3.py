students = [
    {"roll": 101, "name": "Aman", "marks": 85},
    {"roll": 102, "name": "Neha", "marks": 90}
]

name = input("Enter student name: ")
found = False

for student in students:
    if student["name"].lower() == name.lower():
        print("Student found:", student)
        found = True

if not found:
    print("Student not found.")