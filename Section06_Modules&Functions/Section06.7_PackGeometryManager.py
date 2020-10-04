__author__ = "crypto"

import tkinter

# structure of Pack GM

#   Main Window     <-- Root Geometry Manager
#       Frame   <-- Frame Manager
#           Pack   <-- Pack Manger
#              canvas_left    <-- canvas_left widget Displaying graphics

mainWindows = tkinter.Tk()

mainWindows.title("Pack Geometry Manager")
mainWindows.geometry("640x480+8+200")

# Main Windows

label_windows = tkinter.Label(mainWindows, text="Main Windows")
label_windows.pack(side='top')

# --------------------------------------------------------

# Pack
#    geometry manager organizes widgets in blocks before placing them in the parent widget.
#    It uses the options fill, expand and side.

# widget.pack( pack_options )

# Example:
#   widget.pack(side = "bottom")
#   widget.pack(side =  "left")
#   widget.pack(side = "right")
#   widget.pack(side = "top")

# --------------------------------------------------------
# Left Frames

leftFrame = tkinter.Frame(mainWindows, relief="raised", borderwidth=2)
label_frame = tkinter.Label(leftFrame, text="Left_Frame")
label_frame.pack(side='top')

# canvas_left
canvas_left = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)

label_canvas_left = tkinter.Label(canvas_left, text="canvas_left")
label_canvas_left.pack(side='top')

# Packs' Examples

#   Buttons
button1_canvas_left = tkinter.Button(canvas_left, text="button1")
button2_canvas_left = tkinter.Button(canvas_left, text="button2")
button3_canvas_left = tkinter.Button(canvas_left, text="button3")
button4_canvas_left = tkinter.Button(canvas_left, text="button4")

button1_canvas_left.pack(side='top', anchor='n')
button2_canvas_left.pack(side='bottom', anchor='s')
button3_canvas_left.pack(side='right', anchor='w')
button4_canvas_left.pack(side='left', anchor='e')

# canvas_left.pack(side="left", fill=tkinter.Y)
# canvas_left.pack(side="left", fill=tkinter.X, expand=True)   # tkinter.X without expand will not work
# canvas_left.pack(side="top", fill=tkinter.X)   # with side='top' we can see that it works
# canvas_left.pack(side="top", fill=tkinter.Y)   # with side='top' we can see that it doesn't works
# canvas_left.pack(side="top", fill=tkinter.Y, expand=True)   # with expand it works
# canvas_left.pack(side="top", fill=tkinter.BOTH)   # without expand it don't work
canvas_left.pack(side="top", fill=tkinter.BOTH, expand=True)

leftFrame.pack(side="left", anchor='n', fill=tkinter.Y, expand=False)
# --------------------------------------------------------

# Right Frames

rightFrame = tkinter.Frame(mainWindows, relief="raised", borderwidth=2)


label_frame = tkinter.Label(rightFrame, text="right_Frame")
label_frame.pack(side='top')

# canvas_right
canvas_right = tkinter.Canvas(rightFrame, relief="raised", borderwidth=1)

label_canvas_right = tkinter.Label(canvas_right, text="canvas_right")
label_canvas_right.pack(side='top')

# Packs' Examples

#   Buttons
button1_canvas_right = tkinter.Button(canvas_right, text="button1")
button2_canvas_right = tkinter.Button(canvas_right, text="button2")
button3_canvas_right = tkinter.Button(canvas_right, text="button3")
button4_canvas_right = tkinter.Button(canvas_right, text="button4")

button1_canvas_right.pack(side='top', anchor='n')
button2_canvas_right.pack(side='bottom', anchor='s')
button3_canvas_right.pack(side='right', anchor='w')
button4_canvas_right.pack(side='left', anchor='e')

canvas_right.pack(side="top", fill=tkinter.Y)   # expand=False with fill=tkinter.Both it doesn't work
rightFrame.pack(side="right", anchor='n', expand=False)
mainWindows.mainloop()
