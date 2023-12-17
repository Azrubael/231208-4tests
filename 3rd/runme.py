import random
import json
import math


# Простір для моделювання обмежений кубом зі стороною
CUBESIDE = 100


def gen():
    """ Генерування випадкового числа у заданому діапазоні з точністю трьох знаків """
    return round(random.random()*(CUBESIDE + 1), 3)


def search(coords):
    """ Функція для розрахування відстані до шукомої точки
        'INPUT.result.random_point' """
    result = math.sqrt( \
        (INPUT['initial']['random_point']['X'] - coords['X'])**2 + \
        (INPUT['initial']['random_point']['Y'] - coords['Y'])**2 + \
        (INPUT['initial']['random_point']['Z'] - coords['Z'])**2
    )
    return result


# Оголошення структури даних для фіксації даних пошуку
INPUT = {
    'initial': {
        'random_point': {'X': gen(), 'Y': gen(), 'Z': gen()},
        'search_points': [
            {'X': gen(), 'Y': gen(), 'Z':gen(), 'dist': 0},
            {'X': gen(), 'Y': gen(), 'Z': gen(), 'dist': 0},
            {'X': gen(), 'Y': gen(), 'Z': gen(), 'dist': 0},
            # {X: CUBESIDE, Y: 0, Z: 0, dist: 0},   # для перевірки обчислювань
            # {X: 0, Y: CUBESIDE, Z: 0, dist: 0},   # для перевірки обчислювань
            # {X: 0, Y: 0, Z: CUBESIDE, dist: 0},   # для перевірки обчислювань
        ],
    'calls': 3
    }
}


print(json.dumps(INPUT, indent=2))


for i in range(len(INPUT['initial']['search_points'])):
    INPUT['initial']['search_points'][i]['dist'] = search(INPUT['initial']['search_points'][i])


print(json.dumps(INPUT, indent=2))