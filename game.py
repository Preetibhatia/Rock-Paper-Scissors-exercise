
#game.py
import random
import random_word



print ("Rock, Paper, Scissors, Shoot!")


#Capture Inputs
user_choice = input("Please choose one of the following options:'rock', 'paper' or 'scissors' (without the quote):")
print ("you chose: ", user_choice)

#Validate Inputs
options = ["rock","paper","scissors"]

if user_choice not in ["rock","paper","scissor"]:
    print("Invalid selection, Please try again")
    exit()


#Generate Computer Selection
print ("Generating.......")
computer_choice = random.choice(["rock","paper","scissor"])
print("Computer choice:", computer_choice)
#Determine  The winner

#display final outputs
