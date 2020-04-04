# import sys

# inputFile = sys.argv[1]
# outputFile = sys.argv[2]
# time = sys.argv[3]
# arr = []
# cost = 29
# file = open(inputFile, 'r')
# for line in file:
# 	fields = line.split(" ")
# 	arr.append((float(fields[1]),float(fields[2])))
# file.close()

# file = open(outputFile, 'w') 
# file.write(str(cost)+'\n')
# file.write(str(arr)) 
# file.close() 

# print(time, inputFile, outputFile)
# print(arr)

#check if target integer is already in the path array

import random as rand
import time

tic = time.perf_counter()
toc = time.perf_counter()
print (f'{toc - tic: 0.4f}')

def repeat(path, tar):
	for i in range(arr.len()):
		if (path[i] == tar):
			return true
	return false

#returns a randomly mutated path
def mutatedGene(path):
	rand1 = rand.randomint(1, n)
	rand2 = rand.randomint(1, n)
	while(rand1 == rand2):
		rand2 = rand.randomint(1, n)
	temp = path[rand1]
	path[rand1] = path[rand2]
	path[rand2] = temp
	return path

def createGnome():
	gnome = [0]
	while (gnmoe.count() != n):
		temp = rand.randomint(1, n)
		if not repeat(gnome, temp):
			gnome.append(temp)
	gnome.append(gnome[0])
	return gnome


