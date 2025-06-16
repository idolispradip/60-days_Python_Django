# This code defines a function to calculate the factorial of a number.
# It takes an integer n as input and returns the factorial of n.

def factorial(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result
# ask user for input
number = int(input("Enter a number to calculate its factorial:"))
# check if the number is negative, zero, or positive
if number<0:
    print("sorry!, factorial does not exist for negative numbers")
elif number==0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {number} is {factorial(number)}")

