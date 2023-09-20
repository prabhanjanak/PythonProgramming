import math

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

triangle = Triangle(5, 8)
circle = Circle(3)
rectangle = Rectangle(4, 6)

print("Area of Triangle:", triangle.area())
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
