__author__ = "crypto"

# Now, we need to take a consider that the images being used in this code where downloaded from:
#    svg-cards.sourceforge.net
# you need to take care of mentioning that this images which have been taken from this site for copyright's purposes
#
# if your Tkinter's version is 8.5 or below, you've to use the 'cards_ppm.zip' for your code,
# otherwise, you can use the 'card_png.zip'

import random

try:
    import tkinter
except ImportError:  # python 02
    import Tkinter as tkinter


# Function Time
# --------------
# image import


def _load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the images for the cards
    for suit in suits:
        # for the number 1 to 10
        for card in range(1, 11):
            name = 'Blackjack/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name).subsample(2, 2)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'Blackjack/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name).subsample(2, 2)
            card_images.append((10, image,))


# -------------------------------------------------------------------------


def _deal_card(canvas):
    # pop the next card off the top of the deck
    # next_card = deck.pop()  # pop is a way to retrieve an item from a list that also removes it from the list at the same time
    # but, if we left the code like that, the card will be popped from the top and the bottom which something wrong
    next_card = deck.pop(0)  # so, we need to ensure that we pop the card from the top only
    deck.append(
        next_card)  # this one is more realistic because when you finish the round, you put the card into the back of the deck of cards
    # add the image to the Label and display the label
    tkinter.Label(canvas, image=next_card[1], relief='raised').pack(side='left')
    return next_card


# -------------------------------------------------------------------------
# sometimes there're global variables being accessed by multiple function, that may cause a mistake or a problem.
# so, its better to create variables getting accessed by the other functions to keep the variables save


def ace_handling(card):
    # Calculate the total score of all cards in the list.
    # Only one ace can have value 11, and this will be reduce to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in card:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


# -------------------------------------------------------------------------

# Deal Player function


def deal_player():
    player_hand.append(_deal_card(player_card_canvas))
    player_score = ace_handling(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        resultText.set("Dealer Wins!!")

    # # now, if you want to use the global variables without shadowing or facing the problem of local variables
    # global player_score
    # global player_ace
    # # notice the difference between player_score && player_ace and why intellij give an error on player_score and not in player_ace
    # # Answer: when we're using player_ace, we're not assigning new variable to it, unlike player_score. So, intellij gave us a warning about it
    # # test it! by ctrl + click, you'll find the player_score assigned as local value and player_ace assigned as Global value
    # # intellij allows you to use global variable in a function until you try to change its value, then intellij will create another variable with the same name as local variable
    # # player_score = 0
    # card_value = deal_card(player_card_canvas)[0]  # assigning the result from this function
    #
    # if card_value == 1 and not player_ace:  # by default and ace has got a value 1 and what we're saying here is if an ace
    #     #                                     was drawn from the card from the deck and
    #     #                                     the player hasn't already got an ace in their hand then we're going to
    #     #                                     assign 11 to this particular card.
    #     player_ace = True   # you've ace and not above 21
    #     card_value = 11
    #
    # player_score += card_value
    #
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False  # you've ace and above 21
    #
    # if player_score > 21:
    #     resultText.set("Dealer Wins!")
    # print(locals())     # for printing all the local variables
    #
    # player_score_label.set(player_score)


# -------------------------------------------------------------------------
# Deal Dealer function
#  The computer should really play the part of the dealer and all the players should do is
#  click their own button for more cards or click dealer button once they want to 'stick'
#  So, the deal_dealer function that's called when the dealer button is clicked will need to score the dealer's hand
#  which only has single card to begin with and then automatically keep dealing more cards until
#  the dealer score is <= 17 or dealer goes bust (over 21) and once that happen
#  the score are then check and the results are displayed so, let's go back


def deal_dealer():
    dealer_score = ace_handling(dealer_hand)
    while 0 < dealer_score < 17:  # after editing
        dealer_hand.append(_deal_card(dealer_card_canvas))
        dealer_score = ace_handling(dealer_hand)
        dealer_score_label.set(dealer_score)
    # so, it should automatically keep dealing cards for him until it get to the score of 17 or higher
    # so, if the dealer has initial card of 8 and the player 'stick', then the dealer will deal with card until he gets total score of 17 or higher
    # so, he may deal with 2 or 3 cards in one deal

    # Rules
    player_score = ace_handling(player_hand)
    if player_score > 21:
        resultText.set("Dealer Wins!!")
    elif dealer_score > 21 or dealer_score < player_score:
        resultText.set("Player Wins!!")
    elif dealer_score > player_score:
        resultText.set("Dealer Wins!!")
    else:
        resultText.set("Draw!!")


# -------------------------------------------------------------------------
# Computer intial deal

def _initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_canvas))
    dealer_score_label.set(ace_handling(dealer_hand))
    deal_player()

# -------------------------------------------------------------------------


def new_game(canvas):
    global dealer_card_canvas
    global player_card_canvas
    global player_hand
    global dealer_hand
    canvas = canvas.winfo_children()
    for items in canvas:
        items.destroy()  # destroy all widgets in the two canvas

    dealer_card_canvas.grid_remove()  # grid_remove() for Canvas && grid_destroy() for Frame
    player_card_canvas.grid_remove()

    # canvas.destroy()    # instead of the above code

    resultText.set(' ')
    player_hand.clear()
    dealer_hand.clear()
    # deck.clear()

    dealer_card_canvas = tkinter.Canvas(card_frame, background="green")
    dealer_card_canvas.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_canvas = tkinter.Canvas(card_frame, background="green")
    player_card_canvas.grid(row=2, column=1, sticky="ew", rowspan=2)


