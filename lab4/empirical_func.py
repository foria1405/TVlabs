from math import sqrt, exp, floor, pi
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('../lab1')
import distributions as dst

#Гауссово ядро
def kernel_func(x: float):
    return exp(-x*x/2)/sqrt(2*pi)

#Ядерная оценка 
def nuclear_assessment(xsel: np.ndarray, sel: np.ndarray, k):
    n = len(sel)
    sigma = sqrt((sel*sel).sum()/n - (sel.sum()/n)**2)
    h = 1.06*sigma*(n**(-0.2))*k #Правило Сильвермана
    result = np.zeros_like(xsel)
    for i in range(len(xsel)):
        for v in sel:
            result[i] += kernel_func((xsel[i] - v)/h)
        result[i] /= n*h
    return result


ds = dst.get_distributions()
nselect = [20, 60, 100]
coefficient = [0.5, 1, 2]

#Ядерная оценка плотности распределения
for d in ds:
    fig, ax = plt.subplots(len(coefficient), len(nselect))
    rng = (-4, 4) if not d.discrete() else (6, 14)
    for i in range(len(nselect)):
        sel = np.array(dst.selection(d, nselect[i]))
        x = np.linspace(*rng, 100)
        y1 = list(map(d.f, x))
        for j in range(len(coefficient)):
            y2 = nuclear_assessment(x, sel, coefficient[j])
            ax1 = ax[i, j]
            ax1.plot(x, y1)
            ax1.plot(x, y2)
            ax1.legend()
            ax1.set_xlabel('x' if i == len(nselect) - 1 else '')
            ax1.set_ylabel(f'$f(x), n = {nselect[i]}$')
            if i == 0:
                ax1.set_title((d.name if j == 1 else '') + f"\n\n$h = h_n * {coefficient[j]}$")
    plt.show()

#Построение эмпирической функции
for d in ds:
    fig, ax = plt.subplots(1, len(nselect))
    rng = (-4, 4) if not d.discrete() else (6, 14)
    for i in range(len(nselect)):
        data = [d.x() for j in range(nselect[i])]
        x = np.linspace(min(data), max(data), 200)
        yF = [d.F(k) for k in x]
        plt.subplot(1, 3, i+1)
        plt.title(d.name + ", n = " + str(nselect[i]))
        plt.xlabel('x')
        plt.ylabel('Функция распределения')
        plt.plot(x, yF, label='ожидание')
        plt.hist(data, density=True, label='результат', bins=floor(len(data)),histtype='step',cumulative=True)
        plt.legend()
    plt.show()
