import numpy as np
import sys
import time
from TSP import GeneticUtil

POP_SIZE = 10
NUM_GENS = 100
elitism = 1

numMutes = 1
prob_thresh = 0.001

def tspGenetic(genU, outputFile, time):

    population = [[[],None] for _ in range(POP_SIZE)]

    for i in range(POP_SIZE):
        tour = genU.createGnome()
        population[i] = [tour, genU.get_cost(tour)]


    temp = 10000

    for gen in range(NUM_GENS):
        population.sort(key=lambda x: x[1])
        print(f"\nGeneration: {gen}")
        print(f"Best:\n  cost: {population[0][1]}\n  tour: {population[0][0]}")
        newPop = [[[],None] for _ in range(POP_SIZE)]

        if elitism:
            newPop[:elitism] = population[:elitism]

        for i in range(elitism, POP_SIZE):
            p1 = population[i][0]


            while(True):
                new_tour = genU.mutatedGene(p1)
                for j in range(numMutes):
                    new_tour = genU.mutatedGene(new_tour)
                ntF = genU.get_cost(new_tour)
                # ntF, ntCL = get_cost2(new_tour, dists)

                # if ntF <= np.max(np.array(population)[:, 1]):
                if ntF <= population[i][1]:
                    newPop[i] = [new_tour, ntF]
                    break

        temp = np.round(temp * 0.9)
        population = np.array(newPop).tolist()
        gen += 1

    population.sort(key=lambda x: x[1])
    print(f"Min tour cost: {population[0][1]}")
    print(f"Tour:\n{population[0][0]}")

    return cost, population[0][0]


def breed(p1, p2, child):
    ind = 0
    for item in p2:
        if item not in child:
            for j in range(ind, len(child)):
                if not child[j]:
                    child[j] = item
                    ind += 1
                    break
    return child

if __name__ == '__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    time = sys.argv[3]
    allNodes = []
    # cost = None
    file = open(inputFile, 'r')
    for line in file:
        fields = line.split(" ")
        allNodes.append((float(fields[1]),float(fields[2])))
    file.close()

    print(time, inputFile, outputFile)
    genU = GeneticUtil(allNodes)
    cost, tour = tspGenetic(genU, outputFile, time)

    file = open(outputFile, 'w')
    file.write(str(cost)+'\n')
    file.write(str(tour))
    file.close()
