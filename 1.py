matrix_1 = [[1, 2, 3, 4], [2, 4, 6, 8], [1, 0, 5, 6]]
matrix_2 = [[2, 6, 3, 4], [5, 2, 9, 6], [6, 3, 9, 4]]

example_array = [1, 2, 4, 5]


class Matrix():
    """
    Matrix Class
    """

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return [[sum(elements) for elements in zip(*values)] for values in zip(self.data, other.data)]

    def __str__(self):
        return '\n'.join('\t'.join(str(el) for el in array) for array in self.data)


object_1 = Matrix(matrix_1)
object_2 = Matrix(matrix_2)

print(object_1)

print(object_1 + object_2)
