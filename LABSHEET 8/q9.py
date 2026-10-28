import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

data = [
    (2, "Priya", 19, 92),
    (3, "Rahul", 21, 76),
    (4, "Neha", 20, 88)
]

cur.executemany("""
INSERT INTO students (id, name, age, marks)
VALUES (?, ?, ?, ?)
""", data)

con.commit()
print("Multiple records inserted successfully!")
con.close()