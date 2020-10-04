__author__ = "Crypto"

#   Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method.
# we can say that example for it would be for()
string = "123456789"
it = iter(string)
while True:
    try:
        value = it.next()   # in Python 2.x
        value = next(it)    # in Python 3.x
    except StopIteration:
        break
    print(value)
# Iterators is a sort of stream or lists

string = "123456789"

for char in string:
    print(char)  # <-- instead of that we can run the object of the iterator
myIterator = iter(string)
print(myIterator)  # <-- print the object pointer of the iterator

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# print(next(myIterator)) # <-- we will get and error because this was the end of the iterator
print("\n")

# Some challenges

footNumbers = [1, 13, 19, 10, 11, 9, 15]
myIterator = iter(footNumbers)
print(myIterator)

for n in footNumbers:
    print(next(myIterator))

print("Number of players: {} ".format(len(footNumbers)))
print("\n")
# Both of them are right!

myList = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
myIterator = iter(myList)

for day in range(0, len(myList)):
    print(next(myIterator))
# --------------------------------------------------------------------------------------

# some rules
#   Note that every iterator is also an iterable, but not every iterable is an iterator. For example,
#   a list is iterable but a list is not an iterator.
# list of cities

cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

 # Output :
 #
# Berlin
# Vienna
# Zurich

# Code #3 : Check object is iterable or not

# Function to check object
# is iterable or not
# def iterable(obj):
# try:
# iter(obj)
#    return True
#
# except TypeError:
#     return False

    # Driver Code
for element in [34, [4, 5], (4, 5),
    {"a": 4}, "dfsdf", 4.5]:

    print(element, " is iterable : ", iterable(element))


# Output :
    #
    # 34  is iterable :  False
    # [4, 5]  is iterable :  True
    # (4, 5)  is iterable :  True
    # {'a': 4}  is iterable :  True
    # dfsdf  is iterable :  True
    # 4.5  is iterable :  False
