import random

comp_choice = random.choice(["scissors", "rock", "paper"])
user_choice = input("Do you want - rock, paper or scissors?\n")

if comp_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and comp_choice == "scissors":
    print("WIN")
elif user_choice == "papper" and comp_choice == "rock":
    print("WIN")
elif user_choice == "scissors" and comp_choice == "papper":
    print("WIN")
else:
    print("You loose : Computer wins :D")
