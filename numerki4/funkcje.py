import numpy as np



def horner(x, tab):
    wartosc = tab[0]

    for a in range(1, len(tab)):
        wartosc = wartosc * x + tab[a]
    return wartosc



def liniowa(x):
    return x*5

def trygonometryczna(x):
    return np.sin(x) + np.cos(x)

def trygonometryczna2(x):
    return np.cos(20*np.sqrt(x))

def modulX(x):
    return abs(x)


class Wielomian:
    def __init__(self,tab):
        self.tab = tab

    def obliczWartosc(self,x):
        return horner(x,self.tab)
