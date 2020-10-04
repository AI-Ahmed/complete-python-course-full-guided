__author__ = "Crypto"

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)
print("\n")
#  we can also iterate over the keys
for snack in fruit:
    print(fruit[snack])
print("\n")
# this will list the value that in the dictionary
# if the notice that the list is actually change its order
# evey time you try to run is again, that what prove that
# Dictionary is unordered collection
# Example for more indication
for i in range(10):
    for snack in fruit:
        print(fruit[snack])
    print('=' * 40)
# ---------------------------------------------------------
print("ordered- Dictionary")
print("\n")
print("Using List")
print("\n")
# Let's using order them: Style 01
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for key in ordered_keys:
#     print(key + "-" + fruit[key])


# you can do both in one line: Style 02
# ordered_keys = sorted(list(fruit.keys()))
# for key in ordered_keys:
#     print(key + "-" + fruit[key])

# another one: Style 03
for key in sorted(fruit.keys()):
    print(key + " -- " + fruit[key])

# ---------------------------------------------------------
print("\n")
# there're totally different between value() and keys()
# fruit.values()
for val in fruit.values():
    print(val)
print("=" * 40)
# fruit.keys()
fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)
# ---------------------------------------------------------
# By using the item method --> Dynamic view object that consists of key and value tuples as well
print(fruit.items())
# By using the tuple function --> turns the dictionary into tuple
f_tuple = tuple(fruit.items())
print(f_tuple)

print()
print("=" * 40)

for snack in f_tuple:
    item, description = snack
    print(item)
    print(description)
# this helps to turns it down to dictionary
print(dict(f_tuple))
