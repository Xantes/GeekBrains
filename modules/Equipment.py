from abc import ABC, abstractclassmethod, abstractmethod
from datetime import datetime
from json import dumps, load, loads


class Equipment():
    def __init__(self, *args):
        # self.manufacturer, self.model = manufacturer, model
        self.manufacturer, self.model, self.expendables = args

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

    @staticmethod
    def check_storage():
        try:
            with open("db\\StorageSituation.txt", encoding="utf-8") as store:
                return loads(store)
        except Exception:
            return "Error"


class Printer(Equipment):
    pass


class Scanner(Equipment):
    def __init__(self, *args):
        self.manufacturer, self.model, self.dpi = args

    def work_please(self, args):
        return f"Обьект {self.__class__.__name__} {self.manufacturer} {self.model} сканирует {args} экземпляров с разрешением {self.dpi} dpi"


class Copier(Equipment):
    def __init__(self, *args):
        self.manufacturer, self.model, self.speed = args


class MFU(Equipment):
    def __init__(self, *args):
        self.manufacturer, self.model, self.wireless = args
