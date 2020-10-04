__author__ = "crypto"

# Let's draw the parabola with Tk() <Second>
try:
    import tkinter
except ImportError:  # python 2.0
    import Tkinter as tkinter


# Simplest equation of parabola <First>


def parabola(x):
    # y = x * x
    y = x * x / 100     #  if we divided by 100 we make sure the the object will fit in the area and prevent the y values from running off the screen
    return y


# -------------------------------------------
# Now, if we want to draw the parabola, we need first to initialize the x-axis and y-axis


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2  # those values divided by 2 to get the values for the x & y origin
    y_origin = canvas.winfo_height() / 2

    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin,
                                   y_origin))  # scrollregion is a box with one corner at minus x origin minus y origin and the other X origin Y origin

    canvas.create_line(-x_origin, 0, x_origin, 0, fill="Black")  # x axis
    canvas.create_line(0, -y_origin, 0, y_origin, fill="Black")  # y axis


# -------------------------------------------
# we need to create the parabola()'s line draw, so we can do that by creating a function for the canvas


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


# -------------------------------------------

mainWindows = tkinter.Tk()
mainWindows.title("Parabola")
mainWindows.geometry("640x480+3+150")
mainWindows.minsize(640, 480)
mainWindows.maxsize(640, 480)

frame = tkinter.Frame(mainWindows, width=640, height=480)
frame.grid(row=0, column=0)

canvas = tkinter.Canvas(frame, width=640, height=480)
canvas.grid(row=0, column=0)
canvas.configure(background="white")

draw_axes(canvas)

for x in range(-100, 100):
    y = parabola(x)
    # print(y)
    # plot(canvas, x, y)  # this function's y we have to flip it over
    plot(canvas, x, -y)  # so, the parabola will be up into the +pos axes
mainWindows.mainloop()
