# Input and Output in Python 
# *User Input -> you can take input from user using the input() function. 
# *Output -> To display information to the screen, use the print() function 
# Here's a simple python project that asks for the user's name and age, then displays greeting with their age in 5 years 
#ask for user's name and age 
name= input("Enter your name:")
age=int(input("Enter you current age:"))
# calculate future age
future_age = age+5
#display greeting with future age 
print(f"hi {name}, you are currently {age} years old.")
print(f" in 5 years you will be {future_age} years old.")



