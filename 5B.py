import re

file_path = input("Enter the file name or path: ")

with open(file_path, "r") as file:
    content = file.read()

matches = re.findall(r'\S+@\S{9}|\+\d{12}', content)

for match in matches:
    label = "Email" if '@' in match else "Phone Number"
    print(f"{label} found: {match}")
