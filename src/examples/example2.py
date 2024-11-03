def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def capitalize_words(sentence):
    return " ".join(word.capitalize() for word in sentence.split())


def get_unique_elements(elements):
    return list(set(elements))


def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def sum_of_squares(numbers):
    return sum(num**2 for num in numbers)


def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


def count_occurrences(items, target):
    return items.count(target)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


def generate_password(length):
    import string
    import random

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(all_chars) for i in range(length))

    return password


class Product:

    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Product ID: {self.id}")
        print(f"Product Price: {self.price}")
        print(f"Product Quantity: {self.quantity}")

    def edit_product(self):
        self.id = int(input("Edit Product ID: "))
        self.price = int(input("Edit Product Price: "))
        self.quantity = int(input("Edit Product Quantity: "))
