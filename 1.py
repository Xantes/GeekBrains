main_var = list()
var_dict = {}

main_var.append(int(1))
main_var.append(float(2.0))
main_var.append(complex(1, 5))
main_var.append(str("Строка"))
main_var.append(list(main_var))
main_var.append(tuple(main_var))

# делаем так, чтобы список не попадал в множество, иначе выкидывает ошибку. Подумать, как избавить от этого
main_var.append(set(main_var.pop(4)))

# заполняем словарь
for i in main_var:
    var_dict[type(i)] = i
del i

main_var.append(var_dict)
main_var.append(bool(False))
main_var.append(bytes('Some byte', encoding="cp1251"))
main_var.append(None)
main_var.append(Exception(EOFError))

for i in main_var:
    print(type(i))
