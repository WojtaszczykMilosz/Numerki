import time

import matplotlib.pyplot as plt
import interpolacja as inter
import numpy as np


def wykres_funkcji(funkcja, a, b, iloscWezlow):
    x = inter.ObliczWezlyCzebyszewa(a, b, iloscWezlow)
    y = np.round(funkcja(x), 5)

    Lagrange = inter.InterpolacjaLagrange(x, y)
    interpolacja = Lagrange.ObliczWartoscInterpolacji
    interpolacjaSzybsza = Lagrange.ObliczWartoscInterpolacjiSzybkie

    for i in range(len(x)):
        print()
        print("Węzeł " + str(i) + ": " + str(x[i]))
        print("Funkcja: " + str(round(funkcja(x[i]), 5)))
        print("Interpolacja: " + str(round(interpolacja(x[i]), 5)))
        print("Interpolacja szybsza: " + str(round(interpolacjaSzybsza(x[i]), 5)))
        print()

    points = np.linspace(a, b, 10000)
    wartoscifunkcji = np.round(funkcja(points), 5)

    wartosciInterpolacji2 = []
    start = time.time()
    for i in range(len(points)):
        wartosciInterpolacji2.append(np.round(interpolacjaSzybsza(points[i]), 5))

    end = time.time()

    print(f"Interpolacja nowa {end - start}")
    # start = time.time()
    # wartosciInterpolacji = []
    # for i in range(len(help)):
    #     wartosciInterpolacji.append(np.round(interpolacja(help[i]), 5))
    #
    # end = time.time()
    # print(f"Interpolacja stara {end-start}")
    zero = np.zeros((len(points)))
    plt.figure(figsize=(10, 6))

    plt.plot(points, wartoscifunkcji, label='zadana funkcja')
    # plt.plot(help, wartosciInterpolacji, color='green', label='interpolacja')
    plt.plot(points, wartosciInterpolacji2, color='orange', label='interpolacjaSzybsza')

    plt.plot(x, y, 'rd', label='węzły')

    plt.plot(points, zero, color='black')
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Wykres funkcji i jej znalezione miejsce zerowe")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 8})
    plt.tight_layout()
    plt.show()
    print("Podaj punkt który chcesz policzyć")
    X = int(input())
    print("wartosc interpolacji:")
    print(interpolacjaSzybsza(X))
