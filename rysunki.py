import matplotlib.pyplot as plt
import numpy as np
import skrypty as sk

def wykres_funkcji(funkcja,a,b,x1,x2):
    help = np.linspace(a,b)
    wartosci = funkcja(help)
    help2 = np.linspace(wartosci.min(),wartosci.max())

    zero = np.zeros((len(help),1))

    z = np.zeros((len(wartosci), 1))
    z += x1
    y = np.zeros((len(wartosci), 1))
    y += x2
    plt.figure(figsize=(10,6))
    plt.plot(help,wartosci,label='zadana funkcja')
    plt.plot(z,help2,linestyle = 'dashed',color='black',label='miejsce zerowe uzyskane metodą bisekcji')
    plt.plot(y,help2, linestyle='dashed', color='red',label='miejsce zerowe uzyskane metodą stycznych')
    plt.plot(help,zero,color='black')
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Wykres funkcji i jej znalezione miejsce zerowe")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 8})
    plt.tight_layout()
    plt.show()


