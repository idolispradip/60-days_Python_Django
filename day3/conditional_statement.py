# conditional statement -> A condtional statement lets your program make decisions.
# it checks a condition if its true , it run a block of code, if it's false, it can do something else,
# Type of conditional statements:
# 1.if statement
# 2.if else statement
# 3.if elif-else statement
# 4.nested if statement 

# 1.if statement
# syntax: if condition:
        # code to execute
#Example:
age=20
if age >=18:
    print("You are eligible to vote") 

# 2.if else statement
# syntax: if condition:
            #   code if true
        #else:
        # code if false
# Example:
age = 16
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# 3.if elif-else statement
# syntax: if condition1:
            # code if condition1 is true
        #elif condition2:
            # code if condition2 is true
        #else:
            # code if both conditions are false 
# Example:
marks = 75
if marks >= 90:
    print("Grade: A")       
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
# 4.nested if statement
# syntax: if condition1:
            # if condition2:
                # code if both conditions are true
            # else:
                # code if condition1 is true and condition2 is false
        # else:
            # code if condition1 is false
# Example:
age=25
citizenship = "Nepali"
if age>=18:
    if citizenship == "Nepali":
        print("You can apply for a national ID card")
    else:
        print("Foreign citizens not allowed.")
else:
    print("you are underage.")
    

