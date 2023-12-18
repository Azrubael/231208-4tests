import json
import os


def check_n_read(path):
    pwd = os.getcwd()
    full_path = pwd + '/' + path
    if os.path.exists(full_path):
        print('Шлях до зчитуваного файлу', full_path)
    else:
        print('Не можу знайти файл', full_path)
    try:
        with open(full_path, 'r') as f:
            return json.load(f)
    except:
        print('Помилка зчитування файла', full_path)


input_path = '4th/input/poll.json'
check_n_read(input_path)