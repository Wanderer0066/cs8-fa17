#!/usr/bin/python3

import random

# To define a class, we use the special keyword class followed by the name
# of the class we want to define. We're going to build a class to represent
# a FortuneTeller.
class FortuneTeller:

    # Class definitions are block statements so we need to indent. We then
    # define functions inside of the class that become its methods.

    # __init__ is a special method known as a constructor. It is used to
    # initialize the state of the object defined by the class when it is
    # being created. All of the methods we define for use with an object will
    # have at least one parameter named self. self refers to the object that
    # all of these methods will be bound to.
    def __init__(self):
        # We can create attributes for our FortuneTeller object
        # by assigning values to self. These are just like normal Python
        # variables, but they are bound to a particular object.
        # Using the special prefix of two underscores makes an object attribute
        # private, or hidden from parts of your program outside of the class.
        self.__answers = [
            'Yes, most certainly',
            'The odds are in your favor',
            'Probably not',
            'No, not a chance',
            'Ask again later'
        ]
        self.__current_answer = ''


    # The determine_fortune method uses a random guess to set the current_answer
    # data attribute to one of the 5 possible answers.
    def determine_fortune(self):
        self.__current_answer = self.__answers[random.randint(0,
            len(self.__answers) - 1)]

    # The tell_fortune method returns the value in self.current_answer
    def tell_fortune(self):
        return self.__current_answer


# Here's our program's main function. Inside of it, we'll build some
# FortuneTeller objects
def main():
    # To create (instantiate) an object, use the name of its class followed
    # by parentheses.
    ft = FortuneTeller()
    # Now, we can use its methods
    question = input('What do you want to know, ask away? ')
    while question != 'Nothing':
        # To call a method, you use the name of the object+dot+name of the
        # method. Notice we didn't supply an argument for the self parameter.
        # That's because our FortunteTeller object becomes self.
        ft.determine_fortune()
        print(ft.tell_fortune())
        question = input('Now what do you want to know, ask away? ')


main()