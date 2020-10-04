__author_ = "crypto"


def python_food():
    print("spam and eggs")


# call the function
python_food()

# or we can just print it, but if you notice we were calling the function not printing its parameters' results
print(python_food())


# so, it will call the function and execute it beside printing the value which None.

# ------------------------------------------------------------------
# let's make it more interest

def python_food_1():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# instead of putting the lines 23, 24 we can pass them as a parameters in a function
# so, it gives use the right space for the text
def center_text(text):
# There're two types of function to produce a string str() and repr(). we need to use them not to face an error of parameter input
    text = str(text)
    # text = repr(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the functions

python_food_1()
center_text("spam and egg")
center_text("spam, spam and egg")
center_text(12)  # After calling str() it's not 1100     0000 1100 or C
center_text("spam, spam, spam, and spam")


# another notice, when you pass parameter with *arg for instance, it means you can pass many variables as you can sep by ,
# Example
print("first", "sec", 3, 4, "spam")
# --------------------------------------------------------------------------------------
# Notices

# difference between str()  and repr()

# import datetime
# today = datetime.datetime.now()
#
# # Prints readable format for date-time object
# print str(today)
#
# # prints the official format of date-time object
# print repr(today)

# Output:
#        2016-02-22 19:32:04.078030
#        datetime.datetime(2016, 2, 22, 19, 32, 4, 78030)
