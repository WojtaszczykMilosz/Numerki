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

    def obliczBlad(self, funkcja, iloscWezlow, x, y):
        kwadratura = kw.KwadraturaLegendre(self.a, self.b)
        wynik = kwadratura.obliczKwadrature(
            lambda zmienna:np.square(funkcja(x) - y), iloscWezlow)

        try:
            wynik = wynik.sum()
        except:
            pass

        return wynik

    def obliczWartoscAproksymacji(self, funkcja, iloscWezlow, x):
        self.obliczWspolczynniki(funkcja, iloscWezlow)
        x = self.przeksztalcWartoscX(x)

        wynik = 0
        for i in range(self.stopienWielomianu + 1):

            wynik += self.wspolczynniki_C[i] * self.Wielomiany[i].obliczWartosc(x)




        return wynik

    def obliczZDokladnoscia(self, funkcja, iloscWezlow, x, dokladnosc):
        stopien = self.stopienWielomianu

        i = 1
        while True:
            self.stopienWielomianu = i

            if (i == len(self.Wielomiany)):
                self.Wielomiany.append(WielomianLegendre(i))

            wynik = self.obliczWartoscAproksymacji(funkcja, iloscWezlow,x)
            blad = self.obliczBlad(funkcja,iloscWezlow,x,wynik)


            if (blad < dokladnosc):
                temp = self.stopienWielomianu
                self.stopienWielomianu = stopien
                return wynik, temp

            i += 1




    def obliczWspolczynniki(self, funkcja, iloscWezlow):
        kwadratura = kw.KwadraturaLegendre(-1, 1)
        self.wspolczynniki_C = []
        for iteracja in range(self.stopienWielomianu + 1):
            c = kwadratura.obliczKwadrature(lambda x: self.Wielomiany[iteracja].obliczWartosc(x) * funkcja(x),
                                            iloscWezlow)
            c /= kwadratura.obliczKwadrature(lambda x: self.Wielomiany[iteracja].obliczWartosc(x) ** 2, iloscWezlow)

            self.wspolczynniki_C.append(c)

    def przeksztalcWartoscX(self, x):
        return ((2 * x) - self.a - self.b) / (self.b - self.a)


    def odwrocPrzeksztalcenie(self, y):
        return (y * (self.b - self.a) + self.b + self.a) / 2
