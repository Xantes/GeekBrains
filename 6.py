main_array_length = 0
counter = 1
main_array = list()
second_array_values = list()
second_array = {}

while main_array_length <= 1:
    try:
        main_array_length = int(
            input("Введите количество товаров: "))
    except ValueError:
        print("Неверный ввод. Количество товаров должно являться целым натуральным числом отличным от 0")
while counter <= main_array_length:
    good_name = str(input("Введите наименование товара: "))
    good_price = int(input("Введите цену товара: "))
    good_quantity = int(input("Введите количество товара: "))
    good_mark = str(input("Введите единицу измерения: "))
    good = {"Название": good_name, "Цена": good_price,
            "Количество": good_quantity, "Единица измерения": good_mark}
    tuple_array = (counter, good)
    main_array.append(tuple_array)
    counter += 1


for key in main_array[0][1].keys():
    counter = 0
    second_array_values.clear()
    while counter < main_array_length:
        second_array_values.append(main_array[counter][1].get(key))
        counter += 1
    second_array[key] = second_array_values

print(second_array)
