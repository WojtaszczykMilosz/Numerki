import matplotlib.pyplot as plt
import numpy as np
import aproksymacja as ap


def rysujWartosci(stopien, a, b, funkcja, iloscWezlow):
    aprox = ap.Aproksymacja(stopien,a,b)

    x = np.linspace(a, b, 500)
    y = aprox.obliczWartoscAproksymacji(funkcja,iloscWezlow,x)
    for cc in aprox.wspolczynniki_C:
        print(cc)
    plt.plot(x, y, c='r')
    y = funkcja(x)
    plt.plot(x, y, c='b')
    plt.show()

rysujWartosci(3,-1,1,lambda x:x**3,100)