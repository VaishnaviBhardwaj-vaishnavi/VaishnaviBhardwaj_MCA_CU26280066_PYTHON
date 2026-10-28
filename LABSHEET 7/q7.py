f = open("data.txt", "w")

n = int(input("Enter number of lines: "))

for i in range(n):
    line = input("Enter a line: ")
    f.write(line + "\n")

f.close()
print("Lines saved successfully.")