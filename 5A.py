import re

def is_phone_number(number):
    return bool(re.match(r'\d{3}-\d{3}-\d{4}', number))

n = input("Enter the number: ")
result = is_phone_number(n)
print("Number is valid with regular expression:", result)
