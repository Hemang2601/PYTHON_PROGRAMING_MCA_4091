def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.\n")
        continue

    choice = input("Enter operation (+, -, *, /) or 'q' to quit : ")

    if choice.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break

    if choice == "+":
        print(f"{a} + {b} = {addition(a, b)}\n")
    elif choice == "-":
        print(f"{a} - {b} = {subtract(a, b)}\n")
    elif choice == "*":
        print(f"{a} * {b} = {multiplication(a, b)}\n")
    elif choice == "/":
        print(f"{a} / {b} = {division(a, b)}\n")
    else:
        print("Invalid operation. Please try again.\n")