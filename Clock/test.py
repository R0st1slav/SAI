from tkinter import *
from Clock.Parser import byte_dict, dict_numbers
from collections import Counter
import random
import datetime


def what_number(wrong_number_lbl):
    dict_of_wrong_numbers = {elem: [] for elem in dict_numbers.keys()}
    for key in dict_numbers.keys():
        number_check = []
        for lst1, lst2 in zip(wrong_number_lbl, dict_numbers[key]):
            for elem1, elem2 in zip(lst1, lst2.strip(' ')):
                if elem1 == '*' and elem2 == '*':
                    number_check.append(True)
                else:
                    number_check.append(False)
        dict_of_wrong_numbers[key] = Counter(number_check)[True]
    print(dict_of_wrong_numbers)
    return max(dict_of_wrong_numbers, key=dict_of_wrong_numbers.get)


def recognize_number(labels):
    number_lbl = []
    for lst in labels:
        temp = []
        for elem in lst:
            temp.append(elem.cget('text'))
            temp.append(' ')
        temp.pop()
        number_lbl.append(''.join(temp))

    return what_number(number_lbl)


def recognize_time():
    numbers = {key: number for key, number in zip(dict_numbers.keys(), range(10))}
    hour_f = recognize_number(lbl_hours_f)
    hour_s = recognize_number(lbl_hours_s)
    minutes_f = recognize_number(lbl_minutes_f)
    minutes_s = recognize_number(lbl_minutes_s)
    print('Распознанное')
    print(hour_f, hour_s)
    print(minutes_f, minutes_s)

    lbl_Time['text'] = f'{numbers.get(hour_f)}{numbers.get(hour_s)}:{numbers.get(minutes_f)}{numbers.get(minutes_s)}'


def broken_number(random_number, label):
    for lst in byte_dict[random_number]:
        lst: list
        random_place = random.randrange(len(lst))
        random_elem = lst[random_place]
        if random_elem is not 1:
            lst.insert(random_place, random_elem)

    for lst1, lst2 in zip(byte_dict[random_number], label):
        for elem1, elem2 in zip(lst1, lst2):
            if elem1 is 1:
                elem2['text'] = '*'


def random_fill():
    list_of_keys = list(byte_dict.keys())

    hours_f = random.choice(list_of_keys[:3])
    hours_s = random.choice(list_of_keys[0:4]) if hours_f == list_of_keys[2] else random.choice(list_of_keys)
    minutes_f = random.choice(list_of_keys[0:6])
    minutes_s = random.choice(list_of_keys)

    broken_number(hours_f, lbl_hours_f)
    broken_number(hours_s, lbl_hours_s)
    broken_number(minutes_f, lbl_minutes_f)
    broken_number(minutes_s, lbl_minutes_s)
    print('Изначальное')
    print(hours_f, hours_s)
    print(minutes_f, minutes_s)


def reset_time():
    for lst1, lst2, lst3, lst4 in zip(lbl_hours_f, lbl_hours_s, lbl_minutes_f, lbl_minutes_s):
        for elem1, elem2, elem3, elem4 in zip(lst1, lst2, lst3, lst4):
            elem1['text'], elem1['fg'] = '.', 'red'
            elem2['text'], elem2['fg'] = '.', 'blue'
            elem3['text'], elem3['fg'] = '.', 'green'
            elem4['text'], elem4['fg'] = '.', 'orange'
    lbl_Time['text'] = '00:00'


def create_list_labels(frame, color):
    return [[Label(frame, width=2, height=1, text='.', font=('Helvetica', 30, 'bold'), fg=color) for _ in range(6)]
            for _ in range(8)]


def grid_labels(labels: list):
    for row, lst in enumerate(labels):
        for col, elem in enumerate(lst):
            elem.grid(row=row, column=col)


root = Tk()
fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
fr4 = Frame(root)
fr5 = Frame(root)

fr1.pack(side=LEFT)
fr2.pack(side=LEFT)
fr3.pack(side=LEFT)
fr4.pack(side=LEFT)
fr5.pack(side=LEFT)

lbl_hours_f = create_list_labels(fr1, 'red')
lbl_hours_s = create_list_labels(fr2, 'blue')
lbl_minutes_f = create_list_labels(fr3, 'green')
lbl_minutes_s = create_list_labels(fr4, 'orange')

lbl_Time = Label(fr5, text='00:00', font=('Helvetica', 30, 'bold'))
btn_random_fill = Button(fr5, text='Fill Random', command=random_fill)
btn_reset_clock = Button(fr5, text='Reset', command=reset_time)
btn_recognize_time = Button(fr5, text='Recognize time', command=recognize_time)

btn_random_fill.pack(side=BOTTOM)
btn_reset_clock.pack(side=BOTTOM)
btn_recognize_time.pack(side=BOTTOM)
lbl_Time.pack(side=BOTTOM)

grid_labels(lbl_hours_f)
grid_labels(lbl_hours_s)
grid_labels(lbl_minutes_f)
grid_labels(lbl_minutes_s)

root.mainloop()
