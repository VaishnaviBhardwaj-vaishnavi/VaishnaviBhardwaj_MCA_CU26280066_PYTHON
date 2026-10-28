import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id
""")

for row in cur.fetchall():
    print(row)

con.close()