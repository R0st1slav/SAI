from tkinter import *
from Clock.Parser import byte_dict
root = Tk()
# root.geometry('500x300')


def change_text():
    zero_number = byte_dict['zero']
    for lst1, lst2 in zip(zero_number, labels):
        for elem1, elem2 in zip(lst1, lst2):
            if elem1 is 1:
                elem2['text'] = '*'


def create_list_labels(frame):
    return [[Label(frame, width=2, height=1, text='.') for col in range(6)]
            for row in range(8)]


fr1 = Frame(root)
fr2 = Frame(root)

fr1.pack()
fr2.pack(side=BOTTOM)

labels = create_list_labels(fr1)


btn = Button(fr2, text='fill fist', command=change_text)
btn.pack(side=LEFT)

for row, lst in enumerate(labels):
    for col, elem in enumerate(lst):
        elem.grid(row=row, column=col)

root.mainloop()
