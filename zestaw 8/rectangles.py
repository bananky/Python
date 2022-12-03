from points import Point
import math

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Must be: x1 < x2 and y1 < y2")
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

    #def center(self):
        #return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):
        a = self.pt1
        b = self.pt2
        c = other.pt1
        d = other.pt2

        x1 = max(a.x, c.x)
        y1 = max(a.y, c.y)
        x2 = min(b.x, d.x)
        y2 = min(b.y, d.y)

        if x1 > x2 or y1 > y2:
            return None

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        a = self.pt1
        b = self.pt2
        c = other.pt1
        d = other.pt2

        x1 = min(a.x, c.x)
        y1 = min(a.y, c.y)
        x2 = max(b.x, d.x)
        y2 = max(b.y, d.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        center = self.center()
        r1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        r2 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        r3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        r4 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        return [r1, r2, r3, r4]

    @classmethod
    def from_points(cls,points):
        return "Rectangle({0}, {1}, {2}, {3})".format(points[0].x,
                                                      points[0].y, points[1].x, points[1].y)



    @property
    def left(self):
        return self.pt1.x

    @left.setter
    def left(self, value):
        self.pt1.x = value

    @left.deleter
    def left(self):
        self.pt1.x = None


    @property
    def bottom(self):
        return self.pt1.y

    @bottom.setter
    def bottom(self, value):
        self.pt1.y = value

    @bottom.deleter
    def bottom(self):
        self.pt1.y = None


    @property
    def right(self):
        return self.pt2.x

    @right.setter
    def right(self, value):
        self.pt2.x = value

    @right.deleter
    def right(self):
        self.pt2.x = None


    @property
    def top(self):
        return self.pt2.y

    @top.setter
    def top(self, value):
        self.pt2.y = value

    @top.deleter
    def top(self):
        self.pt2.y = None


    @property
    def width(self):
        return math.sqrt(math.pow(self.pt2.x - self.pt1.x, 2) + math.pow(self.pt2.y - self.pt1.y, 2))


    @property
    def height(self):
        return math.sqrt(math.pow(self.pt2.x - self.pt2.x, 2) + math.pow(self.pt2.y - self.pt1.y, 2))


    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)


    @property
    def bottom_left(self):
        return Point(self.pt1.x, self.pt1.y)

    @bottom_left.setter
    def bottom_left(self, point):
        self.pt1.x = point.x
        self.pt1.y = point.y

    @bottom_left.deleter
    def bottom_left(self):
        self.pt1.x = None
        self.pt1.y = None


    @property
    def top_left(self):
        return Point(self.pt1.x, self.pt2.y)

    @top_left.setter
    def top_left(self, point):
        self.pt1.x = point.x
        self.pt2.y = point.y

    @top_left.deleter
    def top_left(self):
        self.pt1.x = None
        self.pt2.y = None


    @property
    def bottom_right(self):
        return Point(self.pt2.x, self.pt1.y)

    @bottom_right.setter
    def bottom_right(self, point):
        self.pt2.x = point.x
        self.pt1.y = point.y

    @bottom_right.deleter
    def bottom_right(self):
        self.pt2.x = None
        self.pt1.y = None


    @property
    def top_right(self):
        return Point(self.pt2.x, self.pt2.y)

    @top_right.setter
    def top_right(self, point):
        self.pt2.x = point.x
        self.pt2.y = point.y

    @top_right.deleter
    def top_right(self):
        self.pt2.x = None
        self.pt2.y = None


if __name__ == '__main__':
    points = [Point(0, 0), Point(2, 1)]
    rectangle = Rectangle.from_points(points)
    print(rectangle.__str__())

    print(rectangle.center)
