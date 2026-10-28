f = open("data.txt", "r")
text = f.read()
f.close()

word = input("Enter word: ")
count = text.lower().split().count(word.lower())

print("Occurrence:", count)