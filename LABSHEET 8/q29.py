import sqlite3

def insert_data():
    con = sqlite3.connect("college.db")
    cur = con.cursor()

    cur.execute("""
    INSERT INTO students (id, name, age, marks)
    VALUES (?, ?, ?, ?)
    """, (10, "Riya", 20, 90))

    con.commit()
    con.close()
    print("Data inserted successfully!")

def fetch_data():
    con = sqlite3.connect("college.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)

    con.close()

insert_data()
fetch_data()