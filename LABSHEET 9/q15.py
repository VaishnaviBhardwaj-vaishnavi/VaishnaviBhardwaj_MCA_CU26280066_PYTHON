import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

roll = int(input("Enter roll number: "))
marks = float(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks = ? WHERE roll = ?",
    (marks, roll)
)
con.commit()

if cur.rowcount > 0:
    print("Marks updated successfully.")
else:
    print("Student not found.")

con.close()