import json

with open('etalon.json', 'r') as file_js:
    data = json.load(file_js)
    numbers = dict(data['numbers'])
    dict_numbers = dict(zip(numbers.keys(), [elem.split('\n') for elem in numbers.values()]))