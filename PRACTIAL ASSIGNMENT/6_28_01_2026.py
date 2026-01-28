a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
c = int(input("Enter Value of C: "))
if a > b:
    if a > c:
        print(f"{a} is Maximum")
    else:
        print(f"{c} is Maximum")
else:
    if b > c:
        print(f"{b} is Maximum")
    else:
        print(f"{c} is Maximum")