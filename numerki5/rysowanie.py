import matplotlib.pyplot as plt
import numpy as np
import aproksymacja as ap
import kwadratura as kw

def rysujWartosci(a, b, funkcja, iloscWezlow, stopien = 1, dokladnosc = None):
    aprox = ap.Aproksymacja(stopien, a, b)

    x = np.linspace(a, b, 1000)
    zero = np.zeros(len(x))
    plt.plot(x, zero,c='black')

    y = funkcja(x)
    plt.plot(x, y, c='b', label="Funkcja bazowa")

    if (dokladnosc == None):
        y = aprox.obliczWartoscAproksymacji(funkcja,iloscWezlow,x)
        print(f"Błąd: {aprox.obliczBlad(funkcja,iloscWezlow,x,y)}")

    else:
        y, ile = aprox.obliczZDokladnoscia(funkcja, iloscWezlow, x, dokladnosc)
        print(f"Stopien uzyskanego wielomianu {ile}")
    print(f"Wielomian: {aprox.wspolczynniki_C}")

    plt.plot(x, y, linestyle = 'dashed', marker = 'o', markersize = 0.05, c='r', label = "Aproksymacja")

    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.title("Wykres funkcji aproksymowanej i bazowej")
    plt.legend(fontsize = 12, loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 8})
    plt.tight_layout()
    plt.show()
