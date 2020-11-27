"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

try:
    with open(r"files\file_5.txt", "r+", encoding="utf-8") as wr_file:
        try:
            list(wr_file.write(input_var + '\n')
                 for input_var in input("Введите данные: ").split())
        except ValueError as e:
            print(e)
        print(sum(list(int(array) for array in wr_file.readlines())))
except Exception as e:
    print(e)
