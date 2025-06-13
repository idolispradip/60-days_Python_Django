# Project: Create a number guessing game.
# set a fixed number to guess
secret_number =7
# varibale to store user guess 
guess = 0
# Loop until user guesses the correct number 
while guess != secret_number:
    guess= int(input("Guess a number between 1 to 10:  "))
    if guess < secret_number:
        print("Too low!, Try again")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! Your guessed it .") 

