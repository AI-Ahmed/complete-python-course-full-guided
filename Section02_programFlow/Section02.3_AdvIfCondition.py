__author__ = "Crypto"

age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):
# if 16 <= age <= 65:
if 15 < age < 66:
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")

if (age < 16) or (age > 65):
    print("Enjoy your free time!")
else:
    print("Have nice day at work!")
# -------------------------------------------------
x = input("Please, enter some text: ")

if x:  # <---- boolean checking condition fo an I/-
    print("you entered '{}'".format(x))
else:
    print("You did not enter anything")
# -------------------------------------------------
# print(not False)
# print(not True)
# -------------------------------------------------
age = int(input("How old are you? "))

if not (age < 18):  # <---- given the result as a boolean
    print("You're old enough to vote")
    print("Please put an X in the box")
else:
    print("Please, come back after {} years".format(18 - age))
# -------------------------------------------------
# ifCondition for string condition
parrot = "Norwegian Blue"

letter = input("Enter a Character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter!")
