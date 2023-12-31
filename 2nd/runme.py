import json
from datetime import datetime


def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except:
        print(f'File {file_path} reading error.')


def save_json(data, file_path):
    try:
        with open(file_path, 'a') as f:
            json.dump(data, f, indent=2)
            f.write('\n')
    except:
        print(f'File {file_path} writing error.')


def include_by_keys(item, condition):
    res = False
    for i in item:
        for j in condition:
            for v in j:
                if item[i] == j[v]:
                    res = True
    return res


def exclude_by_keys(item, condition):
    res = False
    for i in item:
        for j in condition:
            for v in j:
                if item[i] == j[v]:
                    res = True
    return res


def sort_by_keys(selection, sort_by):
    sorted_selection = []
    for i in sort_by:
        print(i)
        sorted_selection = sorted(selection, key=lambda x: x[i], reverse=False)
    return sorted_selection


conditions = read_json('2nd/input/ext_conditions.json')
in_data = read_json('2nd/input/input_data.json')['data']

selection = []
include = []
exclude = []
sort_by = []
result = {}

if 'include' in conditions['condition']:
    include = conditions['condition']['include']
if 'exclude' in conditions['condition']:
    exclude = conditions['condition']['exclude']
if 'sort_by' in conditions['condition']:
    sort_by = conditions['condition']['sort_by']

if include != [] and exclude == []:
    selection = [item for item in in_data if include_by_keys(item, include)]
if exclude != [] and include == []:
    selection = [item for item in in_data if not exclude_by_keys(item, exclude)]
if exclude != [] and include != []:
    int_sel = [item for item in in_data if include_by_keys(item, include)]
    selection = [item for item in int_sel if not exclude_by_keys(item, include)]
if sort_by != []:
    selection = sort_by_keys(selection, sort_by)

result['result'] = selection
print('Your selection:')
print(json.dumps(result, indent=2))
ms = round(datetime.now().timestamp() * 1e4)
save_json(result, f'2nd/output/output_{ ms }.json')

