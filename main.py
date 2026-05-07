class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    shapes = [circle, rectangle, triangle]

    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
        print()


if __name__ == "__main__":
    main()
```

Kodda `Shape` classi asosiy class bo'lib, unga `Circle`, `Rectangle` va `Triangle` classlari qarshi. Har bir classda `area` va `perimeter` metodlari mavjud bo'lib, ularda shaklning maydoni va perimetri hisoblanadi. `main` funksiyasida uchta shakl yaratiladi va ulardan maydon va perimetri olinadi.
