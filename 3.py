months_list = ("Январь", "Февраль", "Март", "Апрель", "Май",
               "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
months_dict = {}
var_used_solution = 0
var_month_number = 0

for number, month in enumerate(months_list):
    months_dict[number + 1] = month
while not var_month_number in range(1, 12):
    try:
        var_month_number = int(input("Введите номер месяца: "))
    except ValueError:
        print("Введеные вами данные не являются числом")

while not var_used_solution in (1, 2):
    try:
        var_used_solution = int(
            input("Выберите вариант решения. 1 - через list, 2 - через dict. "))
    except ValueError:
        print("Неверный вариант решения")

print(months_list[var_month_number - 1]
      ) if var_used_solution == 1 else print(months_dict[var_month_number])
