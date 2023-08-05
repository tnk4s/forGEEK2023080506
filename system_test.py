import random
import numpy as np

import insertCalendarv2 as IC

def ActiveTime():
    y = np.random.randint(0, 2, 1020)

    return y

class Iden:
    def __init__(self, generation):
        self.IC = IC.InsertCalendarv2(15)
        self.plan_num = 30
        self.gene = []
        for i in range(self.plan_num):
            self.gene.append(self.IC.generate_plan())
        self.gene = np.array(self.gene)
        self.AT = ActiveTime()
        kisota, eal = self.IC.kiso_table
        self.PS = np.tile(kisota, (self.plan_num, self.gene.shape[1], 1))
        self.generation = generation

    def calc_fitness(self, gene):
        extended = np.tile(self.AT, (gene.shape[0],gene.shape[1],1))
        adama1 = extended * gene
        adama2 = self.PS * gene
        tonari = []
        for i in range(gene.shape[0]):
            tonari2 = 0
            for j in range(gene.shape[1]):
                tonari3 = 0
                for k in range(gene.shape[2]-1):
                    tonari3 += gene[i][j][k] * gene[i][j][k+1]
                tonari2 += tonari3   
            tonari.append(tonari2)
        fitness = adama1.sum(axis=(1,2)) + adama2.sum(axis=(1,2)) + np.array(tonari)
        return fitness

    # 選択

    def select_elite(self, gene, fitness):

        sort_index = np.argsort(fitness)[::-1]
        select_gene = gene[sort_index[:2], :, :]

        return select_gene, sort_index[0]

    # 交叉
    def crossover(self, p1, p2):

        genom_list = np.zeros((p1.shape[0], p1.shape[1]))

        for i in range(p1.shape[0]):

            for j in range(p1.shape[1]):
                if np.random.rand() < 0.5:
                    genom_list[i, j] = p1[i, j]
                else:
                    genom_list[i, j] = p2[i, j]

        return genom_list

    # 突然変異
    def mutaion(self, genoms, individual_mutation, genom_mutation):

        next_gene = np.zeros((genoms.shape[0], genoms.shape[1], genoms.shape[2]))

        for n, genom in enumerate(genoms):
            genom2 = np.zeros((genoms.shape[1], genoms.shape[2]))

            if np.random.rand() < individual_mutation:

                for i in range(genom.shape[0]):

                    for j in range(genom.shape[1]):
                        if np.random.rand() < genom_mutation:

                            genom2[i, j] = int(not genom[i, j])

                        else:
                            genom2[i, j] = genom[i, j]

            else:
                next_gene[n, :, :] = genom

        return next_gene

    def run_genetic_algorithm(self):
        gene = self.gene
        #print(gene)
        gen_num = gene.shape[0]
        task_num = gene.shape[1]
        time = gene.shape[2]
        for i in range(self.generation):
            # 適応度の計算
            fitness = self.calc_fitness(gene)
            max_index = np.argsort(fitness)[::-1][0]
            print(f'{i+1}世代：最大{max(fitness)}')
            # エリート選択
            select_gene, max_index = self.select_elite(gene, fitness)

            p1 = select_gene[0]
            p2 = select_gene[1]

            # 交叉
            genoms = np.zeros((gen_num, task_num, time))

            for i in range(gen_num):
                genoms[i, :, :] = self.crossover(p1, p2)

            gene = self.mutaion(genoms, 0.01, 0.2)
        
        fitness = self.calc_fitness(gene)
        max_index = np.argsort(fitness)[::-1][0]
        print(gene[max_index, :, :])

        return gene[max_index, :, :]

generation = 30
IA = Iden(generation)
IA.run_genetic_algorithm()