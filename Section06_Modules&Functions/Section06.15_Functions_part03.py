__author_ = "crypto"


def center_text(*args, sep=' ', end='\n', file=None, flush=False):  # args is default parameter's value
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


#
# with open("centred", mode='w') as centred_file:
#
#     # call the functions
#     center_text("spam and egg", file=centred_file)
#     center_text("spam, spam and egg", file=centred_file)
#     center_text(12, file=centred_file)  # After calling str() it's not 1100     0000 1100 or C
#     center_text("spam, spam, spam, and spam", file=centred_file)
#     center_text("first", "sec", 3, 4, "spam", file=centred_file)
#     center_text("first", "sec", 3, 4, "spam", sep=":", file=centred_file)  # at the end you will face a problem that last char : will be at the end of the text
# -----------------------------------------------------------------
# the above code flush print is only works in python 3.3, so, there's anothor way for returning this value which 'return' in python 3.2


def center_text_1(*args, sep=' '):  # args is default parameter's value
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text  # require string


# with open("centred", mode='w') as centred_file:

# if you notice when you return the value you need to print the function into your code instead of calling the function only,
# because printing is actually print 'returned' value

# call the functions
# print("spam and egg")
# s = center_text_1("spam, spam and egg")
# print(s)
# print(center_text_1(12))  # After calling str() it's not 1100     0000 1100 or C
# print(center_text_1("spam, spam, spam, and spam"))
# print(center_text_1("first", "sec", 3, 4, "spam"))
# print(center_text_1("first", "sec", 3, 4, "spam"))  # at the end you will face a problem that last char : will be at the end of the text
#
# print("=" + str(12 * 3))
# print(sorted(["b", "a", "c", "d"]))

with open("menu", mode='w') as menu:
    s1 = center_text_1("spam, spam and egg")
    print(s1, file=menu)
    s2 = center_text_1(12)  # After calling str() it's not 1100   0000 1100 or C
    print(s2, file=menu)
    s3 = center_text_1("spam, spam, spam, and spam")
    print(s3, file=menu)
    s4 = center_text_1("first", "sec", 3, 4, "spam")
    print(s4, file=menu)
    s5 = center_text_1("first", "sec", 3, 4, "spam")  # at the end you will face a problem that last char : will be at the end of the text
    print(s5, file=menu)
    print("=" + str(12 * 3))
    print(sorted(["b", "a", "c", "d"]))
