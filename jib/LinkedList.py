"""
    A simple linked list
"""
class LinkedList:
    def __init__(self, value=None, next_item= None):
        """Create a node

        Args:
            value (Any): whatever you want, baby!
            next (LinkedList): just the next node
        """
        self.value = value
        self.next_item = next_item

    def insert(self, node, end=True):
        """Insert a node either following a specific node (by_value) or at
           the end of the list

        Args:
            node (LinkedList): node to insert
            end (boolean): insert at the of list, if false following self
        """
        if end:
            while self.next_item:
                self = self.next_item
            self.next_item = node
        else:
            self.next_item, node.next_item = node, self.next_item

    def remove(self, node):
        """Remove specified node.  Assumes self is the head

        Args:
            node (LinkedList): node to remove

        Returns:
            head (LinkedList): return the head of the list
        """
        # If the head is removed, just cut it off and return next
        if self is node:
            return self.next_item
        # Save entry point to return
        head = self
        # Save your most recent node
        last = self
        # Find the node to remove
        while self.next_item and self is not node:
            # Update your most recent node
            last = self
            # Step into the next node
            self = self.next_item
        if self is node:
            # Jump self
            last.next_item = self.next_item
        return head

    def __iter__(self):
        """Returns self

        Returns:
            node (LinkedList): self
        """
        return self

    def __next__(self):
        """Advances to next item

        Returns:
            node (LinkedList): next node
        """
        if self.next_item is None:
            raise StopIteration
        else:
            return self.next_item
