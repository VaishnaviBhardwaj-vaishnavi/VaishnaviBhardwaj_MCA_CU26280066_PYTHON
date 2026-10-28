import sqlite3
import csv

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([col[0] for col in cur.description])
    writer.writerows(rows)

print("Data exported to students.csv successfully!")
con.close()