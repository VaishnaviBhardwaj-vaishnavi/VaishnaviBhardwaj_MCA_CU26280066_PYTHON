f = open("data.txt", "r")
text = f.read()

print("Lines:", len(text.splitlines()))
print("Characters:", len(text))

f.close()