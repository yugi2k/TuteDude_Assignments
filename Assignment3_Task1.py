# Task 1: Calculate Factorial Using a Function 

# Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i   
    return fact # Returns the calculated factorial.


n = int(input("Enter a number: "))
result = factorial(n) # function calling

#output
print("Factorial of", n, "is", result)





