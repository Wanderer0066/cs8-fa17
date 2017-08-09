#!/usr/bin/python3

class Customer:

    def __init__(self, name, email):
        """Customer constructor."""
        self.__name = name
        self.__email = email

    # Accessor methods.
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    # Mutator methods.
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        """String method."""
        return 'Customer {} ({})'.format(self.__name, self.__email)

