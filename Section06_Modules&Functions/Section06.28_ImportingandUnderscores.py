__author__ = "crypto"

# unlike other languages, with python you can miss out with the variables
# there's no Private or protected variables in python

#  so, lets try miss out with Blackjack
import Blackjack

Blackjack._deal_card(Blackjack.dealer_card_canvas)   # we've added new card to the dealer's canvas which something unusual
# Blackjack.play()

# if you notice, we're giving access to areas of the game that we wouldn't ordinarily want someone who's imported this
# module to be access our code that way that sort of breaking the game.
# so, the way you can protect these function from hacking or editing, you can add _ at the beginning of the function:
# Example: deal_card() ---> _deal_card()

# you've to be careful when you add this underscore, because it may effect you code.
# so, if you're writing your own code, it doesn't matter, you may know what you're doing

# ----------------------------------------------------------------------------------------------
print('='*40)

# Let's talk about importing the module
g = sorted(globals())
for x in g:
    print(x)
print('='*20)
# if you notice, the Blackjack module when we imported it, it has been imported as the module itself not the contents of it
# we can now import the contents (which something not recommended):
from Blackjack import *

g = sorted(globals())
for x in g:
    print(x)
# if you notice here everything in the Blackjack module has been imported

# ----------------------------------------------------------------------------------------------
print('='*40)

# underscore can be used as a variables: Ex
personal_details = ("Tim", 34, "Australia")

name, _, country = personal_details
print(name, country)
print(_)
