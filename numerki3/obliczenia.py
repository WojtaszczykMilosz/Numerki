def horner(x, tab):
    wartosc = tab[0]

    for a in range(1, len(tab)):
        wartosc = wartosc * x + tab[a]
    return wartosc