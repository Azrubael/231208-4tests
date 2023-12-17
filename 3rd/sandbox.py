import json
import random
from types import SimpleNamespace


CUBESIDE = 100


def gen():
    """ Генерування випадкового числа у заданому діапазоні з точністю трьох знаків """
    return round(random.random()*(CUBESIDE + 1), 3)


INPUT = {
    'initial': {
        'random_point': {'X': gen(), 'Y': gen(), 'Z': gen()},
        'search_points': [
            {'X': gen(), 'Y': gen(), 'Z':gen(), 'dist': 0},
            {'X': gen(), 'Y': gen(), 'Z': gen(), 'dist': 0},
            {'X': gen(), 'Y': gen(), 'Z': gen(), 'dist': 0},
        ],
    'calls': 3
    }
}

input = SimpleNamespace(**INPUT)

print(input.initial)
# print(json.dumps(INPUT, indent=2))
