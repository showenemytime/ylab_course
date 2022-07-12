from antagonistfinder import AntagonistFinder
from weapon import Gun, Lasers, MeleeWeapon


#  Родительский класс супергероя.
class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=False):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        # Функция для поиска Антогониста на конкретной локации.
        self.finder.get_antagonist(place)

    def attack(self):
        # Функция Атаки, в зависимости от доступных классов из Weapon.
        pass

    def ultimate(self):
        # Функция Ультимативной способности, если она есть у Супергероя.
        pass


# Создаём отдельный класс Супергероя Человека, кем и является Чак Норрис. Наследуемся от оружия, которым владеет Чак
class Human(SuperHero, Gun, MeleeWeapon):

    def __init__(self, name):
        super(Human, self).__init__(name, False)

    def attack(self, use_weapon=True):

        if use_weapon:
            self.fire_a_gun()
        else:
            self.roundhouse_kick()

# Создаём Супергероя - Супермена. Он не умеет стрелять из пистолета, зато умеет в лазеры.
class Superman(SuperHero, Lasers, MeleeWeapon):

    def __init__(self):
        super(Superman, self).__init__(name='Кларк Кент', can_use_ultimate_attack=True)

    def ultimate(self):
        self.incinerate_with_lasers()

    def attack(self):
        self.roundhouse_kick()
