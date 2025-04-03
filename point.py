class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


p1 = Point(1, 2, 3)
print(p1)

p2 = Point(1, 2, 3)
print(p1 == p2)
p2.x = 4
print(p1 == p2)
