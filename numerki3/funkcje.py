import numpy as np
import obliczenia as ob

class Liniowa:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def obliczWartosc(self,x):
        return self.a*x + self.b

class ModulX:
    def obliczWartosc(self,x):
        return abs(x)


class Wielomian:
    def __init__(self,tab):
        self.tab = tab

    def obliczWartosc(self,x):
        return ob.horner(x,self.tab)

    def obliczPochodna(self):
        pochodna = [self.tab[0] * (len(self.tab) - 1)]
        for i in range(1, len(self.tab) - 1):
            pochodna.append(self.tab[i] * (len(self.tab) - i - 1))
        return pochodna

    def obliczWartoscPochodnej(self, x):
        return  ob.horner(x,self.obliczPochodna())