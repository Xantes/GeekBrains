def divide(var1: float, var2: float):
    """
    var1 float
    var2 float

    Divide var1 to var2
    """
    return var1 / var2


while True:
    try:
        var_input1 = float(input("Введите число 1: "))
        var_input2 = float(
            input("Введите число 2. Оно не может являться нулем: "))
        if var_input2 == 0:
            raise Exception("Второе число не должно быть нулем")
    except ValueError as e:
        print("Введеное вами значение не является числом")
    except Exception as e:
        print(e)
    else:
        break

print(divide(var_input1, var_input2))
