__author__ = "Crypto"

# Simplest way to print a Range
print(range(100))

myList = list(range(10))
print(myList)

# Another Example
# range(beginning, end, noOfSteps)
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)
print("\n")
# range() is a very efficient function in terms of memory

myString = "abcdefghijklmnopgrstuvwxyz"
print(myString.index('h'))
print(myString[7])

print("\n")

smallDecimals = range(0, 10)
print(smallDecimals)
print(smallDecimals.index(7))

print("\n")

odd = range(1, 1000, 2)
print(odd)
print(odd.index(985))
# -------------------------------------------------
# Let's try a program
# sevens = range(7, 1000000, 7)
# x = int(input("Please  enter a positive number less than one million: "))
# if x in sevens:
#     print("Your {} is divisible by seven".format(x))
# else:
#     print("Your {} is not divisible by seven".format(x))

print("\n")

print(smallDecimals)
myRange = smallDecimals[::2]  # [Default:Default:2]
print(myRange)
print(myRange.index(4))  # <-- [0, 2, 4, 6, 8, 10] the counter counts spacing, too. be aware that we start counting from 0

print("\n")


# another Example
decimals = range(0, 100)
print(decimals)

myRange = decimals[3:40:3]
print(myRange)

for i in myRange:
    print(i)

print('=' * 40)

# OR

for i in range(3, 40, 3):
    print(i)
# So, the conclusion is whether it's range or myRange its equal no matter what the sequence is
print(myRange == range(3, 40, 3))

# Another Example
print(range(0, 5, 2) == range(0, 6, 2))  # True
print(range(0, 5, 2) == range(0, 10, 2))  # False

# it's all what to do with the same sequence of values regardless what the end result is
print("\n")
# Let's print and see
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

# Another Example
print("\n")
r = range(0, 100)

for i in r[::-2]:
    print(i)

print("=" * 50)
# OR
for i in range(99, 0, -2):
    print(i)

print("=" * 50)

print(range(0, 100)[::-2] == range(99, 0, -2))
# < -- instead of initialized a variable we can multiply the range with the list range range()[]
# ------------------------------------------------------
# For slicing a backward string or Number
backString = "egaugnal lufrewop yrev si nohtyp"
print(backString[::-1])
