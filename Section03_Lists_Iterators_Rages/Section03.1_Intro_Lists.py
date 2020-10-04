__author__ = "Crypto"

# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))
# --------------------------------------------
# Append Example

parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]
parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)
# --------------------------------------------
# sort Example

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# numbers.sort()
# print(numbers)
print(sorted(numbers))

# lets test if the list of number is the same of sorted list

numbers_in_order = sorted(numbers)

if numbers == numbers_in_order:
    print("Lists are equal!")
else:
    print("Lists aren't equal!")  # <--- This will be the result because sorted() function create a new list

if sorted(numbers) == numbers_in_order:
    print("Lists are equal!")
else:
    print("Lists aren't equal!")

