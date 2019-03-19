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

    def test_insert(self):
        # Default to max-heap
        jeap = Jeap()
        jeap.insert(10)
        jeap.insert(20)
        self.assertTrue(jeap.find() == 20)


if __name__ == '__main__':
    unittest.main()
