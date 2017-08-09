#!/usr/bin/python3

def main():
  # Lists are mutable objects. This means they behave
  # differently than primitive types like int's or str's.
  # Let's see this in action.
  groceries = [
    'Milk',
    'Eggs',
    'Butter',
    'Bread',
    'Cheese',
    'Chicken'
  ]
  add_item(groceries)
  print('Grocery List:', groceries)
  print('---------------------------------------------------------------------')

  # What about assigning a new variable that will have the same
  # contents as groceries?
  groceries2 = groceries
  # Let's take some items out of our groceries list
  del groceries[0]
  del groceries[1]
  print('Grocery List (after del):', groceries)
  print('Grocery List 2:', groceries2)
  print('---------------------------------------------------------------------')

  # Notice how the changes to groceries affected groceries2.
  # That's because both variables pointed to the same object
  # in Python's memory. They weren't seperate copies.
  # To create a copy, you can use the .copy method of a list
  # or the [:] slice shortcut.
  groceries2 = groceries[:]
  del groceries[0]
  del groceries[1]
  print('Grocery List (after 2nd del):', groceries)
  print('Grocery List 2:', groceries2)


def add_item(groceries):
  # groceries is a parameter which behaves the same
  # as a local variable. However, when we call the add_item
  # function with a list as the argument, we can modify
  # the state of the list object in this method and those
  # changes will be reflected in the caller's scope.
  groceries.append(input('What would you like to add? '))

main()
