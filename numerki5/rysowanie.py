import matplotlib.pyplot as plt
import numpy as np
import aproksymacja as ap


def rysujWartosci(stopien, a, b, funkcja, iloscWezlow):
    aprox = ap.Aproksymacja(stopien, a, b)

    x = np.linspace(a, b, 1000)
    y,ile = aprox.obliczZDokladnoscia(funkcja, iloscWezlow, x, 0.1)

    print(y,ile)
    plt.plot(x, y, c='r')
    y = funkcja(x)
    plt.plot(x, y, c='b')
    plt.show()
