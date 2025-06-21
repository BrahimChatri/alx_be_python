import math

class Shape:
    """Base class for shapes."""
    
    def area(self):
        """Calculate area - to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area method")


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle class that inherits from Shape."""
    
    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

