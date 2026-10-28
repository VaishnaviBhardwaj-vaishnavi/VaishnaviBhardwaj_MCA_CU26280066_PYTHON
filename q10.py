f = open("data.txt", "r")
text = f.read()
f.close()

print(text.upper())