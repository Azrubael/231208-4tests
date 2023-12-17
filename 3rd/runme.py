import random
import json
from threelateracy import ThreeLateracy


# Простір для моделювання обмежений кубом зі стороною
CUBESIDE = 100


def gen():
    """ Генерування випадкового числа у заданому діапазоні з точністю трьох знаків """
    return round(random.random()*(CUBESIDE + 1), 3)


def search(coords):
    """ Функція для розрахування відстані до шукомої точки
        'INPUT.init.random_pt' """
    result = ( \
        (INPUT['init']['random_pt']['X'] - coords['X'])**2 + \
        (INPUT['init']['random_pt']['Y'] - coords['Y'])**2 + \
        (INPUT['init']['random_pt']['Z'] - coords['Z'])**2 )**0.5
    return result


# Оголошення структури даних для фіксації даних пошуку
INPUT = {
    'init': {
        'random_pt': {'X': gen(), 'Y': gen(), 'Z': gen()},
        'try_pts': [
            {'X': gen(), 'Y': gen(), 'Z':gen(), 'dist': 0},
            {'X': gen(), 'Y': gen(), 'Z': gen(), 'dist': 0},
            {'X': gen(), 'Y': gen(), 'Z': gen(), 'dist': 0},
            # {X: CUBESIDE, Y: 0, Z: 0, dist: 0},   # для перевірки обчислювань
            # {X: 0, Y: CUBESIDE, Z: 0, dist: 0},   # для перевірки обчислювань
            # {X: 0, Y: 0, Z: CUBESIDE, dist: 0},   # для перевірки обчислювань
        ]
    }
}


# print(json.dumps(INPUT, indent=2))

for e in range(len(INPUT['init']['try_pts'])):
    dist = round(search(INPUT['init']['try_pts'][e]), 6)
    INPUT['init']['try_pts'][e]['dist'] = dist

estimate = ThreeLateracy(INPUT['init']['try_pts'], CUBESIDE)

i = 0
if len(estimate) == 1:
    print("Шукана точка знайдена на перетині сфер, утворених \
          трьома радіусами 'dist'")
    print('Координати довільно заданої точки:')
elif len(estimate) == 2:
    print("Розрахунки кажуть про дві ймовірні точки в просторі ", \
        "розміром {CUBESIDE}x{CUBESIDE}, тож виконана додаткова перевірка.")
    check = search(estimate[i])
    INPUT['init']['try_pts'].append( { \
        'X': estimate[i]['X'], \
        'Y': estimate[i]['Y'], \
        'Z': estimate[i]['Z'], 'dist': round(check, 6)} )
    if ( check > 0.0e6 ):
        i += 1
        INPUT['init']['try_pts'].append( { \
                'X': estimate[i]['X'], \
                'Y': estimate[i]['Y'], \
                'Z': estimate[i]['Z'], 'dist': round(search(estimate[i]), 6)} )
    print("Результат додатковго розрахунку: ")
    
print(estimate[i])
print(f"Всього для пошуку координат шуканої точки знадобилося \
      {len(INPUT['init']['try_pts'])} ітерацій")

print()
print("Перевірка: ")
print(json.dumps(INPUT, indent=2))