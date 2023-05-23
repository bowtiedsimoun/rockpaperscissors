# importing the RANDINT function from the RANDOM library
from random import randint 

# list of possible plays for the computer and player
plays = ['Rock', 'Paper', 'Scissors']

while True:
    computer = plays[randint(0,2)]
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

print(f"Ending Program!")