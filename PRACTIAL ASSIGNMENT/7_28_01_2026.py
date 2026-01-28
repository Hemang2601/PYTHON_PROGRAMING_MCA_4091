a = ['Physics','Chemistry',1997,2000]
b = [1,2,3,4,5,6,7]

print("Original List A : ",a)
print("Original List B : ",b,"\n")

print("1.List Concatenation")
print(a+b,"\n")

print("2.Remove FirstList[3]")
print(f"Before Delete Element : {a}")
a.remove(a[3])
print(f"After Delete Element : {a}","\n")

print("3.Add Java in List1")
print(f"Before Adding Element : {a}")
a.append('Java')
print(f"After Adding Element : {a}","\n")

print("4.Update List2 as SecondList[3]=11")
print(f"Before Updating Element : {b}")
b[3] = 11
print(f"After Updating Element : {b}","\n")

print("5.Delete SecondList[2]")
print(f"Before Deleting Element : {b}")
del b[2]
print(f"After Deleting Element : {b}","\n")

print("6.Print Welcome to Marwadiuniversity 4 times")
print("Welcome to Marwadiuniversity\n"*4)

print("7 Slicing Oprations : FirstList[-2] , SecondList[1:3], FirstList[-1:-3]")
print(f"FirstList[-2] : {a[-2]}")
print(f"SecondList[1:3] : {a[1:3]}")
print(f"FirstList[-1:-3] : {a[-1:-3]}\n")

print("8.Find the Length of SecondList")
print(f"Length of SecondList : {len(b)}\n")

print("9.Find the Maximum Value of SecondList")
print(f"Maximum Value of SecondList : {max(b)}")

print("10.Find the Minimum Value of SecondList")
print(f"Minimum Value of SecondList : {min(b)}")

print("11.Use SecondList.append(2) = 100")
print(f"Before Adding Element : {a}")
print(f"After Adding Element : {a}","\n")
