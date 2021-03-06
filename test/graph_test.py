#!/usr/bin/env python
"""Test the GraphNode class"""

import unittest
import warnings
from jib.graph import GraphNode

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class TestGraphNode(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(GraphNode(), GraphNode)

    def test_independence(self):
        node1 = GraphNode()
        node2 = GraphNode()
        self.assertNotEqual(node1, node2)

    def test_add(self):
        node1 = GraphNode()
        node2 = GraphNode()
        node1.add(node2)
        self.assertIn(node2, node1.adjacent)

    def test_add_warning(self):
        node1 = GraphNode()
        node2 = GraphNode()
        node1.add(node2)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node1.add(node2)
            self.assertTrue(len(w) == 1)
            self.assertIsInstance(w[0], warnings.WarningMessage)

    def test_remove(self):
        node1 = GraphNode()
        node2 = GraphNode()
        node1.add(node2)
        node1.remove(node2)
        self.assertNotIn(node2, node1.adjacent)

    def test_remove_warning(self):
        node1 = GraphNode()
        node2 = GraphNode()
        node1.add(node2)
        node1.remove(node2)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node1.remove(node2)
            self.assertTrue(len(w) == 1)
            self.assertIsInstance(w[0], warnings.WarningMessage)


if __name__ == '__main__':
    unittest.main()
