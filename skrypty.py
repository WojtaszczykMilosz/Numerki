class Obliczenia:



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
            wartosc = wartosc*x + tab[a]
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


    def styczne(self,funkcja,pochodna,pochodna2,a,b,epsilon,iteracja):
        if funkcja(a) * funkcja(b) > 0:
            return None
        if pochodna(a) * pochodna2(a) > 0:
            xN = a
        elif pochodna(b) * pochodna2(b) > 0:
            xN = b
        else:
            return None
        while True:
            xN1 = xN - (funkcja(xN)/pochodna(xN))
            iteracja -= 1
            if abs(funkcja(xN1)) < epsilon:
                return xN1
            elif iteracja == 0:
                return xN1
            else:
                xN = xN1
