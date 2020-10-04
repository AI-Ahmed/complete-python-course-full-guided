__author__ = "crypto"

# create a program that takes some text and returns a list of
# all the characters in the test that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string

text = input("please enter some text: ")
char = set(text)
vowels = frozenset("aeiou")    # this will be better because frozen is immutable set that can't be change or modify
#vowels = set(["a", "e", "i", "o", "u"])
char.discard(' ')
char.difference_update(vowels)
print(char)
print(list(sorted(char)))



