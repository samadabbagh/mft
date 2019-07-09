class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def add_vectors(a, b):
    x_new = a.x + b.x
    y_new = a.y + b.y
    return Vector(x_new, y_new)


v1 = Vector(3, 4)
v2 = Vector(10, 1)
v3 = add_vectors(v1, v2)
v3 = add_vectors(v3, v3)

print(v3.x, v3.y)