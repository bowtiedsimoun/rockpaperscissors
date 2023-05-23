# importing the RANDINT function from the RANDOM library
from random import randint 

# list of possible plays for the computer and player
plays = ['Rock', 'Paper', 'Scissors']

# MAIN CODEBASE
# WHILE TRUE is used to ensure that looping is activated and the program 
# continues indefinitely unless EXIT is entered by the player
while True:
    # the computer starts picking out its play from the PLAYS list
    computer = plays[randint(0,2)]
    # the player enters his play manually and a TITLE function is used
    # to ensure that the case of the COMPUTER PLAY and PLAYER PLAY is similar
    player = input("Please enter your play: ").title()
    if player == computer:
        print(f"It's a tie!")
    elif player == 'Rock':
        if computer == 'Scissors':
            print(f"You win! {player} beats {computer}")
        else:
            print(f"You lose! {computer} beats {player}")
    elif player == 'Paper':
        if computer == 'Rock':
            print(f"You win! {player} beats {computer}")
        else:
            print(f"You lose! {computer} beats {player}")
    elif player == 'Scissors':
        if computer == 'Paper':
            print(f"You win! {player} beats {computer}")
        else:
            print(f"You lose! {computer} beats {player}")
    elif player == 'Exit':
        break
    else:
 		print(f"Please enter a valid input")
		print(f"Only choose between Rock, Paper, Scissors, or Exit")

print(f"Ending Program!")
