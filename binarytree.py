#!/usr/bin/env python
"""BinaryTreeNode objects: inherits from TreeNode"""

import warnings
from jib.tree import TreeNode
from jib.exceptions import TreeAddException

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class BinaryTreeNode(TreeNode):

    def __init__(self, value=None, root=None):
        # BinaryTreeNodes have zero children at creation
        super().__init__(value)
        # init left, right
        self.left, self.right = None, None

    def __getattribute__(self, name):
        """Override TreeNode __getattribute__ in order to override
           the adjacency dict with left and right

           Args:
            name (str): The attribute name
        """
        if name == "left" or name == "right":
            if name in self.adjacent:
                object.__setattr__(self, name, self.adjacent[name])
            else:
                object.__setattr__(self, name, None)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """Override TreeNode __setattr__ in order to override
           the adjacency dict with left and right

           Args:
            name (str): The attribute name
            value (BinaryTreeNode): The node to set
        """
        if name == "left" or name == "right":
            # Raise exception if tree constraint violation
            self.__nocycle__(value)
            if value:
                if isinstance(value, BinaryTreeNode):
                    value.parent = self
                    adjacent_dict = object.__getattribute__(self, "adjacent")
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        adjacent_dict[name] = value
                    object.__setattr__(self, "adjacent", adjacent_dict)
                else:
                    raise ValueError("value must be type '%s'" % type(self))
        # elif name == "adjacent":
            # Only allow two
        else:
            object.__setattr__(self, name, value)

    def add(self, child):
        """Override parent add().  Allow setting of first two children.  Return
           exception is two children already present.

        Args:
            node: BinaryTreeNode
                add node as left or right
        """
        if self.left is None:
            self.__setattr__("left", child)
        elif self.right is None:
            self.__setattr__("right", child)
        else:
            raise TreeAddException(self)
