import numpy as np
import skrypty as sk

def cosinus(x):
    return np.cos(2 * x) - (1.5 * x)

def cosinus_pochodna(x):
    return (-2 * np.sin(2 * x)) - 1.5

def cosinus_pochodna2(x):
    return -4 * np.cos(2 * x)

def wykładnicza(x):
    return 2 ** x - 6

def wykładnicza_pochodna(x):
    return np.log(2) * 2 ** x

def wykładnicza_pochodna2(x):
    return (np.log(2)**2) * (2 ** x)

def złożenie(x):
    return 3 ** np.sin(x) - 2

def złożenie_pochodna(x):
    return np.log(3) * (3 ** np.sin(x)) * np.cos(x)

def złożenie_pochodna2(x):
    return (np.log(3) ** 2) * (3 ** np.sin(x)) * (np.cos(x) ** 2) - np.log(3) * (3 ** np.sin(x)) * np.sin(x)

class Wielomian:
    def __init__(self,tab):
        self.tab = tab

    def wartosc(self,x):
        return sk.Obliczenia.horner(x,self.tab)

    def pochodna(self):
        pochodna = [self.tab[0] * (len(self.tab) - 1)]
        for i in range(1, len(self.tab) - 1):
            pochodna.append(self.tab[i] * (len(self.tab) - i - 1))
        return pochodna

    def pochodna_wartosc(self, x):
        return  sk.Obliczenia.horner(x,self.pochodna())

