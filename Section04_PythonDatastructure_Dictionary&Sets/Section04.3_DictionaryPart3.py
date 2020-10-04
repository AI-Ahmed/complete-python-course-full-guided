__author__ = "Crypto"

# ---------------------'Join function'------------------

# string is immutable, as a result this means that it's not all efficient to concatenate
# strings in a loop
# Anytime you concatenate a string to an existing string, the new string has to be
# it becomes expensive and slow, so you really do want to avoid that
# ---the string join method is here to actually help you
# It actually takes a sequence and produces a string from it a string from it

# Example 01
myList = ["a", "b", "c", "d"]

newString = ''
for c in myList:
    newString += c + ", "
print(newString)

# 1- First problem: if you notice there's a ',' at the end of the loop that been printed
#    That's why we're saying that the string is immutable
# so, to  fix this problem we can use join method
# which it doesn't need loop

newString = ", ".join(myList)
print(newString)

# Example 02

letters = "abcdefghijklmnopqrsturstuvwxyz"

newString2 = ", ".join(letters)
print(newString2)

# ---------------------------------------------------------------
print("\n")
# Example for locations 'north movement for quiting'

locations = {0: "You're sitting in front of a computer learning python",
             1: "You're standing at the end of a road before a small brick building",
             2: "You're at the top of a hill",
             3: "You're inside a building, a well house for a small stream",
             4: "You're in a valley beside a stream",
             5: "You're in the forest"}
# locations' assign with keys 1, 2, 3 ...
# pointing with ANOTHER keys "value" in another Dictionaries N, S, W, E
# Location inserts one-at-time, and then move to next round
# 'Remember the graph'
# This's list of dictionaries
exits = [{'Q': 0},  # <--- '0' means quitting the game
         {'W': 2, 'E': 3, 'N': 5, 'S': 4},    # <--- '1' means Road location
         {'N': 5, 'Q': 0},    # <--- '2' means Hill location
         {'W': 1, 'Q': 0},    # <--- '3' means Building location
         {'W': 2, 'N': 1, 'Q': 0},    # <--- '4' means Valley location
         {'Q': 0, 'S': 1, 'W': 2}]    # <--- '5' means Forest location

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    print(locations[loc])
    if loc == 0:
        break
    availableExits = ", ".join(exits[loc])
    direction = input("Available exits are {}: ".format(availableExits)).upper()
    # <-- upper() helps the user to write upper-case char
    if direction in exits[loc]:
        loc = exits[loc][direction]
    print()
