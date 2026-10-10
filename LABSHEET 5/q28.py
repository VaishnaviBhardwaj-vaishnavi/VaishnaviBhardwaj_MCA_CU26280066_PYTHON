t = (10, 20, 10, 30, 20, 40, 10)

repeated = tuple(x for x in set(t) if t.count(x) > 1)

print("Repeated items:", repeated)