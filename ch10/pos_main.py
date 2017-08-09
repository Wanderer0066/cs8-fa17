#!/usr/bin/python3
"""
This is the main module for our POS program. Most of the heavy lifting
is done in our class definitions so this file is mostly just user-interface.
We'll import the names of the modules where each of our classes is by saying
import <name of file containing class> without the .py extension.
"""
import customer
import inventory
import product
import sale
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


def inventory_management():
    """Manage Inventory."""
    # Create the Inventory object. Notice we have to qualify the name of the
    # class with the name of its module first then a period.
    inv = inventory.Inventory()
    try:
        inv.read_products_from_file(INVENTORY_FILENAME)
    except (FileNotFoundError, EOFError, pickle.PickleError):
        print('Unable to open', INVENTORY_FILENAME, 'will save new')

    # Print the current Inventory status. All we need to do is use the print
    # function and Python will automagically call the __str__ method.
    print(inv)

    # Prompt the user for a SKU. If the SKU is not found in our Inventory
    # we will create a new Product object and add it. If it is found, we'll
    # prompt the user to update its quantity and price.
    sku = input('Enter a SKU >>> ')
    if inv.has_product(sku):
        p = inv.get_product(sku)
        print(p)
        try:
            quantity = int(input('Update quantity on hand >>> '))
            price = float(input('Update price >>> '))
            p.set_quantity(quantity)
            p.set_price(price)
            print('Updated', p.get_sku(), p.get_name())
        except ValueError as e:
            print(e, 'Failed to update', sku)
    else:
        try:
            name = input('Enter name for SKU {} >>> '.format(sku))
            quantity = int(input('Enter quantity on hand >>> '))
            price = float(input('Enter price >>> '))
            p = product.Product(sku, name, quantity, price)
            inv.add_product(p)
            print('Added', p.get_sku(), p.get_name())
        except ValueError as e:
            print(e, 'Failed to create', sku)

    # Save the Inventory object's products so we can use them later.
    inv.write_products_to_file(INVENTORY_FILENAME)


def transaction():
    """Transact a sale from user supplied data."""
    # Create the Inventory object and read its products from the file.
    inv = inventory.Inventory()
    try:
        inv.read_products_from_file(INVENTORY_FILENAME)
    except (FileNotFoundError, EOFError, pickle.PickleError):
        print(
            'Cannot read from inventory file! Are you sure you have inventory?')
        return

    print(inv)
    # Create a Customer object by gathering a name and e-mail address.
    # Notice how we can use the return value from the input() function
    # as the name and email arguments for our constructor
    cust = customer.Customer(
        input('Enter your Name >>> '), input('Enter your Email >>> ')
    )

    # Create a Sale object and pass it the Customer object we just created
    s = sale.Sale(cust)

    # Prompt the user for a SKU. If the sku is found in the inventory,
    # ask the user how many units they want to buy. If the Product has
    # has sufficient quantity (>= the desired quantity), add the Product
    # to the Sale by calling the appropriate method. Repeat until the user
    # types DONE
    sku = input('Enter a SKU (or DONE to complete) >>> ')
    while sku != 'DONE':
        if inv.has_product(sku):
            p = inv.get_product(sku)
            try:
                quantity = int(input('How many "{}" do you want? >>> '.format(
                    p.get_name())))
                if quantity <= p.get_quantity():
                    print('Completing sale of {} units for ${:,.2f}'.format(
                        quantity, p.get_price() * quantity
                    ))
                    p.set_quantity(p.get_quantity() - quantity)
                    s.add_product(p)
                else:
                    print('Insufficient quantity ({} in stock)'.format(
                        p.get_quantity()))
            except ValueError as e:
                print(e, 'Try again')
        else:
            print(sku, 'is not a valid product!')
        sku = input('Enter a SKU (or DONE to complete) >>> ')

    # Out of loop, if sale has products, write it to the sales file.
    if len(s.get_products()):
        f = open(SALES_FILENAME, 'ab')
        pickle.dump(s, f)
        f.close()

        # We also need to update inventory since quantities have changed
        inv.write_products_to_file(INVENTORY_FILENAME)


def sales_report():
    """Build a report with the sales data"""
    # Try to read Sale objects from file.
    # If FileNotFoundError, EOFError or PickleError occurs, return immediately
    try:
        f = open(SALES_FILENAME, 'rb')
    except (FileNotFoundError, pickle.PickleError):
        print('Cannot read from sales file! Are you sure you have sales?')
        return

    # Pickle can read back Sale objects just like any other object. Inside of a
    # while loop, we'll continually read out Sale objects and print them, which
    # as we've said implicitly calls the __str__ method.
    sales = 0
    total = 0
    try:
        s = pickle.load(f)
        while s:
            print(s)
            sales += 1
            total += s.get_total()
            s = pickle.load(f)
    except EOFError:
        print('Finished reading all Sales from file!')
    finally:
        f.close()
    print('Total Sales: {:,}, Total Amount: ${:,.2f}'.format(sales, total))


# Call main()
main()
