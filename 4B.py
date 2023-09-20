def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, prev = 0, 0
    for char in roman:
        value = roman_dict[char]
        total += value - 2 * prev if value > prev else value
        prev = value
    return total

roman = input("Enter the Roman number: ")
print(f"Roman Number {roman} in Integer is: {roman_to_int(roman)}")
