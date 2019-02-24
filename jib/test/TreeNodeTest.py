import unittest
import warnings
from jib.TreeNode import TreeNode

class TestTreeNode(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(TreeNode(), TreeNode)

    def test_independence(self):
        node1 = TreeNode()
        node2 = TreeNode()
        self.assertNotEqual(node1, node2)

    def test_add(self):
        node1 = TreeNode()
        node2 = TreeNode()
        node1.add(node2)
        self.assertIn(node2, node1.adjacent)

    def test_add_warning(self):
        node1 = TreeNode()
        node2 = TreeNode()
        node1.add(node2)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node1.add(node2)
            self.assertTrue(len(w) == 1)
            self.assertIsInstance(w[0], warnings.WarningMessage)

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

    def test_non_cyclic_create(self):
        # Ensure non-cyclic behavior add instanciating with adjacent param
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
