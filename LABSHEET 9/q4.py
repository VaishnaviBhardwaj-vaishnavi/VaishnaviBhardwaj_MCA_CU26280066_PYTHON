students = [
    {"roll": 101, "name": "Aman", "marks": 85},
    {"roll": 102, "name": "Neha", "marks": 90}
]

roll = int(input("Enter roll number: "))
found = False

for student in students:
    if student["roll"] == roll:
        student["marks"] = int(input("Enter new marks: "))
        print("Marks updated successfully.")
        print(student)
        found = True
        break

if not found:
    print("Student not found.")