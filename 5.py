revenues = float(input("Введите выручку за текущий период: "))
expenses = float(input("Введите расходы за текущий период: "))

profit = revenues - expenses

if profit > 0:
    rent = (profit / revenues) * 100
    print(
        f"Ваша организация отработала в плюс. Рентабельность составила {rent:.2f}%")
    employees = int(input("Введите количество сотрудников: "))
    rev_employe = profit / employees
    print(f"Прибыль в расчете на сотрудника составила {rev_employe:.2f} у.е.")
elif profit < 0:
    print(
        f"Ваша организация отработала в минус. Сожалеем. Скорее всего ваша ставка будет сокращена.")
else:
    print(f"Внезапно ваша организация отработала в ноль. Можете загадать желание")
