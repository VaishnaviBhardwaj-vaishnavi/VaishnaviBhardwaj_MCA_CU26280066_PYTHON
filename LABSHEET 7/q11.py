f = open("data.txt", "r")
text = f.read()
f.close()

word = input("Enter word to search: ")

if word.lower() in text.lower().split():
    print("Word found.")
else:
    print("Word not found.")