__author__ = "crypto"

# notice:
#       The .columncofigure() / .rowconfigure() is configuration
#       for the masters' object so,
#       for item's location you can use sticky='nswe'
#       and for item's size, you initialize the object parameters into the grid()
#       and configure the item by calling the parameter using the main master
#       Example:
#               frame = tkinter.Frame(mainWindows)
#               frame.grid(row=0, column= 1)    # those are parameters of the row and column locations
#               # when i call it, i've to use the master to configure it by
#               mainWindows.columnconfigure(1, weight= 5) # by pixels (resize the col 5 times)
#               mainWindows.rowconfigure(0, weight= 10)   # by pixels (resize the col 10 times)
#
#               canvas = tkinter.Canvas(frame)
#               canvas.grid(/home/crypto/Documents/PythonProgramming/Section08_DatabaseInPython/Section08.29_to_08.39_GUIDatabaseViewer/jukeBox_using_subclasse.pyrow=1, column=0)
#
#               frame.columnconfigure(0, weight=5)
#               frame.rowconfigure(1, weight=2)

# weight is in the simplest terms possible, a non-zero weight causes a row or column to grow if there's extra space.
# The default is a weight of zero, which means the column will not grow if there's extra space.
# -------------------------------------------------------------------------
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import os      # to import OS

mainWindows = tkinter.Tk()

mainWindows.title("Advanced GUI Part 01")
mainWindows.geometry("640x480+3+150")


label = tkinter.Label(mainWindows, text="Tkinter Demo")
label.grid(row=0, column=0, columnspan=5)
label['pady'] = 10

# configure the columns
mainWindows.columnconfigure(0, weight=0)

# configure the rows
mainWindows.rowconfigure(0, weight=0)
# ----------------------------------------------
# Frame
frame = tkinter.Frame(mainWindows)
frame.grid(row=1, column=0, sticky='nsew', columnspan=9)
# sticky instead of expand in Pack
# rowspan/columnspan is for expanding the edges
frame.config(relief='ridge', borderwidth=5)     # extension instead of putting it into the first line
# configure the columns
mainWindows.columnconfigure(0, weight=1)
# configure the rows
mainWindows.rowconfigure(1, weight=3)

# Aliens the widgets
frame['padx'] = 2

# ----------------------------------------------
# Canvas_1
canvas_1 = tkinter.Canvas(frame)
canvas_1.grid(row=1, column=0, sticky='nswe', columnspan=1)
canvas_1.config(relief='raised', borderwidth=2)
# configure the columns
frame.columnconfigure(0, weight=0)
# configure the rows
frame.rowconfigure(1, weight=5)
# canvas_1.config(relief='flat', borderwidth=2)
# ----------------------------------------------
# canvas_1 Label
labelCanvas = tkinter.Label(canvas_1, text="Tools")
labelCanvas.grid(row=0, column=0, columnspan=2)

# ----------------------------------------------
# Listbox
fileList = tkinter.Listbox(canvas_1)
fileList.grid(row=1, column=0, sticky='nswe', padx=5, columnspan=3)    # sticky='nsew' for expanding the entire Listbox
fileList.config(border=2, relief='sunken')
# configure the columns
canvas_1.columnconfigure(0, weight=1)
# configure the rows
canvas_1.rowconfigure(1, weight=10)
# let's write some code to pop-up some items into the list
for zone in os.listdir('/usr/bin'):  # '/Windows/System32'
    fileList.insert(tkinter.END, zone)    #   tkinter.END when you're inserting an item to a list box

