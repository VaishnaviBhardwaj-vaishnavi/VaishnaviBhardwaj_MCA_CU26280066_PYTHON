import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

roll = int(input("Enter roll number to delete: "))

cur.execute("DELETE FROM students WHERE roll = ?", (roll,))
con.commit()

if cur.rowcount > 0:
    print("Record deleted successfully.")
else:
    print("Student not found.")

con.close()