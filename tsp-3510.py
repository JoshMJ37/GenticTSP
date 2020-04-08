import numpy as np
import sys
import time
from TSP import GeneticUtil

POP_SIZE = 20
NUM_GENS = 30000
elitism = 5

show = 100

def tspGenetic(genU, outputFile, time):

    population = [[[],None] for _ in range(POP_SIZE)]

    for i in range(POP_SIZE):
        tour = genU.createGnome()
        population[i] = [tour, genU.get_cost(tour)]

    for gen in range(NUM_GENS):
        population.sort(key=lambda x: x[1])
        if gen % show == 0:
            print(f"\nGeneration: {gen}")
            print(f"Best:\n  cost: {population[0][1]}\n  tour: {population[0][0]}")
        newPop = [[[],None] for _ in range(POP_SIZE)]

        if elitism:
            newPop[:elitism] = population[:elitism]

        for i in range(elitism, POP_SIZE):
            if np.random.randint(10) >= 7:
                p1 = tournyWinner(population)
            else:
                p1 = tournyElite(population)

            p2 = tournyWinner(population)

            child = breed(p1, p2)
            newPop[i] = [child, genU.get_cost(child)]

        for i in range(elitism, POP_SIZE):
            genU.mutatedGene(newPop[i][0])
            newPop[i][1] = genU.get_cost(newPop[i][0])

        population = np.array(newPop).tolist()

    population.sort(key=lambda x: x[1])
    print(f"Min tour cost: {population[0][1]}")
    print(f"Tour:\n{population[0][0]}")

    return population[0]


def breed(p1, p2):
    ind = 0

    child = [0 for _ in p1]
    child[0] = 1
    child[-1] = 1

    n = len(child) - 1
    rand1 = np.random.randint(1, n)
    rand2 = np.random.randint(1, n)

    while abs(rand2 - rand1) < 3:
        rand2 = np.random.randint(1, n)

    startN = min(rand1, rand2)
    endN = max(rand1, rand2)
    child[startN:endN] = p1[startN:endN]

    for item in p2:
        if item not in child:
            for j in range(ind, len(child)):
                if not child[j]:
                    child[j] = item
                    ind += 1
                    break
    return child

def tournyWinner(pop):
    tourny = []

    for i in range(len(pop)):
        randI  = np.random.randint(0, len(pop))
        tourny.append(pop[randI])

    tourny.sort(key=lambda x: x[1])

    return tourny[0][0]

def tournyElite(pop):
    tourny = []

    for i in range(elitism):
        randI  = np.random.randint(0, elitism)
        tourny.append(pop[randI])

    tourny.sort(key=lambda x: x[1])

    return tourny[0][0]

if __name__ == '__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    time = sys.argv[3]
    allNodes = []
    file = open(inputFile, 'r')
    for line in file:
        fields = line.split(" ")
        allNodes.append((float(fields[1]),float(fields[2])))
    file.close()

    print(time, inputFile, outputFile)
    genU = GeneticUtil(allNodes)
    tour, cost = tspGenetic(genU, outputFile, time)

    file = open(outputFile, 'w')
    file.write(str(cost)+'\n')
    file.write(str(tour))
    file.close()
