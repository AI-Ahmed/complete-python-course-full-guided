__author__ = "crypto"

import shelve

locations = shelve.open("map")
letters = shelve.open("vocabulary")

loc = '1'
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["des"])

    if loc == '0':
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are {}: ".format(availableExits)).upper()
    # Parse the user input, using our letters' dictionary if necessary
    #                             so, when we have more vocabulary and splitting the paragraph into splitting of words
    if len(direction) > 1:  # more than one letter, so check the letter dictionary
        words = direction.split()   # split() is actually useful for dictionary knowledgeable,
        for word in words:  # does it contain a familiar word?
            if word in letters:
                direction = letters[word]
                break

    if direction in allExits:
        loc = allExits[direction]
        print()

    else:
        print("you can't go in that direction")
        print()

letters.close()
locations.close()
