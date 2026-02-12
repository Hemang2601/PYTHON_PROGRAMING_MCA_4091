def deposit(current_balance, amount):
    if amount > 0:
        current_balance += amount
        print(f"Successfully deposited {amount}")
    else:
        print("Deposit amount must be positive.")
    return current_balance


def withdraw(current_balance, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount <= current_balance:
        current_balance -= amount
        print(f"Successfully withdrew {amount}")
    else:
        print("Error: Insufficient Balance!")
    return current_balance


# Initialize balance
balance = 0

while True:
    print("--- Banking Menu ---")
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amt = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amt)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        try:
            amt = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amt)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "3":
        print(f"Current Balance: {balance}")

    elif choice == "4":
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid Choice. Please try again.")
    print()