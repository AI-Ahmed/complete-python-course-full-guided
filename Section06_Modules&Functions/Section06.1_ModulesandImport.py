__author__ = "crypto"

# Turtle is a module that give you the ability to graph lines

import turtle
# import time  # this module helps to give us time for the module to run on time

# if you notice, there an error related to reference structure, to fix that we need to use this hash

# noinspection PyUnresolvedReferences
turtle.forward(150)
# if you notice, the bug disappears but we can't do that with all the lines

# you can click on the item itself and "unresolved references"
turtle.right(250)   # degree
turtle.forward(150)

# style 01
# time.sleep(5)

# style 02
turtle.done()   # the graph will still up there until you stop it!

# if you want to get back the error
# Analyze ->  Configure Current file Analysis -> configure inspections -> python -> unresolved Ref -> ignore ref

# ----------------------------------------------------------------------------------------------------------------------

# for importing a specific function from module

from turtle import forward, right, done
import turtle
forward(150)
right(250)
forward(150)
turtle.circle(75)
done()

# ----------------------------------------------------------------------------------------------------------------------

# we can import everything using * (Not recommended)

from turtle import *
