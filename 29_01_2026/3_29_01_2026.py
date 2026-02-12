n = float(input("Enter Percentage: "))

if 90 <= n <= 100:
    print("GRADE : O")
elif 80 <= n < 90:
    print("GRADE : A")
elif 70 <= n < 80:
    print("GRADE : B")
elif 60 <= n < 70:
    print("GRADE : C")
elif 50 <= n < 60:
    print("GRADE : D")
elif 0 <= n < 50:
    print("GRADE : FAIL")
else:
    print("Invalid Percentage")
