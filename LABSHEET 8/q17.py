import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
UPDATE students SET name = ?
WHERE id = ?
""", ("Aman Sharma", 1))

con.commit()
print("Name updated successfully!")
con.close()