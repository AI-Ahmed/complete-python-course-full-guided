__author__ = "crypto"
# Section 07.16: Composition


class Wings:
    """we'll need to create a "Wing class" to compose the "Duck Class"
     So, any duck objects we create will have their own wing object and
     can use the attributes of a wing the wing's fly method

     Attribute(s):
         ratio (float): The ratio of the level of wings' actions

     Method(s):
        fly(): a method that control the wings
    """
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this's fun")
        elif self.ratio == 1:
            print("This's hard work, but I'm flying")
        else:
            print("I think I'll just walk")

# ==============================================================================
# Section 07.15: Duck Test
# in this session we wil try to introduce and figure the use of polymorphism


class Duck:
    # now, we've to create the Duck constructor to include the wings object
    # this's how you can implement the composition by including object of
    #  the class into another class. By syntax (Duck has a Wings)
    def __init__(self):
        self._wings = Wings(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wings.fly()   # Wings methods, too


class Penguin:

    def walk(self):
        print("Waddle, waddle, I waddle, too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':

# Section 07.15: Duck Test
#     donald = Duck()
#     test_duck(donald)
#
#     percy = Penguin()
#     test_duck(percy)

# if you notice here, with two different classes produce different sort of outputs using the same function
# although Penguin isn't a duck but it can walk, swim and quack (you can check Polymorphism.py for more details)
# ==============================================================================
# Section 07.16: Composition
    donald = Duck()
    donald.fly()
