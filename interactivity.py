"""
# import the 'tkinter' module
import tkinter
# create a new window
window = tkinter.Tk()
# set the window title
window.title("Commands")
# set the window icon
window.wm_iconbitmap('Icon.ico')


# a function that changes the text of the label
def callback():
    lbl.configure(text="Button clicked!")

# create a label to display a message
lbl = tkinter.Label(window, text="Nothing happened yet")
lbl.pack()

# create a new button, and provide an argument called 'command'
# which in this case calls a function called 'callback'
btn = tkinter.Button(window, text="Click Me", command=callback)
btn.pack()

# draw the window, and start the 'application'
window.mainloop()
"""
"""
# import the 'tkinter' module
import tkinter
# create a new window
window = tkinter.Tk()
# set the window title
window.title("Commands")
# set the window icon
window.wm_iconbitmap('Icon.ico')

# initially, the button hasn't been pressed
presses = 0


# a function that changes the text of the label
def add_click():
    # this means that this function should
    # use the presses variable declared outside
    # of the function
    global presses
    # add one to presses
    presses += 1
    # update the label text with the new value of 'presses'
    lbl.configure(text=presses)

# create a label to display a message
lbl = tkinter.Label(window, text=presses)
lbl.pack()

# create a new button, and provide an argument called 'command'
# which in this case calls a function called 'callback'
btn = tkinter.Button(window, text="Click Me", command=add_click)
btn.pack()

# draw the window, and start the 'application'
window.mainloop()
"""
import tkinter


def set_red():
    window.configure(background="red")


def set_blue():
    window.configure(background="blue")


if __name__ == "__main__":
    window = tkinter.Tk()

    window.geometry("200x60")
    window.title("Red or Blue?")

    red_btn = tkinter.Button(window, text="Red", command=set_red)
    blue_btn = tkinter.Button(window, text="Blue",command=set_blue)

    red_btn.pack()
    blue_btn.pack()

    window.mainloop()