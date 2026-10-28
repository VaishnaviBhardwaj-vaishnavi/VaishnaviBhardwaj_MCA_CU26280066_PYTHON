import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

try:
    cur.execute("ALTER TABLE students ADD COLUMN course_id INTEGER")
except sqlite3.OperationalError:
    pass

cur.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id
""")

for row in cur.fetchall():
    print(row)

con.close()