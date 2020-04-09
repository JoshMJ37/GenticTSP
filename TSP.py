import numpy as np
import random
from scipy.spatial.distance import pdist

class GeneticUtil(object):
	"""
		Here are a list of functiions which help solve the TSP problem
		with a genetic algorithm
	"""
	def __init__(self, allNodes):
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

	# returns a randomly mutated path
	def mutatedGene(self, path):
		n = len(path) - 1
		rand1 = np.random.randint(1, n)
		rand2 = np.random.randint(1, n)
		while(rand1 == rand2):
			rand2 = np.random.randint(1, n)
		temp = path[rand1]
		path[rand1] = path[rand2]
		path[rand2] = temp

	# returns a randomly mutated path, where there
	# is a mutationRate chance of changing each node for another
	def mutatedGeneLoop(self, path, mutationRate):
		n = len(path) - 1
		for pos1 in range(1, n):
			if random.random() < mutationRate:
				pos2 = np.random.randint(1, n)
				while(pos1 == pos2):
					pos2 = np.random.randint(1, n)
				temp = path[pos1]
				path[pos1] = path[pos2]
				path[pos2] = temp

	# depricated
	# 	initializes a random order tour
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

		path.append(path[0])
		return path

	# performs 2-opt for a given tour and recalculates cost
	# 	tour = gene[0]
	# 	cost = gene[1]
	def two_opt(self, gene):
		tour = np.array(gene[0]).tolist() # creates shallow copy
		costR = gene[1]
		winner = np.array(tour).tolist()

		cheaper = True
		while cheaper:
			cheaper = False

			for i in range(1, len(tour)-2):
				for j in range(i+1, len(tour)):
					if j-i == 1:
						continue
					new_tour = np.array(tour).tolist()
					new_tour[i:j] = tour[j-1:i-1:-1] # swap with 2-opt (reverse path between nodes)
					new_tour_cost = self.get_cost(new_tour)
					if new_tour_cost < costR:
						winner = new_tour
						costR = new_tour_cost
						cheaper = True

			tour = np.array(winner).tolist()

		return winner, costR


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
