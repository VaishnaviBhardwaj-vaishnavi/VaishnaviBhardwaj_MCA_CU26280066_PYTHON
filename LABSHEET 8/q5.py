import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table'
""")

for table in cur.fetchall():
    print(table[0])

con.close()