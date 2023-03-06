import random
user= input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
choice = random.choice(possible_actions)
if user not in possible_actions:
    print('invaild')
if user== choice:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user== "paper":
    if choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

