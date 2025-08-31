def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

i = int(input("Enter a number: "))
print("Factorial:", factorial(i))