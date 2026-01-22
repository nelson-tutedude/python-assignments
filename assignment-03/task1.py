# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result # 2.   Returns the calculated factorial.
    
number = int(input("Enter a number to calculate its factorial: "))

# 3.   Calls the function with a sample number and prints the output.
fact = factorial(number)

print(f"The factorial of {number} is {fact}")

