data = [("A", 10), ("B", 20), ("C", 30)]

names, marks = zip(*data)

print("Names:", list(names))
print("Marks:", list(marks))