class Adjacent:
    """docstring for ."""
    def __init__(self):
        self.adjacency_dict = {}

    # def __setattr(self, name, value):
    #     object.__setattr(self, name, value)
    #
    # def __getattribute__(self, name):
    #     object.__getattribute__(self, name)

    def __iter__(self):
        """Returns self.adjacent

        Returns:
            self.adjacent (dict)
        """
        return iter(self.adjacency_dict)

    def __next__(self):
        """Advances to next item

        Returns:
            node (LinkedList): next node
        """
        if hasnext(self.adjacency_dict):
            return next(self.adjacency_dict)
        else:
            raise StopIteration
