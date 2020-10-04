__author__ = "Crypto"

myRange = range(0, 100, 4)
print(myRange)

for i in range(0, 100, 4):
    print(i)

print('=' * 40)

# -------------------------------------------------------------------------------------
for i in myRange:
    print(i)

print('=' * 40)
# -------------------------------------------------------------------------------------
for i in myRange[0:100:2]:  # <-- if you initialized an new range like [0, 100, 2]
                   # it will start comparing between the old range and the new range then mutiply the new segment with the old one
    print(i)

print('=' * 40)
# -------------------------------------------------------------------------------------
myNewRange = myRange[::2]
print(myNewRange)
for i in myNewRange:  # <-- if you initialized an new range like [0, 100, 2]
                   # it will start comparing between the old range and the new range then mutiply the new segment with the old one
    print(i)

print('=' * 40)
# -------------------------------------------------------------------------------------

# For overall
# When you write down "myRange = range(0, 100)" you're only initialize an object into the memory
# The same thing with the iterator when you write the function of the iteration iter(myList) you just initialize the object

my_range = range(0, 10)
print(my_range)  # <--- print the object

for sequenceOfNumber in my_range:
    print(sequenceOfNumber)  # <--- Object execution

print('=' * 40)

myIterator = iter(list(range(10)))
print(myIterator)  # <--- print the object

for appended in range(0, len(list(range(10)))):
    print(next(myIterator))  # <--- Object execution
