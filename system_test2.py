from datetime import datetime
import random
from decimal import Decimal
import numpy as np
from itertools import zip_longest

def Yutarou():
    z = np.random.randint(0, 2, (5, 3, 3))

    return z

def ActiveTime():
    y = np.random.randint(0, 2, 3)

    return y

def PreSch():
    z = np.random.randint(0, 2, (5,3,3))


#Yutarou(5)

class Algo:
    def __init__(self):
        self.gene = Yutarou() # ゆうたろうから受け取った配列
        self.presch = PreSch()
        self.AT = ActiveTime()
        self.selected = []
        self.children = []
        self.mutation_ratio = 0.1
        self.best = []
        self.worst = []

    def get_fitness(self):
        extended = np.tile(self.AT, (5,3,1))
        adama1 = extended * self.gene
        adama2 = self.presch * self.gene
        fitness = adama.sum(axis=(1,2)) + adama2.sum(axis=(1,2))
        return fitness

    def mutate(self):
        tmp = self.gene.copy
        i = np.random.randint(0, len(self.gene[0])-1)
        for i in range(len(self.gene))
            tmp[i] = float(not self.gene[i])
        self.gene = tmp

    def cross(self):
        

    def select(self, gene):
        self.selected = []
        tournament = np.random.choice(self.gen, 3, replace=False)
        self.selected = max()

        return self.selected

    def mutate(self, children):
        for child in self.children:
            if np.random.rand() < self.mutation_ratio:
                
        return self.children


    def solve(self, gene):
        for i in range(num_of_gene):
            best_one = max(gene, key=get_fitness())
            self.best.append()
            worst_one = min(gene, key=get_fitness())
            self.worst.append()

            self.selected = select(self.gene)
            self.children = cross(self.selected)
            self.gene = mutate(self.children)
        
            print("best"+str(best_one)+"worst"+str(worst_one))
        
        return self.best, self.worst



    def do(self):
        self.best, self.worst = solve(self.gene)

        return self.best


