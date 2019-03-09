import warnings
from jib.GraphNode import GraphNode
from jib.exceptions import TreeCyclicException
from collections import deque

"""
    n-ary tree: inherits from GraphNode. Enforces tree constraints
"""
class TreeNode(GraphNode):

    def __init__(self, value=None, root=None):
        # TreeNodes have zero children at creation
        super().__init__(value, adjacent=None)
        # They do not have parents either
        self.parent = None

    def __find_root__(self):
        """Walk up the tree by parents

        Args: TreeNode

        Returns: TreeNode
            The root of node
        """
        # Follow parents to root, if no parents then self is root
        if self.parent:
            parent = self.parent
            while parent.parent:
                parent = parent.parent
            return parent
        else:
            return self

    def __no_cycle__(self, node):
        """Check tree rooted at root for the presence of node.

        Args:
            node: TreeNode
                The node we want to verify is not already present

        Returns:
            boolean
                Raise exception if cycle found, otherwise return true
        """
        # Find root
        root = self.__find_root__()
        # BFS
        bfs_queue = deque()
        bfs_queue.append(root)
        seen = set()
        seen.add(root)
        while bfs_queue:
            # Early exit if violation found
            if node in seen:
                raise TreeCyclicException(root=root, node=node)
            current_node = bfs_queue.popleft()
            for adj_node in current_node.adjacent:
                seen.add(adj_node)
                bfs_queue.append(adj_node)
        # Violation could be caused by last node in bfs_queue
        if node in seen:
            raise TreeCyclicException(root=root, node=node)
        return True

    def add(self, child):
        """Add child to self's adjacency dict

        Args:
            node: TreeNode
                add node to adjacency dict
        """
        # Enforce tree constraints
        if self.__no_cycle__(child):
            child.parent = self
            self.adjacent[child] = child
