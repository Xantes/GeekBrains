class Stationery():
    title = str()

    def draw(self):
        return f"Метод отрисовки"


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Пишем аккуратную строку с помощью инструмента {self.title}"


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Делаем набросок портрета с помощью инструмента {self.title}"


class Handle(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Жирно выделяем интересующие строки в статье с помощью инструмента {self.title}"


pen = Pen('Черная ручка')
print(pen.draw())
pencil = Pencil('Цветной карандаш')
print(pencil.draw())
handle = Handle('Черный перманентный маркер')
print(handle.draw())
