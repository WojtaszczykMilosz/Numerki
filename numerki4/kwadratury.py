import operacjePlikowe as op
import time

class NewtonCotes:
    def __init__(self, a, b, dokladnosc):
        self.a = a
        self.b = b
        self.dokladnosc = dokladnosc

    def obliczKwadrature(self, funkcja):
        start = time.time()
        iloscPodprzedzialow = 2
        staryWynik = 0
        while True:
            self.obliczWartosci(funkcja,iloscPodprzedzialow)

            wynik = self.wartosci[0] + self.wartosci[iloscPodprzedzialow]
            for i in range(1, iloscPodprzedzialow):
                wynik += (2 + 2 * (i % 2)) * self.wartosci[i]
            wynik *= 1 / 3 * self.h

            if abs(staryWynik - wynik) < self.dokladnosc:
                end = time.time()
                return wynik, iloscPodprzedzialow, end - start

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
        self.wspolczynniki, self.pierwiastki = op.wczytajDane()

    def obliczKwadrature(self, funkcja, ileWezlow):
        start = time.time()
        wynik = 0

        for x in range(ileWezlow):

            wynik += self.wspolczynniki[ileWezlow-2][x] * \
                     self.przeskalowanaWartoscFunkcji(funkcja,self.pierwiastki[ileWezlow - 2][x])

        end = time.time()
        return wynik, end - start

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