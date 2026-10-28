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

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        try:
            cur.execute(
                "INSERT INTO students VALUES (?, ?, ?)",
                (roll, name, marks)
            )
            con.commit()
            print("Student added successfully.")
        except sqlite3.IntegrityError:
            print("Roll number already exists.")

    elif choice == "2":
        cur.execute("SELECT * FROM students")
        records = cur.fetchall()

        if records:
            for record in records:
                print(record)
        else:
            print("No records found.")

    elif choice == "3":
        roll = int(input("Enter roll number: "))
        marks = float(input("Enter new marks: "))

        cur.execute(
            "UPDATE students SET marks = ? WHERE roll = ?",
            (marks, roll)
        )
        con.commit()

        if cur.rowcount > 0:
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter roll number to delete: "))

        cur.execute("DELETE FROM students WHERE roll = ?", (roll,))
        con.commit()

        if cur.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")

con.close()