class MyOwnException(Exception):
    def __init__(self, text):
        self.text = text


arr = []
while True:
    try:
        var = input(
            "Вводите данные для формирование списка из чисел. :q для выхода ")
        if var == ':q':
            break
        if var.isalpha():
            raise MyOwnException(f"{var} не является числом")
    except MyOwnException as err:
        print(err)
    else:
        arr.append(float(var))
    finally:
        print(arr)
