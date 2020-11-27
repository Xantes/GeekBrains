class Cell():
    """
    Class Cell
    """

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number > other.number:
            return self.number - other.number
        else:
            return "Нельзя вычесть меньшее из большего"

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number // other.number

    def make_order(self, cols):
        return ('*' * (cols) + '\n') * (self.number // cols) + '*' * (self.number % cols)


cell_1 = Cell(3)
cell_2 = Cell(10)
cell_3 = cell_1 + cell_2

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_2.make_order(4))
