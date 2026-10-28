import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")
print("Total records:", cur.fetchone()[0])

con.close()