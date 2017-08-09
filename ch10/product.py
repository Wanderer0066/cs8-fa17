#!/usr/bin/python3

class Product:

    def __init__(self, sku, name, quantity, price):
        """A Product will have four primary data attributes, so we make
           the user provide them when instantiating a Product object."""
        # Note, by using the __ prefix for each of our attributes, we have
        # made them only visible within the class definition of a Product.
        # That means that no code outside of the Product class' definition
        # can access them or modify them directly. Thus, we need to write
        # accessor/mutator methods
        self.__sku = sku
        self.__name = name
        self.__quantity = int(quantity)
        self.__price = float(price)

    # Accessor methods are usually straight-forward. They accept no params
    # and return the value of the object's attribute. They are usually prefixed
    # with get_
    def get_sku(self):
        return self.__sku

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    # Mutator methods are used to change the state of an object's attributes.
    # They will typically have a single parameter and are prefixed with set_.
    def set_sku(self, sku):
        self.__sku = sku

    def set_name(self, name):
        self.__name = name

    def set_quantity(self, quantity):
        self.__quantity = int(quantity)

    def set_price(self, price):
        self.__price = float(price)

    def __str__(self):
        """It's always good form to define a __str__ method. This makes it easy
           to print out an object when building your program and debugging it
           along the way."""
        return 'Product ID {}: {} ${:,.2f}, {:,} on hand'.format(
            self.__sku, self.__name, self.__price, self.__quantity)

