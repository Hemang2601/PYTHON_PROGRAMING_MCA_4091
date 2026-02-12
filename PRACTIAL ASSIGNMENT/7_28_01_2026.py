a = ['Physics', 'Chemistry', 1997, 2000]
b = [1, 2, 3, 4, 5, 6, 7]

print("--- Original Lists ---")
print(f"a: {a}")
print(f"b: {b}\n")

# 1. List Concatenation
print("1. List Concatenation")
print(f"Result: {a + b}\n")

# 2. Remove a[3]
print("2. Remove element at index 3 from a")
print(f"Before: {a}")
a.pop(3)
print(f"After:  {a}\n")

# 3. Add 'Java' in a
print("3. Add 'Java' to a")
a.append('Java')
print(f"Result: {a}\n")

# 4. Update b[3] = 11
print("4. Update b at index 3 to 11")
print(f"Before: {b}")
b[3] = 11
print(f"After:  {b}\n")

# 5. Delete b[2]
print("5. Delete element at index 2 from b")
print(f"Before: {b}")
del b[2]
print(f"After:  {b}\n")

# 6. String Repetition
print("6. Repeat Welcome Message")
print("Welcome to Marwadi University\n" * 4)

# 7. Slicing Operations
print("7. Slicing Operations")
print(f"a[-2]      : {a[-2]}")
print(f"b[1:3]     : {b[1:3]}")
print(f"a[-1:-3:-1]: {a[-1:-3:-1]}\n")



# 8. Length of b
print("8. Length of List b")
print(f"Length: {len(b)}\n")

# 9. Maximum Value in b
print("9. Maximum Value in b")
print(f"Max: {max(b)}\n")

# 10. Minimum Value in b
print("10. Minimum Value in b")
print(f"Min: {min(b)}\n")

# 11. Append 100 to b
print("11. Append 100 to b")
b.append(100)
print(f"Result: {b}\n")

# 12. Extend a
print("12. Extend a with more elements")
a.extend(['Python', 'C++'])
print(f"Result: {a}\n")

# 13. Pop vs Remove
print("13. Pop (by index) vs Remove (by value)")
popped = b.pop(0)
b.remove(11)
print(f"Popped index 0 ({popped}) and removed value 11. Result: {b}\n")

# 14. Reverse and Sort
print("14. Reverse a and Sort b")
a.reverse()
b.sort()
print(f"a (Reversed): {a}")
print(f"b (Sorted):   {b}")