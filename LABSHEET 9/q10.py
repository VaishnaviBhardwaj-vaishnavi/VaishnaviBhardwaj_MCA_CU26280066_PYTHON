def read_records():
    try:
        with open("records.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.txt", "w") as f:
        for record in records:
            f.write(record + "\n")

while True:
    print("\n1. Add  2. View  3. Modify  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    records = read_records()

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        if any(r.split(",")[0] == roll for r in records):
            print("Roll number already exists.")
        else:
            records.append(f"{roll},{name},{marks}")
            save_records(records)
            print("Record added.")

    elif choice == "2":
        for record in records:
            print(record)

    elif choice == "3":
        roll = input("Enter roll number to modify: ")
        found = False

        for i, record in enumerate(records):
            data = record.split(",")
            if data[0] == roll:
                data[2] = input("Enter new marks: ")
                records[i] = ",".join(data)
                found = True
                break

        if found:
            save_records(records)
            print("Record modified.")
        else:
            print("Record not found.")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        new_records = [
            r for r in records if r.split(",")[0] != roll
        ]

        if len(new_records) < len(records):
            save_records(new_records)
            print("Record deleted.")
        else:
            print("Record not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")