import math
import matplotlib.pyplot as plt

def func(x, y):
	return x*math.exp(-x*x)-2*x*y

def euler(x0, y0, h):
        n = int(((y0-x0)/h))
        x, y = [], []
        x.append(x0)
        y.append(y0)
        for i in range(1, n + 1):
            y.append(y[i - 1] + h * func(x[i - 1], y[i - 1]))
            x.append(x[i - 1] + h)
        print("Метод Эйлера: \t\th = %.3f" %h, "y = %.5f" %y[n])
        plt.plot(x, y, label="Метод Эйлера")

def rungekutta(x0, y0, h):
        n = int(((y0-x0)/h))
        xgraph, ygraph = [], []
        x = x0
        y = y0
        xgraph.append(x)
        ygraph.append(y)
        for i in range(1, n + 1):
            k1 = h*func(x, y)
            k2 = h*func(x+0.5*h, y+0.5*k1)
            k3 = h*func(x+0.5*h, y+0.5*k2)
            k4 = h*func(x+h, y+k3)
            y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            x = x + h
            xgraph.append(x)
            ygraph.append(y)
        print("Метод Рунге-Кутта: \th = %.3f" %h, "y = %.5f" %y)
        plt.plot(xgraph, ygraph, label="Метод Рунге-Кутта")

def graphshow(h):
    plt.title('Сравнение методов Эйлера и Рунге-Кутта с шагом %.5f' % h)
    plt.legend()
    plt.grid()
    plt.show()

x0=0
y0=1
h=0.001
euler(x0, y0, h)
rungekutta(x0, y0, h)
graphshow(h)