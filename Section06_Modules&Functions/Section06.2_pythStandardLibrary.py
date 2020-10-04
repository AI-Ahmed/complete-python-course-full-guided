__author__ = "crypto"
import shelve
# we have function called dir() that list the directories so to see what
# is imported for us automatically.
# print(dir())
# print(dir(__builtins__))
# for n in dir(__builtins__):
#     print(n)
# print(dir(shelve))
print("=" * 40)
for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
print("=" * 40)
help(shelve)    # function that could help you explain object you entered 
# ------------------------------------------

