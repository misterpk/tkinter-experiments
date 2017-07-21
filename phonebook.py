"""
Create a window that displays contact information based on name

commented out shows pickle
"""
import tkinter
# import pickle
import os
import json


def create_phonebook():
    with open("phonebook.json", "w") as book:
        # global phone_book
        phonebook = {"Marvin": {"Mobile": 8057292500,
                                "Email": "marvin.martian@gmail.com"},
                     "Fareeda": {"Mobile": 8057295112,
                                 "Email": "fareeda@gmail.com"},
                     "Oliver": {"Mobile": 8056906434,
                                "Email": "angryhippo@yahoo.com"}}
        # pickle.dump(phonebook, open("./phonebook.txt", "wb"))
        json.dump(phonebook, book)


def display_info(name):
    message = "Details for {}:\nMobile: {}\n" \
              "Email: {}".format(name,
                                 phone[name]["Mobile"],
                                 phone[name]["Email"])

    details.configure(text=message)

if __name__ == "__main__":
    if not os.path.isfile("phonebook.json"):
        create_phonebook()

    with open("phonebook.json", "r") as phone_book:
        # phone = pickle.load(open("phonebook.txt", "rb"))
        phone = json.load(phone_book)
        window = tkinter.Tk()
        window.title("Phone Book")
        title = tkinter.Label(window, text="Click a contact to display details")
        title.pack()

        for k in phone:
            btn = tkinter.Button(text=k,
                                 command=lambda name=k: display_info(name))
            btn.pack()

        details = tkinter.Label(window)
        details.pack()

        window.mainloop()

'''
Example from website

import random
# import the 'tkinter' module
import tkinter
# create a new window
window = tkinter.Tk()
# set the window title
window.title("")
# set the window icon
window.wm_iconbitmap('Icon.ico')

# decide randomly on which door contains the prize
doorToGuess = random.randint(0, 2)


# a function that changes the text of the label
# based on the number of the button clicked
def checkDoor(number):
    # use the variable defined outside of the function
    global doorToGuess
    # if the button number is equal to the door containing the prize
    if number == doorToGuess:
        # display 'Yes'
        lbl.configure(text="Yes")
    else:
        lbl.configure(text="No")

# create a label to display a message
lbl = tkinter.Label(window, text="Which door contains the prize?")
lbl.pack()

# make 3 buttons
for i in range(3):
    # each button should say 'door 0/1/2'
    # and call the checkDoor callback function if clicked
    btn = tkinter.Button(text="Door " + str(i),
                         command=lambda door_no=i: checkDoor(door_no))
    btn.pack(side=tkinter.LEFT)

# draw the window, and start the 'application'
window.mainloop()
'''