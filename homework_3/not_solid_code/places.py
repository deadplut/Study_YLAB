from abc import abstractmethod


class Place():
    @abstractmethod
    def get_enemy(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def get_enemy(self):
        print('Orcs hid in the forest')


class Tokyo:
    name = 'Tokyo'

    def get_enemy(self):
        print('Godzilla stands near a skyscraper')
