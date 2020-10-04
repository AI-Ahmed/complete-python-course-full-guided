__author__ = "crypto"

# in import techniques, we will try to import the blackjack

import Blackjack    # with import the Blackjack game, you can run it throw here

print(__name__)     # the name of the module which we can attach with the Blackjack program, by adding this line into the blackjack code, too or it will be printed as '__main__'

# now because we made Blackjack accessed by the main only, the game will not be executed from the Blackjack.py but we can now import the code

# you can run is with a code in terminal like that
# cd /Documents/PythonProgramming/Section06_Modules&Functions
# python -m Blackjack or python3 -m Blackjack

# lets try to access the Blackjack game, now using code:
Blackjack.play()
print(Blackjack.cards)      #to print the list of cards
