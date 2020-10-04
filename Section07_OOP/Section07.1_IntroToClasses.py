__author__ = "crypto"

"""
OOP which Object_Oriented Programming:
          Aims to combine data and the processes act on that data into object
          which is called encapsulation.

encapsulation involves encapsulation the functionality of the program "data and methods"

OOP makes use of imperative programming within the methods that objects used to manipulate the data.
OOP works into sort of steps that leads the data to be processed into some sort of methods which 'steps'

One more thing which important "Everything in Python is an object!"
unlike java, which is Class-based object-oriented
"""

"""
Imperative Programming: 
        is a paradigm of computer programming in which the program describes a sequence of steps that change the state of the computer. 
        Unlike Functional programming --> 'declarative programming', which describes "what" a program should accomplish, 
        'imperative programming' explicitly tells the computer "how" to accomplish it. 
        Programs written this way often compile to binary executables that run more efficiently 
        since all CPU instructions are themselves imperative statements.

Paradigm: new method of thinking about a problem or situation.

============================

Python is Multi-paradigm Language
            imperative Programming 
                            <Shell Scripting>
            procedural programming 
                            <language with functions>
            Declarative programming 
                            <functional programming>
"""
# Example about that:

a = 12
b = 4
print(a + b)
print(a.__add__(b))     # in python, we used string object to run a data operation, which something totally different from what we learned in C or Java
print()
# on more thing, in python.. running a method is actually the same of running function
#
# Now, we will give you an example of python objects used by writing a code about the 'electric kettle'.. like the steps of lightning an 'electric kettle' :D
# ----------------------------------------------------------------------------------------------------------------------

"""
class is set of template from which objects can be created
and all objects created from the same class will share the same characteristics
"""


class Kettle(object):   # if you tried to write down the class name with small case instead of CamelCase, intelliJ will give you an error

    def __init__(self, make, price):    # it's look like the constructor in java, 'self' is 'this'
        self.make = make
        self.price = price
        self.on = False


# so, now if i created kettle called 'Kenwood' then 'Kenwood' will be instance of the Kettle class
kenwood = Kettle("Kenwood", 8.99)   # instance from Kettle class
print(kenwood.make)     # retrieved value
print(kenwood.price)    # retrieved value

kenwood.price = 12.55
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)    # instance from Kettle class

print("module: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

"""
one of the important points here you have to understand that Kenwood and hamilton are objects.
so, we can specify their attributes in the replacement fields
"""
print("module: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))


# From Microsoft
"""
Functional Programming vs. Imperative Programming

The functional programming paradigm was explicitly created to support a pure functional approach to problem solving. 
Functional programming is a form of declarative programming. In contrast, most mainstream languages,
including object-oriented programming (OOP) languages such as C#, Visual Basic, C++, and Java were designed to primarily support imperative (procedural) programming.

With an imperative approach, a developer writes code that describes in exacting detail the steps that the computer must take to accomplish the goal. 
This is sometimes referred to as algorithmic programming. In contrast, a functional approach involves composing the problem as a set of functions to be executed. 
You define carefully the input to each function, and what each function returns. The following table describes some of the general differences between these two approaches.

"""