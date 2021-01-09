def sort(dist, n: int):
    return sorted(dist.x() for i in range(n))

def avr(sel: list):
    return sum(sel) / len(sel)

def med(sel: list): 
    l = len(sel) // 2
    if len(sel) % 2 == 0:
        return (sel[l-1] + sel[l]) / 2
    else:
        return sel[l]

def zr(sel: list): 
    return (sel[0] + sel[-1]) / 2

def zq(sel: list): 
    n = len(sel)
    z = 0
    if n % 4 == 0:
        z += sel[n // 4 - 1]
    else:
        z += sel[n // 4]
    if 3*n % 4 == 0:
        z += sel[3*n // 4 - 1]
    else:
        z += sel[3*n // 4]
    return z / 2

def ztr(sel: list):  
    r = len(sel) // 4
    selr = sel[r:-r]
    return sum(selr) / len(selr)
