__author__ = "crypto"

# Challenge

# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid Statements,
# but consider using lists and a for loop
#
# There's no need to store the buttons in variables.
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and .winfo_width()
# methods, in which case you should know that they will not return the correct
# results unless the window has been forced to draw the widgets by calling its .update()
# method first.
#
# if you're using Windows you will probably find that the width
# is already constrained and can't be resized too small.
# the height will still need to be constrained, though.

try:
    import tkinter
except ImportError:     # python 2
    import Tkinter as Tk

mainWindows = tkinter.Tk()

mainWindows.title("calculator")
mainWindows.geometry("340x280+120+180")
mainWindows.minsize(340, 280)
mainWindows.maxsize(340, 280)
mainWindowsPaddingX = 85
mainWindows['padx'] = mainWindowsPaddingX
mainWindows['pady'] = 50
# --------------------------------------
# Label
resultLabel = tkinter.Entry(mainWindows)
resultLabel.grid(row=0, column=0, sticky="ns")
resultLabel.winfo_width()
# --------------------------------------
# Generate Buttons
keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]
keyPad = tkinter.Frame(mainWindows, relief='ridge', borderwidth=5)
keyPad.grid(row=1, column=0, sticky='nswe')
r = 0
for keyRow in keys:
    c = 0
    for keys in keyRow:
        tkinter.Button(keyPad, text=keys[0], relief="raised").grid(row=r, column=c, sticky=tkinter.E + tkinter.W)
        c += keys[1]
    r += 1

# we can also use the win.update() so, we can min and max but without effect the window
# mainWindows.update()
# mainWindows.minsize(keyPad.winfo_width() + mainWindowsPaddingX, resultLabel.winfo_height() + keyPad.winfo_height())
# mainWindows.maxsize(keyPad.winfo_width() + 50 + mainWindowsPaddingX, resultLabel.winfo_height() + 50 + keyPad.winfo_height()
# 50 is recommendation for max size to make the GUI works on any OS
mainWindows.mainloop()
