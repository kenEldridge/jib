import warnings
from jib.GraphNode import GraphNode
"""
    n-ary tree: inherits from GraphNode. Enforces tree constraints
"""
class TreeNode(GraphNode):

    def __init__(self, value=None, root=None):
        # TreeNodes have zero children at creation
        super().__init__(value, adjacent=None)
        # If root not supplied, assume self to be root
        if not root:
            self.root = self
        else:
            self.root = root

    def add(self, node):
        """Add node to self's adjacency dict

        Args:
            node (TreeNode): node add to adjacency dict
        """
        # Enforce tree constraints from perspective of self.root
