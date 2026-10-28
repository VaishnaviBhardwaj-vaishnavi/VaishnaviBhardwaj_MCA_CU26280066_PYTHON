import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
)
""")

data = [
    (1, "Python"),
    (2, "Database"),
    (3, "Computer Networks")
]

cur.executemany("""
INSERT OR IGNORE INTO courses
(course_id, course_name)
VALUES (?, ?)
""", data)

con.commit()
print("Courses table created and data inserted!")
con.close()