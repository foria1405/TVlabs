import random
import math
import numpy as np
from typing import Tuple
from math import ceil, sqrt, floor


#Лабораторная работа № 1 

def selection(dist, n: int):
    return sorted([dist.x() for i in range(n)])


def rV()->float:
    return random.random()


class Normal:
    laplas_table = np.zeros(1)
     
    def __init__(self, s, m):
        self.sigma = s
        self.mu=m
       
    def f(self, x:float)->float:
        return math.exp(-(x - self.mu)**2/(2*self.sigma))/(self.sigma*math.sqrt(2*math.pi))

    def x(self)->float:
        y = -6
        for i in range(12):
            y += rV()
        return self.mu + self.sigma * y

    def F(self, x:float)->float:
        if self.laplas_table.shape == (1,):
            self.laplas_table = np.zeros(400)
            f = open('for normal.txt')
            i = 0
            for line in f:
                self.laplas_table[i] = float(line.split()[1])
                i += 1
            #print(self.laplas_table)
        y = (x - self.mu) / self.sigma
        #print(x, y)
        n = math.floor(abs(y * 100))
        val = 0
        if n > 399:
            val = 0.9999
        else:
            val = self.laplas_table[n]
        if y > 0:
            return 0.5 + val / 2
        else:
            return 0.5 - val / 2

    def interval(self):
        return (mu - 4*sigma, mu + 4*sigma)



class Cauchy:
    def __init__(self, l, m):
        self.lm = l
        self.mu=m
        
    def f(self, x: float)->float:
        return self.lm / (math.pi * (self.lm**2 + (x - self.mu)**2))

    def F(self, x:float)->float:
        return 0.5 + math.atan((x - self.mu)/self.lm)/math.pi

    def x(self)->float:
        e = 0.0001
        while True:
            y = rV()
            if abs(y - 0.25) > e and abs(y - 0.75) > e:
                return self.mu + self.lm * math.tan(2*math.pi*y)

    def interval(self)->float:
        return (self.mu - math.sqrt(self.lm * (300 - l)), self.mu + math.sqrt(self.lm * (300 - l)))



class Laplace:
    def __init__(self, l, m):
        self.lm = l
        self.mu=m
    def f(self, x:float)->float:
        return 0.5 * self.lm * math.exp(-self.lm * abs(x - self.mu))

    def F(self, x:float)->float:
        if x < self.mu:
            return 0.5 * math.exp(self.lm * (x - self.mu))
        else:
            return 1 - 0.5 * math.exp(-self.lm * (x - self.mu))

    def x(self):
        return self.mu + math.log(rV() / rV()) / self.lm

    def interval(self):
        rng = -math.log(0.002 / self.lm)/self.lm
        return (self.mu - rng, self.mu + rng)


class Poisson:
    def __init__(self, m):
        self.mu=m
    def f(self, x: float)->float:
        if x < 0:
            return 0
        n = math.floor(x)
        v = math.exp(-self.mu)
        for i in range(1, n+1):
            v *=self.mu / i
        return v

    def F(self, x:float)->float:
        if x < 0:
            return 0
        k = math.ceil(x)
        v = math.exp(-self.mu)
        s = v
        for i in range(1, k):
            v *= self.mu / i
            s += v
        return s

    def x(self)->float:
        p = math.exp(-self.mu)
        r1 = rV() - p
        x = 0
        while r1 > 0:
            x += 1
            p *= self.mu / x
            r1 -= p
        return x

    def interval(self):
        return (0, self.mu*3)



class Uniform:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def f(self, x:float)->float:
        if x < self.a or x > self.b:
            return 0
        else:
            return 1 / (self.b - self.a)

    def F(self, x:float)->float:
        if x < self.a:
            return 0
        elif x > self.b:
            return 1
        else:
            return (x - self.a) / (self.b - self.a)

    def x(self)->float:
        return self.a + (self.b - self.a)*rV()

    def interval(self):
        return (self.a, self.b)



class Histogram:
    def __init__(self, data, discrete=False):
        n = len(data)
        min_x = min(data)
        max_x = max(data)
        b = self.bins(n)
        if discrete:
            b = max_x - min_x
        self.h = (max_x - min_x) / b
        self.x = np.array([min_x + (i + 1)*self.h for i in range(b)])
        self.y = np.zeros(b)
        for val in data:
            if val == max_x:
                self.y[-1] += 1 / (n * self.h)
                continue
            i = floor((val - min_x) / self.h)
            self.y[i] += 1 / (n * self.h)

    def F(self):
        return np.cumsum(self.y * self.h)
      
    @staticmethod
    def bins(n: int):
        return ceil(sqrt(n))

   
