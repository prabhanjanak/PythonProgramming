fname = input("Enter your file name or path: ")
n = int(input("Enter the number of Lines: "))

with open(fname, "r") as file:
    data = file.read().splitlines()[:n]

print("\n".join(data))

word = input("\nEnter the word to count: ")
counting = sum(line.count(word) for line in data)
print(f"Word Found: {counting} times in file")
