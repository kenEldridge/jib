#!/usr/bin/env python
"""Provides dict with a warning when __setitem__ is called, encourages use of
   add methods.

   Adjacent object allows classes to address Adjacent attributes as if
   they are dictionaries.  They support index get/set, del, iteration, and warn
   a user if they are being used incorrectly.
"""

import warnings

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class Adjacent:
    """docstring for ."""
    def __init__(self):
        object.__setattr__(self, "_adjacency_dict", {})

    def __getattribute__(self, name):
        if name == "keys":
            return object.__getattribute__(self, "_adjacency_dict").keys
        if name == "values":
            return object.__getattribute__(self, "_adjacency_dict").values
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """Allow user to set adjacent dict within Adjacent object

           Args:
            name (str): The element name to add to adjacent_dict
            value (object): The element to add to adjacent_dict
        """
        self._adjacency_dict[name] = value
        object.__setattr__(self, "_adjacency_dict", self._adjacency_dict)

    def __getitem__(self, name):
        return self._adjacency_dict[name]

    def __setitem__(self, name, value):
        warnings.warn("Items should be added to adjacent dict via \
                       self.add()")
        self._adjacency_dict[name] = value

    def __delitem__(self, name):
        del self._adjacency_dict[name]

    def __iter__(self):
        """Returns self.adjacent

        Returns:
            self.adjacent (dict)
        """
        return iter(self._adjacency_dict)

    def __next__(self):
        """Advances to next item

        Returns:
            node (LinkedList): next node
        """
        if hasnext(self._adjacency_dict):
            return next(self._adjacency_dict)
        else:
            raise StopIteration
