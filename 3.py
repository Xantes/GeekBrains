def my_fun(var1: float, var2: float, var3: float):
    """
    var1 float
    var2 float
    var3 float

    return sum of 2 arguments

    """
    array = [var1, var2, var3]
    array.remove(min(array))
    array = sum(array)
    return(array)


while True:
    try:
        var_input1 = float(input("Введите 1 число: "))
        var_input2 = float(input("Введите 2 число: "))
        var_input3 = float(input("Введите 3 число: "))
    except ValueError:
        print("Введены неверные данные. Повторите ввод")
    else:
        break
print(my_fun(var_input1, var_input2, var_input3))
