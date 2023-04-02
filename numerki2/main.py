import numpy as np
import rozwiazywanie as roz
import operacjePlikowe as pliki



def menu():
    wybor = 1
    while wybor != '0':
        print("Wybierz układ równań:")
        print("1: Układ początkowy")
        print("2: Wczytaj układ z pliku 'uklad.txt'")
        print("0: wyjscie")
        wybor = input()

        try:
            int(wybor)
        except:
            wybor = '0'

        if wybor != '0':

            if wybor == '1':
                wspl = np.array([[0.5, -0.0625, 0.1875, 0.0625], [-0.0625, 0.5, 0.0, 0.0], [0.1875, 0.0, 0.375, 0.125],
                                 [0.0625, 0.0, 0.125, 0.25]])
                b = np.array([1.5, -1.625, 1.0, 0.4375])


            elif wybor == '2':
                dane = pliki.wczytajZpliku('uklad.txt')
                wspl = []
                b = []
                for x in dane:
                    wspl.append(np.array(x[0]))
                    b.append(np.array(x[1]))

            print("Wybierz kryterium zatrzymania algorytmu")
            print("1) Osiągnięcie zadanej dokładności.")
            print("2) Osiągnięcie zadanej liczby iteracji.")
            warunek = input()

            print("Podaj wartość dokładności/liczby iteracji")
            wartosc = input()

            if warunek == '1':
                epsilon = float(wartosc)
                iteracja = 0
            elif warunek == '2':
                epsilon = 0
                iteracja = float(wartosc)

            algorytm = roz.GaussSeidl()

            if type(wspl) == list:
                for i in range(len(wspl)):
                    x = algorytm.rozwiaz(wspl[i],b[i],epsilon,iteracja)
                    if algorytm.ilosciteracji != None:
                        print(f"Obliczone rozwiązania dla równiania {i+1}: ")
                        print(x)
                        print("Ilośc potrzebnych iteracji: " + str(int (algorytm.ilosciteracji)))
            else:
                x = algorytm.rozwiaz(wspl, b, epsilon, iteracja)
                if algorytm.ilosciteracji != None:
                    print("Obliczone rozwiązania: ")
                    print(x)
                    print("Ilośc potrzebnych iteracji: " + str(int(algorytm.ilosciteracji)))







if __name__ == '__main__':
    menu()





