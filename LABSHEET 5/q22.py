t = ((1, 2), (3, 4), (5, 6))

flat = tuple(item for subtuple in t for item in subtuple)

print("Flattened tuple:", flat)