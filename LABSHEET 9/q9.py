# Write student data
with open("students.txt", "w") as file:
    file.write("101,Aman,85\n")
    file.write("102,Neha,90\n")
    file.write("103,Rahul,78\n")

print("Student data saved successfully.")

# Read student data
with open("students.txt", "r") as file:
    print("Student Records:")
    print(file.read())