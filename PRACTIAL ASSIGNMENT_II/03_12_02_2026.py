# Recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

a = int(input("Enter a Number for Factorial : "))
print(f"{a} for Factorial =  {factorial(a)}")


# Normal function
def factorial_noraml(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
b = int(input("Enter a Number for Factorial : "))
print(f"{b} for Factorial =  {factorial_noraml(b)}")