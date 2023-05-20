import funkcje as fun
import numpy as np
import kwadratura as kw

class WielomianLegendre:
    def __init__(self, i):
        self.tab = np.flip(self.obliczWspolczynniki(i))


    def obliczWspolczynniki(self, i):

        if i == 0:
            return np.append([], 1)
        elif i == 1:
            return np.append([], [0, 1])

        tab1 = np.insert(self.obliczWspolczynniki(i - 1) * (2 * i - 1), 0, 0)
        tab2 = np.append(self.obliczWspolczynniki(i - 2) * (i - 1), [0, 0])

        res = tab1 - tab2
        return res / i

    # def obliczWspolczynnikiIteracyjnie(self, i):
    #     if (i == 0):
    #         return [np.array([1])]
    #     elif (i == 1):
    #         return [np.array([1]),np.array([0, 1])]
    #     tab = np.array([[1],[0,1]],np.ndarray)
    #
    #
    #     for x in range(2, i + 1):
    #
    #         helptab = np.insert(np.asarray(tab[x - 1]) * (2 * x - 1), 0, 0)
    #         helptab2 = np.append(np.asarray(tab[x - 2]) * (x - 1), [0, 0])
    #         np.append(tab,(helptab - helptab2) / x)
    #
    #     for x in tab:
    #         x = np.flip(x)
    #
    #     return tab

    def obliczWartosc(self, x):
        return fun.horner(x, self.tab)


class Aproksymacja:

    def __init__(self, stopienWielomianu, a, b):
        self.stopienWielomianu = stopienWielomianu
        self.a = a
        self.b = b
        self.uzupelnijWielomiany()

    def uzupelnijWielomiany(self):
        self.Wielomiany = []
        for i in range(self.stopienWielomianu + 1):
            self.Wielomiany.append(WielomianLegendre(i))


    # def obliczBlad(self):


    def obliczWartoscAproksymacji(self, funkcja, iloscWezlow, x):
        self.obliczWspolczynniki(funkcja,iloscWezlow)
        wynik = 0
        for i in range(self.stopienWielomianu + 1):
            wynik += self.wspolczynniki_C[i] * self.Wielomiany[i].obliczWartosc(x)
        return wynik


    def obliczWspolczynniki(self, funkcja, iloscWezlow):
        kwadratura = kw.KwadraturaLegendre(self.a,self.b)
        self.wspolczynniki_C = []
        for iteracja in range(self.stopienWielomianu + 1):
            c = kwadratura.obliczKwadrature(lambda x: self.Wielomiany[iteracja].obliczWartosc(x) * funkcja(x), iloscWezlow)

            c /= kwadratura.obliczKwadrature(lambda x: self.Wielomiany[iteracja].obliczWartosc(x)**2, iloscWezlow)
            self.wspolczynniki_C.append(c)


