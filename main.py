import skrypty as sk
import numpy as np
import rysunki as r
import funkcje as fun

dict = {"1":sk.Obliczenia.horner}
def menu():
    x = 1
    while x != 0:
        print("Wybierz funkcje:")
        print("1: ")
        print("2: ")
        print("3: ")
        print("0: wyjscie")
        x = input()
        dict['1'](0, [1, 1, 1])
        try:
            x = int(x)
        except:
            x = 0

        if x != 0:
            print("Podaj przedział [a,b] na którym poszukiwane jest miejsce zerowe")
            print("a:",end=' ')
            a = input()
            print("b:",end=' ')
            b = input()

            print("Wybierz kryterium zatrzymania algorytmu")
            print("1) |f(x)| < e.")
            print("2) Osiągnięcie zadanej liczby iteracji.")
            warunek = input()

            # r.wykres_funkcji()
            print("Naciśnij klawisz aby kontynuować")
            input()





if __name__ == '__main__':
   # print()
    #menu()
    obiekt = sk.Obliczenia()
    print(obiekt.styczne(fun.złożenie,fun.złożenie_pochodna,fun.złożenie_pochodna2,2.3,2.9,0.001,0))



