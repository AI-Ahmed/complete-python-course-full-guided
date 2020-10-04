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
# Simplest equation of Drawing the Parabola <First>

# Style 01
def parabola(page, size):
    for x1 in range(-size, size):
        y1 = x1 * x1 / size
        plot(page, x1, y1)


# Style 02
def parabola_efficient(page, size):
    for x1 in range(size):
        y1 = x1 * x1 / size
        plot(page, x1, y1)
        plot(page, -x1, y1)
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
label01 = tkinter.Label(frame, text="parabola 01")
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
label02 = tkinter.Label(frame, text="parabola 02", padx=5)
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
label03 = tkinter.Label(frame, text="Circle 01", padx=5)
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
label04 = tkinter.Label(frame, text="Circle 02", padx=5)
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
# Parabolas

# style 01
parabola(canvas, 100)
parabola(canvas, 200)
# style 02
parabola_efficient(canvas02, 100)
parabola_efficient(canvas02, 200)

# --------------------
# Circles
# Notice: g --> x axis      || h --> y axis
# Big Circles
circle(canvas03, 50, 50, 50)
circle(canvas03, 50, 50, -50)    # -h
circle(canvas03, 50, -50, 50)    # -g
circle(canvas03, 50, -50, -50)   # -g, -h

# small Circles
circle(canvas04, 10, 30, 30)
circle(canvas04, 10, 30, -30)   #-h
circle(canvas04, 10, -30, 30)   #-g
circle(canvas04, 10, -30, -30)   # -g, -h

circle(canvas04, 30, 0, 0)   # circle on the origin


mainWindows.mainloop()
