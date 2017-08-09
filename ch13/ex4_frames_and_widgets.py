#!/usr/bin/python3
import tkinter

class Application:
    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title('Tip Calculator')

        # We'll build three frames to help organize our widgets
        self.__top_frame = tkinter.Frame(self.__window)
        self.__middle_frame = tkinter.Frame(self.__window)
        self.__bottom_frame = tkinter.Frame(self.__window)

        # Our Label widget will be added to the Top Frame
        self.__label = tkinter.Label(self.__top_frame, text='Enter Bill Amount')

        # A DoubleVar object is used to automatically capture the value from
        # an Entry Widget
        self.__amount = tkinter.DoubleVar()

        # an Entry widget can be used to get input from the user
        self.__entry = tkinter.Entry(self.__top_frame,
            textvariable=self.__amount)

        # Pack the top frame widgets
        self.__label.pack(side='left')
        self.__entry.pack(side='right')


        # Now add the Radiobutton objects. When a group of Radiobuttons are
        # added to a parent frame, only one can be selected at a time. We
        # Will create a DoubleVar object and set it to 0.15 as our default
        # tip amount.
        self.__tip = tkinter.DoubleVar()
        self.__tip.set(0.15)
        self.__rb1 = tkinter.Radiobutton(self.__middle_frame,
            text='15%', value=0.15, variable=self.__tip)
        self.__rb2 = tkinter.Radiobutton(self.__middle_frame,
            text='20%', value=0.20, variable=self.__tip)
        self.__rb3 = tkinter.Radiobutton(self.__middle_frame,
            text='25%', value=0.25, variable=self.__tip)

        # Pack the Radiobuttons side by side in a row
        self.__rb1.pack(side='left')
        self.__rb2.pack(side='left')
        self.__rb3.pack(side='left')

        # A Checkbutton can be toggled on or off independently of any other
        # widgets. We need an IntVar which will hold the result of the
        # Checkbutton (1 if checked, 0 if not).
        self.__split = tkinter.IntVar()
        self.__cb = tkinter.Checkbutton(self.__bottom_frame,
            text='Split 2 Ways?', variable=self.__split)
        self.__cb.pack()

        # Finally, add our Button and Message
        self.__button = tkinter.Button(self.__bottom_frame, text='Calculate',
            command=self.calculate)
        self.__button.pack()

        self.__calculation = tkinter.StringVar()
        self.__message = tkinter.Message(self.__bottom_frame, width=250,
            textvariable=self.__calculation)
        self.__message.pack()

        self.__top_frame.pack()
        self.__middle_frame.pack()
        self.__bottom_frame.pack()

    def start(self):
        """This method starts our GUI application."""
        tkinter.mainloop()

    def calculate(self):
        """It's usually better to have another module do the calculations,
           but we'll cheat here."""
        bill = self.__amount.get()
        tip = self.__amount.get() * self.__tip.get()
        calculation = 'Tip ${:,.2f}'.format(tip)
        # By default, if a Checkbutton is selected,
        # it will return 1, a 'truthy' value
        if self.__split.get():
            tip /= 2
            calculation += ' (split 2 ways is ${:,.2f})'.format(tip)
        self.__calculation.set(calculation)


def main():
    # We will create a new Application object and pass it a new AgeCalculator
    # in the constructor.
    app = Application()
    app.start()

main()

