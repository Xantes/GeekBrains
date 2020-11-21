class Road:
    _length = float()
    _width = float()

    def __init__(self):
        self._length = float(input("Введите длину участка: "))
        self._width = float(input("Введите ширину участка: "))

    def price_per_road(self):
        self.mass = float(input("Введите массу асфальта в кг: "))
        self.height = float(input("Введите толщину слоя в см: "))
        return self._length * self._width * self.mass * self.height


lenin_street = Road()
print(lenin_street.price_per_road())
