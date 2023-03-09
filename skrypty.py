class Obliczenia:

    def __init__(self, funkcja, kryterium, wartosc):
        self.tab = funkcja
        self.kryterium = kryterium
        self.wartosc = wartosc
    #     self.ustaw_kryterium()

    def ustaw_kryterium(self):
        if self.kryterium:
            self.warunek = self.dokladnosc
        else:
            self.warunek = self.iteracje

    def dokladnosc(self,x):
        return abs(self.horner(x,self.tab)) < self.wartosc

    def iteracje(self, i):
        return i > self.wartosc

    @staticmethod
    def horner(x, tab):
        wartosc = tab[0]

        for a in range(1,len(tab)):
            wartosc += wartosc*x + tab[a]
        return wartosc

    def bisekcja(self,funckja,a,b,epsilon):
        if self.horner(a, funckja) * self.horner(b, funckja) > 0:
            return None
        x = (a + b) / 2
        while abs(self.horner(x, funckja)) > epsilon:
            x = (a + b) / 2
            if self.horner(x, funckja) * self.horner(a, funckja) < 0:
                b = x
            else:
                a = x
        return round(x,3)


    def styczne(self,funckja,pochodna,a,b,epsilon):
        if self.horner(a, funckja) * self.horner(b, funckja) > 0:
            return None
        x = (a + b) / 2
        while abs(self.horner(x, funckja)) > epsilon:
            x = x - self.horner(x, funckja) / self.horner(x, pochodna)
        return round(x,3)