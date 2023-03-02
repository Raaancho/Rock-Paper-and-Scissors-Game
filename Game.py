import random

while True:
    print("""
Welcome to the Rock, Paper and Scissors Game.
Note: You can only choose either of Rock, Scissors or Paper.
Have Fun!!!
    """)
    user_choice = input("What's your choice? ")
    possible_choices = ["rock", "scissors", "paper"]
    computer_choice = random.choice(possible_choices)

    print(f"You chose {user_choice} and the computer chose {computer_choice}")
    print()

    if user_choice.lower() == computer_choice:
        print("It's a tie")
    elif user_choice.lower() == "rock":
        if computer_choice == "paper":
            print("Paper covers Rock, You lose")
        else:
            print("Rock smashes scissors, You win")

    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Paper covers Rock, You win")
        else:
            print("Scissors cuts Paper, You lose")

    elif user_choice.lower() == "scissors":
        if computer_choice == "rock":
            print("Rock smashes Scissors, You lose!")
        else:
            print("Scissors cuts Paper, You win")

    else:
        print("You can only choose either of Rock, Scissors or Paper")
        continue

    play_again = input("Do you want to continue playing? y/n: ")

    if play_again.lower() == "y":
        print("Let's go!!!")
        print()
        continue
    elif play_again.lower() == "n":
        print("See you next time")
        break
    else:
        print("You can only choose y/n ")
        print()
        continue
