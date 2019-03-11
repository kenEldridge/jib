import warnings
"""
    n-ary graph
"""


class GraphNode:
    def __init__(self, value=None, adjacent=None):
        """Create a graph node

        Args:
            value (Any): whatever you want, baby!
            adjacent (dict): dict of GraphNodes
        """
        if not adjacent:
            adjacent = {}
        self.value = value
        # Normal setter here invoked sub-classes __setattr__
        object.__setattr__(self, "adjacent", adjacent)

    def add(self, node):
        """Add node to self's adjacency dict

        Args:
            node (GraphNode): node add to adjacency dict
        """
        if node not in self.adjacent:
            self.adjacent[node] = node
        else:
            warnings.warn('%s already in %s\'s adjacency dict' % (node, self))

    def remove(self, node):
        """Remove node from self's adjacency dist

        Args:
            node (GraphNode): node to remove from adjacency dict
        """
        if node in self.adjacent:
            del self.adjacent[node]
        else:
            warnings.warn('%s not in %s\'s adjacency dict' % (node, self))
