# match-case with objects and classes
# match-case can be used with class instances to check an object's type and access its attributes
# This makes it easier to handle different kinds of objects using separate matching patterns

# __match_args__ defines which attributes can be matched positionally in a case pattern
# without it, pattern matching on custom objects would require keyword-style matching only
# Without __match_args__:
# case Circle(radius=radius):   # must use keyword form
# With __match_args__ = ("radius",):
# case Circle(radius):          # positional form works too


class Circle:
    __match_args__ = ("radius",)

    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    __match_args__ = ("width", "height")

    def __init__(self, width, height):
        self.width = width
        self.height = height


def check_shape(shape):
    match shape:
        case Circle(radius):
            print(f"Circle radius: {radius}")
        case Rectangle(width, height):
            print(f"Rectangle: {width} × {height}")
        case _:
            print("Unknown shape")


check_shape(Circle(10))
check_shape(Rectangle(4, 6))
