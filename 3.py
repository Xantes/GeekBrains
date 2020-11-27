"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open(r"files\file_3.txt", encoding="utf-8") as r_file:
        print(sum(list(float(array.split()[1])
                       for array in r_file.readlines())))
        r_file.seek(0)
        list(print(f'Доход меньше 20000 у {array.split()[0]}')
             for array in r_file.readlines() if float(array.split()[1]) < 20000)
except Exception as e:
    print(e)
