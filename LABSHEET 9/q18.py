import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("SELECT * FROM students ORDER BY name ASC")
records = cur.fetchall()

print("Students sorted by name:")

for record in records:
    print(record)

con.close()