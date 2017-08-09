#!/usr/bin/python3
import tkinter

import ex3_age_calculator

class Application:
    def __init__(self, age_calculator):
        # This is the main window object where all of our other widgets will go
        # We expect age_calculator to be an AgeCalculator object that gets
        # passed in.
        self.__age_calculator = age_calculator
        self.__window = tkinter.Tk()
        self.__window.title('Age Calculator')

        # Let's add a Label widget
        self.__label = tkinter.Label(self.__window, text='Enter your age')

        # an Entry widget can be used to get input from the user
        self.__entry = tkinter.Entry(self.__window, width=2)

        # a Button widget to take action. The command argument specifies
        # the method that will be invoked with this Button is clicked.
        self.__button = tkinter.Button(self.__window, text='Calculate',
            command=self.calculate)

        # A Message for output. 250 pixels in width. We'll use a special
        # StringVar object that will be used to display a value that
        # we will calculate.
        self.__calculation = tkinter.StringVar()
        self.__message = tkinter.Message(self.__window, width=250,
            textvariable=self.__calculation)

        # Calling the .pack method for each widget adds them to the window
        # in the order that we specify
        self.__label.pack()
        self.__entry.pack()
        self.__button.pack()
        self.__message.pack()


    def start(self):
        """This method starts our GUI application."""
        tkinter.mainloop()

    def calculate(self):
        """Our Application object's calculate method will be invoked when
           the user presses our Button. We'll then use the __age_calculator
           object to do the calculation and set our output field's text."""
        # Get the input from the user and convert it to an int
        age = int(self.__entry.get())
        self.__age_calculator.calculate(age)
        # Build a string and then use it to set self.__calculation
        calculation = '{:,.0f} days\n'.format(
            self.__age_calculator.get_age_in_days())
        calculation += '{:,.0f} hours\n'.format(
            self.__age_calculator.get_age_in_hours())
        calculation += '{:,.0f} seconds\n'.format(
            self.__age_calculator.get_age_in_seconds())
        self.__calculation.set(calculation)


def main():
    # We will create a new Application object and pass it a new AgeCalculator
    # in the constructor.
    app = Application(ex3_age_calculator.AgeCalculator())
    app.start()

main()

