def factorial(a):
    if a < 0:
        return -1
    elif a < 2:
        return 1
    else:
        return a * factorial(a - 1)

a = int(input("Enter a number : "))

if factorial(a) == -1:
    print("Invalid Input!")
else:
    print("Factorial of", a, "is :", factorial(a))