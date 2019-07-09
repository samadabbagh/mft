class Rectangle:
    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h
    def __repr__(self):
        return """
        +-----{w:4}-----+
        |               |
        {h:4}            |
        |               |
        +------------------+
        """.format(w=self.width, h=self.height)
    def area(self):

        return self.width * self.height

    def perimeter(self):

        return self.width + self.height


class Square:
    def __init__(self, s):
        self.width = s


    def area_square(self):
        return self.width * 4

    def perimeter_square(self):

        return self.width + 4


t = Rectangle(6, 9)
t.area()
print(t.area())
print(t)


r = Square(5)
r.area_square()
print(r.area_square())
