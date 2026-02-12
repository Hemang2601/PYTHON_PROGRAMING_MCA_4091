def maximum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
        pass
    else:
        if b > c:
            return b
        else:
            return c
        pass


f = int(input("Enter the First Number : "))
s = int(input("Enter the Second Number : "))
t = int(input("Enter the Third Number : "))
print(f"[{f}, {s}, {t}] Into Maxiumum Value = {maximum(f, s, t)}")
