__author__ = "crypto"
# One important aspect you need to understand that "any superClass you're creating is ultimately  sub-class from a built-in class called "object" <Only Python 3.0>
import random


class Enemy:    # or Enemy(object)
    """The Base class for all the things our players will have to fight
    in this fictional game.

    This's The Super class and any class that extends this class or inherits,
    should always have these attributes

    Attributes:
        name (str): The enemy name.
        hit_points (int): the scores of hitting the target.
        lives (int): the total changes of getting alive in the fictional game

    Methods:
        take_damage(damage(int)): the interaction results between the enemy and the players
    """
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._set_point = hit_points
        self._lives = lives
        self._alive = True

    @property
    def alive(self):
        return self._alive

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("\nI took {} point(s) damage and {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} Lost a life".format(self))
                self._hit_points = self._set_point
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Hit Point(s): {0._hit_points}, Live(s): {0._lives}".format(self)


class Troll(Enemy):     # Troll class extends/ inherit from Enemy class
    # pass    # is an object that doing nothing rather than running the programme without facing a problem into the method or the object we're dealing with
    # now,we will create the Troll constructor method instead of passing the superclass attributes\methods
    def __init__(self, name):
        # pass    # if we passed the attributes of the superclass like that we'll get an error of localization the attributes
        # so, there're multiple way to pass the superclass attribute and the last one will be for Python 3.0

        # [Prefixing the superclass method]

        # (Python 2.0) --> import the superclass constructor and prefixing the parameter like we want
        # Enemy.__init__(self, name=name, hit_points=20, lives=1)

        # SPython 3.0:
        # super(Troll, self).__init__(name=name, hit_points=20, lives=1)
        super().__init__(name=name, hit_points=20, lives=1)  # Recommended

    def grunt(self):
        print("Me {0._name}, {0._name} stomp you!".format(self))
# ==============================================================================================
# Section 07.21: Changing Behavior of Methods

# Challenge:
#       Create a new "Vampire" class that's a subclass of Enemy.
#       Vampire have 3 lives, and take 12 hit points of damage.
#  you can create a new python file for the Vampire if you like, but i'd suggest adding the existing "superClass_Enemy.py"
#
# Test your class by creating one or two Vampire instances and display their details
# Also inflict some damage  to make sure the "take_damage" method works ok.
#
# Also make sure that the trolls can also take damage. because we haven't tested yet


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 4) == 2:    # Number of time the vampire dodge the hit
            print("\t\t**** {0._name} Dodges ****".format(self))
            return True
        else:
            return False

    # Section 07.12: Overriding the Methods
    # Overriding Method in Python you just write a new method with the same name as
    # as the one that you want to override. the new method doesn't even have to have
    # the same or accept the same number of parameters although it usually will so.

    def take_damage(self, damage):
        if not self.dodges():   # now dodging turns to be apart of the vampire class
            super().take_damage(damage=damage)

    # one of the problem that we need to focus on is to prefixing the Attributes of the class
    # not to be easily accessed by adding _ to the variables
# ==============================================================================================
# Section 07.13: Regular Expression to change the variables name + Inheritance Challenge

# To change the Class Attributes name in the print()
# you can use this Regex (Ctrl+R): (\{\d\.)
#                                  $1_
#  \ : means escape anything before the next letter
# \d : matches any digits
# $1 : specifies anything that matches inside the parentheses in the search box
# ---------------------------------------------------------------------------
# Challenge:
#   Create a VampireKing subclass of Vampire
#   VampireKing is going to be incredibly powerful,
#   and any points of damage inflicted will be divided by 4
#   VampireKing objects will also start off with 140 hit points.
#
#   So, extend Vampire to create VampireKing class with those additional properties
#
#   Test the new class by creating a new VampireKing object and checking that it does
#   start with 140 hit points and only takes a quarter of the damage inflicted.


class VampireKing(Vampire, Enemy):
    def __init__(self, name):
        Enemy.__init__(self, name=name, hit_points=140)

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage // 4)   # use the // to prevent the double number to int

