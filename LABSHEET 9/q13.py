import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("SELECT * FROM students")
records = cur.fetchall()

for record in records:
    print(record)

con.close()