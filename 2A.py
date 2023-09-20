def fibonacci(n):
    return 0 if n == 1 else 1 if n == 2 else fibonacci(n - 1) + fibonacci(n - 2)
try:
    n = int(input("Enter the number: "))
    print("Fibonacci of", n, "is:", fibonacci(n))
except ValueError as error:
    print(error)