def resContent():
    global deck
    new_game(player_card_canvas)
    new_game(dealer_card_canvas)

    # deck = list(cards)    # not obviously realistic, because not every time you start a new game you start with new dec of cards
    random.shuffle(deck)

    player_score_label.set(player_hand)
    dealer_score_label.set(dealer_hand)

    # it will be better if we create a method to handel the initial deal better than this duplicates

    # # player gets his first card automatically
    # deal_player()
    # # then the dealer card
    # dealer_hand.append(deal_card(dealer_card_canvas))
    # # show the dealer score
    # dealer_score_label.set(ace_handling(dealer_hand))
    # # then the player second card
    # deal_player()
    _initial_deal()


# Related to Importing Techniques, if you want your game getting accessed by any other code you've to create a function that allows it to be accessed by it
def play():

    # deal_player()
    # dealer_hand.append(deal_card(dealer_card_canvas))
    # dealer_score_label.set(ace_handling(dealer_hand))
    # deal_player()
    _initial_deal()
    tkinter.mainloop()


# -----------------------------------------------------------------------------------------
# Module name
print(__name__)

# if we want Blackjack game being executed ONLY or accessed only by the main code, you can put this line:

# if __name__ == '__main__':

# GUI
# set up the screen and frames for the dealer and player
mainWindow = tkinter.Tk()
mainWindow.title("Blackjack")
mainWindow.geometry("575x600")
mainWindowPaddingX = 1
mainWindow['padx'] = mainWindowPaddingX
mainWindow['pady'] = 2
mainWindow.configure(background='white')

# Result Label
resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText)
result.grid(row=0, column=0, sticky='n', columnspan=3)

# Card Frame
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2, ipady=3, ipadx=2)

# Dealer menu
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Dealer Canvas
# embedded frame hold the card images
dealer_card_canvas = tkinter.Canvas(card_frame, background="green")
dealer_card_canvas.grid(row=0, column=1, sticky="ew", rowspan=2)

# ---------------------

# Player menu
player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)  # 'fg' is the label's colour
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Player Canvas
# embedded frame hold the card images
player_card_canvas = tkinter.Canvas(card_frame, background="green")
player_card_canvas.grid(row=2, column=1, sticky="ew", rowspan=2)

# ---------------------

# buttons_frame
buttonFrame = tkinter.Frame(mainWindow, relief='raised', borderwidth=2)
buttonFrame.grid(row=4, column=0, columnspan=3, sticky="w")

# Dealer Button
# dealer_button = tkinter.Button(buttonFrame, text="Dealer", command=deal_card)   # you've to be very careful when you pass the function to the object, if you passed the function with the parameter within 'function(parameters)', that's mean you want the event to be executed when you user click on the button instead of making it active for multiple time 'function'. what has been meant here is you want to assigning the command instead of calling the function. what's really mean by that you need to assign the function rather assigning the result of calling the function. Now, we're facing a problem of how we'll assign the parameters to a specific canvas of dealer and player. what we can do it to create two function that help to assign the canvas of the player and the dealer within the function.
dealer_button = tkinter.Button(buttonFrame, text="Dealer", command=deal_dealer)  # command represents the event in java
dealer_button.grid(row=0, column=0)

# Player Button
player_button = tkinter.Button(buttonFrame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# New game button
newGame_button = tkinter.Button(buttonFrame, text="New Game", command=resContent)
newGame_button.grid(row=0, column=2)

# Exit Button
exit_button = tkinter.Button(buttonFrame, text="Exit Game", command=mainWindow.quit)
exit_button.grid(row=0, column=3)

# load cards
cards = []
_load_images(cards)
print(cards)
# create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)
# another mini challenge, if you want to play with 2 or more pack of cards you can add more to the deck
# deck = list(cards) + list(cards) + list(cards)

# create a list to store the Dealer's and player's hands
dealer_hand = []
player_hand = []

# ---------------------------------------------------------------------------------------------
# Computer "Dealer"

# Focus that the main program don't want the dealer to play his turn as their initial card
# we just want them to 'deal' a card and stored in their hands
# player gets his first card automatically
# deal_player()
# then the dealer card
# dealer_hand.append(deal_card(dealer_card_canvas))
# show the dealer score
# dealer_score_label.set(ace_handling(dealer_hand))
# then the player second card
# deal_player()
# ----------------------------------------------------------------------------------------------
# sizing
mainWindow.update()
mainWindow.minsize(card_frame.winfo_width() + mainWindowPaddingX + buttonFrame.winfo_width(),
                   card_frame.winfo_height() + buttonFrame.winfo_height())
mainWindow.maxsize(card_frame.winfo_width() + 550 + mainWindowPaddingX + buttonFrame.winfo_width(), 600)

# This one instead of "Computer Dealer" line 313, or there will be some duplicates and unrealistic bug
if __name__ == "__main__":
    play()
