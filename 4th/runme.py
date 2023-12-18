from storage_svc import check_n_read, save_result


# Змінна для буферізації сценарію
DATA = {}


def DFS(pointer, stack):
    current_node = None
    children = None
    process = DATA['process']
    print(process)
    for item in process:
        if item.get('node') == pointer:
            current_node = item
            children = len(item.get('nextNode'))
            stack.append(item['node'])
            break
    if children == 0:
        stack.append['END']
        return stack
    for i in range(children-1):
        DFS(current_node['nextNode'][i], stack)
        if children == 0:
            stack.append['END']
            return stack
    print(f"It was found a node {current_node}, with {children} children")


    return stack


def path_list(expl_array):
    pass



if __name__ == '__main__':
    input_path = '4th/input/poll.json'
    output_path = '4th/boutput/'
    print('Цей скріпт виконує перевірку сценарія опитання')
    DATA = check_n_read(input_path)
    
    expl_array = DFS('0',[])
    qty = len(expl_array)

    print(f'Знайдено {qty} унікальних ланцюжков відповідей:\n')
    output_data = { 'Шляхи': \
            { 'Кількість': qty, 'Перелік шляхів':  path_list(expl_array)} }

    save_result(output_path, output_data)