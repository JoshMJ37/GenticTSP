import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]
time = sys.argv[3]
arr = []
cost = 29
file = open(inputFile, 'r')
for line in file:
	fields = line.split(" ")
	arr.append((int(float(fields[1])),int(float(fields[2]))))
file.close()

file = open(outputFile, 'w') 
file.write(str(cost)+'\n')
file.write(str(arr)) 
file.close() 

print(time, inputFile, outputFile)
print(arr)