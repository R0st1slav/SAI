from tkinter import *


class Classification(Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.draw_red)
        self.canvas.bind("<Button-3>", self.draw_green)
        self.arr_green = []
        self.arr_red = []
        self.btn_draw = Button(self.root, text='draw_line', command=self.draw_line)
        self.btn_draw.pack(side=BOTTOM)

    def draw_red(self, event):
        pos1 = event.x - 10, event.y - 10
        pos2 = event.x + 10, event.y + 10
        self.arr_red.append(pos1)
        self.canvas.create_oval(pos1, pos2, fill='red')

    def draw_green(self, event):
        pos1 = event.x - 10, event.y - 10
        pos2 = event.x + 10, event.y + 10
        self.arr_green.append(pos1)
        self.canvas.create_oval(pos1, pos2, fill='green')

    def draw_line(self):
        if self.arr_green != [] and self.arr_red != []:
            x1 = 0
            y1 = 0
            for x, y in self.arr_green:
                x1 += x
                y1 += y
            x2 = 0
            y2 = 0
            for x, y in self.arr_red:
                x2 += x
                y2 += y
            X = (x1 // len(self.arr_green) + x2 // len(self.arr_red)) // 2
            Y = (x1 // len(self.arr_green) + x2 // len(self.arr_red)) // 2
            self.canvas.create_line(0, self.root.winfo_height(), X, Y)
            k = (self.root.winfo_height() - Y) / (0 - X)
            b = Y - k * X
            y = k * self.root.winfo_width() + b
            self.canvas.create_line(X, Y, self.root.winfo_width(), y)


if __name__ == '__main__':
    root = Tk()
    app = Classification(root)
    app.mainloop()
