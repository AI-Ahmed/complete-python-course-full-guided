__author__ = "crypto"

import math
# Let's draw the parabola with Tk() <Second>
try:
    import tkinter
except ImportError:  # python 2.0
    import Tkinter as tkinter


# Draw X axis & Y axis


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    page.create_line(-x_origin, 0, x_origin, 0, fill="Black")  # x axis
    page.create_line(0, -y_origin, 0, y_origin, fill="Black")  # y axis


# -------------------------------------------
# Drawing Circle


def circle(page, radius, g, h):
    for x in range(g, g + radius):
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)
# -------------------------------------------
# Drawing Enhanced Circle

# Style 01


def circle_Enhanced_1(page, radius, g, h):
    for x in range(g * 100, (g + radius) * 100):    # we used the multiplied by a hundred to give us a bigger range, effectively the same as we had a range that increments 0.01
        x /= 100    # Scaled back X to take it back to the original point
        print(x)    # this will help you to visualize what it meant to be
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)
# -------------------------------------------
# Style 02

# Challenge:
# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to 'blue' if a colour is not given. You may want to review the previous lectures
# about named parameters and default values


def circle_Enhanced_2(page, radius, g, h, colour="blue"):  # best performance and perfectly faster
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)

# The point here is to make a hundred times more calculation to we can sick the edges of the circle, so, it may takes little bit more time <more buffering and worst performance
# -------------------------------------------
# Draw the plot for drawing the shape's lines


def plot(page, x1, y1):
    page.create_line(x1, -y1, x1 + 1, -y1 + 1, fill="red")


# -------------------------------------------

mainWindows = tkinter.Tk()
mainWindows.title("Shapes with Functions")
mainWindows.geometry("760x640+5+0")
mainWindows.minsize(760, 760)
mainWindows.maxsize(760, 760)

frame = tkinter.Frame(mainWindows, width=760, height=760)
frame.grid(row=0, column=0)

# label 01
label01 = tkinter.Label(frame, text="Circle 01")
label01.grid(row=0, column=0)
label01.rowconfigure(0, weight=0)
label01.columnconfigure(0, weight=0)

# Canvas 01
canvas = tkinter.Canvas(frame, width=380, height=380)
canvas.grid(row=1, column=0)
canvas.configure(background="white")
canvas.rowconfigure(1, weight=1)
canvas.columnconfigure(0, weight=1)

# ------------------------------------------

# label 02
label02 = tkinter.Label(frame, text="Circle 02", padx=5)
label02.grid(row=0, column=1)
label02.rowconfigure(0, weight=0)
label02.columnconfigure(1, weight=0)

# Canvas 02
canvas02 = tkinter.Canvas(frame, width=380, height=380)
canvas02.grid(row=1, column=1)
canvas02.configure(background="white")
canvas02.rowconfigure(1, weight=1)
canvas02.columnconfigure(1, weight=1)

# ------------------------------------------

# label 03
label03 = tkinter.Label(frame, text="Circle Enhanced 01", padx=5)
label03.grid(row=2, column=0)
label03.rowconfigure(2, weight=0)
label03.columnconfigure(0, weight=0)

# Canvas 03
canvas03 = tkinter.Canvas(frame, width=380, height=380)
canvas03.grid(row=3, column=0)
canvas03.configure(background="white")
canvas03.rowconfigure(3, weight=1)
canvas03.columnconfigure(0, weight=1)

# ------------------------------------------

# label 04
label04 = tkinter.Label(frame, text="Circle Enhanced 02", padx=5)
label04.grid(row=2, column=1)
label04.rowconfigure(2, weight=0)
label04.columnconfigure(1, weight=0)

# Canvas 04
canvas04 = tkinter.Canvas(frame, width=380, height=380)
canvas04.grid(row=3, column=1)
canvas04.configure(background="white")
canvas04.rowconfigure(3, weight=1)
canvas04.columnconfigure(1, weight=1)

# ------------------------------------------
# Draw axes

draw_axes(canvas)
draw_axes(canvas02)
draw_axes(canvas03)
draw_axes(canvas04)

# --------------------
# Circles

# Notice: g --> x axis      || h --> y axis
# Big Circles
circle(canvas, 50, 50, 50)
circle(canvas, 50, 50, -50)    # -h
circle(canvas, 50, -50, 50)    # -g
circle(canvas, 50, -50, -50)   # -g, -h

# small Circles
circle(canvas02, 10, 30, 30)
circle(canvas02, 10, 30, -30)   #-h
circle(canvas02, 10, -30, 30)   #-g
circle(canvas02, 10, -30, -30)   # -g, -h

circle(canvas02, 30, 0, 0)   # circle on the origin

# --------------------
# Enhanced Circles Style 01

# Big Circles
circle_Enhanced_1(canvas03, 50, 50, 50)
circle_Enhanced_1(canvas03, 50, 50, -50)    # -h
circle_Enhanced_1(canvas03, 50, -50, 50)    # -g
circle_Enhanced_1(canvas03, 50, -50, -50)   # -g, -h

# small Circles
circle_Enhanced_1(canvas03, 10, 30, 30)
circle_Enhanced_1(canvas03, 10, 30, -30)   #-h
circle_Enhanced_1(canvas03, 10, -30, 30)   #-g
circle_Enhanced_1(canvas03, 10, -30, -30)  # -g, -h

circle_Enhanced_1(canvas03, 30, 0, 0)   # circle on the origin

# --------------------
# Enhanced Circles Style 02

# Big Circles
circle_Enhanced_2(canvas04, 50, 50, 50, colour="red")
circle_Enhanced_2(canvas04, 50, 50, -50, colour="yellow")    # -h
circle_Enhanced_2(canvas04, 50, -50, 50, colour="green")    # -g
circle_Enhanced_2(canvas04, 50, -50, -50, colour="black")   # -g, -h

# small Circles
circle_Enhanced_2(canvas04, 10, 30, 30)
circle_Enhanced_2(canvas04, 10, 30, -30)   #-h
circle_Enhanced_2(canvas04, 10, -30, 30)   #-g
circle_Enhanced_2(canvas04, 10, -30, -30)  # -g, -h

circle_Enhanced_2(canvas04, 30, 0, 0)   # circle on the origin


mainWindows.mainloop()
