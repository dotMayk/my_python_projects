import random


def computer_input():
    options = ["rock", "paper", "scissors"]
    computerInput = random.choice(options)
    return computerInput


userInput = input("Please choose your action (ROCK / PAPER / SCISSORS): ")
print(f"User chose {userInput}")
computerInput = computer_input()
if userInput.lower() == "rock" or userInput.lower == "paper" or userInput.lower() == "scissors":
    if userInput.lower() == computerInput:
        print(f"Computer chose {computerInput}")
        print("TIED. Try again!")
    elif userInput.lower()  == "rock":
        if computerInput == "paper":
            print(f"Computer chose {computerInput}")
            print("COMPUTER WINS!")
        else:
            print(f"Computer chose {computerInput}")
            print("USER WINS!")
    elif userInput.lower() == "paper":
        if computerInput == "scissors":
            print(f"Computer chose {computerInput}")
            print("COMPUTER WINS!")
        else:
            print(f"Computer chose {computerInput}")
            print("USER WINS!")
    elif userInput.lower() == "scissors":
        if computerInput == "rock":
            print(f"Computer chose {computerInput}")
            print("COMPUTER WINS!")
        else:
            print(f"Computer chose {computerInput}")
            print("USER WINS!")
else:
    print("Wrong input! Try again.")

