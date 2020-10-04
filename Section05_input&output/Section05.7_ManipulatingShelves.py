__author__ = "crypto"

import shelve
# if you want to close your file by yourself

# with shelve.open("shelveTest") as fruit:
fruit = shelve.open("shelveTest")
# we will comment these values because we actually trying to read from the shelve db

# fruit["orange"] = "a sweet, orange, citrus fruit"
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour, yellow citrus fruit"
# fruit["grape"] = "a small, sweet fruit growing in bunches"
# fruit["lime"] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
# ------------------------------------------------------------------------------
print("-" * 40)

# another example

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break

    # description = fruit.get(dict_key, "We don't have a " + dict_key)
    # print(description)

# another way to check if the key into the shelve before attempting to retrieve
# and print the value. just like dictionary
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have " + dict_key)

# ------------------------------------------------------------------------------
print("=" * 40)

# now, lets try to manipulating the value from the db and try to read it!

for f in fruit:
    print(f + ' - ' + fruit[f])

# in this case it doesn't show in alphabetical order but it does on some system so
# keep that in mind again because it's coming from db
# ------------------------------------------------------------------------------
print("-" * 40)

# you can get them into ordered by using list
ordered_key = sorted(list(fruit.keys()))

for f in ordered_key:
    print(f + ' - ' + fruit[f])
# ------------------------------------------------------------------------------
print("=" * 40)

# now if you want to show the dic values and items
print("Dictionary's Value")
for v in fruit.values():
    print(v)
print(fruit.values())   # you can't modify it

print("-" * 20)

print("Dictionary's Items")
for i in fruit.items():
    print(i)
print(fruit.items())    # you can't modify it
fruit.close()
