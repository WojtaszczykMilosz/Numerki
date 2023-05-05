import funkcje as fun
import kwadratury as kw

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

            print("Podaj przedział calkowania [a,b)")
            print("a:", end=' ')
            a = float(input())

            print("b:", end=' ')
            b = float(input())

            print("Podaj dokladnosc dla kwadratury Newtona-Cotesa")
            dokladnosc = float(input())

            ileWezlow = 0
            while (ileWezlow < 2) or (ileWezlow > 5):
                print("Podaj ilosc wezlow dla kwadratury Gaussa-Legendre'a")
                ileWezlow = int(input())

            newton = kw.NewtonCotes(a, b, dokladnosc)
            leg = kw.Legendre(a, b)

            print(f"Wartości calki na przedziale [{a}, {b}) dla wybranej funkcji obliczone przy pomocy kwadratur wynoszą: ")

            print(f"Newton-Cotes: {newton.obliczKwadrature(funkcja)}, dokladnosc - {dokladnosc}")
            print(f"Gauss-Legendre: {leg.obliczKwadrature(funkcja,ileWezlow)}, ilosc wezlow - {ileWezlow}")

if __name__ == '__main__':
    menu()
