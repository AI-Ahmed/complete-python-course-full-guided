__author__ = "crypto"

# Modify the program so that the exits is a dictionary rather than a list,
# with the key being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at the present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.
print()
locations = {0: "You're sitting in front of a computer learning python",
             1: "You're standing at the end of a road before a small brick building",
             2: "You're at the top of a hill",
             3: "You're inside a building, a well house for a small stream",
             4: "You're in a valley beside a stream",
             5: "You're in the forest"}

# we've changed the list into full dictionaries
exits = {0: {'Q': 0},  # <--- '0' means quitting the game
         1: {'W': 2, 'E': 3, 'N': 5, 'S': 4},    # <--- '1' means Road location
         2: {'N': 5, 'Q': 0},    # <--- '2' means Hill location
         3: {'W': 1, 'Q': 0},    # <--- '3' means Building location
         4: {'W': 2, 'N': 1, 'Q': 0},    # <--- '4' means Valley location
         5: {'Q': 0, 'S': 1, 'W': 2}}    # <--- '5' means Forest location

letters = {"QUIT": 'Q',
           "WEST": 'W',
           "EAST": 'E',
           "NORTH": 'N',
           "SOUTH": 'S'}
loc = 1
while True:
    print(locations[loc])
    if loc == 0:
        break
    availableExits = ", ".join(exits[loc])
    direction = input("Available exits are {}: ".format(availableExits)).upper()
    # Parse the user input, using our letters' dictionary if necessary
    #                             so, when we have more vocabulary and splitting the paragraph into splitting of words
    if len(direction) > 1:  # more than one letter, so check the letter dictionary
        words = direction.split()   # split() is actually useful for dictionary knowledgeable,
        for word in words:  # does it contain a familiar word?
            if word in letters:
                direction = letters[word]
                print(direction)
                break
    if direction in exits[loc]:
        loc = exits[loc][direction]
        print(loc)
    print()
