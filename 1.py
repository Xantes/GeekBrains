try:
    with open(r"files\file_1.txt", "w", encoding="utf-8") as w_file:
        while True:
            if list(w_file.writelines(input_var + '\n') for input_var in input("Введите данные: ").split()):
                True
            else:
                break
except Exception as e:
    print(e)
