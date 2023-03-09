import skrypty as sk




epsilon = 0.01


funkcja1 = [2,5,0]
pochodna1 = [4,5]


if __name__ == '__main__':
    object = sk.Obliczenia(funkcja1,1,0.01)
    print(object.bisekcja(pochodna1,-122,5,epsilon))
    print("wybierz funkcje:")
    print("1: ")
    print("2: ")
    print("3: ")


