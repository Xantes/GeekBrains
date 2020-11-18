# with open(r"files\file_3.txt", encoding="utf-8") as c_file:
#     avg = []
#     for rows in c_file.readlines():
#         row = rows.split()
#         try:
#             print(f"{row[0]} получает меньше 20000.") if int(
#                 row[1]) < 20000 else False
#             avg.append(int(row[1])) if int(row[1]) > 0 else False
#         except ValueError as e:
#             pass
# print(f"Средняя заработная плата: {sum(avg) / len(avg)}")

try:
    with open(r"files\file_3.txt", encoding="utf-8") as r_file:
        print(sum(list(int(array.split()[1])
                       for array in r_file.readlines())))
        list(print(f'Доход меньше 20000 у {array.split()[0]}')
             for array in r_file.readlines() if int(array.split()[1]) < 20000)
except Exception as e:
    print(e)
