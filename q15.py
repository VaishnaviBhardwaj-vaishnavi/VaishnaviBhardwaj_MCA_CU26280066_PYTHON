f = open("data.txt", "r")
text = f.read()
f.close()

old = input("Enter old word: ")
new = input("Enter new word: ")

text = text.replace(old, new)

f = open("data.txt", "w")
f.write(text)
f.close()

print("Word replaced successfully.")