import sys
sys.path.append('../lab1')
import classes as dst
import functions as f
from math import sqrt


N = 1000
chars = ['avr', 'med', 'zr', 'zq', 'ztr']
arr=[10, 100, 1000]
print("Лабораторная работа №2; Выполнила: Фомина Дарья\n")
norm = dst.Normal(1,0)
print("/************************************************/\n")
print("Normal distribution\n")
for n in arr:
    print(f'n={n}')
    res = {}
    for i in range(5):
        res[i] = [0, 0]
    for i in range(N):
        s = f.sort(norm, n)
        z = f.avr(s)
        res[0][0] += z/N
        res[0][1] += z*z/N
        z = f.med(s)
        res[1][0] += z/N
        res[1][1] += z*z/N
        z = f.zr(s)
        res[2][0] += z/N
        res[2][1] += z*z/N
        z = f.zq(s)
        res[3][0] += z/N
        res[3][1] += z*z/N
        z = f.ztr(s)
        res[4][0] += z/N
        res[4][1] += z*z/N  
    for i in range(5):
        res[i][1] = res[i][1] - res[i][0]**2
    for ch in chars:
        print(ch)
        print(f'\tE = {res[chars.index(ch)][0]}\n\tD = {res[chars.index(ch)][1]}\n\td = {sqrt(res[chars.index(ch)][1])}')
    print()
        
cauchy = dst.Cauchy(1,0)
print("/************************************************/\n")
print("Cauchy distribution\n")
for n in arr:
    print(f'n={n}')
    res = {}
    for i in range(5):
        res[i] = [0, 0]
    for i in range(N):
        s = f.sort(cauchy, n)
        z = f.avr(s)
        res[0][0] += z/N
        res[0][1] += z*z/N
        z = f.med(s)
        res[1][0] += z/N
        res[1][1] += z*z/N
        z = f.zr(s)
        res[2][0] += z/N
        res[2][1] += z*z/N
        z = f.zq(s)
        res[3][0] += z/N
        res[3][1] += z*z/N
        z = f.ztr(s)
        res[4][0] += z/N
        res[4][1] += z*z/N  
    for i in range(5):
        res[i][1] = res[i][1] - res[i][0]**2
    for ch in chars:
        print(ch)
        print(f'\tE = {res[chars.index(ch)][0]}\n\tD = {res[chars.index(ch)][1]}\n\td = {sqrt(res[chars.index(ch)][1])}')
    print()

laplas = dst.Laplace(2**(-0.5), 0)
print("/************************************************/\n")
print("Laplace distribution\n")
for n in arr:
    print(f'n={n}')
    res = {}
    for i in range(5):
        res[i] = [0, 0]
    for i in range(N):
        s = f.sort(laplas, n)
        z = f.avr(s)
        res[0][0] += z/N
        res[0][1] += z*z/N
        z = f.med(s)
        res[1][0] += z/N
        res[1][1] += z*z/N
        z = f.zr(s)
        res[2][0] += z/N
        res[2][1] += z*z/N
        z = f.zq(s)
        res[3][0] += z/N
        res[3][1] += z*z/N
        z = f.ztr(s)
        res[4][0] += z/N
        res[4][1] += z*z/N  
    for i in range(5):
        res[i][1] = res[i][1] - res[i][0]**2
    for ch in chars:
        print(ch)
        print(f'\tE = {res[chars.index(ch)][0]}\n\tD = {res[chars.index(ch)][1]}\n\td = {sqrt(res[chars.index(ch)][1])}')
    print()
        
poisson = dst.Poisson(10)
print("/************************************************/\n")
print("Poisson distribution\n")
for n in arr:
    print(f'n={n}')
    res = {}
    for i in range(5):
        res[i] = [0, 0]
    for i in range(N):
        s = f.sort(poisson, n)
        z = f.avr(s)
        res[0][0] += z/N
        res[0][1] += z*z/N
        z = f.med(s)
        res[1][0] += z/N
        res[1][1] += z*z/N
        z = f.zr(s)
        res[2][0] += z/N
        res[2][1] += z*z/N
        z = f.zq(s)
        res[3][0] += z/N
        res[3][1] += z*z/N
        z = f.ztr(s)
        res[4][0] += z/N
        res[4][1] += z*z/N  
    for i in range(5):
        res[i][1] = res[i][1] - res[i][0]**2
    for ch in chars:
        print(ch)
        print(f'\tE = {res[chars.index(ch)][0]}\n\tD = {res[chars.index(ch)][1]}\n\td = {sqrt(res[chars.index(ch)][1])}')
    print()


uniform = dst.Uniform(-3**0.5, 3**0.5)
print("/************************************************/\n")
print("Uniform distribution\n")
for n in arr:
    print(f'n={n}')
    res = {}
    for i in range(5):
        res[i] = [0, 0]
    for i in range(N):
        s = f.sort(uniform, n)
        z = f.avr(s)
        res[0][0] += z/N
        res[0][1] += z*z/N
        z = f.med(s)
        res[1][0] += z/N
        res[1][1] += z*z/N
        z = f.zr(s)
        res[2][0] += z/N
        res[2][1] += z*z/N
        z = f.zq(s)
        res[3][0] += z/N
        res[3][1] += z*z/N
        z = f.ztr(s)
        res[4][0] += z/N
        res[4][1] += z*z/N  
    for i in range(5):
        res[i][1] = res[i][1] - res[i][0]**2
    for ch in chars:
        print(ch)
        print(f'\tE = {res[chars.index(ch)][0]}\n\tD = {res[chars.index(ch)][1]}\n\td = {sqrt(res[chars.index(ch)][1])}')
    print()
