import json


def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except:
        print(f'File {file_path} reading error.')



def save_json(data, file_path):
    try:
        with open(file_path, 'a') as f:
            json.dump(data, f, indent=4)
            f.write('\n')
    except:
        print(f'File {file_path} writing error.')



in_data = read_json('1st/input.json')
in_length = in_data['distance']['value']
rules = read_json('1st/src/conv_rules.json')
factor = rules[in_data['distance']['unit']][in_data['convert_to']]

the_result = {'unit':'','value':''}
the_result['unit'] = in_data['convert_to']

try:
    the_result['value'] = round( in_length * factor, 3)
except:
    print(f'Calculation error during multipy {in_length} and {factor}')

print(f'Output result: {the_result}')
save_json(the_result, '1st/output.json')
