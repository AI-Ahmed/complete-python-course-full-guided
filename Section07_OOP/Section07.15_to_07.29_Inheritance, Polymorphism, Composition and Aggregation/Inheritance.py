__author__ = "crypto"


class Inheritance:
    """ Define a base that objects are based on, things that are common
    for classes that derive from the base class. then we can allow a class
    to define a unique characteristics of itself just like in the bird example

                                    Class  Bird
        Base Class                     +Beak
           or      ---->               +wings
        Super class                      |
                                         |
                                         |
                                         |
                  _____________________________________________
                  |           |          |          |         |
                  |           |          |          |         |
                Eagle       Crow        Gull      Ostrich   Penguin

                                        Subclass


    In Python, Classes can inherit directly from several superclasses, which
    known as "multiple Inheritance. Many Languages don't allow this,
    so the class structure ends up being strictly hierarchical as I've shown here,
    Java classes, for example, can have more than one superclass, but it has to be hierarchical

                                    Class  Bird
        Base Class                     +Beak
           or      ---->               +wings
        Super class                      |
                                         |
                                         |
                                         |
                    _____________________________________________
                   |                                            |
                   |                                            |
                FlyingBird                                FlightlessBird
                 +fly()                                         |
       ____________|___________                        _________|___________
       |           |          |                        |                   |
       |           |          |                        |                   |
     Eagle       Crow        Gull                    Ostrich             Penguin
                                                      +Run()              Swim()
                                        Subclass



    Python allows multiple inheritance, but i strongly recommend you avoid it until
    you're really comfortable with classes and inheritance. Once you're really
    comfortable with classes and inheritance, i recommend you multiple inheritance.
    The Sphinx may have inherited the head of a human, the body if a loin and the wings
    of a bird, but you don't see many sphinxes wandering around. If nature's decided that
    multiple inheritance is a bad idea, I'm not going to argue

    So, you can write that code once, put that code in the "Super" class and then any class
    that "extends" or "inherits" from - the're the same thing effectively - that class,
    is going to be able to take advantage of the properties or methods that are defined in the
    "Super" class

    """


help(Inheritance)
