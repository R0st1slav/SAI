
list_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dict_of_numbers = dict.fromkeys(list_numbers, [])


"""что нужно сдедать прочитать файл по строкам и занести в список списокво в словаре
а для этого нуно итерироваться по файлу построчно и записывать строку в массив в значении словаря 
при этом ключ должен быть словаря
нужно как то итерироватьсяпо файлу с промежутком в 8 строк 
первая строка начинается с нуля значит мы считываем след восемь строк в массив нуля"""

with open('etalon', 'r') as file:
    list_file = [line.strip('\n') for line in file]


# print(dict_of_numbers)



