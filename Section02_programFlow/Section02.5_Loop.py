__author__ = "Crypto"
## The idea of this example is to learn how you can actually extracting a data from
#   Spreadsheet while the data may contain invalid char which effect a scientific  or exponential data


number = "9,846,4646,544564,54654,564,445,44,46"
for i in range(0, len(number)):
    print(number[i])

# print only stringNumbers
number = "9,846,4646,544564,54654,564,445,44,46"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

# print only stringNumbers "At the same line"
number = "9,846,4646,544564,54654,564,445,44,46"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')

# Now, lets converting it into numbers
number = "9,846,4646,544564,54654,564,445,44,46"
cleanNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
        cleanNumber += number[i]
    # newNumbers = int(cleanNumber)  <---- with a long range of numbers may cause a problem in the operation
newNumbers = int(cleanNumber)
print("The number is {}".format(newNumbers))

# Another way for writing a loop
number = "9,846,4646,544564,54654,564,445,44,46"
cleanNumber = ''
for char in number:
    if char in '0123456789':
        cleanNumber += char
    # newNumbers = int(cleanNumber)  <---- with a long range of numbers may cause a problem in the operation
newNumbers = int(cleanNumber)
print("The number is {}".format(newNumbers))

# Another example of a type of sequence of list of string "One of the best depending of the range"
for state in ["no pinin", "No more", "a stiff", "bereft of Life"]:
    print("This's "+state)  # Preferred
    # print("This's {}".format(state))

# Stepping loop
for i in range(0, 100, 5):
     print("i is {}".format(i))

# Double Loop "By Column"
for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i * j))
    print("==================")

# Double Loop "By Row"
for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i * j), end='  \t')  # 'end' helps you to print results into the same row
    # print("==================")
    print(" ")
