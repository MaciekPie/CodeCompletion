def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else None


def modulus(a, b):
    return a % b


def power(base, exponent):
    return base**exponent


def is_equal(a, b):
    return a == b


def absolute_value(x):
    return abs(x)


def ceiling(x):
    import math

    return math.ceil(x)


def floor_value(x):
    import math

    return math.floor(x)


def square_root(x):
    import math

    return math.sqrt(x)


def sine(x):
    import math

    return math.sin(x)


def cosine(x):
    import math

    return math.cos(x)


def tangent(x):
    import math

    return math.tan(x)


def arc_sine(x):
    import math

    return math.asin(x)


def arc_cosine(x):
    import math

    return math.acos(x)


def arc_tangent(x):
    import math

    return math.atan(x)


def natural_log(x):
    import math

    return math.log(x)


def log_base_10(x):
    import math

    return math.log10(x)


def exponential(x):
    import math

    return math.exp(x)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def square_root(x):
    return x**0.5


def absolute_value(x):
    return abs(x)


def is_odd(x):
    return x % 2 == 1


def is_even(x):
    return x % 2 == 0


def meters_to_inches(val):
    return val * 39.37


def get_square_roots(numbers):
    import math

    return [math.sqrt(n) for n in numbers if n >= 0]


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * (self.radius**2)

    def circumference(self):
        import math

        return 2 * math.pi * self.radius

    def scale(self, factor):
        self.radius *= factor


def get_lengths(words):
    return map(len, words)


def calculate_area(radius):
    import math

    return math.pi * radius**2


def get_max_value(numbers):
    if not numbers:
        return None
    return max(numbers)


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def get_real(self):
        return self.real

    def get_imaginary(self):
        return self.imaginary


class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width
