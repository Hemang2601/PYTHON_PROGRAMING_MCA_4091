vowels = ['a', 'e', 'i', 'o', 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
a = input("Enter a string: ")
count = 0
for ch in a:
    if ch in vowels:
        count += 1
print(f"{a} : {count} vowels")

count = 0
for i in a:
    count = count + 1
print(f"Length of String: {count}")


