# what is loop? 
# A loop means repeating some code again and again until a condition is met or for a fixed number of times .
# There are two types of loops in Python:
# 1. for loop
# 2. while loop

#1. for loop: -> The for loop repeats code for each item in a sequence(like a list, or range of number ).
# syntax:
# for varibale in sequence:
    # code to repeat
# Example:
# for i in range(5):
    # print("hello")
# Example2:
# print number 1 to 5
# for i in range(1,6):
    # print(i)

# 2 while loop: -> The while loop runs a block of code as long as the condtion is true.
# syntax:
# while condition:
#     code to repeat
# Example:
count = 1
while count <= 5:
    print("hello")
    count += 1  