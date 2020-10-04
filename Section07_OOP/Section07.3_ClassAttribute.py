__author__ = "crypto"

# one of the notice that methods is also an attribute of the classes
# also, classes can have an attributes related to it!


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):    # constructor
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)   # instance from Kettle class

hamilton = Kettle("Hamilton", 14.55)    # instance from Kettle class

# lets print the Kettle attribute and see if it shares the same value or not
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# Let's try to print the namespace via the __dic__ attribute
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

"""
what we're trying to accomplish here is when we ty to access the power_source
attribute for the instance. Python checks to see if the power_source exists in the
instance name space. If it doesn't which is the case here. It then checks the class for the instance and finds
power_source in the Kettle class and that's why the reason it printed out because 
basically it got it from the class attribute  
"""
print()
# let's try to change class attribute value from here
Kettle.power_source = "atomic"
print("Switch to Atomic")
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
# that's prove how python dynamically works beside the concept of the global variables
