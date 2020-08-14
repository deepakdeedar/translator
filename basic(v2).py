from random import randint

print("...Rock...")
print("...Paper...")
print("...Scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays: {computer}")

if player == computer:
    print("It's a tie")
elif player == "rock":
    if computer == "scissors":
        print("Player 1 win.")
    else:
        print("Player 2 win.")
elif player == "paper":
    if computer == "rock":
        print("Player 1 win.")
    else:
        print("Player 2 win.")
elif player == "scissors":
    if computer == "paper":
        print("Player 1 win.")
    else:
        print("Player 2 win.")
else: 
    print("Something went wrong.")