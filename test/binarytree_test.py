#!/usr/bin/env python
"""Test the BinaryTreeNode class"""

import unittest
import warnings
from jib.binarytree import BinaryTreeNode
from jib.exceptions import (TreeCyclicException,
                            TreeAddException
                            )

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class BinaryTestTreeNode(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(BinaryTreeNode(), BinaryTreeNode)

    def test_independence(self):
        node1 = BinaryTreeNode()
        node2 = BinaryTreeNode()
        self.assertNotEqual(node1, node2)

    def test_add_children(self):
        # Simple add left, right
        node1 = BinaryTreeNode()
        node2 = BinaryTreeNode()
        node1.left = node2
        self.assertIs(node2, node1.left)
        # Cyclic add violation base-case
        node1 = BinaryTreeNode()
        try:
            node1.left = node1
            # fail if no exception
            self.assertTrue(False)
        except Exception as e:
            # Ensure correct exception
            self.assertIsInstance(e, TreeCyclicException)
        # Cyclic add violation
        node1 = BinaryTreeNode()
        node2 = BinaryTreeNode()
        node3 = BinaryTreeNode()
        node4 = BinaryTreeNode()
        node5 = BinaryTreeNode()
        node6 = BinaryTreeNode()
        node7 = BinaryTreeNode()
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        try:
            node6.left = node5
            # fail if no exception
            self.assertTrue(False)
        except Exception as e:
            # Ensure correct exception
            self.assertIsInstance(e, TreeCyclicException)
        node6.left = node7
        self.assertIs(node6.left, node7)

    def test_manual_add_warning(self):
        node1 = BinaryTreeNode()
        node2 = BinaryTreeNode()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node1.adjacent[node2] = node2
            self.assertTrue(len(w) == 1)
            self.assertIsInstance(w[0], warnings.WarningMessage)

    def test_using_add(self):
        node1 = BinaryTreeNode()
        node2 = BinaryTreeNode()
        node3 = BinaryTreeNode()
        node4 = BinaryTreeNode()
        node1.add(node2)
        node1.add(node3)
        self.assertTrue(node1.left is node2)
        self.assertTrue(node1.right is node3)
        try:
            # Add should only work twice
            node1.add(node4)
            # fail if no exception
            self.assertTrue(False)
        except TreeAddException as e:
            self.assertIsInstance(e, TreeAddException)
        try:
            # Tree cycle violation
            node2.add(node4)
            node4.add(node3)
            # fail if no exception
            self.assertTrue(False)
        except Exception as e:
            # Ensure correct exception
            self.assertIsInstance(e, TreeCyclicException)

if __name__ == '__main__':
    unittest.main()
