__author_ = "crypto"

# another notice, when you pass parameter with *arg for instance, it means you can pass many variables as you can sep by ,

# Example 01 - with print function
print("first", "sec", 3, 4, "spam")
# -----------------------------------

# Example 02 - with created function


def center_text(*args):     #  args is default parameter's value
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# -----------------------------------

# Example 03 - print parameters into our owned function

# you can change the name of the parameters, it's not restricted names then manipulate it with the print function


def center_text_1(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):     #  args is default parameter's value
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char, file=centered_file, flush=flush_me)


# call the functions
center_text("spam and egg")
center_text("spam, spam and egg")
center_text(12)  # After calling str() it's not 1100     0000 1100 or C
center_text("spam, spam, spam, and spam")
center_text("first", "sec", 3, 4, "spam")
center_text_1("first", "sec", 3, 4, "spam", sep=":")    # at the end you will face a problem that last char : will be at the end of the text
print()



