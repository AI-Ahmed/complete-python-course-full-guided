__author__ = "crypto"

# Graphical User Interfaces with Tk

# for defending some error we can use this exception
try:
    import tkinter
except ImportError:     #python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()   # for Tkinter testing

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
# geometry("640x480'+ or -'leftEdge'+ or -'rightEdge") by pixels
# Example .geometry("SIZE x SIZE + LEFT EDGE MERGE SPACE + TOP EDGE MERGE SPACE ") <-- '-' OR '+' for the windows location
mainWindow.geometry("640x480+12+500")
mainWindow.mainloop()
