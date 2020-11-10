def strange_abs(x: float, y: int):
    """
    x float
    y float

    return abs of x and y
    """
    def sol1(sol1_x=x, sol1_y=y):
        return(sol1_x ** sol1_y)

    def sol2(sol2_x=x, sol2_y=y):
        pow2_x = sol2_x
        while abs(sol2_y) >= 2:
            pow2_x = pow2_x * sol2_x
            sol2_y += 1
        return(1 / pow2_x)

    return(sol1(), sol2())


while True:
    try:
        var_input1 = float(
            input("Введите действительное положительное число: "))
        var_input2 = int(input("Введите целое отрицательное число: "))

        if var_input1 <= 0 or var_input2 >= 0:
            raise Exception("Введены неверные данные. Повторите ввод")

    except ValueError:
        print("Неверный формат данных")
    except Exception as e:
        print(e)
    else:
        break

print(strange_abs(var_input1, var_input2))
