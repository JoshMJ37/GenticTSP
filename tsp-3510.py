import numpy as np
import sys
import time
# from timeit import default_timer as timer
from TSP import GeneticUtil

POP_SIZE = 20
elitism = 5
mutationRate = 0.05
tournySize = 10

show = 1

time_start = time.perf_counter()

def tspGenetic(genU, outputFile, timeout):
    start = genU.onlyMins()
    cS = genU.get_cost(start)

    population = [[start,cS] for _ in range(POP_SIZE)]

    for i in range(1, POP_SIZE):
        genU.mutatedGeneLoop(population[i][0], mutationRate)
        population[i][1] = genU.get_cost(population[i][0])

    gen = 0
    prevBestCost = min(np.array(population)[:, 1])
    sameCounter = -1

    # timeout functionality implemented in this while loop
    while sameCounter < 10 and time.perf_counter() - time_start < timeout - 1:
        print (f'time elaped: {time.perf_counter() - time_start: 0.4f}')
        population.sort(key=lambda x: x[1])
        if prevBestCost == population[0][1]:
            sameCounter += 1
        else:
            sameCounter = 0
        # print(f"sameCounter: {sameCounter}")

        if gen % show == 0:
            print(f"\nGeneration: {gen}")
            print(f"Best:  cost: {population[0][1]}")
            print(f"sameCounter: {sameCounter}")
            # print(f"Best:\n  cost: {population[0][1]}\n  tour: {population[0][0]}")
            # print(f"worst cost: {population[-1][1]}\n")

        newPop = [[[],None] for _ in range(POP_SIZE)]

        if elitism:
            newPop[:elitism] = population[:elitism]

        for i in range(elitism, POP_SIZE):
            if not elitism or np.random.randint(10) >= 7:
                p1 = tournyWinner(population, tournySize)
            else:
                p1 = tournyElite(population)

            p2 = tournyWinner(population, tournySize)

            child = breed(p1, p2)
            newPop[i] = [child, genU.get_cost(child)]

        for i in range(elitism, POP_SIZE):
            genU.mutatedGeneLoop(newPop[i][0], mutationRate)
            newPop[i] = genU.two_opt(newPop[i])

        prevBestCost = population[0][1]
        population = np.array(newPop).tolist() # creates shallow copy
        gen += 1

    population.sort(key=lambda x: x[1])
    print(f"Min tour cost: {population[0][1]}")
    print(f"Tour:\n{population[0][0]}")

    print (f'END time elaped: {time.perf_counter() - time_start: 0.4f}')
    return population[0]

# creates a child where child[rand1:rand2] is a segement from parent1 (p1)
# and the rest of child are the in-order nodes from parent2 (p2) that are not
# already in child
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

# creates a matingPool from random tours in population,
# then selects and returns most fit of random matingPool
# to be the returned parent
def tournyWinner(pop, tSize):
    tourny = []

    for i in range(tSize):
        randI  = np.random.randint(0, len(pop) - elitism)
        tourny.append(pop[randI])

    tourny.sort(key=lambda x: x[1])

    return tourny[0][0]

# creates a matingPool from elite tours in population,
# then selects and returns most fit of elite matingPool
# to be the returned parent
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
    timeout = int(sys.argv[3])
    allNodes = []
    file = open(inputFile, 'r')
    for line in file:
        fields = line.split(" ")
        allNodes.append((float(fields[1]),float(fields[2])))
    file.close()

    print(timeout, inputFile, outputFile)
    genU = GeneticUtil(allNodes)
    tour, cost = tspGenetic(genU, outputFile, timeout)

    file = open(outputFile, 'w')
    file.write(str(cost)+'\n')
    file.write(str(tour))
    file.close()
