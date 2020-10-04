__author__ = "crypto"


class Polymorphism:
    """Polymorphism:
                That ability of object to have different forms is called Polymorphism - which
                 means many forms.

                 - Poly: many
                 - Morphe: form

    (-) Example: "in Python, there's no such mean of 'Types' only 'objects'"

    an int is not a float       int.__str__() ---------  >

    a float is not a list       float.__str__() --------->
                                                                    They all behave as "printable"
    a list is not a tuple       list.__str__() --------->           objects in addition to their normal
                                                                    behaviour as int, float, etc.
    a tuple is not an int       tuple.__str__() --------->


    All these objects are distinct types, but they can all be printed, because they all behave
    in the same way as far as the print function is concerned.
    --------------------------------------------------------------------
    (-) Example:

    a = 10  # int

    b = "hello" # string

    c  = 1, 2, 3    # tuple

    In this particular example, the polymorphic behaviour of the objects is implemented
    using inheritance, All Python objects inherit from a bas class called "object", which defines a __str__ method

    So, polymorphism allows the 'print' function to accept arguments of any type, and it's able to print them

    Java's a "statically typed" language, which means that the 'type' of everything is checked
    when the program's compiled. So if you try to pass a string to a method that expects an 'int',
    the program won't compile. In python, the 'type' of something is only of interest when it's used -
    Python's a "dynamically typed" language.

    By the way, this's what's meant by "Overloading" methods - you create different versions
    of the method that take different parameters. and the compiler decides which one to use based on
    the number and type of the parameters passed to it.

    In both languages, classes inherit from the topmost base called "object", and
    this base class defines a basic implementation of the "toString" method (in the case if java)
    and the "__str__" method in Python. The default implementation isn't very pretty, it just
    returns the name of the class, and a hash cod or the address in the memory where the object lives
    -------------------
    (-) Example:
        Java--
            public class Main {

                public static void main(String[] args){
                    Object x = new Object();
                    System.out.println(x);
                }
            }

        Output:
        java.lang.Object@67732b8
        -----------------------
        Python--
            x = object()
            print(x)

        Output:
        <object object at 0x7ff369fcd0258>


    So, polymorphism basically means that objects can be more than one thing at the same time.
    An 'int' is a number, so, it's something you can use to perform arithmetic.
    But it's also something that can be printed.

    "Inheritance" is one way to implement polymorphism. So, in this example of making things printable,
    every object can be printed, as well as used for whatever else it does.
    This is possible because every object automatically inherits the __str__ method from its object base class
    """