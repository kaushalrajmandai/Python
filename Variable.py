a=10
print(type (a))
b=30
print(type(b))
c=None
print(type(c))
d=c
print(type(d))
f= 'String' 
print(type(f))

# Integer, Float, String, Boolean
a, b, c, d = 10, 3.14, "Hello", True

print(f"Integer: {a}, Type: {type(a)}")
print(f"Float: {b}, Type: {type(b)}")
print(f"String: {c}, Type: {type(c)}")
print(f"Boolean: {d}, Type: {type(d)}")

# Number word list
num = int (input("Enter a number:"))
word = str(input("Enter a word: "))
list_input = list(input("Enter list (like 1,2,3):"))

print("Type of num:", type (num))
print("Type of word:", type(word))
print("Type of list_input:", type(list_input))


# Program to check if two variables have the same data type


variable_one = 10        
variable_two = "hello"    

are_types_same = type(variable_one) is type(variable_two)

print(f"Variable One: Value='{variable_one}', Type={type(variable_one)}")
print(f"Variable Two: Value='{variable_two}', Type={type(variable_two)}")

if are_types_same:
    print(f"\nThe types are the same: {are_types_same}")
else:
    print(f"\nThe types are NOT the same: {are_types_same}")


# I
    n= eval(input("Enter what you want to assign in variable:"))
    print(type(n))


