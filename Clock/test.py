from tkinter import *
from Clock.Parser import byte_dict
root = Tk()
# root.geometry('500x300')


def change_text():
    zero_number = byte_dict['zero']
    for lst1, lst2 in zip(zero_number, lbl_hours_f):
        for elem1, elem2 in zip(lst1, lst2):
            if elem1 is 1:
                elem2['text'] = '*'


def create_list_labels(frame):
    return [[Label(frame, width=2, height=1, text='.') for col in range(6)]
            for row in range(8)]


def grid_labels(labels: list):
    for row, lst in enumerate(labels):
        for col, elem in enumerate(lst):
            elem.grid(row=row, column=col)


fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
fr4 = Frame(root)
fr5 = Frame(root)

fr1.pack(side=LEFT)
fr2.pack(side=LEFT)
fr3.pack(side=LEFT)
fr4.pack(side=LEFT)
fr5.pack(side=BOTTOM)

lbl_hours_f = create_list_labels(fr1)
lbl_hours_s = create_list_labels(fr2)
lbl_minutes_f = create_list_labels(fr3)
lbl_minutes_s = create_list_labels(fr4)



btn = Button(fr5, text='fill fist', command=change_text)
btn.pack(side=LEFT)

grid_labels(lbl_hours_f)
grid_labels(lbl_hours_s)
grid_labels(lbl_minutes_f)
grid_labels(lbl_minutes_s)




root.mainloop()
