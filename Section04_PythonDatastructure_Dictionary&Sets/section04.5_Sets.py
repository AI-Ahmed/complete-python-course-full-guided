__author__ = "Crypto"

# Sets is very useful for cleaning data

# First way to initialize Set

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

# Second way to create set

wild_animals = set(["lion", "tiger", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# for appending a new element in the set

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# if you notice the results, you will find that the'Sets' results is "Unordered" like we have discussed in dictionary
print("=" * 40)
# -------------------------------------------------------------------------------------
# if you create two empty function and you want to append on them
# Example 01
empty_set = set()
empty_set.add("a")
print(empty_set)
# Example 02
# The second example will give an error because you can't use add() to append values in a null set without using set()
print("=" * 40)
# -------------------------------------------------------------------------------------
# range() in sets
print("range()")
even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print()
# -------------------------------------------------------------------------------------
# getting the length of the set()
print("length")
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))
print()
# -------------------------------------------------------------------------------------
print("=" * 40)
# let's use the union()
print("Print the union --> 'common' values together ---> common of even with squares")
print(even.union(squares))
print("Print the length of the set after the union")
print(len(even.union(squares)))
print("Print the union --> 'common' values together ---> common of squares with even")
print(squares.union(even))
print("Print the length of the set after the union")
print(len(squares.union(even)))

print("-" * 40)

# intersection()
print("intersection()\n")
print("intersection between even and squares")
print(even.intersection(squares))
# OR
print(even & squares)
print("intersection between squares and even")
print(squares.intersection(even))
# OR
print(squares & even)
# ------------------------------------------------------------------------
print("=" * 40)
# let's see how  it can be sorted
print(sorted(even))
print(sorted(squares))

# let's see the difference between two sets
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even ")
print(sorted(squares.difference(even)))
print(sorted(squares - even))
# ------------------------------------------------------------------------
print("=" * 40)
# difference_update() is a function that update removes the duplicates in two sets
print("difference update")
even2 = set(even)
print(sorted(even2))
print(squares)
even2.difference_update(squares)
print(sorted(even2))
print(even2)
# ------------------------------------------------------------------------
print("=" * 40)
# A symmetric difference of two sets
# this function removes the similar values in both sets depending on the first then union them
print(sorted(even))
print(squares)
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

# symmetric_difference_update() the difference between it and symmetric_difference is only will operate the set itself
# print(sorted(even.symmetric_difference_update(squares)))
# ------------------------------------------------------------------------
print("=" * 40)
# Now, lets put some more function that helps to remove or discard values
_squares = set(squares)
print(_squares)
_squares.discard(4)
# print(_squares)
_squares.remove(16)
# print(_squares)
_squares.discard(8)  # no error, does nothing. because it removes the value, silently
print(_squares)
#_squares.remove(8)  # this will give an error because value 8 doesn't exist
# so, to activate function remove() you've to ensure that the value isn't in the set otherwise you've to put
# if condition or use discard()
if 8 in squares:
    _squares.remove(8)
# print(_squares)
# or use the exception
try:
    _squares.remove(8)
except KeyError:
    print("This item is not a member of the set")
# ------------------------------------------------------------------------
print("=" * 40)
# Now, last thing is issuperset() & issubset()
# those will be used to test if one set is a sub or super set of the other set
i_even = set(range(0, 40, 2))
print(i_even)
i_squares_tuple = (4, 6, 16)
i_squares = set(i_squares_tuple)

if i_squares.issubset(i_even):
    print("squares is a subset of even set")

if i_even.issuperset(i_squares):
    print("even is a superset of squares set")
# ------------------------------------------------------------------------
print("=" * 40)
# last thing is the frozen set

# frozen set is immutable set which of course can't be changed
# so, when being immutable at least we can use a frozen set as a dictionary key
# keep in mind, there's no remove, add, change, or discard method available with frozen set
# once created it can't be changed

frozen = frozenset(range(0, 100, 2))
print(frozen)
# frozen.add(3)   # this will give an error because after you created it can't be changed
