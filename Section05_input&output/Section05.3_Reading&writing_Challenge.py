__author__ = "Crypto"

# write a program that append the time tables to our jabberwocky poem
# in the sample.txt. We want the table from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 2).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this
# 1 times 2 is 2
# 2 times 2 is 4
# 3 times 2 is 6
# 4 times 2 is 8
# 5 times 2 is 10
# 6 times 2 is 12
# 7 times 2 is 14
# 8 times 2 is 16
# 9 times 2 is 18
# 10 times 2 is 20
# 11 times 2 is 22
# 12 times 2 is 24
# ---------------------
result = 0
with open("sample1.txt", 'a') as counting_file:
    for i in range(1, 13):
        for j in range(2, 13):
            result = i * j
            print("{0} times {1} is {2}".format(i, j, result), end='  \t', file=counting_file)
        print(" ", file=counting_file)
