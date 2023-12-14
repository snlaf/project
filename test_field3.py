import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="Введите функцию:")
        self.label.pack()

        self.dim_var = tk.StringVar(value='2D')

        self.dim_option = tk.OptionMenu(self, self.dim_var, '2D', '3D')
        self.dim_option.pack()

        self.entry = tk.Entry(window)
        self.entry.pack()

        self.button = tk.Button(text="Построить график", command=self.plot_function)
        self.button.pack()

    def plot_function(self):
        function = self.entry.get()
        x = np.linspace(-10, 10, 400)
        y = eval(function)

        funct = function
        if funct is None:
            self.show_error("Неверный выбор")
            return
        value = self.entry
        if value is None:
            self.show_error("Неверное значение")
            return

        dim = self.get_dimensionality()
        if dim is None:
            self.show_error("Неверный выбор")
            return

        if dim == '2D':
            self.plot_function_2d(funct, value)
        else:
            self.plot_function_3d(funct, value)

        figure = Figure(figsize=(5, 4), dpi=100)
        plot = figure.add_subplot(111)
        plot.plot(x, y)

        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def get_dimensionality(self):
        return self.dim_var.get()

    def plot_function_2d(self, func, value):
        fig, ax = plt.subplots()
        X = np.linspace(-np.pi, np.pi, 256)
        Y = func(value * X)
        ax.plot(X, Y)

        ax.set_title("Функция")
        ax.set_xlabel("X координата")
        ax.set_ylabel("Y координата")
        plt.show()

    def plot_function_3d(self, func, value):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X = np.linspace(-np.pi, np.pi, 1000)
        Y = np.linspace(-np.pi, np.pi, 1000)
        X, Y = np.meshgrid(X, Y)
        Z = func(value * np.sqrt(X ** 2 + Y ** 2))
        ax.plot_surface(X, Y, Z, cmap='plasma')

        ax.set_title("Функция")
        ax.set_xlabel("X координата")
        ax.set_ylabel("Y координата")
        ax.set_zlabel("Z координата")
        plt.show()


window = tk.Tk()
window.title("Функция")
app = Application(master=window)
app.mainloop()