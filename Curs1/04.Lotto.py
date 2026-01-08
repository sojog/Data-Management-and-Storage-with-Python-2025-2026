import random

class Lotto:
    def __init__(self, minim, maxim):
        self.min = minim
        self.max = maxim

    def genereaza_numar(self):
        return random.randint(self.min, self.max)
    
    def genereaza_n_numere(self, n):
        numere = []
        while len(numere) < n:
            nr_nou = self.genereaza_numar()
            if nr_nou not in numere:
                numere.append(nr_nou)
        return numere


extragere = Lotto(1, 49)
numere = extragere.genereaza_n_numere(11)
print(numere)

numere = [ f"{i}\n" for i in numere ]
print(numere)

with open("04.numere_extrase_lista.txt", "a") as file_writer:
    file_writer.writelines(numere)



# for i in range(6):
#     nr = extragere.genereaza_numar()
#     print(nr)
#     with open("04.numere_extrase.txt", "a") as file_writer:
#         file_writer.write(str(nr) + "\n")




