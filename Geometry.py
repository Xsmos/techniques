class Geometry:
    def get_square(self):
        raise NotImplementedError


class Rectangle(Geometry):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def get_square(self):
        return self.length * self.height


class Cycle(Geometry):
    def __init__(self, r):
        self.pi = 3.1415926
        self.r = r

    def get_square(self):
        return self.pi * self.r**2


def square(value):
    if not isinstance(value, Geometry):
        raise ValueError("value must be Geometry instance")
    value.square = value.get_square()
