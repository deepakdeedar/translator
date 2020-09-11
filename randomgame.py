from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number from 1 to 10:  '))

        if guess > 0 and guess < 11:
            if guess == answer:
                print('You are a Genius!')
                break
        else:
            print('Hey Bozo, I said 1~10')
    except ValueError:
        print('Please enter a number')
        continue
