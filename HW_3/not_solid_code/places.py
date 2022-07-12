from abc import ABC, abstractmethod

from typing import List




# Родительский класс для создания Локаций с абстрактным методом на запрос врага.
class Place(ABC):

    @abstractmethod
    def get_enemy(self):
        pass

# Дочерний класс конкретной локации.
class Kostroma(Place):
    city_name = 'Кострома'

    def get_orcs(self):
        print('Орки вышли из лесов Костромы!')

    def get_enemy(self):
        self.get_orcs()

# Дочерний класс конкретной локации.
class Tokyo(Place):
    city_name = 'Токио'

    def get_godzilla(self):
        print('Годзила вышла из воды и нападает на Токио!')

    def get_enemy(self):
        self.get_godzilla()



# Дочерний класс для другой планеты, чтобы проверить отправку новостей с координатами.
class Planet(Place):

    def __init__(self, coordinates: List[float]):
        self.coordinates = coordinates

    def get_alien(self):
        print('Пришельцы атакуют!')

    def get_enemy(self):
        self.get_alien()
