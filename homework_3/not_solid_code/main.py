from typing import Union
from heroes import Superman, SuperHero, Media, ChackNorris
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], media: Media, news):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(hero.name, news, hero.place.name)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), Media(), 'TV')
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), Media(), 'Radio')
