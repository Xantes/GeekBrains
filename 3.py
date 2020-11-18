try:
    with open(r"files\file_3.txt", encoding="utf-8") as r_file:
        print(sum(list(float(array.split()[1])
                       for array in r_file.readlines())))
        r_file.seek(0)
        list(print(f'Доход меньше 20000 у {array.split()[0]}')
             for array in r_file.readlines() if float(array.split()[1]) < 20000)
except Exception as e:
    print(e)
