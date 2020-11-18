with open(r"files\file_2.txt", "r", encoding="utf-8") as c_file:
    array = c_file.readlines()
    print(f"Количество строк {len(array)}")
    for rows in array:
        print(f"Количество символов: {len(rows)}")
