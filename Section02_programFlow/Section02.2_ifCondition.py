__author__ = "Crypto"

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 4))
    print("Calculation Complete")
    print("Try again!")  # <------  use Ctrl + /
# ------------------------------------------------------------------
name = input("Please enter your name:")
age = input("How old are you,{0}? ".format(name))
# Python 3.0
print("""{0}'s Information(s):
        Age: {1}
         """.format(name, age))
print("\n")
# Python 2.0
# print("%s's Information(s):\n\tAge: %2s\n" % (name,age)) # <--- Dealing with the age as a string I/o
# but if you want to trace the age as an int not str. you can convert it usong int()
age = int(input("How old are you,{0}? ".format(name)))
# print("%s's Information(s):\n\tAge: %2d\n" % (name,age)) # <--- Dealing with the age as a int I/o
# ------------------------------------------------------------------
# if condition
if age >= 18:
    print("you're old enough to vote")
    print("Please put an X in the box")
else:
    print("you still young, please come back after {0} years ".format(18-age))
# ------------------------------------------------------------------
print("Please, guess a number between 1 and 10: ")
guess = int(input("Your guess: "))

# if guess > 5:
# Ex
if guess != 5:
    if guess > 5:
        print("Please, guess lower")
    else:  # guess must be greater than 5
        print("please, guess higher")

    guess = int(input("Your guess: "))
    # if guess == 5:
    #     print("you've successfully got it!")
    # else:
    #     print("Unfortunately, You guessed wrong!")
# elif guess < 5:
    # print("Please, guess higher")
    # guess = int(input("Your guess: "))
    if guess == 5:
        print("you've successfully got it!")
    else:
        print("Unfortunately, You guessed wrong!")
else:
    print("you got it first time!")
