var_list = list()
i = 0

while True:
    try:
        var_list_length = int(
            input("Введите желаемое количество элементов для заполнения: "))
        break
    except ValueError:
        print("Введеные вами данные не являются числом")

while i != abs(var_list_length):
    var_list.append(input("Введите значение под индексом %i: " % i))
    i += 1
i = 0

while i <= var_list_length:
    try:
        var_list[i + 1]
    except IndexError:
        break
    else:
        var_list[i], var_list[i + 1] = var_list[i + 1], var_list[i]
    i += 2

print(var_list)
