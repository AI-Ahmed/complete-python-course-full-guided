__author__ = "crypto"

# Shelve
#   Dealing with large data like Dictionaries
#       you can say using Pickle, but unfortunately using pickle to load large data into
#       memory may not be realistic

#   So, here the data being stored into a file not in memory
#
#   Like pickle, just don't use shelve files themselves from untrusted sources.

# One of the most important different between Shelve and dictionary:
#   shelves a shelve key must be a string
#   dictionaries can accept any immutable object as a key as we talked about

import shelve

with shelve.open("shelveTest") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

# print(fruit["lemon"]) # Those will give an error because we're calling them after closing the shelve
# print(fruit["grape"])

print(fruit)    # This's a shelve object
# -----------------------------------------------------------------------------
print('=' * 40)

# if you want to close your file by yourself

# with shelve.open("shelveTest") as fruit:
fruit = shelve.open("shelveTest")   # <-- this's individual Dictionary
fruit["orange"] = "a sweet, orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow citrus fruit"
fruit["grape"] = "a small, sweet fruit growing in bunches"
fruit["lime"] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit.close()

# -----------------------------------------------------------------------------
print('=' * 40)
# What the different between the shelve and the dictionary:
#   Is that there's no shelve literal . so, what it means by
#   that shelve doesn't have restricted way to write down the objects literal


# let's show that by example the same example above with different literal

with shelve.open("shelveTest") as fruit:    # <-- this's literal Dictionary
    fruit = {"orange": "a sweet, orange, citrus fruit",
             "apple": "good for making cider",
             "lemon": "a sour, yellow citrus fruit",
             "grape": "a small, sweet fruit growing in bunches",
             "lime": "a sour, green citrus fruit"}

print(fruit["lemon"])
print(fruit["grape"])

print(fruit)

# in another words the shelve itself has now been closed
# obviously because we're out of that loop in that indentation level
# The point is, you can't initialize a shelve using literal as we could with Dictionary
# -----------------------------------------------------------------------------
print('=' * 40)

# Now, lets see an example of what we can store in shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["colour"])

# -----------------------------------------------------------------------------
print('=' * 40)

# what we need to know, shelve has persistent in its file, we can show that by example

with shelve.open("bike2") as bike2:
    bike2["make"] = "Honda"
    bike2["model"] = "250 dream"
    bike2["colour"] = "red"
    # bike["engin_size"] = 250    # this will show an error
    # so, we need to clear that and edit it
    bike2["engine_size"] = 250

# but if we check the keys in the file we will find that:
    for key in bike2:
        print(key)
# you will find that we have 2 key now instead of one key being shown

# what we really need to do is to delete that key
    del bike2["engin_size"]     # put into line 93
    print(bike2["engine_size"])  # this will show an error
    print(bike2["colour"])

