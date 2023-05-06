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
wczytajDane()