import random
from decimal import Decimal
import numpy as np
from itertools import zip_longest

def Yutarou():
    z = np.random.randint(0, 2, (30, 10, 1020))

    return z

def ActiveTime():
    y = np.random.randint(0, 2, 1020)

    return y

def PreSch():
    z = np.random.randint(0, 2, (30,10,1020))

    return z


class FitNess:
    def __init__(self):
        self.gene = Yutarou() # ゆうたろうから受け取った配列
        self.presch = PreSch()
        self.AT = ActiveTime()

    def get_fitness(self):
        extended = np.tile(self.AT, (self.gene.shape[0],self.gene.shape[1],1))
        adama1 = extended * self.gene
        adama2 = self.presch * self.gene
        tonari = []
        for i in range(self.gene.shape[0]):
            tonari2 = 0
            for j in range(self.gene.shape[1]):
                tonari3 = 0
                for k in range(self.gene.shape[2]-1):
                    tonari3 += self.gene[i][j][k] * self.gene[i][j][k+1]
                tonari2 += tonari3   
            tonari.append(tonari2)
        fitness = adama1.sum(axis=(1,2)) + adama2.sum(axis=(1,2)) + np.array(tonari)
        return fitness

FN = FitNess()
print(str(FN.get_fitness()))

