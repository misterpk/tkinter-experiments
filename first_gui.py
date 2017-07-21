'''
import tkinter

window = tkinter.Tk()

window.title("login")
# window.wm_iconbitmap('moogle.bmp')

username = tkinter.Label(window, text="Username:", bg="#a1dbcd")
username_ent = tkinter.Entry(window)
password = tkinter.Label(window, text="Password:", bg="#a1dbcd")
password_ent = tkinter.Entry(window)
login = tkinter.Button(window, text="Login", fg="#a1dbcd", bg="#383a39")
window.configure(background="#a1dbcd")

photo = tkinter.PhotoImage(file="moogle icon.gif")
w = tkinter.Label(window, image=photo)

w.pack()
username.pack()
username_ent.pack()
password.pack()
password_ent.pack()
login.pack()

window.mainloop()
'''
'''
# import the 'tkinter' module
import tkinter
# create a new window
window = tkinter.Tk()
# set the window background to hex code '#a1dbcd'
window.configure(background="#a1dbcd")
# set the window title
window.title("Welcome")
# set the window icon
# window.wm_iconbitmap('Icon.ico')

photo = tkinter.PhotoImage(file="Moogle icon.gif")
w = tkinter.Label(window, image=photo)
w.pack()

# create a label for the instructions
lblInst = tkinter.Label(window, text="Please login to continue:", fg="#383a39",
                        bg="#a1dbcd", font=("Helvetica", 16))
# and pack it into the window
lblInst.pack()

# create the widgets for entering a username
lblUsername = tkinter.Label(window, text="Username:", fg="#383a39",
                            bg="#a1dbcd")
entUsername = tkinter.Entry(window)
# and pack them into the window
lblUsername.pack()
entUsername.pack()

# create the widgets for entering a username
lblPassword = tkinter.Label(window, text="Password:", fg="#383a39",
                            bg="#a1dbcd")
entPassword = tkinter.Entry(window)
# and pack them into to the window
lblPassword.pack()
entPassword.pack()

# create a button widget called btn
btn = tkinter.Button(window, text="Login", fg="#a1dbcd", bg="#383a39")
# pack the widget into the window
btn.pack()

# draw the window, and start the 'application'
window.mainloop()
'''
'''
import tkinter
#create a list of buttons
#you could also just write 'buttons = ['0','1','2',...]
window = tkinter.Tk()
window.title("Numbers")

buttons = [i for i in range(10)] + ['+','-','/','x','=']
print(buttons)

for b in buttons:
    btn = tkinter.Button(window, text=b)
    btn.pack(side=tkinter.LEFT)

window.mainloop()
'''
'''
# import the 'tkinter' module
import tkinter
# create a new window
window = tkinter.Tk()
# set the window title
window.title("Colours")
# set the window icon
# window.wm_iconbitmap('Icon.ico')

# create a list variable containing colours
colours = ['red', 'yellow', 'pink', 'green', 'purple', 'orange', 'blue']

# loop through each colour
for c in colours:
    # create a new button, using the text/bg of the list item
    b = tkinter.Button(text=c, bg=c)
    # pack the button, filling up the X axis
    b.pack(fill=tkinter.X)

# draw the window, and start the 'application'
window.mainloop()
'''