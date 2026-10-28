employees = {}

# Create
employees[101] = {"name": "Aman", "salary": 25000}
employees[102] = {"name": "Neha", "salary": 30000}

# Read
print("Employees:", employees)

# Update
employees[101]["salary"] = 28000
print("After update:", employees)

# Delete
del employees[102]
print("After deletion:", employees)