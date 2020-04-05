import numpy as np
import scipy
from scipy.spatial.distance import pdist
import sys

import time

POP_SIZE = 5
numMutes = 3
prob_thresh = 0.01

def tspGenetic(allNodes, outputFile, time):
    dists = np.round(pdist(allNodes))
    numNodes = len(allNodes)
    gen = 1
    gen_thresh = 100

    population = [[[],None] for _ in range(POP_SIZE)]

    for i in range(POP_SIZE):
        tour = createGnome(numNodes)
        population[i] = [tour, get_cost(tour, dists)]

    temp = 10000

    while temp > 1000 and gen <= gen_thresh:
        population.sort(key=lambda x: x[1])
        print(f"\nGeneration: {gen}")
        print(f"Best:\n  cost: {population[0][1]}\n  tour: {population[0][0]}")
        newPop = [[[],None] for _ in range(POP_SIZE)]

        for i in range(POP_SIZE):
            p1 = population[i]

            while(True):
                new_tour = mutatedGene(p1[0])
                for j in range(numMutes):
                    new_tour = mutatedGene(new_tour)
                ntF = get_cost(new_tour, dists)

                # if ntF <= np.max(np.array(population)[:, 1]):
                if ntF <= population[i][1]:
                    newPop[i] = [new_tour, ntF]
                    break
                else:
                    prob = pow(2.7, -1*(ntF - population[i][1]) / temp)

                    if prob > prob_thresh:
                        newPop[i] = [new_tour, ntF]

        temp = np.round(temp * 0.9)
        population = np.array(newPop).tolist()
        gen += 1

    population.sort(key=lambda x: x[1])
    print(f"Min tour cost: {population[0][1]}")
    print(f"Tour:\n{population[0][0]}")

    return cost, population[0][0]


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def sumtorial(n):
    if n <= 1:
        return n
    else:
        return n + sumtorial(n-1)

def get_pdist(n1, n2, arr, numNodes):
    minNode = min(n1, n2)
    maxNode = max(n1, n2)

    if minNode == 1:
        base = 0
    else:
        base = sumtorial(numNodes - 1) - sumtorial(numNodes - minNode)

    return arr[base + maxNode - minNode - 1]

def get_cost(tour, arr):
    cost = 0
    numNodes = len(tour) - 1
    for i in range(len(tour) - 1):
        cost += get_pdist(tour[i], tour[i+1], arr, numNodes)

    return cost

# def repeat(path, tar, rem):
#     # for i in range(len(path)):
#     #     if (path[i] == tar):
#     #         return True
#     # return False

#     for i in range(len(path)):
#         if (path[i] == tar):
#             return True
#     return False


#returns a randomly mutated path
def mutatedGene(path):
    n = len(path) - 1
    rand1 = np.random.randint(1, n)
    rand2 = np.random.randint(1, n)
    while(rand1 == rand2):
        rand2 = np.random.randint(1, n)
    temp = path[rand1]
    path[rand1] = path[rand2]
    path[rand2] = temp
    return path

def createGnome(numNodes):
    gnome = [1]
    rem = np.arange(1, numNodes)+ 1

    while (len(rem)):
        temp = np.random.randint(len(rem))

        gnome.append(rem[temp])
        rem = np.delete(rem, temp)

    gnome.append(1)
    return gnome


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
    cost, tour = tspGenetic(allNodes, outputFile, time)

    file = open(outputFile, 'w')
    file.write(str(cost)+'\n')
    file.write(str(tour))
    file.close()
