from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        if self.side_length < 0:
            raise ValueError("Side length must be nonnegative.")
        if not isinstance(self.side_length, (int, float)):
            raise TypeError("Side length must be a number.")
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("Radius must be nonnegative.")
        if not isinstance(self.radius, (int, float)):
            raise TypeError("Radius must be a number.") 
        return math.pi * (self.radius ** 2)

