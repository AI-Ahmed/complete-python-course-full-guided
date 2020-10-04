__author__ = "crypto"

# Let's draw the parabola with Tk() <Second>
try:
    import tkinter
except ImportError:  # python 2.0
    import Tkinter as tkinter


# Simplest equation of parabola <First>


def parabola(x):
    # y = x * x
    y = x * x / 100  # if we divided by 100 we make sure the the object will fit in the area and prevent the y values from running off the screen
    return y


# -------------------------------------------
# Now, if we want to draw the parabola, we need first to initialize the x-axis and y-axis


def draw_axes(page):  # we need to rename the parameters so, not to have this tinny error
    page.update()
    x_origin = page.winfo_width() / 2  # those values divided by 2 to get the values for the x & y origin
    y_origin = page.winfo_height() / 2

    page.configure(scrollregion=(-x_origin, -y_origin, x_origin,
                                 y_origin))  # scrollregion is a box with one corner at minus x origin minus y origin and the other X origin Y origin

    page.create_line(-x_origin, 0, x_origin, 0, fill="Black")  # x axis
    page.create_line(0, -y_origin, 0, y_origin, fill="Black")  # y axis
    # canvas.create_line(0, -y_origin, 0, y_origin, fill="Black")  # y axis # this will work but makes a complex confusion
    # hyxx.create_line(0, -y_origin, 0, y_origin, fill="Black")  # y axis     # this wouldn't work and cause an serious error
    print(locals())  # objects of the function's locations


# -------------------------------------------
# we need to create the parabola()'s line draw, so we can do that by creating a function for the canvas


def plot(page, x, y):
    page.create_line(x, y, x + 1, y + 1, fill="red")


# -------------------------------------------

mainWindows = tkinter.Tk()
mainWindows.title("Parabola")
mainWindows.geometry("640x480+3+150")
mainWindows.minsize(640, 480)
mainWindows.maxsize(640, 480)

frame = tkinter.Frame(mainWindows, width=640, height=480)
frame.grid(row=0, column=0)

# Canvas 01
canvas = tkinter.Canvas(frame, width=320, height=480)
canvas.grid(row=0, column=0)
canvas.configure(background="white")

# Canvas 02
canvas02 = tkinter.Canvas(frame, width=320, height=480, background="gray")
canvas02.grid(row=0, column=1)

print(repr(canvas), repr(canvas02))  # two objects allocation which being assigned from the funtion so, its number will be different
draw_axes(canvas)
draw_axes(canvas02)

for x in range(-100, 100):
    y = parabola(x)
    # print(y)
    # plot(canvas, x, y)  # this function's y we have to flip it over
    plot(canvas, x, -y)  # so, the parabola will be up into the +pos axes
mainWindows.mainloop()

# -------------------------------------------------
# Notice:

# The point of this section is to highlight the scope of the similarity between
# the variables in the function and in the main code, which is something not recommended !
# hence, the similarity between the variables cause a problem into the object's allocation
# thus, you may in the future face a problem that two variables  allocated into the memory with the same hash
# which something is totally wrong and cause a huge error if the bulk of the code totally connected and complicated
#
# The point is: Function can use the variables from the main program BUT the main program cannot see the variables that are local to the function
