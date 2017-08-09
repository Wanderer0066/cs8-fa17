#!/usr/bin/python3

class SortedList(list):
    """You can inherit from built-in Python classes like list and
    override their methods with special behavior. In this case, we want to make
    the append method of a SortedList object keep the items in sorted order.
    We don't care about any other methods that list objects have. We can use
    the implementation from the superclass.
    """

    def append(self, item):
        # Loop through my items until we find one that the current item
        # parameter is less than. Then insert it there.
        inserted = False
        for i in range(len(self)):
            if item < self[i]:
                self.insert(i, item)
                inserted = True
                break
        # If we never inserted it, we can just append it to the end with
        # our superclass's method
        if not inserted:
            super().append(item)


def main():
    s = SortedList()
    s.append(6)
    s.append(1)
    s.append(2)
    s.append(11)
    s.append(5)
    s.append(0)
    print('s=', s)


main()



