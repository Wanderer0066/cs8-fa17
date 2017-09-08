#!/usr/bin/python3

prompt = 'Enter a primary color (red, blue, or yellow): '
color1 = input(prompt)
color2 = input(prompt)

# Our first conditional test checks to make sure both color1 and color2
# are valid values. We do this by taking the 'not' operator on the three
# possible colors combined together with 'or' operators. Remember, if
# any condition joined with an 'or' is True, than the entire statement
# is True. So, for the not statement to be True, all conditions
# inside joined by or's must be False.
if (not (color1 == 'red' or color1 == 'blue' or color1 == 'yellow')
    or not (color2 == 'red' or color2 == 'blue' or color2 == 'yellow')):
  print("You didn't input two primary colors")
else:
  result = ''
  if color1 == color2:
    result = color1
  elif ((color1 == 'red' and color2 == 'blue')
        or (color2 == 'red' and color1 == 'blue')):
    result = 'purple'
  elif ((color1 == 'red' and color2 == 'yellow')
        or (color2 == 'red' and color1 == 'yellow')):
    result = 'orange'
  elif ((color1 == 'blue' and color2 == 'yellow')
        or (color2 == 'blue' and color1 == 'yellow')):
    result = 'green'
  print('When you mix {} and {}, you get {}'.format(
    color1, color2, result))
