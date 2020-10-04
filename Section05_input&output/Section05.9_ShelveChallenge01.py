__author__ = "crypto"

import shelve

# before the challenge let's check some error for handling
books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast": ["beans", "bread"],
                     "scrambles eggs": ["eggs", "butter", "milk"],
                     "soup": ["tin of soap"],
                     "pasta": ["pasta", "cheese"]},

         "maintenance": {"stuck": ["oil"],
                         "loose": ["gaffer tape"]}}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambles eggs"])

print(books["maintenance"]["loose"])
# ------------------------------------------------------------------------
print("=" * 40)

# Let's save this dic into a shelve file
books = shelve.open("books")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambles eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soap"],
                    "pasta": ["pasta", "cheese"]}

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}


print(books["recipes"])
print(books["maintenance"])

# print(books["recipes"]["soup"])
# print(books["recipes"]["scrambles eggs"])
#
# print(books["maintenance"]["loose"])

books.close()
# ----------------------------------------------------------------------------------------------------------
print("=" * 40)
# Now, the challenge

# Modify the program from the Second Dictionary challenge of lecture 9
# to use shelves instead of dictionaries.
#
# Do this by creating two programs:
#           1- cave_initialise.py should create the two shelves
#               (locations and vocabulary with appropriate keys and values)
#           2- cave_game.py will then use the two shelves instead of dictionaries.
#
# Apart from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be strings!
#
# Just to be clear, cave_game.py will contain the code from line 93,
# everything before that (modified to use shelves) will be in cave_initialise.py


#  cave_initialise.py

locations = {0: {"des": "You're sitting in front of a computer learning python",
                 "exits": {},
                 "namedExits": {}},

             1: {"des": "You're standing at the end of a road before a small brick building",
                 "exits": {'W': 2, 'E': 3, 'N': 5, 'S': 4},
                 "namedExits": {"2": 2, "3": 3, "4": 4, "5": 5}},

             2: {"des": "You're at the top of a hill",
                 "exits": {'N': 5, 'Q': 0},
                 "namedExits": {"5": 5}},

             3: {"des": "You're inside a building, a well house for a small stream",
                 "exits": {'W': 1, 'Q': 0},
                 "namedExits": {"1": 1}},

             4: {"des": "You're in a valley beside a stream",
                 "exits": {'W': 2, 'N': 1, 'Q': 0},
                 "namedExits": {"1": 1, "2": 2}},

             5: {"des": "You're in the forest",
                 "exits": {'Q': 0, 'S': 1, 'W': 2},
                 "namedExits": {"1": 1, "2": 2}}
           }

letters = {"QUIT": 'Q',
           "WEST": 'W',
           "EAST": 'E',
           "NORTH": 'N',
           "SOUTH": 'S',
           "ROAD": "1",
           "HILL": "2",
           "BUILDING": "3",
           "VALLEY": "4",
           "FOREST": "5"}


# cave_game.py

loc = 1
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["des"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are {}: ".format(availableExits)).upper()
    print()
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
    else:
        print("you can't go in that direction")
