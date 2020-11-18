import pytest

class Person:
    def __init__(self, a ,b):
        self.age = a
        self.net = b

    def __lt__(self, other):
        return self.age < other.age

p1 = Person(3,10)
p2 = Person(4,9)

print(p1>p2)