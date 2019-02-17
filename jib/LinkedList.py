
class LinkedList:
    def __init(self, value=None, next = None):
        self.value = value
        self.next = next

    def insert(self, node, value=None):
        if value is not None:
            by_value = True
        while self.next:
            if by_value and self.value == value:
                # The templess swap. Thanks, Python
                self.next, node.next = node, self.next
            else:
                self.next = node

    def delete(self, node):
        head = self
        last = self
        while self.next:
            if self is node:
                last.next = self.next
                # If you are dropping the head, update our
                # head, since that's what we're returning
                if node is head:
                    head = head.next
            # Advance our last tracker
            last = self
            # Step into the next node
            self = self.next
        return head
