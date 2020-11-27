from abc import ABC, abstractmethod


class Cloth(ABC):
    """
    Class Cloth
    """

    def __init__(self, number):
        self.number = float(number)

    @abstractmethod
    def make_counts(self):
        pass


class Coat(Cloth):
    """
    Class Coat extends class Cloth
    """
    @property
    def make_counts(self):
        return f"Для пошива пальто {self.number:.1f} размера, потребуется {self.number/6.5 + 0.5:0.2f} метров ткани"


class Suit(Cloth):
    """
    Class Suit extends class Cloth
    """
    @property
    def make_counts(self):
        return f"Для пошива костюма на рост {self.number:.1f} см. потребуется {2 * self.number * 0.3:0.2f} сантиметров ткани"


coat = Coat(10.5)
suit = Suit(30)

print(coat.make_counts)
print(suit.make_counts)
