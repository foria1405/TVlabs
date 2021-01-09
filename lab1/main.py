import matplotlib.pyplot as plt
import numpy as np
import classes as dst

#нормальное распределение
norm = dst.Normal(1,0)
arr=[10, 100, 1000]
for n in arr:
    data = [norm.x() for i in range(n)]
    hs = dst.Histogram(data)
    x = np.linspace(min(data), max(data), 200)
    yf = [norm.f(k) for k in x]
    yF = [norm.F(k) for k in x]
    plt.subplot(2, 3, arr.index(n)+1)
    plt.title("Нормальное распределение, n = " + str(n))
    plt.xlabel('x')
    plt.ylabel('Функция плотности')
    plt.plot(x, yf, label='ожидание', color='green')
    plt.bar(hs.x, hs.y, label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
    plt.subplot(2, 3, arr.index(n)+4)
    plt.xlabel('x')
    plt.ylabel('Функция распределения')
    plt.plot(x, yF, label='ожидание')
    plt.bar(hs.x, hs.F(), label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
plt.show()

#распределение Коши
cauchy = dst.Cauchy(1,0)
for n in arr:
    data = [cauchy.x() for i in range(n)]
    hs = dst.Histogram(data)
    x = np.linspace(min(data), max(data), 200)
    yf = [cauchy.f(k) for k in x]
    yF = [cauchy.F(k) for k in x]
    plt.subplot(2, 3, arr.index(n)+1)
    plt.title("Распределение Коши, n = " + str(n))
    plt.xlabel('x')
    plt.ylabel('Функция плотности')
    plt.plot(x, yf, label='ожидание', color='green')
    plt.bar(hs.x, hs.y, label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
    plt.subplot(2, 3, arr.index(n)+4)
    plt.xlabel('x')
    plt.ylabel('Функция распределения')
    plt.plot(x, yF, label='ожидание')
    plt.bar(hs.x, hs.F(), label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
plt.show()

#распределение Лапласа
laplas = dst.Laplace(2**(-0.5), 0)
for n in arr:
    data = [laplas.x() for i in range(n)]
    hs = dst.Histogram(data)
    x = np.linspace(min(data), max(data), 200)
    yf = [laplas.f(k) for k in x]
    yF = [laplas.F(k) for k in x]
    plt.subplot(2, 3, arr.index(n)+1)
    plt.title("Распределение Лапласа, n = " + str(n))
    plt.xlabel('x')
    plt.ylabel('Функция плотности')
    plt.plot(x, yf, label='ожидание', color='green')
    plt.bar(hs.x, hs.y, label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
    plt.subplot(2, 3, arr.index(n)+4)
    plt.xlabel('x')
    plt.ylabel('Фукнция распределения')
    plt.plot(x, yF, label='ожидание')
    plt.bar(hs.x, hs.F(), label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
plt.show()

#распределение Пуассона
poisson = dst.Poisson(10)
for n in arr:
    data = [poisson.x() for i in range(n)]
    hs = dst.Histogram(data, True)
    x = np.linspace(min(data), max(data), 200)
    yf = [poisson.f(k) for k in x]
    yF = [poisson.F(k) for k in x]
    plt.subplot(2, 3, arr.index(n)+1)
    plt.title("Распределение Пуассона, n = " + str(n))
    plt.xlabel('x')
    plt.ylabel('Функция плотности')
    plt.plot(x, yf, label='ожидание', color='green')
    plt.bar(hs.x, hs.y, label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
    plt.subplot(2, 3, arr.index(n)+4)
    plt.xlabel('x')
    plt.ylabel('Фукнция распределения')
    plt.plot(x, yF, label='ожидание')
    plt.bar(hs.x, hs.F(), label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
plt.show()

#равномерное распределение
uniform = dst.Uniform(-3**0.5, 3**0.5)
for n in arr:
    data = [uniform.x() for i in range(n)]
    hs = dst.Histogram(data)
    x = np.linspace(min(data), max(data), 200)
    yf = [uniform.f(k) for k in x]
    yF = [uniform.F(k) for k in x]
    plt.subplot(2, 3, arr.index(n)+1)
    plt.title("Равномерное распределение, n = " + str(n))
    plt.xlabel('x')
    plt.ylabel('Функция плотности')
    plt.plot(x, yf, label='ожидание', color='green')
    plt.bar(hs.x, hs.y, label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
    plt.subplot(2, 3, arr.index(n)+4)
    plt.xlabel('x')
    plt.ylabel('Фукнция распределения')
    plt.plot(x, yF, label='ожидание')
    plt.bar(hs.x, hs.F(), label='результат', color='pink', edgecolor='black', linewidth=0.5, width=hs.x[len(hs.x)-1]-hs.x[len(hs.x)-2])
    plt.legend()
plt.show()
