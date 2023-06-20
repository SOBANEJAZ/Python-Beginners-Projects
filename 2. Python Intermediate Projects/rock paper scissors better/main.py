# rock paper scissors game in python

import random

# Available options for the game
options = ["rock", "paper", "scissors"]

# Variables to control the game
playing = True
j = 0  # Round count
p_points = 0  # Player points
c_points = 0  # Computer points

# Game instructions and setup
print(
    """\t It is a rock paper scissors game  
     \t and its a five round match\n"""
)

while playing:
    j += 1  # Increment round count
    player = None  # Player's choice
    computer = random.choice(options)  # Randomly select computer's choice

    # Display current score
    print(
        f""" your points:
               ┌───────────────┐┌───────────────┐
               │  YOU          ││  COMPUTER     │
               └───────────────┘└───────────────┘
               │{p_points:02}             ││{c_points:02}             │
               │               ││               │
               └───────────────┘└───────────────┘
               """
    )

    # Prompt the player to choose
    while True:
        player = input("please choose (rock, paper, scissors): ")
        if player in options:
            break
        else:
            print("please choose from these three (rock, paper, scissors)")

    # Display the player's and computer's choices
    print(f"You: {player} \t computer: {computer}")

    # Determine the outcome of the round
    if player == computer:
        print("Its a tie!")
        p_points += 0  # No points awarded for a tie
        c_points += 0  # No points awarded for a tie
    elif player == "rock" and computer == "scissors":
        print("You win!")
        p_points += 1  # Player wins, add 1 point
    elif player == "rock" and computer == "paper":
        print("You lose!")
        c_points += 1  # Computer wins, add 1 point
    elif player == "scissors" and computer == "paper":
        print("You win!")
        p_points += 1  # Player wins, add 1 point
    elif player == "scissors" and computer == "rock":
        print("You lose!")
        c_points += 1  # Computer wins, add 1 point
    elif player == "paper" and computer == "rock":
        print("You win!")
        p_points += 1  # Player wins, add 1 point
    elif player == "paper" and computer == "scissors":
        print("You lose!")
        c_points += 1  # Computer wins, add 1 point

    # Check if five rounds have been played
    if j == 5:
        # Display final score
        print(
            f""" your points:
               ┌───────────────┐┌───────────────┐
               │  YOU          ││  COMPUTER     │
               └───────────────┘└───────────────┘
               │{p_points:02}             ││{c_points:02}             │
               │               ││               │
               └───────────────┘└───────────────┘
               """
        )
        # Determine the winner or draw
        if p_points > c_points:
            print(f"Congratulations! You won the game!")
        elif p_points == c_points:
            print("It's a draw!")
        elif p_points < c_points:
            print(f"Noob, You lost the game.")
        # Prompt the player to play again or quit
        n = input("\n Do you want to play again? (y/n):").lower()
        if n == "y":
            # Reset round count and points
            j = 0
            p_points = 0
            c_points = 0
        if n == "n":
            break  # Exit the game loop
    else:
        pass

print("Thanks for playing the game :)")


#suiii