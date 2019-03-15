#!/usr/bin/env python
"""jeap objects: (jib) heap implemented via inheritance from BinaryTreeNode"""

import warnings
from jib.binarytree import BinaryTreeNode

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class Jeap(BinaryTreeNode):

    def __init__(self, value=None, root=None, max=True):
        # Jeap have zero children at creation
        super().__init__(value, root)
        # Default to max-heap, allow max=False to create a min-heap
        if max:
            self.max = True
        else:
            self.max = False

    def find():
        return warnings.warn("Not Implemented")

    def delete():
        return warnings.warn("Not Implemented")

    def insert():
        return warnings.warn("Not Implemented")

    def merge():
        return warnings.warn("Not Implemented")
