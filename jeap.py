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
         replaced_item: the item that was replaced
         node: the current node from self._tree
        """
        queue = deque()
        queue.append(node_current)
        while queue:
            node_current = queue.popleft()
            if node_insert.value < node_current.value:
                # insert if space available, otherwise keep searching
                if not node_current.left:
                    node_current.left = node_insert
                    return None, node_insert
                else:
                    queue.append(node_current.left)
                if not node_current.right:
                    node_current.right = node_insert
                    return None, node_insert
                else:
                    queue.append(node_current.right)
            else:
                # Swap values because it's simpler than replacing in tree
                node_insert.value, node_current.value = node_current.value, node_insert.value
                return node_insert, node_current
        # if no value needs replaced, we just need to add node_insert as a child
        if not node_current.left:
            # Swap values because it's simpler than replacing in tree
            node_insert.value, node_current.value = node_current.value, node_insert.value
        return None, node_current


    def insert(self, item):
        """Insert item in to tree maintaining heap order inplace

        Args:
         item: item to insert
        """
        # Is this the first insert?
        if self._tree.value is None:
            self._tree.value = item
            item_node = self._tree
        else:
            item_node = BinaryTreeNode(value=item)
        replaced, node_current = self._replace_(item_node, self._tree)
        import pdb; pdb.set_trace()
        while replaced:
            replaced, node_current = self._replace_(replaced, node_current)

        # this is getting sloppy.  take a step back tomorrow and think this through
        # before writing more code

    def merge():
        return warnings.warn("Not Implemented")
