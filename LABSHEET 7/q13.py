f = open("numbers.txt", "r")
numbers = list(map(float, f.read().split()))
f.close()

if numbers:
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
else:
    print("No numbers found.")