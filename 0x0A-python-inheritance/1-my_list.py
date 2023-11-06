#!/usr/bin/python3
"""
Contains a class MyList that inherits from list builtin
"""


class MyList(list):
  
    """ A class that inherits from list and provides a
        method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        Example:
        >>> my_list = MyList()
        >>> my_list.append(1)
        >>> my_list.append(4)
        >>> my_list.append(2)
        >>> my_list.append(3)
        >>> my_list.append(5)
        >>> print(my_list)
        [1, 4, 2, 3, 5]
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        """
        print(sorted(self))
