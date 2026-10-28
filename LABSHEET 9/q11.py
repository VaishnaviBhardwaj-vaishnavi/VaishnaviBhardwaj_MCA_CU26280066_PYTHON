import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks REAL
)
""")

con.commit()
print("Database connected and table created successfully.")

con.close()