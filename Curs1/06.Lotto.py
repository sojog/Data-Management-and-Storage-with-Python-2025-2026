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


class LottoRomania(Lotto):
    def __init__(self):
        super().__init__(6, 49)

class LottoItalia(Lotto):
    def __init__(self):
        super().__init__(6, 90)

class LottoPolonia(Lotto):
    def __init__(self):
        super().__init__(20, 80)  


lottoRomania = LottoRomania()
print("Romania", lottoRomania.genereaza_numere())
lottoItalia = LottoItalia()
print("Italia", lottoItalia.genereaza_numere())
lottoPolonia = LottoPolonia()
print("Polonia", lottoPolonia.genereaza_numere())




