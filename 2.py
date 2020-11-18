try:
    with open(r"files\file_2.txt", encoding="utf-8") as r_file:
        print(
            f"Количество строк: {len(list(print(f'Количество символов: {len(array)}') for array in r_file.readlines()))}")
except Exception as e:
    print(e)
