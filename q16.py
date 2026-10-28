f = open("data.txt", "r")
lines = f.readlines()
f.close()

if lines:
    print("First line:", lines[0], end="")
    print("Last line:", lines[-1], end="")
else:
    print("File is empty.")