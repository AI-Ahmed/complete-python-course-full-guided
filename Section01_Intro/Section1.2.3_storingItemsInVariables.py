__author__ = "Crypto"
#
greeting = "john"
_myname = "Tim"
Tim45 = "Good"
Tim_was_57 = "Hello"
Greeting = "There"
print(Tim_was_57+' '+greeting)

age = 24
print(age)

#To concatenate the int with  String you can use str()

greeting+=' ' + str(age)

print(greeting)
print('\n')
# -----------------------------------------------
# Operations
print("operations")
a = 12
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # Double print
print(a // b)  # int print
print(a % b)  # MOD
print(a ** b)  # Caret (2^13)
# -----------------------------------------------
# Loop
print('\n')
for i in range(1, 4):  # Double
    print(i)
print('\n')
for i in range(1, a // b):  # integer
    print(i)
print('\n')
# -----------------------------------------------
# Multiplication
print(a + b / 3 - 4 * 12)
print((((a + b) / 3) - 4) * 12)
# -----------------------------------------------
# Print char
parrot = "Welcome to Youto"
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])

number = "9,658,412,146,486,846"
print(number[1::4])
numbers = "1,2,3,4,5,6,7,8"
print(numbers[0::3])
print(numbers[0::1])
print(numbers[0::5])
print(numbers[0::8])


print("Hello" * 5)
print("Hello" * (5+4))
print("Hello" * 5 + "")

# Print Boolean
today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")


