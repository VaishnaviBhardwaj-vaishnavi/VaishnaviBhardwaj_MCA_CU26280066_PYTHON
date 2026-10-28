f = open("data.txt", "r")
words = f.read().split()
f.close()

unique = list(dict.fromkeys(words))

f = open("unique.txt", "w")
f.write(" ".join(unique))
f.close()

print("Unique words saved.")