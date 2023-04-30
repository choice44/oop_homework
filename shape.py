class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


circle = Circle(5)
print(circle.get_area())

rectangle = Rectangle(2, 4)
print(rectangle.get_area())
