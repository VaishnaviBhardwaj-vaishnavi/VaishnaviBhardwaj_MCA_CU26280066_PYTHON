import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

roll = int(input("Enter roll number to search: "))

cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
student = cur.fetchone()

if student:
    print("Student found:", student)
else:
    print("Student not found.")

con.close()