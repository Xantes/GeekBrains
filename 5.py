from functools import reduce

print(reduce(lambda x, y: x * y, list(el for el in range(100, 1000+1) if el % 2 == 0)))
