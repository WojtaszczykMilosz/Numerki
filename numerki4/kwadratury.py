import numpy as np

class NewtonCotes:
    def __init__(self, a, b, dokladnosc):
        self.a = a
        self.b = b
        self.dokladnosc = dokladnosc

    def obliczKwadrature(self, funkcja):
        iloscPodprzedzialow = 2
        staryWynik = 0
        while True:
            self.obliczWartosci(funkcja,iloscPodprzedzialow)

            wynik = self.wartosci[0] + self.wartosci[iloscPodprzedzialow]
            for i in range(1, iloscPodprzedzialow):
                wynik += (2 + 2 * (i % 2)) * self.wartosci[i]
            wynik *= 1 / 3 * self.h

            if abs(staryWynik - wynik) < self.dokladnosc:
                print(iloscPodprzedzialow)
                return wynik

            iloscPodprzedzialow *= 2
            staryWynik = wynik

    def obliczWartosci(self, funkcja, ilePrzedzialow):
        self.h = (self.b - self.a) / ilePrzedzialow
        x = self.a
        self.wartosci = []

        for i in range(ilePrzedzialow + 1):
            self.wartosci.append(funkcja(x))
            x += self.h


class Legendre:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.pierwiastki = [[-np.sqrt(3)/3,np.sqrt(3)/3],
                            [-np.sqrt(15)/5, 0, np.sqrt(15)/5],
                            [-np.sqrt(525 + 70 * np.sqrt(30))/35,-np.sqrt(525 - 70 * np.sqrt(30))/35,
                             np.sqrt(525 - 70 * np.sqrt(30))/35, np.sqrt(525 + 70 * np.sqrt(30))/35],
                            [-np.sqrt(245 + 14 * np.sqrt(70)) / 21, -np.sqrt(245 - 14 * np.sqrt(70)) / 21, 0,
                            np.sqrt(245 - 14 * np.sqrt(70)) / 21, np.sqrt(245 + 14 * np.sqrt(70)) / 21]]
        self.wspolczynniki = [[1,1],
                              [5/9,8/9,5/9],
                              [(18 - np.sqrt(30))/36, (18 + np.sqrt(30))/36, (18 + np.sqrt(30))/36, (18 - np.sqrt(30))/36],
                              [(322 - 13 * np.sqrt(70)) / 900, (322 + 13 * np.sqrt(70)) / 900, 128/225,
                               (322 + 13 * np.sqrt(70)) / 900, (322 - 13 * np.sqrt(70)) / 900]
                              ]

    def obliczKwadrature(self, funkcja, ileWezlow):
        wynik = 0

        for x in range(ileWezlow):

            wynik += self.wspolczynniki[ileWezlow-2][x] * \
                     self.przeskalowanaWartoscFunkcji(funkcja,self.pierwiastki[ileWezlow - 2][x])

        return wynik

    def przeskalowanaWartoscFunkcji(self, funkcja, t):
        x = ((self.b - self.a) * t + self.a + self.b) / 2
        dx = (self.b - self.a ) / 2

        return funkcja(x) * dx

# #
# leg = Legendre(0,4)
#
#
#
# def fun(x):
#     return x * x + 3
# a = leg.obliczKwadrature(fun,5)
#
# print(a)