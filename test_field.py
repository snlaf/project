import matplotlib.pyplot as plt
import numpy as np

def plot_function(function):
    x = np.linspace(-10, 10, 400)
    y = eval(function)

    plt.plot(x, y)
    plt.title('График функции')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

function = input("Введите функцию: ")
plot_function(function)