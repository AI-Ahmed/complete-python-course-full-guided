__author__ = "Crypro"
# concatenate Sting with INT
age = 24
print("my age is " + str(age) + " years")
# formatting the string within number

print("my age is {0} years".format(age))

print("There're {0} Days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31,
      "January", "March", "May", "July", "August", "October", "December"))

print("\n")
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}
""".format(28, 29, 30))
# -------------------------------------------
# Another way with Python 2.0

# 1.0 concatenate string with int
print("my age is %d years" % age)
# 2.0 concatenate multiple string with /w numbers
print("my age is %d %s, %d %s" % (age, "years", 6, "months"))
print("\n")

# Using the Loop function for printing string within numbers
for i in range(1, 12):  # The numbers will start from the Right because of the spaces of digits that we increased
    print("No. %2d squared is %4d and the cubed is %4d" %
          (i, i ** 2, i ** 3))  # ** means caret
print("\n")

# print the operations
print("Pi is approximately %12f" % (22 / 7))
print("Pi is approximately %12.50f" % (22 / 7))
# -------------------------------------------
# Another way with Python 3.0
# Using the Loop function for printing string within numbers
print("\n")
for i in range(1, 12):  # The numbers will start from the Left because we haven't given it a specific space of digits
    # {NoOfFormat:>leftSpace} || {NoOfFormat:leftSpace} || {NoOfFormat:<rightSpace}
    print("No.{0:2} squared is {1:<4}and the cubed is{2:>5}"
          .format(i, i ** 2, i ** 3))  # ** means caret
print("\n")

for i in range(1, 12):  # Here, we gave it an open range of spaces depending of the range of digits "The ideal one"
    print("No. {} squared is {} and the cubed is {:4}"
          .format(i, i ** 2, i ** 3))  # ** means caret

# print the operations
print("Pi is approximately {0:12.50}".format(22 / 7))
