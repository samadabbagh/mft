class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y

        return Vector(x_new, y_new)

    def __sub__(self, other):
        x_sub = self.x - other.x
        y_sub = self.y - other.y

        return Vector(x_sub, y_sub)

    def __neg__(self):
        return Vector(-self.x, -self.y)


v1 = Vector(3, 4)
v2 = Vector(10, 1)
v3 = v1 + v2 + v1 + v2 + v2
v4 = v2 - v1

print(v4.x, v4.y)
print(v3.x, v3.y)
