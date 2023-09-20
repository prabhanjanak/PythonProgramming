from difflib import SequenceMatcher as sm

str1, str2 = input("Enter the original string: "), input("Enter the string to check similarity: ")
similarity = sm(None, str1, str2).ratio()
print(f"Similarity: {similarity:.2%}")
