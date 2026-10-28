import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")
con.commit()

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        try:
            cur.execute("""
            INSERT INTO students VALUES (?, ?, ?, ?)
            """, (sid, name, age, marks))
            con.commit()
            print("Student added successfully!")
        except sqlite3.Error as e:
            print("Error:", e)

    elif choice == "2":
        cur.execute("SELECT * FROM students")
        for row in cur.fetchall():
            print(row)

    elif choice == "3":
        sid = int(input("Enter Student ID: "))
        marks = float(input("Enter new marks: "))

        cur.execute("""
        UPDATE students SET marks = ? WHERE id = ?
        """, (marks, sid))
        con.commit()
        print("Marks updated successfully!")

    elif choice == "4":
        sid = int(input("Enter Student ID: "))

        cur.execute("DELETE FROM students WHERE id = ?", (sid,))
        con.commit()
        print("Student deleted successfully!")

    elif choice == "5":
        print("Exiting application...")
        break

    else:
        print("Invalid choice. Try again.")

con.close()