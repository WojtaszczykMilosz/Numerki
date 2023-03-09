import matplotlib.pyplot as plt
import numpy as np
import skrypty as sk

def wykres_funkcji(tab,a,b):

    help = np.linspace(a,b)
    wartosci = sk.horner(help,tab)


    plt.plot(help,wartosci)
    plt.show()

wykres_funkcji([2,1,3])