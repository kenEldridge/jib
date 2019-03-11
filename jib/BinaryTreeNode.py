from jib.TreeNode import TreeNode
"""
    binary tree: inherits from TreeNode
"""


class BinaryTreeNode(TreeNode):

    def __init__(self, value=None, root=None):
        # BinaryTreeNodes have zero children at creation
        super().__init__(value)
        # init left, right
        self.left, self.right = None, None

    def __getattribute__(self, name):
        """Override TreeNode __getattribute__ in order to override
           the adjacency dict with left and right

           Args:
            name (str): The attribute name
        """
        if name == "left":
            object.__setattr__(self, name, self.adjacent[name])
        elif name == "right":
            object.__setattr__(self, name, self.adjacent[name])
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """Override TreeNode __setattr__ in order to override
           the adjacency dict with left and right

           Args:
            name (str): The attribute name
            value (BinaryTreeNode): The node to set
        """
        if name == "left" or name == "right":
            # Raise exception if tree constraint violation
            self.__nocycle__(value)
            if value:
                if isinstance(value, BinaryTreeNode):
                    value.parent = self
                    adjacent_dict = object.__getattribute__(self, "adjacent")
                    adjacent_dict[name] = value
                    object.__setattr__(self, "adjacent", adjacent_dict)
                else:
                    raise ValueError("value must be type '%s'" % type(self))
        # elif name == "adjacent":
            # Only allow two
        else:
            object.__setattr__(self, name, value)
