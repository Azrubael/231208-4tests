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


def save_result(path, data):
    from datetime import datetime

    ms = round(datetime.now().timestamp() * 1e4)
    save_path = path + 'output_' + str(ms) + '.json'
    print('Шлях до записуваного файлу', save_path)

    try:
        with open(save_path, 'w') as f:
            json.dump(data, f, indent=2)
    except:
        print('Помилка під час запису в файл', save_path)