import matplotlib.pyplot as plt
import numpy as np
import skrypty as sk

def wykres_funkcji(funkcja,pochodna,pochodna2,a,b,x1,x2):
    help = np.linspace(a,b,1000)
    wartosci = funkcja(help)
    help2 = np.linspace(wartosci.min(),wartosci.max(),1000)

    zero = np.zeros((len(help),1))
    plt.figure(figsize=(10, 6))

    if x1 != None:
        z = np.zeros(len(wartosci))
        z += x1
        plt.plot(z, help2, linestyle='dashed', color='black', label='miejsce zerowe uzyskane metodą bisekcji')

    if x2 != None:
        y = np.zeros(len(wartosci))
        y += x2
        plt.plot(y, help2, linestyle='dashed', color='red', label='miejsce zerowe uzyskane metodą stycznych')


    plt.plot(help,wartosci,label='zadana funkcja')
    plt.plot(help,pochodna(help),color='green',label='pierwsza pochodna')
    plt.plot(help,pochodna2(help),color='orange',label='druga pochodna')


    plt.plot(help,zero,color='black')
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Wykres funkcji i jej znalezione miejsce zerowe")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 8})
    plt.tight_layout()
    plt.show()


