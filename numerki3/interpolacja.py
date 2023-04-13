from scipy.interpolate import lagrange
import numpy as np


class InterpolacjaLagrange:
    def __init__(self, x, y):
        self.wezly = x
        self.wartosciWezlow = y
        self.N = len(x)


    def ObliczWartoscInterpolacji(self, x):

        wynik = 0
        for i in range(self.N):
            mnozenie = 1
            for j in range(self.N):
                if (j == i): continue
                mnozenie *= x - self.wezly[j]
                mnozenie /= self.wezly[i] - self.wezly[j]

            wynik += self.wartosciWezlow[i] * mnozenie
        return wynik



def ObliczWezlyCzebyszewa(a, b, N):
    tab = []
    for i in range(N):
        argument = 2 * i + 1
        argument /= 2 * N + 2
        argument *= np.pi

        x = b - a
        x *= np.cos(argument)
        x += b + a
        x /= 2
        tab.append(x)

    return np.array(tab)


# punkty = [1, 2, 4]
# wartosci = [2, 10, 2]
# inter = InterpolacjaNewtona(punkty, wartosci)
# czebyszew = WezlyCzebyszewa(0,5,6)
#
# print(inter.ObliczWartoscInterpolacji(3))
# print(czebyszew.ObliczWezly())