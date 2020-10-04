__author__ = "crypto"

# Section 09.1: Generator and Yield
"""Adv: How Generators're saving memory actually a lots of memory"""

import sys

# lets try to see the size  of memory that will be taken by two different iterators

# 1- range  <--- builtin function
big_range = range(5)

print("big_range is {} bytes".format(
    sys.getsizeof(big_range)))  # sys.getsizeof() if a function that helps you to get the size of any object you enter

# 2- list   <--- builtin object

big_list = []
for value in big_range:
    big_list.append(value)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))


# 3- create our own function as 'generator object'


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is retuning {}".format(start))
        yield start
        # return start  # TODO this represent error for iterable
        start += 1


print("my_range is {} bytes".format(sys.getsizeof(my_range(5))))

# let's print all of them
print(big_range)
print(big_list)
print(my_range(5))

# -----------------------------------------------------------------------
# what's the generator?
"""
when you write a normal function the function finishes after returning
the result. You can see that if we change this 'yield' and change that
keyword to 'return' ---> you will face error

because right now, you will return a single variable "which is not iterable"
and if you did that and get an error you will find that the returned
bytes equal 24 instead of 128 bytes

when it's a generator and uses yield, it actually takes up a bit more memory.

- the difference actually when we use 'yield' the function actually returns
the yielded value then ges into a sort of suspended state so, it doesn't just
return the value it keeps track of all its variables and worry about int its code
so, the next time it's called it wakes up and continues from where it stops.

So, it's actually not called once, it's called each time it's iterated over in the loop

** one more thing you've to know that generators works like iterators
"""


# -----------------------------------------------------------------------
# Section 09.2: Next and Range
# let's see why its bad to add generator to iterator code
print("===== section 02 ====")


def my_range2(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is retuning {}".format(start))
        yield start
        # return start  # TODO this represent error for iterable
        start += 1


# lets try to assign it into an object

rangeX = my_range2(5)

print('with iterator 1 ({})'.format(next(rangeX)))
print('with iterator 2 ({})'.format(next(rangeX)))
print('with iterator 3 ({})'.format(next(rangeX)))
print('with iterator 4 ({})'.format(next(rangeX)))
print('with iterator 5 ({})'.format(next(rangeX)))

print("Looping again ... or not")
for i in rangeX:    # you will find that the object has been executed and not executable any more
    print("i is {}".format(i))

# generate a new passing function
print("\nNew looping")
for i in my_range2(5):
    print("i is {}".format(i))
