import json

def to_byte(dict_of_numbers: dict):
    byte_dict = {k: [] for k in dict_numbers.keys()}
    for key, value in dict_numbers.items():
        for elem in value:
            temp = []
            for char in elem:
                if char == '.':
                    temp.append(0)
                elif char == '*':
                    temp.append(1)
            byte_dict[key].append(temp)
    return byte_dict



with open('etalon.json', 'r') as file_js:
    data = json.load(file_js)
    numbers = dict(data['numbers'])
    dict_numbers = dict(zip(numbers.keys(), [elem.split('\n') for elem in numbers.values()]))
    byte_dict = to_byte(dict_numbers)



