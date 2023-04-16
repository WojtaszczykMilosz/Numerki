import matplotlib.pyplot as plt
import interpolacja as inter
import numpy as np


def wykres_funkcji(funkcja, a, b, iloscWezlow):

    x = inter.ObliczWezlyCzebyszewa(a, b, iloscWezlow)
    y = funkcja(x)


    Lagrange = inter.InterpolacjaLagrange(x, y)
    interpolacja = Lagrange.ObliczWartoscInterpolacji
    interpolacjaSzybsza = Lagrange.ObliczWartoscInterpolacjiSzybkie

    for i in range(len(x)):
        print()
        print("Węzeł " + str(i) + ": " + str(x[i]))
        print("Funkcja: " + str(round(funkcja(x[i]),5)))
        print("Interpolacja: " + str(round(interpolacja(x[i]),5)))
        print("Interpolacja szybsza: " + str(round(interpolacjaSzybsza(x[i]),5)))
        print()

    help = np.linspace(a, b, 10000)
    wartoscifunkcji = np.round(funkcja(help),5)
    #wartosciInterpolacji = np.round(interpolacja(help),5)
    wartosciInterpolacji2 = []
    for i in range(len(help)):
        wartosciInterpolacji2.append(np.round(interpolacjaSzybsza(help[i]),5))

    #np.round(y,5)
    zero = np.zeros((len(help)))
    plt.figure(figsize=(10, 6))


    plt.plot(help, wartoscifunkcji,label='zadana funkcja')
    #plt.plot(help, wartosciInterpolacji, color='green', label='interpolacja')
    plt.plot(help, wartosciInterpolacji2, color='orange', label='interpolacjaSzybsza')

    plt.plot(x, y, 'rd', label='węzły')

    plt.plot(help, zero, color='black')
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Wykres funkcji i jej znalezione miejsce zerowe")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 8})
    plt.tight_layout()
    plt.show()
