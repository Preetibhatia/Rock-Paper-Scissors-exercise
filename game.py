
print ("Rock, Paper, Scissors, Shoot!")


#Capture Inputs
user_choice = input("Please choose one of the following options:'rock', 'paper' or 'scissors' (without the quote):")
print ("you chose: ", user_choice)

#Validate Inputs

if user_choice in ["rock","paper","scissor"]:
    print ("Valid")
else:
    print("Invalid selection, Please try again")
    exit()
#Generate Computer Selection
print ("Generating.......")
#Determine  The winner

#display final outputs
