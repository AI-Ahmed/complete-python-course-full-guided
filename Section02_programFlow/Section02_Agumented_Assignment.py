__author__ = "crypto"

number = "9, 223, 568, 564, 45, 156, 49"
cleanNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanNumber += number[i]  # <-- Aug Assignment +=, -=, *=, /=, !=, **=, %=, &=, |=, ^=, <<=, >>=

newNumber = int(cleanNumber)
print("The number is {} ".format(newNumber))
