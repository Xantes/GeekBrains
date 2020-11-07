rating_list = [7, 5, 3, 3, 2]
max_rating = rating_list[0]
min_rating = rating_list[0]

for max_digit in rating_list:
    if max_rating < max_digit:
        max_rating = max_digit
for min_digit in rating_list:
    if min_rating > min_digit:
        min_rating = min_digit

while True:
    try:
        var_input = int(
            input("Введите целое натуральное число "))
        break
    except ValueError:
        print("Неверный ввод. Введите целое натуральное число")

if var_input in rating_list:
    rating_list.insert(rating_list.index(var_input), var_input)
else:
    if var_input > max_rating:
        rating_list.insert(0, var_input)
    else:
        rating_list.append(var_input)

print(rating_list)
