#!/usr/bin/python3

# You must import the tkinter module. Note that this may fail on certain systems
# and you may be required to install the tkinter library.
# (ex. On Ubuntu, you have to do: sudo apt-get install python3-tk
import tkinter

def main():
    # We need to build a Tk object. That's the base object provided by Tkinter
    # to create a GUI program.
    window = tkinter.Tk()

    # GUI programs need to listen for events. Calling the window.mainloop()
    # method starts this process.
    tkinter.mainloop()

main()
