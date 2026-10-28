import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("DELETE FROM students WHERE id = ?", (1,))

con.commit()
print("Student record deleted successfully!")
con.close()