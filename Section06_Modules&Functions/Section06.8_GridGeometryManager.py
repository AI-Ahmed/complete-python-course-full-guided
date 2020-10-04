__author__ = "crypto"

# now, lets start with "Place"
# So, the structure will be changed to be suitable for the new method which grid

# structure of Grid GM
#   Main Window     <-- Root Geometry Manager
#       Frame   <-- Frame Manager
#           Grid   <-- Place Manger
#              canvas_left    <-- canvas_left widget Displaying graphics

import tkinter

mainWindows = tkinter.Tk()

mainWindows.title("Geometry Grid Geometry")
mainWindows.geometry("640x480+8+200")

# Main Windows

label_windows = tkinter.Label(mainWindows, text="Main Windows")
label_windows.grid(row=0, column=0)  # Now, we'll change the Pack with Grid

# Left Frames

leftFrame = tkinter.Frame(mainWindows, relief="raised", borderwidth=2)
leftFrame.grid(row=1, column=0)

label_frame = tkinter.Label(leftFrame, text="Left_Frame")
label_frame.grid(row=0, column=0)  # Now, we'll change the Pack with Grid

# canvas_left

canvas_left = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas_left.grid(row=2, column=0)  # Now, we'll change the Pack with Grid

label_canvas_left = tkinter.Label(canvas_left, text="canvas_left")
label_canvas_left.grid(row=3, column=2, sticky='n')  # Now, we'll change the Pack with Grid

#   Buttons
button1_canvas_left = tkinter.Button(canvas_left, text="button1")
button2_canvas_left = tkinter.Button(canvas_left, text="button2")
button3_canvas_left = tkinter.Button(canvas_left, text="button3")
button4_canvas_left = tkinter.Button(canvas_left, text="button4")

button1_canvas_left.grid(row=4, column=2, sticky='n')
button2_canvas_left.grid(row=5, column=4, sticky='w')
button3_canvas_left.grid(row=5, column=0, sticky='e')
button4_canvas_left.grid(row=8, column=2, sticky='s ')

# --------------------------

# configure the columns

# Notice: columnconfigure() && grid_columnconfigure() are the same
mainWindows.columnconfigure(0, weight=0)
mainWindows.columnconfigure(1, weight=0)
mainWindows.grid_columnconfigure(0, weight=0)
# mainWindows.columnconfigure(2, weight=0)
mainWindows.grid_columnconfigure(3, weight=2)
mainWindows.columnconfigure(4, weight=2)
mainWindows.grid_columnconfigure(5, weight=4)
mainWindows.columnconfigure(5, weight=0)
mainWindows.columnconfigure(8, weight=2)

# for specific object
canvas_left.columnconfigure(4, weight=0)
# --------------------------

# to create borders allocate the objects something like<stick>

leftFrame.config(relief='sunken', borderwidth=5)
canvas_left.config(relief='sunken', borderwidth=2)
button1_canvas_left.config(relief='sunken', borderwidth=2)
button2_canvas_left.config(relief='sunken', borderwidth=3)
button3_canvas_left.config(relief='sunken', borderwidth=1)
button4_canvas_left.config(relief='sunken', borderwidth=4)
leftFrame.grid(sticky='n')
canvas_left.grid(sticky='ns')
button1_canvas_left.grid(sticky='new')
button2_canvas_left.grid(sticky='ne')
button3_canvas_left.grid(sticky='nw')
button2_canvas_left.grid(sticky='sw')

# --------------------------

# change background

mainWindows.config(background="white")
leftFrame.config(background="white")
canvas_left.config(background="white")

# --------------------------------------

# Right Frames

# rightFrame = tkinter.Frame(mainWindows, relief="raised", borderwidth=2)
#
#
# label_frame = tkinter.Label(rightFrame, text="right_Frame")
# label_frame.pack(side='top')
#
# # canvas_right
# canvas_right = tkinter.Canvas(rightFrame, relief="raised", borderwidth=1)
#
# label_canvas_right = tkinter.Label(canvas_right, text="canvas_right")
# label_canvas_right.pack(side='top')
#
#
# #   Buttons
# button1_canvas_right = tkinter.Button(canvas_right, text="button1")
# button2_canvas_right = tkinter.Button(canvas_right, text="button2")
# button3_canvas_right = tkinter.Button(canvas_right, text="button3")
# button4_canvas_right = tkinter.Button(canvas_right, text="button4")
#
# button1_canvas_right.pack(side='top', anchor='n')
# button2_canvas_right.pack(side='bottom', anchor='s')
# button3_canvas_right.pack(side='right', anchor='w')
# button4_canvas_right.pack(side='left', anchor='e')
#
# canvas_right.pack(side="top", fill=tkinter.Y)   # expand=False with fill=tkinter.Both it doesn't work
# rightFrame.pack(side="right", anchor='n', expand=False)
mainWindows.mainloop()
