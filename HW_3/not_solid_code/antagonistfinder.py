
from places import Place

# Класс, который получает локацию и говорит вернуть Врага с этой локации.
class AntagonistFinder:

    @staticmethod
    def get_antagonist(place: Place):
        place.get_enemy()
