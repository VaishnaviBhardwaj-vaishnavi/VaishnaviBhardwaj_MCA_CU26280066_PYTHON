import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(students)")
for column in cur.fetchall():
    print(column)

con.close()