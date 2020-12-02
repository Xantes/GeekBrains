from abc import ABC, abstractclassmethod, abstractmethod
from datetime import datetime
from json import dumps


class Equipment(ABC):
    def __init__(self, manufacturer, model):
        self.manufacturer, self.model = manufacturer, model

    def __str__(self):
        return f"{self.__class__.__name__, self.model, self.manufacturer}"

    def work_please(self, args):
        return f"Объект {self.__class__.__name__} {self.manufacturer} {self.model} печатает в количестве {args} экземпляров"

    def receive_equipment(self, quantity):
        self.quantity = quantity
        self.datetime = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        self.direction = "Receive"
        try:
            with open("db\\StorageSituation.txt", "a", encoding="utf-8") as store:
                print(dumps(self.__dict__, indent=4, sort_keys=True), file=store)
        except Exception as e:
            return e

    def issue_equipment(self, room, quantity):
        self.quantity = quantity
        self.datetime = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        self.direction = "Issue"
        self.room = room.name
        self.owner = room.headof
        try:
            with open("db\\StorageSituation.txt", "a", encoding="utf-8") as store:
                print(dumps(self.__dict__, indent=4, sort_keys=True), file=store)
        except Exception as e:
            return e


class Printer(Equipment):
    def __init__(self, manufacturer, model, expendables):
        self.expendables = expendables
        super(Printer, self).__init__(manufacturer, model)


class Scanner(Equipment):
    def __init__(self, manufacturer, model, dpi):
        self.dpi = dpi
        super(Scanner, self).__init__(manufacturer, model)

    def work_please(self, args):
        return f"Обьект {self.__class__.__name__} {self.manufacturer} {self.model} сканирует {args} экземпляров с разрешением {self.dpi} dpi"


class Copier(Equipment):
    def __init__(self, manufacturer, model, speed):
        self.speed = speed
        super(Copier, self).__init__(manufacturer, model)


class MFU(Equipment):
    def __init__(self, manufacturer, model, wireless):
        self.wireless = wireless
        super(MFU, self).__init__(manufacturer, model)
