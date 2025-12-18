a = int(input("Enter first value (0 for False, any nonzero for True): "))
b = int(input("Enter second value (0 for False, any nonzero for True): "))

a = bool(a)
b = bool(b)

print("Results of Logical Operations:")
print("a and b →", a and b)
print("a or b  →", a or b)
print("not a   →", not a)
print("not b   →", not b)