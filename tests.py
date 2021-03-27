from unittest import TestCase
from py_lru import DoublyLinkedList

class DoublyLinkedListTest(TestCase):
    def setUp(self) -> None:
        self.dll = DoublyLinkedList()

    def test_insert_left(self):
        items = list(range(10))
        for i in items:
            self.dll.insert_left(i)
        test_items = [i for i in self.dll]
        test_items.reverse()
        self.assertListEqual(items, test_items)

    def test_insert_right(self):
        items = list(range(10))
        for i in items:
            self.dll.insert_right(i)
        test_items = [i for i in self.dll]
        self.assertListEqual(items, test_items)

    def test_insert_left_right(self):
        for i in range(5, 10):
            self.dll.insert_right(i)
        for i in range(4, -1, -1):
            self.dll.insert_left(i)
        self.assertEqual(list(range(10)), [i for i in self.dll])

    def test_pop_left(self):
        self.assertIsNone(self.dll.pop_left(), "Should return None when list is empty")
        for i in range(10):
            self.dll.insert_left(i)
        self.assertEqual(9, self.dll.pop_left().val, "Should return leftmost element in the list")

    def test_pop_right(self):
        self.assertIsNone(self.dll.pop_right(), "Should return None when list is empty")
        for i in range(10):
            self.dll.insert_left(i)
        self.assertEqual(0, self.dll.pop_right().val, "Should return rightmost element in the list")

