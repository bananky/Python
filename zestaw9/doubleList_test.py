import unittest
from doubleList import *

class testDoubleList(unittest.TestCase):
    double_list = None

    def setUp(self):
        self.double_list = DoubleList()
        self.double_list.insert_head(Node(2))
        self.double_list.insert_head(Node(5))
        self.double_list.insert_head(Node(3))

    def test_is_empty(self):
        self.assertTrue(DoubleList().is_empty())
        self.assertEqual(self.double_list.is_empty(), False)

    def test_count(self):
        self.assertEqual(self.double_list.count(), 3)

    def test_insert_head(self):
        self.double_list.insert_head(Node(1))
        self.assertEqual(self.double_list.head.data, 1)
        self.assertEqual(self.double_list.head.next.data, 3)
        self.assertEqual(self.double_list.head.next.next.data, 5)
        self.assertEqual(self.double_list.head.next.next.next.data, 2)

    def test_insert_tail(self):
        self.double_list.insert_tail(Node(7))
        self.assertEqual(self.double_list.head.data, 3)
        self.assertEqual(self.double_list.head.next.data, 5)
        self.assertEqual(self.double_list.head.next.next.data, 2)
        self.assertEqual(self.double_list.head.next.next.next.data, 7)


    def test_remove_head(self):
        self.double_list.remove_head()
        self.assertEqual(self.double_list.head.data, 5)
        self.assertEqual(self.double_list.head.next.data, 2)

    def test_remove_tail(self):
        self.double_list.remove_tail()
        self.assertEqual(self.double_list.head.data, 3)
        self.assertEqual(self.double_list.head.next.data, 5)

    def test_find_min(self):
        node = self.double_list.find_min()
        self.assertEqual(node.data, 2)

    def test_find_max(self):
        node = self.double_list.find_max()
        self.assertEqual(node.data, 5)

    def test_remove(self):
        self.double_list.remove(Node(5))
        self.assertEqual(self.double_list.head.data, 3)
        self.assertEqual(self.double_list.head.next.data, 2)


    def test_clear(self):
        self.double_list.clear()
        self.assertEqual(self.double_list.is_empty(), True)


if __name__ == '__main__':
    unittest.main()


