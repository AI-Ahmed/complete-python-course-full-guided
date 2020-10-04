__author__ = "Crypto"

# # Read a file
print("simplest way to read a file\n")

sample = open("sample.txt", 'r')

# sample = open("/home/crypto/Desktop/sample.txt", 'r')
for i in sample:
    print(i)

sample.close()
# -------------------------------------------------------------
print('=' * 40)
# if you want to specify a certain line you can do that

sample = open("sample.txt", 'r')

for i in sample:
    if "jabberwock" in i.lower():
        print(i, end='')

sample.close()
# -------------------------------------------------------------
print('=' * 40)
# another good way to read a file and that will be the best way you can go with it
# copied from python2.5

with open("sample.txt", 'r') as sample:
    for line in sample:
        if "JAB" in line.upper():
            print(line, end='')
# you don't need here to close() because 'with' can handle that after the end of the file
# -------------------------------------------------------------
print('=' * 40)
# another way to open the whole file without facing the double spacing
print("Best way to read a file without facing the double space\n")

with open("sample.txt", 'r') as sample:
    line = sample.readline()  # the benefit of this line is to check whether the
    #                             file has a problem or empty so that it will not enter the while wall
    while line:
        print(line, end='')
        line = sample.readline()
# -------------------------------------------------------------
print('=' * 40)
# Now, lets print the file into a list
# this will be not beneficial for large lines

# with open("sample.txt", 'r') as sample:
#     lines = sample.readlines()  # this will help to read the entire file at once to a list
# print(lines)
#
# # print the values of the list
# for line in lines:
#     print(line, end='')  # end will help us here to avoid the double spacing line

# to avoid the mixed line between the lines and the list

with open("sample.txt", 'r') as sample:
    lines = sample.readlines()  # this will help to read the entire file at once to a list
print(lines)

# print the values of the list
for line in lines[::-1]:
    print(line, end='')  # end will help us here to avoid the double spacing line
