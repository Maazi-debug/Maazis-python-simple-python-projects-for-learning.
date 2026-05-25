import random, sys

guess = random.randint(1, 10)

try:
    while True:
        answer = int(input('Guess a number from 1-10: '))

        if answer == guess:
            print('Yeah, you guessed it!')
            break
        elif answer < guess:
            print('Your guess is too low!')
        elif answer > guess:
            print('Your guess is too high!')

except ValueError:
    print('Bro did not enter a number!')
