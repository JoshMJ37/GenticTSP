import numpy
import scipy
from scipy.spatial.distance import pdist


def tsp(input_coor, output-tour, time):
    read(input_coor)

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


# if __name__ == "__main__":
#     tsp()ls
#
