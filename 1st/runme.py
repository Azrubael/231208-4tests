import json


def read_json(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def save_json(data, file_name):
    with open(file_name, 'a') as f:
        json.dump(data, f, indent=4)
        f.write('\n')


in_data = read_json('1st/input.json')
in_length = in_data['distance']['value']
rules = read_json('1st/src/conv_rules.json')
factor = rules[in_data['distance']['unit']][in_data['convert_to']]

the_result = {'unit':'','value':''}
the_result['unit'] = in_data['convert_to']
the_result['value'] = round( in_length * factor, 3)

print(the_result)
save_json(the_result, '1st/output.json')



