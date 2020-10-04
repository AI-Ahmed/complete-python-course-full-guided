__author__ = "crypto"

import random

# Try to figure it out within 10 times

highest = 1000
answer = random.randint(1, highest)
# answer = 4

guess = int(input("Please, guess a number between 1 and {}: ".format(highest)))
q = '0'
while guess != answer:

    if guess == 0:
        guess = int(input("""Are you sure you want to Quit "zero for Quitting"? [0/-1] """))
        if guess == 0:
            break
        else:
            guess = int(input("Please, guess a number between 1 and {}: ".format(highest)))

    if guess > answer:
        print("Please, guess lower")
    else:
        print("Please, guess higher")
    guess = int(input("Enter a guess, again: "))

if guess == answer:
    print("well done, you guessed correctly!")

