import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize

print("Лабораторная работа №6; Выполнила: Фомина Дарья\n")


def lin(a, b):
    return lambda x: np.full_like(x, a)+np.full_like(x, b)*x \
           if isinstance(x, np.ndarray) else a + b * x

def abs_func(params, x, y):
    return np.sum(np.abs(y - params[0] - params[1] * x))

#Оценкa методом наименьших квадратов
size = 20
ref = lin(2, 2)
x = np.linspace(-1.8, 2, size)
y1 = ref(x) + norm.rvs(size=size)
y2 = y1.copy()
y2[0] += 10
y2[-1] -= 10
xm = np.mean(x)
d = np.mean(x*x) - xm**2
for y, name in zip([y1, y2]):
    ym = np.mean(y)
    b = (np.mean(x*y) - ym*xm) / d
    MNK = (ym - xm*b, b)
    MNM = minimize(abs_func, [0, 1], #Для реализации метода наименьших модулей функционал был минимизирован
                   args=(x, y),
                   method='COBYLA').x
    plt.plot(x, ref(x), label='Модель')
    plt.plot(x, lin(*MNK)(x), label='МНК')
    plt.plot(x, lin(*MNM)(x), label='МНМ')
    plt.scatter(x, y, label='Выборка')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(name)
    print(MNK, MNM)
    plt.show()
