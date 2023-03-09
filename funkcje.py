import numpy as np
import skrypty as sk

def cosinus(x):
    return np.cos(2 * x) - (1.5 * x)

def cosinus_pochodna(x):
    return (-2 * np.sin(2 * x)) - 1.5

def cosinus_pochodna2(x):
    return -4 * np.cos(2 * x)

def wykładnicza(x):
    return 2 ** x - 6

def wykładnicza_pochodna(x):
    return np.log(2) * 2 ** x

def wykładnicza_pochodna2(x):
    return (np.log(2)**2) * (2 ** x)

def złożenie(x):
    return 3 ** np.sin(x) - 2

def złożenie_pochodna(x):
    return np.log(3) * (3 ** np.sin(x)) * np.cos(x)

def złożenie_pochodna2(x):
    return (np.log(3) ** 2) * (3 ** np.sin(x)) * (np.cos(x) ** 2) - np.log(3) * (3 ** np.sin(x)) * np.sin(x)

def wielomian(x, tab):
    return sk.Obliczenia.horner(x,tab)

def wielomian_pochodna(x,tab):
    pochodna = [tab[0] * (len(tab) - 1)]
    for i in range(1, len(tab) - 1):
        pochodna.append(tab[i] * (len(tab) - i - 1))
        print(pochodna)
    return  sk.Obliczenia.horner(x,pochodna)
