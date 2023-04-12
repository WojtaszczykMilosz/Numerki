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






