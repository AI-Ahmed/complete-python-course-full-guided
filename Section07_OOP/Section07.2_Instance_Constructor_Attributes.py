__author__ = "crypto"

# Let's summarise what we've mentioned in the last session
"""
Class: template for creating objects. All created object using the same class will have the same characteristics

Object: an instance of a class

Instantiate: create an instance of a class.

Method: a function defined in a class.

Attribute: a variable bound to an instance of a class

self: It's a reference to the instance of the class

Constructor: refers to special method that is executed when an instance of a class is created or constructed in Python
"""
# In another language, our sample program is being of type 'Kettle' but they also have
# types that are not classes. But in python --> every type is a class which is why
# we were able to call __add__ method of "Class int" object at the start of the previous video
#
""" 
Function that are bounded to a class called methods, and the main difference between 
method and function is the presence of this self parameter that's been added automatically
"""


class Kettle(object):

    def __init__(self, make, price):    # constructor
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)   # instance from Kettle class

hamilton = Kettle("Hamilton", 14.55)    # instance from Kettle class

print(hamilton.on)
# hamilton.switch_on()
# print(hamilton.on)

# we can call the method with the class itself
Kettle.switch_on(kenwood)
print(kenwood.on)
# -------------------------------------------------------------------
print()
# Python classes are dynamic and it can be modified after being created

hamilton.power = 1.5    # if you notice power variable isn't in Kettle class
print(hamilton.power)
print(kenwood.power)    # you notice that this will give an error unlike hamilton

# That's because kenwood instance doesn't have a power attribute. but in line 55
# we added an instance variable for hamilton instance of the kettle class but of course
# we didn't do that for kenwood instance, that's why we got and error.
