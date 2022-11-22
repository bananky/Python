from points import *
import unittest


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(2, 4)), "(2, 4)")
        self.assertEqual(repr(Point(2, 4)), "Point(2, 4)")

    def test_cmp(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(3, 2))
        self.assertTrue(Point(1, 2) != Point(1, 3))
        self.assertTrue(Point(1, 2) != Point(4, 5))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 3), Point(4, 5))

    def test_subtract(self):
        self.assertEqual(Point(4, 2) - Point(2, 1), Point(2, 1))
        self.assertEqual(Point(2, 1) - Point(4, 2), Point(-2, -1))

    def test_scalar(self):
        self.assertEqual(Point(4, 2) * Point(2, 1), Point(8, 2))

    def test_cross(self):
        self.assertEqual(Point(4, 1).cross(Point(3, 2)), 5)

    def test_len(self):
        self.assertEqual(Point(4, 3).length(), 5)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy