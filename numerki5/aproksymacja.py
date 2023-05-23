import funkcje as fun
import numpy as np
import kwadratura as kw


class WielomianLegendre:
    def __init__(self, i):
        self.tabs = self.obliczWspolczynnikiIteracyjnie(i)


    def obliczWspolczynnikiIteracyjnie(self, i):
        if (i == 0):
            return [np.array([1])]
        elif (i == 1):
            return [np.array([1]),np.array([1, 0])]

        tab = [np.array([1]),np.array([0, 1])]


        for x in range(2, i + 1):

            helptab = np.insert(tab[x - 1] * (2 * x - 1), 0, 0)

            helptab2 = np.append(tab[x - 2] * (x - 1), [0, 0])

            tab.append((helptab - helptab2) / x)


        for x in range(len(tab)):
            tab[x] = np.flip(tab[x])

        return tab

    def dodajWielomian(self, i):
        if (i + 1 <= len(self.tabs)):
            return
        tab = []
        tab.append(np.flip(self.tabs[i - 1]))
        tab.append(np.flip(self.tabs[i - 2]))

        helptab = np.insert(tab[0] * (2 * i - 1), 0, 0)
        helptab2 = np.append(tab[1] * (i - 1), [0, 0])


        tab.append((helptab-helptab2) / i)
        self.tabs.append(np.flip(tab[2]))




    def obliczWartosc(self, x, wielomian):
        return fun.horner(x, self.tabs[wielomian])


class Aproksymacja:

    def __init__(self, stopienWielomianu, a, b):
        self.stopienWielomianu = stopienWielomianu
        self.a = a
        self.b = b
        self.uzupelnijWielomiany()

    def uzupelnijWielomiany(self):
        self.Wielomian = WielomianLegendre(self.stopienWielomianu)


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


        wynik = 0
        for i in range(self.stopienWielomianu + 1):
            wynik += self.wspolczynniki_C[i] * self.Wielomian.obliczWartosc(x, i)



        return wynik

    def obliczZDokladnoscia(self, funkcja, iloscWezlow, x, dokladnosc):
        stopien = self.stopienWielomianu

        i = 1

        while True:
            self.stopienWielomianu = i
            self.Wielomian.dodajWielomian(i)

            wynik = self.obliczWartoscAproksymacji(funkcja, iloscWezlow,x)
            blad = self.obliczBlad(funkcja,iloscWezlow,x,wynik)
            if (i == 1):
                pierwszyblad = blad
            print(f"{i} - {blad}")

            if blad < dokladnosc or blad > pierwszyblad:
                if(blad > pierwszyblad):
                    print("nie udalo sie znalezc aproksymacji o podanej dokladnosci")
                temp = self.stopienWielomianu
                self.stopienWielomianu = stopien
                return wynik, temp

            i += 1




    def obliczWspolczynniki(self, funkcja, iloscWezlow):
        kwadratura = kw.KwadraturaLegendre(self.a, self.b)
        self.wspolczynniki_C = []
        for iteracja in range(self.stopienWielomianu + 1):


            c = kwadratura.obliczKwadrature(lambda x: self.Wielomian.obliczWartosc(x, iteracja) * funkcja(x),
                                            iloscWezlow)
            c /= (1/(iteracja + 1 / 2))

            self.wspolczynniki_C.append(c)



