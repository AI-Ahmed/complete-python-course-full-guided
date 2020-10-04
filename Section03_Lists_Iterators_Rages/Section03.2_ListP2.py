__author__ = "Crypto"

# List Assignment

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 1: {}".format(list_2))

if list_1 == list_2:
    print("List are equal!")

print(list("The lists are equal!"))

# ---------------------------------------------------
print("\n")
# Let's try to sort a list an reverse it and see if it still equal

even = [2, 4, 6, 8]
print(even)  # <--- even without reversing
another_even = even
another_even.sort(reverse=True)
print(even)  # <--- even with reversing
print(another_even is even)  # <--- 'True' result because the list haven't changed. It stills pointing the same numbers
print(another_even == even)  # <--- 'True' result because the list haven't changed. It stills pointing the same numbers
print("\n")

# Another example 'Let's try to create a new list'

another_even = list(even)
print(another_even)
print(another_even is even)  # <--- 'False' because we created another list with another_even(newVariable)
print("\n")

# Another example 'Let's try to equalize them'

another_even = list(even)
print(another_even)
print(another_even == even)  # <--- 'True' because that's saying whether the content are equal
#  not whether they're actually pointing to different variables in memory if that makes sense,
#  different list essentially
print("\n")

# Another example 'Let's try to equalize them with sorted() the new variable'

another_even = sorted(even, reverse=True)
print(another_even)
print(another_even == even)  # <--- 'True' sorter does return a new list, but now its soring it in a different order
# if we tried to pointing another_even again


print(another_even is even)  # <--- 'False' we still comparing a different lists. sorted() initialize a new list to the variable
print("\n")

# let's see if we concatenate two lists and put some code

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
