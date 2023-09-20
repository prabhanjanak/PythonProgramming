word = input("Enter word or Number to check palindrome: ")
is_palindrome = word == word[::-1]
if is_palindrome:
    print(word, "is a palindrome word")
else:
    print(word, "is not a palindrome word")
for char in set(word):
    print(char, "IS OCCURED HERE :", word.count(char), "Times")
