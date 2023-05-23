import rysowanie as rysuj
import funkcje as fun

#
dict = {"1": fun.liniowa,
        "2": fun.modulX,
        "4": fun.trygonometryczna,
        "5": fun.zlozenie}


def wczytaj_wielomian():
    print("Podaj stopien wielomianu: ", end='')
    stopien = input()
    tab = []
    for i in range(int(stopien) + 1):
        print(f"Podaj wartosc {int(stopien) + 1 - i} wspolczynnika: ", end=' ')
        wsp = input()
        wsp = int(wsp)
        tab.append(wsp)
    return tab


def menu():
    wybor = 1
    while wybor != '0':



        print("Wybierz funkcje:")
        print("1: liniowa")
        print("2: |x|")
        print("3: wielomian")
        print("4: trygonometryczna")
        print("5: zlozenie")
        print("0: wyjscie")
        wybor = input()

        try:
            int(wybor)
        except:
            wybor = '0'

        if wybor != '0':
            if wybor == '3':
                tab = wczytaj_wielomian()
                wielomian = fun.Wielomian(tab)

                funkcja = (wielomian.obliczWartosc)

            else:
                funkcja = dict[wybor]




            print("Podaj liczbę węzłów - 100")
            iloscWezlow = 100

            print("Wybierz tryb:")
            print("1: Podawanie stopnia wielomianu")
            print("2: Obliczanie aproksymacji z dokladnoscia")

            tryb = input()
            if tryb ==  "1":
                print("Podaj stopien wielomianu aproksymujacego - Legendre'a")
                stopienWielomianu = int(input())
                rysuj.rysujWartosci(-1, 1, funkcja, iloscWezlow, stopienWielomianu)
            elif tryb == "2":
                print("Podaj dokladnosc z jaka ma byc aproksymowana wybrana funkcja")
                dok = float(input())
                rysuj.rysujWartosci(-1, 1, funkcja, iloscWezlow, dokladnosc=dok)








if __name__ == '__main__':
    menu()
