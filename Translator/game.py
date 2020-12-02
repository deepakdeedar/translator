import random

number = random.randint(1, 100)

print("Welcome to number guessing game")
print("I'm thinking of a number between 1 to 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} left to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it. The answer was {number}")
        break
    elif guess > number:
        print("Guess is too high")
        attempts -= 1
    else:
        print("Guess is too low")
        attempts -= 1