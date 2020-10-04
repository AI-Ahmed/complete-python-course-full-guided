__author__ = "Crypto"

# Tuples are a term for an ordered set of data
# Tuples are similar to lists the difference is its 'immutable' which can't be changed

t = "a", "b", "c"  # <--- This's a Tuple
print(t)

print("a", "b", "c")  # <--- This's NOT a Tuple
# Tuples are a term for an ordered set of data
# Tuples are similar to lists the difference is its 'immutable' which can't be changed

print(("a", "b", "c"))  # <--- This's a Tuple
print("\n")
# ------------------------------------------------------
welcome = "welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhen", "Emilda May", 2011

print(welcome)
print(welcome[0])
print(welcome[1])
print(welcome[2])
print("\n")

# welcome[0] = "Master of puppets"  # if you notice this give an error because you can't change the item of the Tuple

print(imelda[1])
imelda = imelda[0], "Imelda May", imelda[2]  # But if you notice you can assign a value like that
print(imelda)
print(imelda[1])
print("\n")
# ------------------------------------------------------
# Instead let's create a list
welcome2 = ["welcome to my nightmare", "Alice Cooper", 1975]
print(welcome2)
welcome2[0] = "Master of Puppets"
print(welcome2)
# ------------------------------------------------------
print("\n")
# ------------------------------------------------------

# So, the question here, why we can use a tuple over List?
#   The answer:
#               1- There're some kind of elements wants a immutable object one of them is "Dictionary key"
#                  Dictionary Key uses a immutable objects.

#               2- Lists intended to have 'homogeneous' items
#                   which meaning an items or a values that have the same types

#               3- Actually Tuples intended to hold 'heterogeneous' items
#                  which items or values of different types of elements --> int, string ...etc

myList = ["firstName", "secondName", "lastName"]
myTuple = ("name", "dataOfBirth", "Address", "Email", "Phone number")
myDictionary = {"name", "dataOfBirth", "Address", "Email", "Phone number"}
# ------------------------------------------------------

# Let's clarify something

a = b = c = d = 12
print(c)
a, b = 12, 13
print(a, b)

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
print("\n")
# Now let's have an example
# How we can Extract the tuples value into variables
title, artist, year = imelda
print(title)
print(artist)
print(year)
# This's Called 'unpacking tuple'
