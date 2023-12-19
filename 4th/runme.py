from storage_svc import check_n_read, save_result


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs_paths(node, current_path, all_paths):
    for item in DATA['process']:
        if node is None:
            return
        if item.get('node') == node:
            current_node = item
            break
    current_path.append(node)  
    if current_node['uin'] == 'Z':
        all_paths.append(current_path[:] + ['END'])
    else:
        for child in current_node['nextNode']:
            dfs_paths(child, current_path, all_paths)  
    # Backtrack: поточна нода із шляху видаляється
    current_path.pop()


# Генерація передіку відповідей
def path_list(expl_array):
    pass


# Змінна для буферізації сценарію
DATA = {}

# Ініціфлизація змінних для зберігання шляхів
all_paths = []
current_path = []

# Файли, з которими працює цей скрипт
input_file = '4th/input/poll.json'
output_file = '4th/boutput/'


print('Цей скрипт виконує перевірку сценарія опитання')
DATA = check_n_read(input_file)

dfs_paths('0',current_path, all_paths)
qty = len(all_paths)

print(f'Знайдено {qty} унікальних ланцюжков відповідей:\n')
output_data = { 'Шляхи': \
        { 'Кількість': qty, 'Перелік шляхів':  path_list(all_paths)} }

for p in all_paths:
    print(p)

save_result(output_file, output_data)