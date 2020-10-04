__author__ = "Crypto"

# Dictionary & Sets are unordered collections unlike Tuples

# Dictionary & Sets don't have a duplicates unlike Lists which don't have a duplicates.

# Dictionary aren't access by point index(), but they're accessed instead by means of a key
# Example:
bike = {"make": "Honda",
        "model": "250 dream",
        "colour": "red",
        "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])
print("\n")
# -------------------------------------------------------------------------------------------
# Another Example

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)
# print(fruit.index[0])  # <-- you can't use the index only you can access by the key
print(fruit["lemon"])
# -------------------------------------------------------------------------------------------
# To append into the dictionary
fruit["pear"] = "an old shaped apple"
fruit["orange"] = "kikke"

print(fruit)
# you only overwrite your value in the dictionary
# -------------------------------------------------------------------------------------------
# If you want to del something from the dictionary
del fruit["lemon"]
print(fruit)
# # del fruit
# print(fruit)  # this gives an error of what you trying to print after deleting the dictionary
#                 So, to clear the dictionary then you can use it later, you can use
# fruit.clear()
# print(fruit)
# -------------------------------------------------------------------------------------------
# if you tried to access and print item that it's not into the dictionary it will give you an error
# print(fruit["tomato"])  #<--- that gives an error
# -------------------------------------------------------------------------------------------
# let's create a code that allow you to enter a fruit
print("\n")
print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "":
        print("Please enter the type of fruit you want!")
        dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "we don't have a " + dict_key)  # This will be better, with retrieve the value
    #                                                                   from the dictionary and insert a default value
    print(description)
    # OR

    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print("we have {}".format(description))
    # else:
    #     print("we don't have {}".format(dict_key))
