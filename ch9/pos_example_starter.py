#!/usr/bin/python3
import pickle

# Multi-line string variable for the main program menu.
MAIN_MENU = (
'''======================================================================
\tEnter I for Inventory Management
\tEnter S to Transact a Sale
\tEnter R to Run Sales Report
\tEnter anything else to exit.
======================================================================
Please type an option from the list above:
>>> ''')

# Module variables to hold filenames
INVENTORY_FILENAME = 'inventory.dat'
SALES_FILENAME = 'sales.dat'


def main():
    """Main execution routine."""
    # Stay in the loop until an invalid action is received.
    while True:
        action = input(MAIN_MENU)
        if action == 'I':
            inventory_management()
        elif action == 'S':
            transaction()
        elif action == 'R':
            sales_report()
        else:
            print('"{}" is not a valid action. Goodbye!'.format(action))
            break


def sales_report():
    """Build a report with the sales data"""
    # Try to read inventory from file.
    # If FileNotFoundError, EOFError or PickleError occurs, return immediately
    try:
        f = open(SALES_FILENAME, 'rb')
    except (FileNotFoundError, pickle.PickleError):
        print('Cannot read from sales file! Are you sure you have sales?')
        return

    # Inside of a try/except that catches the EOFError, read a dict object from
    # the f file object using pickle. The dict should have 'sku', 'quantity',
    # and 'total' as valid keys and represents a sale logged by the system.
    # For each sale, write the contents out using the following format string:
    sale_report_line = 'SKU: {}, Quantity: {:,}, Total ${:,.2f}'    


def transaction():
    """Transact a sale from user supplied data."""
    # Try to read inventory from file.
    # If FileNotFoundError, EOFError or PickleError occurs, return immediately
    try:
        f = open(INVENTORY_FILENAME, 'rb')
        inventory = pickle.load(f)
        f.close()  # Close the file after reading
    except (FileNotFoundError, EOFError, pickle.PickleError):
        print(
            'Cannot read from inventory file! Are you sure you have inventory?')
        return

    print('SKUs in Inventory:', list(inventory.keys()))
    
    # Prompt the user for a SKU. If the sku is found in the inventory dict as
    # a key, ask the user how many units they want to buy. If the inventory
    # information for the given SKU has sufficient quantity (>= the desired
    # quantity, create a sale dict object with the following keys:
    # {'sku': <sku entered by the user>, 
    #  'quantity': <quantity entered by the user>,
    #  'total': <quantity entered by the user> * inventory entry's price
    # }.
    # Then, append that dict object to the sales file using the following
    # code snippet:
    # f = open(SALES_FILENAME, 'ab')
    # pickle.dump(sale, f)
    # f.close()
    # If a SKU cannot be found, or if insufficient quantity exists, or
    # if the user tries to enter a non-numeric quantity, let the
    # user know with an informative message but don't write any sales data
    # to the file.    


def inventory_management():
    """Load a dict object from inventory.dat, manipulate it, and save it."""
    # Try to read inventory from file.
    # If FileNotFoundError, EOFError or PickleError occurs, create an empty dict
    try:
        f = open(INVENTORY_FILENAME, 'rb')
        inventory = pickle.load(f)
        f.close()  # Close the file after reading
    except (FileNotFoundError, EOFError, pickle.PickleError):
        inventory = {}

    keys = list(inventory.keys())
    keys.sort()
    # Loop through the keys list. Print out a line for each inventory entry
    # using the following format string:
    inventory_report_line = 'SKU {}: Name: {}, Quantity: {:,}, Price: ${:,.2f}'
    
    # Prompt the user for a SKU. If the SKU is not found as a key in inventory
    # create a new dict object to represent the product. It should contain
    # the following keys:
    # {'name': <name of product entered by the user>, 
    #  'quantity': <int quantity on hand entered by the user>,
    #  'price': <float price entered by the user>
    # }
    # If the SKU is already found in the inventory dict, print its name, 
    # then prompt the user to update the quantity and price. Assign the
    # 'quantity' and 'price' values of the dict object at inventory[sku] based
    # on the values given by the user.    
    # If any of the user's inputs throw a ValueError, print a useful message.
    # The last three lines of the function will persist the inventory dict
    # to the inventory.dat file.
    

    # Persist the inventory data in a serialized file
    f = open(INVENTORY_FILENAME, 'wb')
    pickle.dump(inventory, f)
    f.close()

# Call main()
main()
