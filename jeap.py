#!/usr/bin/env python
"""jeap objects: (jib) heap implemented via inheritance from BinaryTreeNode"""

import warnings
from collections import deque
from jib.binarytree import BinaryTreeNode

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class Jeap():

    def __init__(self, max=True):
        # Jeaps use BinaryTreeNodes to store heap
        self._tree = BinaryTreeNode()
        # Default to max-heap, allow max=False to create a min-heap
        if max:
            self.max = True
        else:
            self.max = False

    def find():
        return warnings.warn("Not Implemented")

    def delete():
        return warnings.warn("Not Implemented")

    def _swap(node1, node2):
        node1.value, node2.value = node2.value, node1.value
        return node1.value, node2.value

    def _replace_(self, node_current, node_insert):
        """Search tree in BFS fashion checking to see if item at node_current
           should be replaced.

        Args:
         node_current (BinaryTreeNode): the position in self._tree
         node_insert (BinaryTreeNode): item to insert

        Returns:
         node_current: the current node from self._tree
         node_removed: the item that was removed
        """
        queue = deque()
        queue.append(node_current)
        while queue:
            node_current = queue.popleft()
            if node_insert.value < node_current.value:
                # insert if space available, otherwise keep searching
                if not node_current.left:
                    node_current.left = node_insert
                    return node_insert, None
                else:
                    queue.append(node_current.left)
                if not node_current.right:
                    node_current.right = node_insert
                    return node_insert, None
                else:
                    queue.append(node_current.right)
            else:
                # Swap values because it's simpler than replacing in tree
                node_current.value, node_insert.value = node_insert.value, node_current.value
                return node_current, node_insert


    def insert(self, item):
        """Insert item in to tree maintaining heap order inplace

        Args:
         item: item to insert
        """
        removed = None
        # Is this the first insert?
        if self._tree.value is None:
            self._tree.value = item
            item_node = self._tree
        else:
            item_node = BinaryTreeNode(value=item)
            node_current, removed = self._replace_(node_current=self._tree,
                                                    node_insert=item_node)
        # import pdb; pdb.set_trace()
        while removed:
            node_current, removed = self._replace_(node_current, removed)

        # this is getting sloppy.  take a step back tomorrow and think this through
        # before writing more code

    def merge():
        return warnings.warn("Not Implemented")
