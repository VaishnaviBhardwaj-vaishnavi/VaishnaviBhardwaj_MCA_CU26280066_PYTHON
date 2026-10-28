import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

student_id = 1
new_marks = 95

cur.execute("""
UPDATE students SET marks = ?
WHERE id = ?
""", (new_marks, student_id))

con.commit()
print("Marks updated successfully!")
con.close()