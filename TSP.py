import numpy as np
from scipy.spatial.distance import pdist

class GeneticUtil(object):
	"""docstring for TSP"""
	def __init__(self, allNodes):
		# super(TSP, self).__init__()
		self.allNodes = allNodes
		self.numNodes = len(allNodes)
		self.dists = np.round(pdist(allNodes))

	def get_pdist(self, n1, n2):
	    minNode = min(n1, n2)
	    maxNode = max(n1, n2)

	    if minNode == 1:
	        base = 0
	    else:
	        base = sumtorial(self.numNodes - 1) - sumtorial(self.numNodes - minNode)

	    return self.dists[base + maxNode - minNode - 1]

	def get_cost(self, tour):
	    cost = 0
	    for i in range(len(tour) - 1):
	        cost += self.get_pdist(tour[i], tour[i+1])

	    return cost

	# alternate func: returns list with costs per node
	def get_cost2(self, tour):
	    cost = 0
	    costlist = [0 for _ in range(len(tour))]
	    for i in range(len(tour) - 1):
	        val = self.get_pdist(tour[i], tour[i+1])
	        cost += val
	        costlist[i] += val
	        costlist[i+1] += val

	    costlist[0] = 0
	    costlist[-1] = 0

	    return cost, costlist

	#returns a randomly mutated path
	def mutatedGene(self, path):
	    n = len(path) - 1
	    rand1 = np.random.randint(1, n)
	    rand2 = np.random.randint(1, n)
	    while(rand1 == rand2):
	        rand2 = np.random.randint(1, n)
	    temp = path[rand1]
	    path[rand1] = path[rand2]
	    path[rand2] = temp
	    return path

	# alt func: mutates gene where rand1 is highes cost node
	def mutatedGene2(self, path, ntCL):
	    n = len(path) - 1
	    rand1 = np.argmax(ntCL)
	    rand2 = np.random.randint(1, n)
	    while(rand1 == rand2):
	        rand2 = np.random.randint(1, n)
	    temp = path[rand1]
	    path[rand1] = path[rand2]
	    path[rand2] = temp
	    return path

	def createGnome(self):
	    gnome = [1]
	    rem = np.arange(1, self.numNodes) + 1

	    while (len(rem)):
	        temp = np.random.randint(len(rem))

	        gnome.append(rem[temp])
	        rem = np.delete(rem, temp)

	    gnome.append(1)
	    return gnome

	def onlyMins(self):
	    path = [1]
	    rem = np.arange(1, self.numNodes) + 1

	    while len(rem):
	        # print(path)
	        cost = None
	        nextNode = None
	        for ind, j in enumerate(rem):
	            curr = self.get_pdist(path[-1], j)
	            if not cost or curr < cost:
	                cost = curr
	                nextNode = (j, ind)

	        if nextNode:
	            path.append(nextNode[0])
	            rem = np.delete(rem, nextNode[1])
	        else:
	            path.append(rem[0])
	            rem = np.delete(rem, 0)

	    path.append(1)
	    # print(path)
	    # print(get_cost(path, dists))
	    return path


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
