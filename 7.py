from functools import reduce


def fact(n):
    yield reduce(lambda x, y: x * y, list(el if el > 0 else 1 for el in range(n + 1)))


for el in fact(4):
    print(el)
