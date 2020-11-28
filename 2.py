class MyOwnException(Exception):
    def __init__(self, text):
        self.text = text


try:
    value_1, value_2 = map(float, input(
        "Введите два числа через пробел. Подтвердите ввод нажатием Enter ").split())
    if value_2 == 0:
        raise MyOwnException('Второе число не может быть нулем')
except ValueError as e:
    print(e)
except MyOwnException as my_exception:
    print(my_exception)
else:
    print(value_1 / value_2)
