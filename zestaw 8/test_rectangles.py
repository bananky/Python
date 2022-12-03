import pytest
import math
from points import Point
from rectangles import Rectangle


def test_str():
    assert Rectangle(1, 2, 3, 4).__str__() == "[(1, 2), (3, 4)]"


def test_repr():
    assert Rectangle(1, 2, 3, 4).__repr__() == "Rectangle(1, 2, 3, 4)"


def test_eq():
    assert Rectangle(1, 2, 3, 4).__eq__(Rectangle(2, 2, 3, 4)) is False


def test_ne():
    assert Rectangle(1, 2, 3, 4).__ne__(Rectangle(1, 0, 3, 4)) is True


def test_area():
    assert Rectangle(1, 2, 3, 4).area() == 4
    assert Rectangle(1, 2, 5, 6).area() == 16


def test_move():
    assert Rectangle(1, 2, 3, 4).move(2, -1) == Rectangle(3, 1, 5, 3)


def test_coordinates():
    assert Rectangle(1, 2, 3, 4).left == 1
    assert Rectangle(1, 2, 3, 4).bottom == 2
    assert Rectangle(1, 2, 3, 4).right == 3
    assert Rectangle(1, 2, 3, 4).top == 4


def test_size():
    assert Rectangle(1, 2, 3, 4).width == math.sqrt(8.0)
    assert Rectangle(1, 2, 3, 4).height == 2.0


def test_center():
    assert Rectangle(1, 2, 3, 4).center == Point(2.0, 3.0)


def test_points():
    assert Rectangle(1, 2, 3, 4).bottom_left == Point(1, 2)
    assert Rectangle(1, 2, 3, 4).top_left == Point(1, 4)
    assert Rectangle(1, 2, 3, 4).bottom_right == Point(3, 2)
    assert Rectangle(1, 2, 3, 4).top_right == Point(3, 4)


if __name__ == '__main__':
    pytest.main()