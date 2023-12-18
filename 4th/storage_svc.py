import json
import os


def check_n_read(path):
    if os.path.exists(path):
        print('Шлях до зчитуваного файлу', path)
    else:
        print('Не можу знайти файл', path)
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        print('Помилка зчитування файла', path)


def write_result(path, data):
        print('Шлях до записуваного файлу', path)



def is_correct(path):
    pass