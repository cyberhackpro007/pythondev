import random
from encodings import normalize_encoding

options = ("rock", "paper", "scissor")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissor) ? :")

    print(f"You choose : {player}.")
    print(f"Computer choose : {computer}.")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n) : ")
    if not play_again == "y":
        running = False



print("Thank you for playing!")


