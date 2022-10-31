class Cycle():
    def __init__(self, r):
        self.pi = 3.1415926
        self.r = r


def square(value):
    if not isinstance(value, Cycle):
        raise ValueError("value must be a Cycle instance")
    value.square = value.pi * value.r**2
