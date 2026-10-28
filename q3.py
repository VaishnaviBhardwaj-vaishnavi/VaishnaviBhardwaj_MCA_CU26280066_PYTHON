f = open("data.txt", "r")

for line in f:
    print(line, end="")

f.close()