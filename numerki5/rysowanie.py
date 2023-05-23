import matplotlib.pyplot as plt
import numpy as np
import aproksymacja as ap


def rysujWartosci(a, b, funkcja, iloscWezlow, stopien = 1, dokladnosc = None):
    aprox = ap.Aproksymacja(stopien, a, b)

    x = np.linspace(a, b, 1000)
    if (dokladnosc == None):
        y = aprox.obliczWartoscAproksymacji(funkcja,iloscWezlow,x)
        print(aprox.obliczBlad(funkcja,iloscWezlow,x,y))
    else:
        y,ile = aprox.obliczZDokladnoscia(funkcja, iloscWezlow, x, dokladnosc)
        print(ile)


    plt.plot(x, y, c='r')
    y = funkcja(x)
    plt.plot(x, y, c='b')
    plt.show()
