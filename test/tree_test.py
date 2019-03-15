#!/usr/bin/env python
"""Test the TreeNode class"""

import unittest
import warnings
from jib.tree import TreeNode
from jib.exceptions import TreeCyclicException

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class TestTreeNode(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(TreeNode(), TreeNode)

    def test_independence(self):
        node1 = TreeNode()
        node2 = TreeNode()
        self.assertNotEqual(node1, node2)

    def test_add(self):
        # Simple add
        node1 = TreeNode()
        node2 = TreeNode()
        node1.add(node2)
        self.assertIn(node2, node1.adjacent)
        # Cyclic add violation base-case
        node1 = TreeNode()
        try:
            node1.add(node1)
            # fail if no exception
            self.assertTrue(False)
        except Exception as e:
            # Ensure correct exception
            self.assertIsInstance(e, TreeCyclicException)
        # Cyclic add violation
        node1 = TreeNode()
        node2 = TreeNode()
        node3 = TreeNode()
        node4 = TreeNode()
        node5 = TreeNode()
        node6 = TreeNode()
        node1.add(node2)
        node1.add(node3)
        node2.add(node4)
        node2.add(node5)
        node3.add(node6)
        try:
            node6.add(node5)
            # fail if no exception
            self.assertTrue(False)
        except Exception as e:
            # ensure excpetion is correct type
            self.assertIsInstance(e, TreeCyclicException)

    def test_remove(self):
        node1 = TreeNode()
        node2 = TreeNode()
        node1.add(node2)
        node1.remove(node2)
        self.assertNotIn(node2, node1.adjacent)

    def test_remove_warning(self):
        node1 = TreeNode()
        node2 = TreeNode()
        node1.add(node2)
        node1.remove(node2)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node1.remove(node2)
            self.assertTrue(len(w) == 1)
            self.assertIsInstance(w[0], warnings.WarningMessage)

    def test_manual_add_warning(self):
        node1 = TreeNode()
        node2 = TreeNode()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node1.adjacent[node2] = node2
            self.assertTrue(len(w) == 1)
            self.assertIsInstance(w[0], warnings.WarningMessage)


if __name__ == '__main__':
    unittest.main()
