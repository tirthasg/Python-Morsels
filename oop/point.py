from __future__ import annotations
from types import NotImplementedType


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Point):
            return NotImplemented

        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other: object) -> Point | NotImplementedType:
        if not isinstance(other, Point):
            return NotImplemented

        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: object) -> Point | NotImplementedType:
        if not isinstance(other, Point):
            return NotImplemented

        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, factor: float) -> Point:
        return Point(self.x * factor, self.y * factor, self.z * factor)

    def __rmul__(self, factor: float) -> Point:
        return self.__mul__(factor)

    def __iter__(self):
        return iter((self.x, self.y, self.z))


p1 = Point(1, 2, 3)
print(p1)

p2 = Point(1, 2, 3)
print(p1 == p2)
p2.x = 4
print(p1 == p2)

p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
print(p1 + p2)
print(p2 - p1)

p1 = Point(1, 2, 3)
print(p1 * 2)
print(2 * p1)

p1 = Point(1, 2, 3)
x, y, z = p1
print(x, y, z)

print(p1 == 5)
