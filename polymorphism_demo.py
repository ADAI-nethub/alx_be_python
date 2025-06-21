# polymorphism_demo.py

class Shape:
    def area(self):
        # This method should be overridden by any specific shape class.
        raise NotImplementedError("Subclass must implement abstract method 'area'")
    
class Rectangle(Shape): # Rectangle inherits from Shape
    def __init__(self, length, width):
        # When you create a Rectangle, you give it a length and width.
        self.length = length
        self.width = width

    def area(self):
        # This method OVERRIDES Shape's area() for rectangles.
        return self.length * self.width

import math # Add this line at the very top of your file!

# ... (keep the Shape and Rectangle classes above) ...

class Circle(Shape): # Circle also inherits from Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # This method OVERRIDES Shape's area() for circles.
        return math.pi * (self.radius ** 2)