# ScrollBar
listScroll = tkinter.Scrollbar(canvas_1, orient=tkinter.VERTICAL, command=fileList.yview)   # orient to merge the Scroll bar with the list
listScroll.grid(row=1, column=1, sticky='nse', padx=5)
# configure the columns
canvas_1.columnconfigure(1, weight=3)
# configure the rows
canvas_1.rowconfigure(1, weight=10)
# let's linking the scroll box with the list box 'yscrollcommand'
fileList['yscrollcommand'] = listScroll.set
# ---------------------------------------------------------------------------------------------------------------------
# Canvas_2
canvas_2 = tkinter.Canvas(frame)
canvas_2.grid(row=1, column=2, sticky='nwes')
canvas_2.config(relief='groove', borderwidth=2)
frame.columnconfigure(2, weight=0)
frame.rowconfigure(1, weight=10)
# # ----------------------------------------------
# Label frame [Radio Buttons]
optionFrame = tkinter.LabelFrame(canvas_2, text="File Details")
optionFrame.grid(row=1, column=2, sticky='nwe', padx=5, pady=5)

# creating values for radio buttons
rbValue = tkinter.IntVar()
rbValue.set(1)  # Default option when you run the program

# Radio Buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
# ----------------------------------------------
# result label
resultLabel = tkinter.Label(canvas_2, text="Result: ")
resultLabel.grid(row=1, column=2, sticky='ws', padx=5)
canvas_2.columnconfigure(2, weight=0)
canvas_2.rowconfigure(1, weight=1)
# widget to display the result
result = tkinter.Entry(canvas_2)
result.grid(row=2, column=2, sticky='ws', padx=5, pady=2)
# ---------------------------------------------------------------------------------------------------------------------
# Canvas_3
canvas_3 = tkinter.Canvas(frame)
canvas_3.grid(row=2, column=0, sticky='sw')
canvas_3.config(relief='solid', borderwidth=2)
frame.columnconfigure(0, weight=0)
frame.rowconfigure(2, weight=1)
# ----------------------------------------------
# canvas_3 Label
labelCanvas_3 = tkinter.Label(canvas_3, text="Time & Date")
labelCanvas_3.grid(row=0, column=0)

canvas_3.columnconfigure(0, weight=1)
canvas_3.rowconfigure(0, weight=1)
# ----------------------------------------------
# Label frame for Time spinners
timeFrame = tkinter.LabelFrame(canvas_3, text="Time")
timeFrame.grid(row=1, column=0, sticky='ns')
canvas_3.columnconfigure(0, weight=1)
canvas_3.rowconfigure(1, weight=1)

# Time Spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

# Hours Grid
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=' ; ').grid(row=0, column=1)
# minutes Grid
minSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=' ; ').grid(row=0, column=3)
# seconds Grid
secSpinner.grid(row=0, column=4)
timeFrame['padx'] = 45  # padx: padding the items from the left and right // pady: padding the object up and down
# ----------------------------------------------
# Frame Label
# Label frame for Date spinners
dateFrame = tkinter.LabelFrame(canvas_3, text="Date")
dateFrame.grid(row=2, column=0, sticky='s', padx=10, pady=10)
canvas_3.columnconfigure(0, weight=1)
canvas_3.rowconfigure(2, weight=1)

# Date Labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
# Grid
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Date Spinner
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
# Grid
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

dateFrame['pady'] = 5
dateFrame['padx'] = 25
# ---------------------------------------------------------------------------------------------------------------------
# Buttons
okButton = tkinter.Button(frame, text="Ok!")
cancelButton = tkinter.Button(frame, text="Cancel", command=mainWindows.quit)   # we can use 'mainWindows.destroy' instead of 'mainWindows.quit' not to make the program idle <Remember Apex programme ;) >
# notice the quit or destroy not with the () because we're not calling the function because we don't return something
# to it but we execute it!
okButton.grid(row=4, column=5, sticky='es')
cancelButton.grid(row=4, column=6, sticky='es')

frame.columnconfigure(5, weight=1)
frame.columnconfigure(6, weight=0)

frame.rowconfigure(4, weight=1)

mainWindows.mainloop()

# let's print the result of the Radio buttons
print(rbValue.get())    # retrieving the selected data

# Notice:
#   Why we did use LabelFrame?
#       It's very similar to the normal frame but this one allows
#       a caption to be sent using the text option and you can see that
#       on line 93 which  the text in the border.
