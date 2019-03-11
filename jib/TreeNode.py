import warnings
from collections import deque
from jib.GraphNode import GraphNode
from jib.exceptions import TreeCyclicException
"""
    n-ary tree: inherits from GraphNode. Enforces tree constraints
"""


class TreeNode(GraphNode):

    def __init__(self, value=None):
        # TreeNodes have zero children at creation
        super().__init__(value, adjacent=None)
        # They do not have parents either
        self.parent = None

    def __setattr__(self, name, value):
        """Warn user if they are attempting to set attribute without using add

           Args:
            name (str): The attribute name
            value (*): the value
        """
        if name == "adjacent":
            warnings.warn("TreeNodes enforce tree constraints when adjacency \
                           objects are added via self.add().  You should not \
                           set self.adjacent explicetly.")
        object.__setattr__(self, name, value)

    def __findroot__(self):
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

    def __nocycle__(self, node):
        """Check tree for the presence of node.

        Args:
            node: TreeNode
                The node we want to verify is not already present

        Returns:
            boolean
                Raise exception if cycle found, otherwise return true
        """
        # Find root
        root = self.__findroot__()
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
            for adj_node in current_node.adjacent.values():
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
        if self.__nocycle__(child):
            child.parent = self
            adjacent_dict = object.__getattribute__(self, "adjacent")
            adjacent_dict[child] = child
            object.__setattr__(self, "adjacent", adjacent_dict)
