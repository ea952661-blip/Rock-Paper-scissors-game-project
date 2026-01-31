import time
import random

time.sleep(1)

print("""
██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝███████╗
██╔══██╗██╔═══╝ ╚════██║
██║  ██║██║     ███████║
╚═╝  ╚═╝╚═╝     ╚══════╝
 ROCK • PAPER • SCISSORS
""")
time.sleep(1)

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 1

while user_score < 2 and computer_score < 2:
    print(f"--- Round {round_number} ---\n")

    while True:
        user_choice = input(
            "Choose rock, paper, scissors (or r/p/s): ").lower()
        if user_choice in ["r", "p", "s"]:
            user_choice = {"r": "rock", "p": "paper",
                           "s": "scissors"}[user_choice]
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Try again.\n")

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print(f"Score — You: {user_score} | Computer: {computer_score}\n")
    round_number += 1

if user_score == 2:
    print(" Congratulations! You won the game! ")
else:
    print(" Computer won the game! Better luck next time! ")
