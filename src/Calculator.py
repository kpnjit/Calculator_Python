import math

def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result=x;
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
