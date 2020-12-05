from datetime import datetime as dt


class Data():
    def __init__(self, date):
        Data.date = date

    @classmethod
    def data_to_int(cls):
        return [int(el) for el in cls.date.split('-')]

    @staticmethod
    def data_validate(input_var):
        try:
            dt.strptime(input_var, '%d-%m-%Y')
        except Exception:
            return "Неверный формат даты. Повторите ввод в формате ДД-ММ-ГГГГ"
        else:
            return True


a_1 = Data('21-10-2003')

print(a_1.data_to_int())
print(Data.data_validate('20-12-2000'))
