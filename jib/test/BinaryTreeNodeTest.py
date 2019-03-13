import unittest
import warnings
from jib.BinaryTreeNode import BinaryTreeNode
from jib.exceptions import TreeCyclicException


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


if __name__ == '__main__':
    unittest.main()
