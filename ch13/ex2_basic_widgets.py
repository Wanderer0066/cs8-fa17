#!/usr/bin/python3

import tkinter

class Application:
    """Often, it's useful to wrap your GUI program inside of a class so that
       all of your GUI setup can happen in one place. Then, an object of this
       class can be created and can be used to manage the user interactions."""

    def __init__(self):
        # This is the main window object where all of our other widgets will go
        self.window = tkinter.Tk()
        self.window.title('Age in Seconds Calculator')

        # Let's add a Label widget
        self.label = tkinter.Label(self.window, text='Enter your age')

        # an Entry widget can be used to get input from the user
        self.entry = tkinter.Entry(self.window, width=2)

        # Finally, a Button widget to take action
        self.button = tkinter.Button(self.window, text='Calculate')

        # Calling the .pack method for each widget adds them to the window
        # in the order that we specify
        self.label.pack()
        self.entry.pack()
        self.button.pack()


    def start(self):
        """This method starts our GUI application."""
        tkinter.mainloop()


def main():
    app = Application()
    app.start()

main()

