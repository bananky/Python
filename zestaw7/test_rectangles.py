import unittest
from rectangles import *

class TestRectangle(unittest.TestCase):
	def setUp(self):
		self.rect1 = Rectangle()
		self.rect2 = Rectangle(1, 2, 3, 4)
		self.rect3 = Rectangle(3, 4, 0, -2)

	def test_str(self):
		self.assertEqual(self.rect2.__str__(), "[(1, 2), (3, 4)]")

	def test_repr(self):
		self.assertEqual(self.rect2.__repr__(), "Rectangle(1, 2, 3, 4)")

	def test_eq(self):
		self.assertTrue(self.rect2 == self.rect2)
		self.assertTrue(self.rect2 != self.rect1)

	def test_center(self):
		self.assertEqual(self.rect1.center(), Point())
		self.assertEqual(self.rect2.center(), Point(2, 3))

	def test_area(self):
		self.assertEqual(self.rect1.area(), 0)
		self.assertEqual(self.rect2.area(), 4)
		self.assertEqual(self.rect3.area(), 18)

	def test_move(self):
		self.rect1.move(2, 1)
		self.rect2.move(2, 1)
		self.assertEqual(self.rect1, Rectangle(2, 1, 2, 1))
		self.assertEqual(self.rect2, Rectangle(3, 3, 5, 5))

	def test_intersection(self):

		self.assertEqual(Rectangle(0, 0, 8, 4).intersection(Rectangle(4, 1, 12, 3)),
						 Rectangle(4, 1, 8, 3))

		self.assertEqual(Rectangle(0, 0, 8, 4).intersection(Rectangle(9, 5, 10, 11)),
						 None)

	def test_cover(self):
		self.assertEqual(Rectangle(0, 0, 8, 4).cover(Rectangle(4, 1, 12, 3)),
						 Rectangle(0, 0, 12, 4))

	def test_make4(self):
		self.assertEqual(Rectangle(0, 0, 8, 4).make4(), [Rectangle(0, 0, 4, 2),
														 Rectangle(4, 0, 8, 2),
														 Rectangle(0, 2, 4, 4),
														 Rectangle(4, 2, 8, 4)])

	def tearDown(self): pass


if __name__ == '__main__':
	unittest.main()