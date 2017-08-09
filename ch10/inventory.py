#!/usr/bin/python3
import pickle

class Inventory:

    def __init__(self):
        """Inventory constructor. For an Inventory object, we don't
           need to accept any parameters. We want our inventory to hold
           a dictionary of Products keyed by their SKU, so we'll create it
           as an attribute in the constructor."""
        self.__products = {}

    # Accessor methods.
    def get_products(self):
        return self.__products

    def add_product(self, product):
        """Takes a Product and adds it to self.__products
           using the Product's sku as the key."""
        self.__products[product.get_sku()] = product

    def has_product(self, sku):
        """Returns True if sku is in self.__products."""
        return sku in self.__products

    def get_product(self, sku):
        """Tries to return the Product identified by sku. Will raise
           a KeyError if the sku is not found in self.__products."""
        return self.__products[sku]

    def remove_product(self, sku):
        """Takes a sku and removes it and the Product it
           refers to if it's present in self.__products."""
        if sku in self.__products:
            del self.__products[sku]

    def read_products_from_file(self, filename):
        """Reads a dictionary containing Product objects from the specified
           filename and uses assigns it to self.__products."""
        f = open(filename, 'rb')
        self.__products = pickle.load(f)
        f.close()

    def write_products_to_file(self, filename):
        """Writes self.__products to the specified filename."""
        f = open(filename, 'wb')
        pickle.dump(self.__products, f)
        f.close()

    def __str__(self):
        """String method. For this, we'll sort self.__product's keys and
           then build a friendlier looking string to return."""
        products = []
        skus = list(self.__products.keys())
        skus.sort()
        for s in skus:
            # self.__products is a dictionary whose values are Product objects.
            # We use the str() built-in function to convert each Product to
            # a str (this implicitly calls the __str__ method of the object, I
            # know it's magic) and append it to the existing string.
            products.append(str(self.__products[s]))

        # Some of you figured out the .join() method of str objects for the last
        # homework. Here, we use it to join our products list into a string
        # seperated by a new line. That puts each Product on its own line.
        return '\n'.join(products)

