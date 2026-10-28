import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS students")

con.commit()
print("Students table deleted successfully!")
con.close()