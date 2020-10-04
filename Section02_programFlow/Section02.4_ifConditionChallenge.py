__author__ = "Crypto"

name = input("Please, Enter your name: ")
age = int(input("How old are you? "))

# if 18 <= age <= 30:
# if 17 < age <31
if (18 <= age) and (age <= 30):
    print("You're welcomed to the holiday,{0}!".format(name))
else:
    print("Sorry {0}, your age not suitable for a holiday!".format(name))
# ------------------------------------------------------
