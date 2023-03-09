import skrypty as sk
import funkcje as fun
import rysunki as r

dict = {"1": (fun.cosinus,fun.cosinus_pochodna,fun.cosinus_pochodna2),
        "2": (fun.wykładnicza,fun.wykładnicza_pochodna,fun.wykładnicza_pochodna2),
        "3": (fun.złożenie,fun.złożenie_pochodna,fun.złożenie_pochodna2)}



def wczytaj_wielomian():
    print("Podaj stopien wielomianu: ", end='')
    stopien = input()
    tab = []
    for i in range(int(stopien)):
        print(f"Podaj wartosc {i + 1} wspolczynnika: ", end=' ')
        wsp = input()
        wsp = int(wsp)
        tab.append(wsp)
    return tab

def menu():
    wybor = 1
    while wybor != '0':
        print("Wybierz funkcje:")
        print("1: cos(2x) - 1.5x")
        print("2: 2^x - 6")
        print("3: 3^sin(x) - 2")
        print("4: wielomian")
        print("0: wyjscie")
        wybor = input()

        try:
            int(wybor)
        except:
            wybor = '0'

        if wybor != '0':
            if wybor == '4':
                tab = wczytaj_wielomian()
                wielomian = fun.Wielomian(tab)
                pochodna = fun.Wielomian(wielomian.pochodna())
                funkcje = (wielomian.wartosc,pochodna.wartosc,pochodna.pochodna_wartosc)

            else:
                funkcje = dict[wybor]




            print("Podaj przedział [a,b] na którym poszukiwane jest miejsce zerowe")
            print("a:",end=' ')
            a = input()
            print("b:",end=' ')
            b = input()

            print("Wybierz kryterium zatrzymania algorytmu")
            print("1) |f(x)| < e.")
            print("2) Osiągnięcie zadanej liczby iteracji.")
            warunek = input()

            print("Podaj wartość e/liczby iteracji")
            wartosc = input()


            x1 = sk.Obliczenia.bisekcja(funkcje[0], a, b, warunek, wartosc)
            x2 = sk.Obliczenia.styczne(funkcje[0],funkcje[1],funkcje[2], a, b, warunek,wartosc)

            r.wykres_funkcji(funkcje[0],a,b,x1,x2)
            print("Naciśnij klawisz aby kontynuować")
            input()





if __name__ == '__main__':
   # print()
    menu()



