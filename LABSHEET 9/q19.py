import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("""
SELECT * FROM students
WHERE marks = (SELECT MAX(marks) FROM students)
""")

student = cur.fetchone()

if student:
    print("Student with highest marks:", student)
else:
    print("No student records found.")

con.close()