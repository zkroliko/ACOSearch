import itertools

from acoAlgorithm.Area import Area
from acoAlgorithm.Rectangle import Rectangle
from acoAlgorithm.Field import Field, FieldType

import unittest

from acoAlgorithm.Point import Point
from acoAlgorithm.View import ViewGenerator
from acoAlgorithm.tools.Printer import Printer
from examples.Scenario1 import Scenario1


class TestView(unittest.TestCase):
    def test_corners(self):
        # Setup
        a = Area(Rectangle(Field(0, 0), Field(15, 15)), 1)
        a += Rectangle(Field(0, 0), Field(10, 10))
        v = ViewGenerator(a)
        # todo: After the corner functionality is working, make it work again
        # corners = list(itertools.chain(*map(lambda x: x.free_corners(), a.all_rectangles())))
        # # Test itself
        # corner_points = []
        # for c in corners:
        #     point = Point.map_to_point(c)
        #     corner_points.append(point)
        # self.assertEqual(Set(corner_points), Set(v.corner_points))

    def test_sorted(self):
        # Setup
        a = Area(Rectangle(Field(0, 0), Field(15, 15)), 1)
        origin = Point(5, 5)
        points = [Point(10, 5), Point(5, 10), Point(0, 5), Point(5, 0), Point(10, 10), Point(0, 10), Point(0, 0),
                  Point(10, 0)]
        # Test
        expected = [Point(5, 0), Point(10, 0), Point(10, 5), Point(10, 10), Point(5, 10), Point(0, 10), Point(0, 5),
                    Point(0, 0)]
        result = ViewGenerator.sorted_to_origin(points, origin)
        # Result check
        self.assertEqual(expected, result)

    def test_sorted2(self):
        # Setup
        a = Area(Rectangle(Field(0, 0), Field(15, 15)), 1)
        origin = Point(0, 0)
        points = [Point(1, -1), Point(-1, -1), Point(-1, 1), Point(1, 1),
                  Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0),]
        # Test
        expected = [Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1),
                    Point(0, 1),Point(-1, 1),Point(-1, 0), Point(-1, -1)]
        result = ViewGenerator.sorted_to_origin(points, origin)
        # Result check
        self.assertEqual(expected, result)

    def gen_area(self):
        # DO NOT CHANGE!!!
        a = Area(Rectangle(Field(0, 0), Field(7, 7)), 1)

        rectangles = [
            Rectangle(Field(2, 2), Field(3, 3), type=FieldType.inaccessible),
            Rectangle(Field(2, 5), Field(3, 6), type=FieldType.inaccessible),
            Rectangle(Field(5, 2), Field(6, 3), type=FieldType.inaccessible),
            Rectangle(Field(5, 5), Field(6, 6), type=FieldType.inaccessible)
        ]
        a += rectangles
        return a

    def test_shine_from(self):
        a = self.gen_area()

        v = ViewGenerator(a)
        self.assertEqual(v.lm.how_many_left(), 48)
        v.shine_from(Point(4, 4))

        self.assertEqual(v.lm.how_many_left(), 17)

    # def test_shine_from_triangles(self):
    #     a = Scenario1.area()
    #
    #     v = ViewGenerator(a)
    #     v.shine_from_triangles(Point.map_to_point(Scenario1.start()))


if __name__ == '__main__':
    unittest.main()
