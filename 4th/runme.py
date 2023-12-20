from storage_svc import check_n_read, save_result


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.children = []


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


# Генерація переліку відповідей
def path_list(all_paths):
    result = []
    next_node = None
    answer_idx = None
    question_uin = None
    question_idx = None
    questions_ctr = len(DATA.get('questions')) - 1
    for path in all_paths:
        stack = []
        for i in range(len(path)):
            if (path[i] == 'END'):
                stack.append( {DATA['questions'][questions_ctr]['body'] : DATA['questions'][questions_ctr]['answers'][0]} )
                break
            for item in DATA['process']:
                if item.get('node') == path[i]:
                    next_node = path[i+1]
                    question_uin = item.get('uin')
                    if next_node != 'END':
                        answer_idx = item['nextNode'].index(next_node)
                    elif next_node != 'END':
                        answer_idx = 0
                    break
            for j in range(questions_ctr):
                if DATA['questions'][j].get('uin') == question_uin:
                    question_idx = j
            stack.append( {DATA['questions'][question_idx]['body'] : DATA['questions'][question_idx]['answers'][answer_idx]} )
        result.append(stack[:])
    return result


# Змінна для буферізації сценарію
DATA = {}

# Ініціфлизація змінних для зберігання шляхів
all_paths = []
current_path = []

# Файли, з которими працює цей скрипт
input_file = '4th/input/poll.json'
output_file = '4th/output/'

print('Цей скрипт виконує перевірку сценарія опитання')
DATA = check_n_read(input_file)

dfs_paths('0',current_path, all_paths)
qty = len(all_paths)

print(f'Знайдено {qty} унікальних ланцюжков відповідей:\n')
output_data = { 'paths': { 'quantity': qty, 'list':  path_list(all_paths)} }

# for p in all_paths:
#     print(p)

save_result(output_file, output_data)