import random

class Lotto:
    # 6 din 49     (n=6, minim=1, maxim=49)
    # 6 din 90     (n=6, minim=1, maxim=90)
    # 20 din 80    (n=20, minim=1, maxim=80)
    def __init__(self, cate, maxim):
        self.n = cate
        self.min = 1
        self.max = maxim

    def genereaza_numar(self):
        return random.randint(self.min, self.max)
    
    def genereaza_numere(self):
        numere = []
        while len(numere) < self.n:
            nr_nou = self.genereaza_numar()
            if nr_nou not in numere:
                numere.append(nr_nou)
        return numere


lottoRomania = Lotto(6, 49)
print("Romania", lottoRomania.genereaza_numere())
lottoItalia = Lotto(6, 90)
print("Italia", lottoItalia.genereaza_numere())
lottoPolonia = Lotto(20, 80)
print("Polonia", lottoPolonia.genereaza_numere())




