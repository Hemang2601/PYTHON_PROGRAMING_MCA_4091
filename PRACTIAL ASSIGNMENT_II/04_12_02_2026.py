def simple_interest(p, n, r=5.0):
    return (p * r * n) / 100

principal = float(input("Enter the Principal Amount : "))
years = float(input("Enter the Number of Years : "))
rate_input = input("Enter the Rate (press Enter to use default 5%) : ")
if rate_input == "":
    result = simple_interest(principal, years)
    print(f"\nUsing default rate of 5%.")
else:
    rate = float(rate_input)
    result = simple_interest(principal, years, rate)
print(f"The Simple Interest for {principal} is : {result}")