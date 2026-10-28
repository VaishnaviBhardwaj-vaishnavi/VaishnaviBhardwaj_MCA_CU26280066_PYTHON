f = open("data.txt", "r")
text = f.read()
words = text.split()

print("Number of words:", len(words))
f.close()