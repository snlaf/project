import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self)
        self.label["text"] = "Выберете функцию из списка 'sin', 'cos', 'tan', 'ctg', 'exp', 'log', 'x', 'x^2', 'sqrt(x)', 'custom':"
        self.label.pack(side="top")

        self.func_var = tk.StringVar(value='sin')

        self.func_option = tk.OptionMenu(self, self.func_var, 'sin', 'cos', 'tan', 'ctg', 'exp', 'log', 'x', 'x^2',
                                         'sqrt(x)', 'custom')
        self.func_option.pack(side="top")

        self.dim_label = tk.Label(self)
        self.dim_label["text"] = "Выберете измерение функции:"
        self.dim_label.pack(side="top")

        self.dim_var = tk.StringVar(value='2D')

        self.dim_option = tk.OptionMenu(self, self.dim_var, '2D', '3D')
        self.dim_option.pack(side="top")

        self.value_label = tk.Label(self)
        self.value_label["text"] = "Введите значение функции:"
        self.value_label.pack(side="top")

        self.value_entry = tk.Entry(self.master)
        self.value_entry.pack(side="top")

        self.custom_func_entry = tk.Entry(self.master)
        self.custom_func_entry.pack(side="top")

        self.plot_button = tk.Button(self)
        self.plot_button["text"] = "Построить график"
        self.plot_button["command"] = self.plot_function
        self.plot_button.pack(side="top")

        self.quit_button = tk.Button(self, text="Выйти", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def get_function(self):
        choice = self.func_var.get()
        functions = {
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'ctg': self.funct_ctg,
            'exp': np.exp,
            'log': np.log,
            'x': self.funct_x,
            'x^2': self.funct_x_squared,
            'sqrt(x)': self.funct_sqrt,
            'custom': self.get_custom_function
        }
        return functions.get(choice)

    def plot_function(self):
        funct = self.get_function()
        if funct is None:
            self.show_error("Неверный выбор")
            return

        value = self.get_value()
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

    def get_custom_function(self, X):
        custom_func = self.custom_func_entry.get()
        try:
            return eval(custom_func)
        except:
            return None

    def get_value(self):
        try:
            return float(self.value_entry.get())
        except ValueError:
            return None

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

    def show_error(self, message):
        messagebox.showerror("Ошибка", message)

    def funct_ctg(self, X):
        return 1.0 / np.tan(X)

    def funct_x(self, X):
        return X

    def funct_x_squared(self, X):
        return X ** 2

    def funct_sqrt(self, X):
        return np.sqrt(X)

root = tk.Tk()
root.title("Функция")
app = Application(master=root)
app.mainloop()