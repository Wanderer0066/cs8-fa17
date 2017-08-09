#!/usr/bin/python3

class Sale:

    def __init__(self, customer):
        """Sale constructor. A Sale consists of a Customer, and 1 or more
           Products. We'll also want to keep a total amount for the sale."""
        self.__customer = customer
        self.__products = []
        self.__total = 0

    # Accessor methods.
    def get_customer(self):
        return self.__customer

    def get_products(self):
        return self.__products

    def get_total(self):
        return self.__total

    def add_product(self, product):
        """Add a Product to self.__products and add its price
           to self.__total."""
        self.__products.append(product)
        self.__total += product.get_price()

    def __str__(self):
        """String method."""
        response = [str(self.__customer)]
        for p in self.__products:
            response.append(str(p))
        response.append('Total: ${:,.2f}'.format(self.__total))
        return '\n'.join(response)

