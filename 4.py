number = 1

var_input_string = str(input("Введите строку: "))

var_input_string = var_input_string.replace('  ', ' ')
str_array = var_input_string.split()

for var_str in str_array:
    print(f"{number} : {var_str[:10]}")
    number += 1
