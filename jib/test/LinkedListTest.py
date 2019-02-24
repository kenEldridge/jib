import unittest
from jib.LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(LinkedList(), LinkedList)

    def test_independence(self):
        head = LinkedList()
        tail = LinkedList()
        self.assertNotEqual(head, tail)

    def test_insert(self):
        head = LinkedList()
        node = LinkedList()
        tail = LinkedList()
        head.insert(node)
        head.insert(tail)
        self.assertEqual(head.next.next, tail)

    def test_remove(self):
        # Remove head
        head = LinkedList()
        node = LinkedList()
        tail = LinkedList()
        head.insert(node)
        head.insert(tail)
        head = head.remove(head)
        self.assertEqual(head, node)
        # Remove node
        head = LinkedList()
        node = LinkedList()
        tail = LinkedList()
        head.insert(node)
        head.insert(tail)
        head = head.remove(node)
        self.assertEqual(head.next, tail)
        # Remove tail
        head = LinkedList()
        node = LinkedList()
        tail = LinkedList()
        head.insert(node)
        head.insert(tail)
        head = head.remove(tail)
        self.assertEqual(head.next.next, None)
        # Only node
        head = LinkedList()
        head = head.remove(head)
        self.assertEqual(head, None)

    def test_iterable(self):
        head = LinkedList(value='one')
        node = LinkedList(value='two')
        tail = LinkedList(value='three')
        head.insert(node)
        head.insert(tail)
        cat = ''.join([nd.value for nd in head])
        self.assertEqual(cat, 'onetwothree')

if __name__ == '__main__':
    unittest.main()
