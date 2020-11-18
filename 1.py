
# try:
#     with open(r"files\file_1.txt", "w", encoding="utf-8") as c_file:
#         while True:
#             input_var = str(input("Введите данные: "))
#             if input_var:
#                 c_file.write(input_var + '\n')
#             else:
#                 break
# except Exception as e:
#     print(e)

try:
    with open(r"files\file_1.txt", "w", encoding="utf-8") as w_file:
        while True:
            if list(w_file.write(input_var + '\n') for input_var in input("Введите данные: ").split()):
                True
            else:
                break
except Exception as e:
    print(e)
