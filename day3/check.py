# Project: Check if a number is even, odd, positive, negative, or zero.
# ask the user to enter a number 
num =int(input("Enter a number:"))
# check if the number is positive, negative,or zero 
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# now check if it's even or odd 
if num !=0:
    if num %2==0:
        print("It is an even number.")
    else:
        print("It is an odd number.")