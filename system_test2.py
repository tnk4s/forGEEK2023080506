from datetime import datetime
import random
from decimal import Decimal
import numpy as np
from itertools import zip_longest

def Yutarou(x):
    z = np.random.randint(0, 2, (5, 3, 3))

    return z

#Yutarou(5)

class Algo:
    def __init__(self):
        self.gene = Yutarou(5) # ゆうたろうから受け取った配列
        self.selected = []
        self.children = []
        self.mutation_ratio = 0.1
        self.best = []
        self.worst = []

    def get_fitness(self):
        fitness = self.gene.sum(axis=(1,2))
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


