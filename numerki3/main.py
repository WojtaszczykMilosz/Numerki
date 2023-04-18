import rysunki as rysuj
import funkcje as fun
#
dict = {"1": fun.liniowa,
        "2": fun.modulX,
        "4": fun.trygonometryczna}


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

            print("Podaj przedział [a,b] na którym poszukiwane jest miejsce zerowe")
            print("a:", end=' ')
            a = float(input())

            print("b:", end=' ')
            b = float(input())


            print("Podaj liczbę węzłów")
            iloscWezlow = int(input())

            rysuj.wykres_funkcji(funkcja,a,b,iloscWezlow)



if __name__ == '__main__':
    menu()