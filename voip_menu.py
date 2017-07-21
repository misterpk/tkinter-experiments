import tkinter

if __name__ == "__main__":
    # create window
    window = tkinter.Tk()

    # create window title
    window.title("VoIP Program")

    menu_title = tkinter.Label(window, text="Click a button to call someone:",
                               font=("Helvetica", 16))
    menu_title.pack()

    people_list = ["Dave", "Francesca", "Hasnain", "Courtney"]

    for i in people_list:
        name_text = tkinter.Label(text="Click to call {}".format(i))
        name_text.pack(fill=tkinter.X)
        name_button = tkinter.Button(text="Call {}".format(i))
        name_button.pack(fill=tkinter.X)

    window.mainloop()
