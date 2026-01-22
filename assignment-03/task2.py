# 1.   Asks the user for a number as input.
number = int(input("Enter a number: "))

# 2.   Uses the math module to calculate the:
# 	o   Square root of the number
# 	o   Natural logarithm (log base e) of the number
# 	o   Sine of the number (in radians)

import math
square_root = math.sqrt(number)
natural_log = math.log(number)  
sine_value = math.sin(number)

# 3.   Displays the calculated results.
print(f"Square root of {number} is {square_root}")
print(f"Natural logarithm of {number} is {natural_log}")
print(f"Sine of {number} is {sine_value}")