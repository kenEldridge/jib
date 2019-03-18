#!/usr/bin/env python
"""Test the jeap class"""

import unittest
from jib.jeap import Jeap

__author__ = "Ken Eldridge"
__copyright__ = "Copyright 2019, Ken Eldridge"
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Development"


class TestJeap(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(Jeap(), Jeap)

    def test_tree_features(self):
        node1 = Jeap()
        node2 = Jeap()
        node3 = Jeap()
        node4 = Jeap()
        node5 = Jeap()
        node6 = Jeap()
        node7 = Jeap()
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = derp


if __name__ == '__main__':
    unittest.main()
