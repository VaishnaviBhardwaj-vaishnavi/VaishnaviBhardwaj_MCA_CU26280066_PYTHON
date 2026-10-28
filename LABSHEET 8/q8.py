import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
INSERT INTO students (id, name, age, marks)
VALUES (?, ?, ?, ?)
""", (1, "Aman", 20, 85))

con.commit()
print("Record inserted successfully!")
con.close()