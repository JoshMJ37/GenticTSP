import numpy
import scipy
from scipy.spatial.distance import pdist
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]
arr = []
cost = 29
file = open(inputFile, 'r')
for line in file:
    fields = line.split(" ")
    arr.append((float(fields[1]),float(fields[2])))
file.close()

file = open(outputFile, 'w')
file.write(str(cost)+'\n')
file.write(str(arr))
file.close()

print(time, inputFile, outputFile)
# print(arr)

tsp(inputFile, outputFile, time)

def tsp(input_coor, output-tour, time):
    print('function goes here')



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

    return arr[base + maxNode]

