# function: A function is a resuable block of code that performs a specific task.
# it helps to :
# 1. Avoid repeating the same code
# 2. make the program organized and clean 
# 3. make debugging easier

# How to define a function in python?
# we use the def keyword to define a function,
# syntax:
# def function_name():
    # block of code 
# example:
def greet():
    print("Hello! Welcome to python section Pradip!")
# How to call a function?
# we just write the function name followed by parentheses
greet()

# -> Function with parameters
# you can pass value to functions using parameters.
def greet(name):
    print("Hello," + name + "!")

greet("pradip")

# -> Function with return value
# Functions can also return valur using the return keyword.
# example:
def add(a,b):
    return a+b
result = add(10,2)
print(result)

# types of function in python:
# 1.built-in functions: Already available in python, like print(),len(),input()
# 2.User-defined functions: Functions you create yourself using def


