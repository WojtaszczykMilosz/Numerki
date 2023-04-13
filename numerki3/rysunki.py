import matplotlib.pyplot as plt
import interpolacja as inter
import numpy as np


def wykres_funkcji(funkcja, a, b, iloscWezlow):

    x = inter.ObliczWezlyCzebyszewa(a, b, iloscWezlow)
    print(a)
    print(b)
    y = funkcja(x)

    Lagrange = inter.InterpolacjaLagrange(x, y)
    interpolacja = Lagrange.ObliczWartoscInterpolacji


    help = np.linspace(a, b, 500)
    wartoscifunkcji = funkcja(help)
    wartosciInterpolacji = interpolacja(help)

    zero = np.zeros((len(help)))
    plt.figure(figsize=(10, 6))


    plt.plot(help, wartoscifunkcji,label='zadana funkcja')
    plt.plot(help, wartosciInterpolacji, color='green', label='interpolacja')


    plt.plot(x, y, 'rd', label='węzły')
    plt.plot(help, zero, color='black')
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Wykres funkcji i jej znalezione miejsce zerowe")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 8})
    plt.tight_layout()
    plt.show()
