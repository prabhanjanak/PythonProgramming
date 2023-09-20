def convert_base(number, base_from, base_to):
    decimal = 0
    power = 0
    while number != 0:
        last_digit = number % 10
        decimal += last_digit * (base_from ** power)
        number //= 10
        power += 1
    if base_to == 10:
        return decimal
    else:
        return hex(decimal).upper()

b = int(input("Enter the binary number: "))
result_dec = convert_base(b, 2, 10)
print("In Decimal:", result_dec)

o = int(input("Enter the octal number: "))
result_hex = convert_base(o, 8, 16)
print("In Hexadecimal:", result_hex)
