from heroes import Superman, SuperHero, Human
from places import Kostroma, Tokyo, Planet, Place
from media import TVNews, Media, PlanetNotifier


def save_the_place(hero: SuperHero, place: Place, media: Media):
    """
    Функция в которой мы зная класс Локации можем подобрать антогониста. Затем провести атаку, зная способности
    класса Супергерой. А затем, рассказать всему миру об успехах с помощью класса Медиа.
    """
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.making_news(place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TVNews(Superman()))
    print('-' * 20)
    save_the_place(Human('Чак Норрис'), Tokyo(), TVNews(Human('Чак Норрис')))
    print('-' * 20)
    save_the_place(Superman(), Planet([1241424.1231, 1215.1242]), PlanetNotifier(Superman()))
