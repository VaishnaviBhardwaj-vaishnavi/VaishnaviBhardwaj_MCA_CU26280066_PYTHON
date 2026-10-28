import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

try:
    cur.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (roll, name, marks)
    )
    con.commit()
    print("Record inserted successfully.")
except sqlite3.IntegrityError:
    print("Roll number already exists.")

con.close()