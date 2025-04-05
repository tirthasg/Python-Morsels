from math import pi


class Circle:
    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius**2

    def __repr__(self):
        return f"Circle({self._radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius**2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")

        self._diameter = diameter
        self._radius = diameter / 2

    @property
    def area(self):
        return self._area


c = Circle(5)
print(c)
print(c._radius)
print(c._diameter)
print(c._area)
