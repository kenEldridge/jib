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

    def _swap_(self, new_node, old_node):
        """Replace new_node with old_node

        Args:
         new_node (BinaryTreeNode): Node to insert
         old_node (BinaryTreeNode): Node to remove
        """
        old_node.value, new_node.value = new_node.value, old_node.value

    def _replace_(self, item, node):
        """Search tree in BFS fashion checking to see if item at node should be
           replaced.

        Args:
         node_insert (BinaryTreeNode): item to insert
         node_current (BinaryTreeNode): the position in self._tree

        Returns:
         replaced_item: the item that was replaced
         node: the current node from self._tree
        """
        queue = deque()
        queue.append(node)
        while queue:
            node = queue.popleft()
            if item.value < node_current.value:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                # swap values inplace, item will have the replace value
                self._swap_(item, node)
                return item, node
        # if we do not replace, signal by returning None
        return None, node


    def insert(self, item):
        """Insert item in to tree maintaining heap order inplace

        Args:
         item: item to insert
        """
        item_node = BinaryTreeNode(value=item)
        replaced, node_current = self._replace_(item_node, self._tree)
        while replaced:
            replaced, node_current = self._replace_(replaced, node_current)
        if not node.left:
            node.left = re

        # this is getting sloppy.  take a step back tomorrow and think this through
        # before writing more code

    def merge():
        return warnings.warn("Not Implemented")
