import skrypty as sk
import funkcje as fun
import rysunki as r
import funkcje as fun

dict = {"1": (fun.cosinus,fun.cosinus_pochodna,fun.cosinus_pochodna2),
        "2": (fun.wykładnicza,fun.wykładnicza_pochodna,fun.wykładnicza_pochodna2),
        "3": (fun.złożenie,fun.złożenie_pochodna,fun.złożenie_pochodna2)}



def wczytaj_wielomian():
    print("Podaj stopien wielomianu: ", end='')
    stopien = input()
    tab = []
    for i in range(int(stopien) + 1):
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
            a = float(input())
            print("b:",end=' ')
            b = float(input())

            print("Wybierz kryterium zatrzymania algorytmu")
            print("1) |f(x)| < e.")
            print("2) Osiągnięcie zadanej liczby iteracji.")
            warunek = input()

            print("Podaj wartość e/liczby iteracji")
            wartosc = input()

            if warunek == '1':
                epsilon = float(wartosc)
                iteracja = 0
            elif warunek == '2':
                epsilon = 0
                iteracja = float(wartosc)
            ob = sk.Obliczenia()
            x1 = ob.bisekcja(funkcje[0], a, b, epsilon, iteracja)
            x2 = ob.styczne(funkcje[0],funkcje[1],funkcje[2], a, b, epsilon, iteracja)

            if x1 != None:
                print("METODA BISEKCJI")
                print("Wartość znaleziona: " + str(x1))
                print("Ilośc potrzebnych iteracji: " + str(ob.bisekcjaiteracje))
            else:
                print("METODA BISEKCJI NIE ZNALAZŁA ROZWIĄZANIA")
            if x2 != None:
                print("METODA STYCZNYCH")
                print("Wartość znaleziona: " + str(x2))
                print("Ilośc potrzebnych iteracji: " + str(ob.iteracjestyczne))
            else:
                print("METODA STYCZNYCH NIE ZNALAZŁA ROZWIĄZANIA")

            r.wykres_funkcji(funkcje[0], funkcje[1], funkcje[2], a, b, x1, x2)




if __name__ == '__main__':
   # print()
    menu()
    #ob = sk.Obliczenia()
   # wielomian = fun.Wielomian([3,6,-4])
   # pochodna = fun.Wielomian(wielomian.pochodna())
   # x1 = ob.bisekcja(wielomian.wartosc,-1,3,0.01,0)
   # x2 = ob.styczne(wielomian.wartosc,pochodna.wartosc,pochodna.pochodna_wartosc,-1,1,0.01,0)
   # r.wykres_funkcji(wielomian.wartosc, -1, 1, x1, x2)
    #print(ob.styczne(fun.cosinus,fun.cosinus_pochodna,fun.cosinus_pochodna2,0,3,0.01,0))



