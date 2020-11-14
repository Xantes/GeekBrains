array = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(list(array[el]
           for el in range(len(array)) if array.count(array[el]) == 1))
