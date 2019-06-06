
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
#rock beats scissors
#paper beats rock
#scissors beat paper
#same selection is a tie

if user_choice == computer_choice:
    print ("It's a Tie!!")

elif user_choice == "rock" and computer_choice == "paper":
    print("paper")
elif user_choice == "rock" and computer_choice =="scissors":
    print("rock")

elif user_choice=="paper" and computer_choice=="rock":
    print("paper")  
elif user_choice=="paper" and computer_choice=="scissors":
    print("scissors")

elif user_choice=="scissors" and computer_choice=="rock":
    print("rock")
elif user_choice=="scissors" and computer_choice=="paper":
    print("scissors")

#display final outputs
