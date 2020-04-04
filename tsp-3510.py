import numpy
import scipy
from scipy.spatial.distance import pdist
import sys
import tsp

POP_SIZE = 20

def tspGenetic(allNodes, outputFile, time):
    dists = np.round(pdist(allNodes))
    gen = 1
    gen_thresh = 100

    population = [[[],None] for _ in range(POP_SIZE)]

    for i in POP_SIZE:
        tour = tsp.create_gnome()
        population[i] = [tour, tsp.cal_fitness(tour)]

    found = False
    temp = 10000

    while temp > 1000 and gen <= gen_thresh:
        population.sort(key=lambda x: x[1])
        newPop = [[[],None] for _ in range(POP_SIZE)]

        for i in range(POP_SIZE):
            p1 = population[i]

            while(True):
                new_tour = tsp.mutatedGene(p1[1])
                ntF = cal_fitness(new_tour)

                if ntF <= population[i][1]:
                    newPop[i] = [new_tour, ntF]
                    break
                else:
                    prob = pow(2.7, -1*(ntF - population[i][1])) / temp

                    if prob > 0.5:
                        newPop[i] = [new_tour, ntF]

        temp = np.round(temp * 0.9)
        population = np.array(newPop).tolist()

    population.sort(key=lambda x: x[1])
    print(f"Min tour cost: {population[0][1]}")
    print(f"Tour:\n{population[0][0]}")




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

def get_cost(tour, arr, numNodes):
    cost = 0
    for i in range(len(tour) - 1):
        cost += get_pdist(tour[i], tour[i+1], arr, numNodes)

    return cost


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

    file = open(outputFile, 'w')
    file.write(str(cost)+'\n')
    file.write(str(allNodes))
    file.close()

    print(time, inputFile, outputFile)
    tsp(allNodes, outputFile, time)
