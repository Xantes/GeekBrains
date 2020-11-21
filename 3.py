class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = str(name)
        self.surname = str(surname)
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    # def __init__(self, position):
    #     self.position = super(Worker).position

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


builder_worker = Position('Zak', 'Kok', 'builder', 1000, 5000)

print(builder_worker.get_full_name())
print(builder_worker.get_total_income())
