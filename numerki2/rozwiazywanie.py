import numpy as np

class GaussSeidl:

    def policz(self,wspl, x):
        b = np.zeros(x.size, dtype="float")
        for i in range(x.size):
            for j in range(wspl.shape[0]):
                b[i] = b[i] + (x[j] * wspl[i][j])

        return b

    def policzX(self,wspl, x, b):
        wynik = 0
        for i in range(x.size):
            wynik = wynik + (x[i] * wspl[i])
        wynik = b - wynik
        return wynik

    def iteracja(self,wspl, x, b):
        for i in range(x.size):
            x[i] = self.policzX(np.delete(wspl[i], i), np.delete(x, i), b[i]) / wspl[i][i]

    def zbieznosc(self,wspl):

        for i in range(wspl.shape[0]):
            if (abs(wspl[i][i]) <= np.absolute(np.delete(wspl[i], i)).sum()):
                return False
        return True

    def zamienWiersze(self,wspl):

        for i in range(wspl.shape[0]):
            index = np.argmax(wspl[i])
            a = np.copy(wspl[i])
            b = np.copy(wspl[index])
            wspl[i] = b
            wspl[index] = a

        return wspl

    def rozwiaz(self,wspl,b, dokladnosc,iteracje):

        if(iteracje != 0):
            self.ilosciteracji = iteracje

        x = np.zeros(wspl.shape[0], dtype="float")

        if(not self.zbieznosc(wspl)):
            wspl = self.zamienWiersze(wspl)


        if (self.zbieznosc(wspl)):
            warunek = True
            while (warunek and iteracje > -50):
                iteracje -= 1
                self.iteracja(wspl, x, b)
                if(iteracje == 0):
                    return x
                wynik = self.policz(wspl, x)
                for i in range(x.size):
                    if (abs(wynik[i] - b[i]) > dokladnosc):
                        break
                    elif (i == x.size - 1):
                        warunek = False
        else:
            print("Podana macierz nie spełnia warunku zbieżności")
            self.ilosciteracji = None
            return None
        self.ilosciteracji = abs(iteracje)
        return x