from points import Point

class Rectangle:

	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):
		return "[{0}, {1}]".format(self.pt1, self.pt2)

	def __repr__(self):
		return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x,
			self.pt1.y, self.pt2.x, self.pt2.y)

	def __eq__(self, other):
		return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

	def __ne__(self, other):
		return not self == other

	def center(self):
		return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

	def area(self):
		return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

	def move(self, x, y):
		self.pt1 = self.pt1 + Point(x, y)
		self.pt2 = self.pt2 + Point(x, y)
