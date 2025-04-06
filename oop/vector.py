class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, factor):
        return Vector(self.x * factor, self.y * factor, self.z * factor)

    def __rmul__(self, factor):
        return self.__mul__(factor)
