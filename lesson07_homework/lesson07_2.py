from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, list_suits):
        n = 0
        for suit in list_suits:
            n += suit.consumption
        return n

coat = Coat(20)
costume = Suit(2.5)
costume_2 = Suit(2.3)
costume_3 = Suit(2.38)
costume_4 = Suit(2.12)
list_suits = [costume_4, costume_3, costume_2, costume]
print(coat.consumption)
print(costume.consumption)
print(costume.sum_consumption(list_suits))

