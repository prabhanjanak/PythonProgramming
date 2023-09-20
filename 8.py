class PalindromeChecker:
    def is_palindrome(self, value):
        return str(value) == str(value)[::-1]

class SI_PalindromeChecker(PalindromeChecker):
    def is_palindrome(self, value):
        return super().is_palindrome(str(value))

def main():
    input_value = input("Enter a string or an integer: ")
    checker = SI_PalindromeChecker()
    result = "is" if checker.is_palindrome(input_value) else "is not"
    print(f"'{input_value}' {result} a palindrome.")

if __name__ == "__main__":
    main()
