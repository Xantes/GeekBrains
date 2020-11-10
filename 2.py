def pers_data(name: str, surname: str, dob: str, city: str, email: str, tel: str):
    """
    name str
    surname str
    dob str
    city str
    email str
    tel str

    return data
    """
    print(f"{name} {surname} {dob} {city} {email} {tel}")


while True:
    var_input = str(input(
        "Введите имя, фамилию, дату рождения, город, почтовый ящик и телефон через пробел: "))
    var_input = var_input.replace('  ', ' ')
    var_input = var_input.split()
    if len(var_input) == 6:
        break
    else:
        print("Неверное количество аргументов. Попробуйте еще")


pers_data(name=var_input[0], surname=var_input[1], dob=var_input[2],
          city=var_input[3], email=var_input[4], tel=var_input[5])
