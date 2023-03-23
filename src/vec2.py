# Note this module isn't heavily used and may be removed in future

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec2(self.x / scalar, self.y / scalar)
    
    @classmethod
    def from_(cls, other):
        if hasattr(other, "x") and hasattr(other, "y"):
            return Vec2(other.x, other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vec2(other[0], other[1])
        else:
            raise TypeError(f"Could not convert type {type(other)} to {type(cls)}")

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        length = self.length()
        if length == 0:
            return Vec2(0, 0)
        else:
            return Vec2(self.x / length, self.y / length)
