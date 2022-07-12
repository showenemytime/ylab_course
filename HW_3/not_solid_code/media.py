from abc import ABC, abstractmethod
from places import Place, Planet
from heroes import SuperHero

# Создаём родительский класс Медия с абстрактным методом Мэйкинг Ньюс.
class Media(ABC):

    def __init__(self, hero: SuperHero):
        self.hero_name = getattr(hero, "name")

    @abstractmethod
    def making_news(self, place: Place):
        pass

# Дочерний класс для новостей на планете Земля.
class TVNews(Media):

    def __init__(self, hero: SuperHero):
        super(TVNews, self).__init__(hero)

    def making_news(self, place: Place):
        # Функция для отправки новости о победе Супергероя.
        place_name = getattr(place, 'city_name')
        print(f"Срочные новости: {self.hero_name} одержал победу в локации {place_name}!")



# Дочерний класс для другие планет.
class PlanetNotifier(Media):

    def __init__(self, hero: SuperHero):
        super(PlanetNotifier, self).__init__(hero)

    def making_news(self, planet: Planet):
        # Функция для отправки новости о победе Супергероя.
        planet_coordinates = getattr(planet, 'coordinates')
        print(f"{self.hero_name} одержал победу. Планета с координатами {planet_coordinates} освобождена!")
