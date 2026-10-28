import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("SELECT AVG(marks) FROM students")
print("Average marks:", cur.fetchone()[0])

con.close()