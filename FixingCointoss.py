# A program that used to have a bug where, when you guessed heads there wasn't a way for the program to verify it by saying toss == guess because guess and toss had a seperate value but then i wrote
# that for example if the user types heads then i would say that guess should have the value 1 which is the same as the toss and therefore the guess
# would've been correct and the same is if the user got tails then i would rewrite the value of guess to 0 to see if it matches the toss's value

import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if guess == 'heads':
    guess = 1

else:
    guess = 0

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()

    if guess == 'heads':
        guess = 1

    else:
        guess = 0

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
