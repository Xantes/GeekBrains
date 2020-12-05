from abc import ABC


class Organisation(ABC):
    def __init__(self, name, headof):
        self.name, self.headof = name, headof

    def __str__(self):
        return f"Помещение {self.name}. Ответственным лицом является {self.headof}"


class Workplace(Organisation):
    pass


class PrinterRoom(Organisation):
    pass
