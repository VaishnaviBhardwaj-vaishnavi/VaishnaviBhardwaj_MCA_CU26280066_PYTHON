products = {}

# Create
products[1] = {"name": "Laptop", "price": 50000}
products[2] = {"name": "Mouse", "price": 500}

# Read
print("Products:", products)

# Update
products[1]["price"] = 48000
print("Updated products:", products)

# Delete
del products[2]
print("Final products:", products)