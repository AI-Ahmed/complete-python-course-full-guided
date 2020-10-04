__author_ = "crypto"


class Player(object):
    """Player is the class object that will play the game

    Attribute(s):
        name (str): The name of the player
        lives (int): The player changes for continue the game-play
        level (int): Player's level in the game
        score (int): Player's score in the game
    """

    def __init__(self, name):
        self.name = name
        self._lives = 3  # change the variable name for sick of privacy
        # self.lives = 3    # if you tried to pass this variable like that and tried to increase or decreased the value of it,
        #                     you will get an error. that's because you passed this variable to setter method within value of 3.
        #                     if you changed the value itself, that will give an error
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        # let's make some validation not to address lives variables less than 0
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative!")
            self.lives = 0

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level     # Calculate how many level the player incremented
            self.score += delta * 1000      # calculate the score
            self._level = level     # the player recent level
        else:
            print("Level can't be less than 01")

    def _get_level(self):
        return self._level

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # another Alternative for getter and setters something called (decorators)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    # lets create a function that prints the string information of the class each and every time we print the instance of the class
    def __str__(self):
        return """
===============================
Name: {0.name}
Live(s): {0.lives}
Level(s): {0.level}
Score(s): {0.score}
===============================""".format(self)
# ---------------------------------------------------------------------------------
# Section 07.15 Getter and Setter
# using getter or setter isn't actually something recommended in python,
# so, you don't want to create them for sick of it.
# in C++ or java, they were creating them for accessing the private or the protected variables
# [Args, Attribute] not to change them or miss with them.
#  but in Python, there's a quote we're saying that you're adult enough to know how and what variables
#  you need to access and what not, beside that most of the variables are reference not the main one
#  som you're not miss with them, literally
# ---------------------------------------------------------------------------------
# Section 07.16 Data Attributes and Properties

# Challenge:
#       Modify the Player class so that the players' scores are increased by one thousand every
#       time their level increases by one.
#
#       So if they jump up two levels, they'll get a bonus of two thousand added to their score.
#       If the players drops back a level, they'll lose one thousand for each level they drop back.
#
#       They can't go below Level One, so your solution should prevent that from happening.
#
#       The  aim of this challenge is to practise properties, so although it may makes more sense
#       to add methods to increase and decrease the level, please don't do it that way - use property.
