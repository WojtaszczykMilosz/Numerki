class Obliczenia:

    @staticmethod
    def horner(x, tab):
        wartosc = tab[0]

        for a in range(1,len(tab)):
            wartosc = wartosc*x + tab[a]
        return wartosc

    def bisekcja(self,funkcja,a,b,epsilon,iteracja):
        if funkcja(a) * funkcja(b) > 0:
            self.bisekcjaiteracje = None
            return None

        if iteracja != 0:
            self.bisekcjaiteracje = iteracja

        while True:

            x = (a + b) / 2
            iteracja -= 1
            if abs(funkcja(x)) < epsilon:
                self.bisekcjaiteracje = abs(iteracja)
                return x
            elif iteracja == 0:
                return x

            if funkcja(x) * funkcja(a) < 0:
                b = x
            else:
                a = x


    def styczne(self,funkcja,pochodna,pochodna2,a,b,epsilon,iteracja):
        if funkcja(a) * funkcja(b) > 0:
            self.iteracjestyczne = None
            return None
        xN = a
        # if funkcja(a) * pochodna2(a) > 0:
        #     xN = a
        # elif funkcja(b) * pochodna2(b) > 0:
        #     xN = b
        # else:
        #     self.iteracjestyczne = None
        #     return None
        if iteracja != 0:
            self.iteracjestyczne = iteracja
        while True:
            xN1 = xN - (funkcja(xN)/pochodna(xN))
            iteracja -= 1
            # if xN1 > b or xN1 < a:
            #     self.iteracjestyczne = None
            #
            #     return None
            if abs(funkcja(xN1)) < epsilon:

                self.iteracjestyczne = abs(iteracja)
                return xN1
            elif iteracja == 0:
                return xN1
            elif iteracja < -50:
                return None
            else:
                xN = xN1

