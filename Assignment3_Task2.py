# Task 2: Using the Math Module for Calculations
 
import math

# 1.   Asks the user for a number as input.
numb = float(input("Enter a number: "))


# 2.   Uses the math module to calculate the:

sqrt_val = math.sqrt(numb)          # Square root
log_val = math.log(numb)            # Natural logarithm (log base e)
sine_val = math.sin(numb)           # Sine (in radians)

# output
print("\nResults:")
print("Square root: ", sqrt_val)
print("Logarithm: ", log_val)
print("Sine: ", sine_val)



