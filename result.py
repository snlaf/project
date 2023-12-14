import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="Введите функцию:")
        self.label.pack(side='top')

        self.dim_var = tk.StringVar(value='2D')

        self.dim_option = tk.OptionMenu(self, self.dim_var, '2D', '3D')
        self.dim_option.pack(side='top')

        self.entry = tk.Entry(self.master)
        self.entry.pack(side='top')

        self.button = tk.Button(text="Построить график", command=self.plot_function)
        self.button.pack(side='top')

        self.quit_button = tk.Button(self, text="Выйти", fg="red", command=self.master.destroy)
        self.quit_button.pack(side='bottom')

    def plot_function(self):
        function = self.entry.get()
        x = np.linspace(-10, 10, 400)
        y = eval(function)

        dim = self.get_dimensionality()
        if dim == '2D':
            self.plot_function_2d(x, y)
        else:
            self.plot_function_3d(x, y)

    def get_dimensionality(self):
        return self.dim_var.get()

    def plot_function_2d(self, x, y):
        fig, ax = plt.subplots()
        ax.plot(x, y)

        ax.set_title("Функция")
        ax.set_xlabel("X координата")
        ax.set_ylabel("Y координата")
        plt.show()

    def plot_function_3d(self, x, y):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, np.zeros_like(x))  # Add zeros for z-axis

        ax.set_title("Функция")
        ax.set_xlabel("X координата")
        ax.set_ylabel("Y координата")
        ax.set_zlabel("Z координата")
        plt.show()


window = tk.Tk()
window.title("Функция")
app = Application(master=window)
app.mainloop()