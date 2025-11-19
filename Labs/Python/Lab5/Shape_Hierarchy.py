from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):

        return self.area()+other.area()





class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        shape=self.__class__.__name__
        return (
            f"Area of Rectangle (w={self.width}, h={self.height}) is {self.area()}\n"
            f"Perimeter: {self.perimeter()}\n"
            f"shape: {shape}"
        )


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        shape = self.__class__.__name__
        return (
            f"Area of Circle (r={self.radius}) is {self.area()}\n"
            f"Perimeter: {self.perimeter()}\n"
            f"shape: {shape}"
        )


class Triangle(Shape):
    def __init__(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def __str__(self):
        shape = self.__class__.__name__
        return (
            f"Area of Triangle ({self.side1},{self.side2},{self.side3}) is {self.area()}\n"
            f"Perimeter: {self.perimeter()}\n"
            f"shape: {shape}"
        )


if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print(rect)
    print("--------------")
    cir = Circle(7)
    print(cir)
    print("--------------")
    tri = Triangle(3, 4, 5)
    print(tri)

    print("--------------")
    # Equality check
    if rect == cir:
        print("Areas are equal")
    elif rect == tri:
        print("Areas are equal")
    elif cir == tri:
        print("Areas are equal")
    else:
        print("Areas are not equal")

    print("--------------")
    total_area = rect + cir
    print(f"Total Area of Shapes = {total_area}")
