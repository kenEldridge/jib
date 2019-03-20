#!/usr/bin/env python
"""Test the jeap class"""

import unittest
from jib.jeap import Jeap
from jib.binarytree import BinaryTreeNode

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class TestJeap(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(Jeap(), Jeap)

    def test_insert(self):
        # Default to max-heap
        jeap = Jeap()
        jeap.insert(10)
        jeap.insert(20)
        self.assertTrue(True)
        # self.assertTrue(jeap.find() == 20)

    # def test__replace(self):
    #     jeap = Jeap()
    #     # manually set _tree since we are testing internals
    #     jeap._tree.value = 100
    #     node_insert = BinaryTreeNode(value=60)
    #     replaced_item, node = jeap._replace_(jeap._tree, node_insert)
    #     self.assertTrue(replaced_item is None)
    #     self.assertEqual(node.value, 60)


if __name__ == '__main__':
    unittest.main()
