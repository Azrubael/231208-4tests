from storage_svc import check_n_read, write_result


input_path = './input/poll.json'
output_path = './output/output.json'


# Вказівник на корінь дерева сценарію
START = '0'


def DFS(in_data):
    return []


def path_list():
    pass



print('Цей скріпт виконує перевірку сценарія опитання')
in_data = check_n_read(input_path)
expl_array = DFS(in_data)


qty = len(expl_array)
print(f'Знайдено {qty} унікальних ланцюжков відповідей:\n')
output_data = { 'Шляхи': { 'Кількість': qty, 'Перелік шляхів':  path_list} }

write_result(output_path, output_data)