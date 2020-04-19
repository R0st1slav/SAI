from tkinter import *
import numpy as np

"""
рисуется массив кнопок
кнопка нажимается на ней меняется текст
этот текст считывается с кнопки


"""


class Application(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry('500x300')
        self.init_menu()

    def init_menu(self):
        self.f_top = Frame(self.root)
        self.f_bot = Frame(self.root)
        self.f_top.pack()
        self.f_bot.pack()
        self.labels = [[Label(self.f_top, width=2, height=1, text='.').grid(row=row, column=col)
                        for col in range(24)] for row in range(8)]

        self.recognize_time_button = Button(self.f_bot, text='recognize time')
        self.fill_time = Button(self.f_bot, text='fill time')
        self.recognize_time_button.pack(side=LEFT)
        self.fill_time.pack(side=LEFT)

    """Заполняет лейблы случайными данными при этом не правильными"""
    def fill_time(self):
        pass


    def recognize_time(self):
        pass



root = Tk()
app = Application(root)
app.mainloop()
