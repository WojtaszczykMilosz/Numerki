
def zwrocPodzielonaLinie(file):
    line = file.readline()
    line = line.replace('  ', ' ')
    line = line.replace('  ', ' ')
    line = line.strip()

    splitted = line.split(' ')
    return splitted

def wczytajDane():
    wspolczynniki = []
    pierwiastki = []

    with open('legendre.txt','r') as f:
        for i in range(0,99):
            tablica = zwrocPodzielonaLinie(f)
            n = int(tablica[2])
            wspolczynniki.append([])
            pierwiastki.append([])
            for x in range(n):
                tablica = zwrocPodzielonaLinie(f)
                wspolczynniki[i].append(float(tablica[0]))
                pierwiastki[i].append(float(tablica[1]))

            f.readline()
    return wspolczynniki, pierwiastki


class KwadraturaLegendre:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.wspolczynniki, self.pierwiastki = wczytajDane()

    def obliczKwadrature(self, funkcja, ileWezlow):

        wynik = 0
        for x in range(ileWezlow):

            wynik += self.wspolczynniki[ileWezlow-2][x] * \
                     self.przeskalowanaWartoscFunkcji(funkcja,self.pierwiastki[ileWezlow - 2][x])


        return wynik

    def przeskalowanaWartoscFunkcji(self, funkcja, t):
        x = ((self.b - self.a) * t + self.a + self.b) / 2
        dx = (self.b - self.a ) / 2

        return funkcja(x) * dx