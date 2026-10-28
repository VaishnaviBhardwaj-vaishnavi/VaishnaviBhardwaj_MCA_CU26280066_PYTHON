students = [
    {"roll": 101, "name": "Aman", "marks": 85},
    {"roll": 102, "name": "Neha", "marks": 90}
]

roll = int(input("Enter roll number to delete: "))

for student in students:
    if student["roll"] == roll:
        students.remove(student)
        print("Record deleted successfully.")
        break
else:
    print("Student not found.")

print(students)