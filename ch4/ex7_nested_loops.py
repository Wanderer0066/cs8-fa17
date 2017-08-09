#!/usr/bin/python3

# Let's build our times tables shall we.
output_lines = 0
for x in range(1, 1001):  # This will iterate x from 1 through 10
      for y in range(1, 1001):  # This will do the same for y
          # Now, inside our 'inner' loop, we will execute a statement for each
          # value of y. Because this inner loop is going to executed 10 times
          # (once for each value of x), we'll have a total of 100 lines of output
          print('{} x {} = {}'.format(x, y, x * y))
          output_lines += 1
        
print('The total output lines (iterations of inner loop) was {}'.format(
    output_lines))
