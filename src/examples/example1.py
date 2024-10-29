import math


def add_numbers(a, b):
    return a + b


def subtract(a, b):
    diff = a - b
    return diff


def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def get_square_roots(numbers):

    return [math.sqrt(n) for n in numbers if n >= 0]


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return math.pi * (self.radius**2)

    def circumference(self):

        return 2 * math.pi * self.radius

    def scale(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    result = add_numbers(10, 20)
    print("Sum:", result)

    numbers = [1, 2, 3, 4, 5, 6]
    evens = filter_even_numbers(numbers)
    print("Even numbers:", evens)

    circle = Circle(5)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())
