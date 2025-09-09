# Write a Python program that does the following

# 1. Takes two numbers as input from the user.

a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))

# 2. Operations

add = a + b
sub = a - b
multi = a * b

if b != 0:
    div = a / b
else:
    div = "cannot divide by 0"


# Output
print("Results:")
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", multi)
print("Division: ", div)

