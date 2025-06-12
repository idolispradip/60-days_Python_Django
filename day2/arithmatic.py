# Arithmatic operators are used to perform basic mathematical operations. 
# The following are the arithmetic operators in Python:
# + (addition), - (subtraction), * (multiplication), / (division), % (modulus), ** (exponentiation), // (floor division)
# Example of using arithmetic operators in Python
# here's a simple python calculator that performs addition, subtraction, multiplication, and division based on user input:
# Basic calculator for +,-,*,/
# ask user for two numbers 
num1=float(input("Enter first number :"))
num2=float(input("Enter second number :"))
# ask user to choose an operation
print("choose an operation:")
operator=input("Enter operation:")
# perform calculation based on user input
if operator=="+":
    result = num1 + num2
    print("Result:",result)
elif operator=="-":
    result = num1 - num2
    print("Result:",result)
elif operator=="*":
    result = num1 * num2
    print("Result:",result)
elif operator=="/":
    if num2 != 0:
        result = num1 / num2
        print("Result:",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")

