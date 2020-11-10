def sum_args(vars, sum_vars=0):

    for var in vars:
        if var != ":q":
            try:
                float(var)
            except ValueError:
                print(f"{var} не является числом")
            else:
                sum_vars += float(var)
        else:
            print(sum_vars)
            exit(0)

    print(sum_vars)
    ask_args(sum_vars)
    return 1


def ask_args(last_sum=0):
    var_input = (
        input("Введите числа через пробел. Для завершения ввода наберите :q "))
    var_input = var_input.replace('  ', ' ')
    var_input = var_input.split()

    sum_args(var_input, last_sum)


ask_args()
