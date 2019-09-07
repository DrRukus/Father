#!/usr/bin/env python

from tkinter import *

class Window(Frame):

    def __init__(self, master=None):

        # parameters that you want to send through the Frame class
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exists
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of out master widget
        self.master.title('GUI')

        # allowing the widget to take the full space of the Window
        self.pack(fill=BOTH, expand=1)

        # Creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create the file object
        file = Menu(menu)

        # Adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label='Exit', command=self.client_exit)

        # Added "file" to our menu
        menu.add_cascade(label='File', menu=file)

        # create the edit object
        edit = Menu(menu)

        # Adds a command to the menu option, calling it Undo, and the
        # command it runs is not yet defined
        edit.add_command(label='Undo')
        edit.add_command(label='Redo')

        # Added 'Edit' to our menu
        menu.add_cascade(label='Edit', menu=edit)

        # # creating a button instance
        # quit_button = Button(self, text='Quit', command=self.client_exit)
        #
        # # placing the button on my window
        # quit_button.place(x=0, y=0)

    def client_exit(self):
        exit()

# Root window created.  Here, that would be the only window, but
# you can later have windows within windows
root = Tk()

# size of the window
root.geometry('400x300')

# Creation of an instance
app = Window(root)

# main loop
root.mainloop()
