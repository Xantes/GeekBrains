class ComplexNumber():
    """
    Class ComplexNumber
    """

    def __init__(self, x, y):
        self.number = complex(x, y)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


a1 = ComplexNumber(3, 2)
a2 = ComplexNumber(4, 12)

print(a1 + a2)
print(a1 * a2)
