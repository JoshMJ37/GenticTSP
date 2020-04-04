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



# import random as rand

# #check if target integer is already in the path array
# def repeat(path, tar):
# 	for i in range(arr.len()):
# 		if (path[i] == tar):
# 			return true
# 	return false

# #returns a randomly mutated path
# def mutatedGene(path):
# 	rand1 = rand.randomint(1, n)
# 	rand2 = rand.randomint(1, n)
# 	while(rand1 == rand2):
# 		rand2 = rand.randomint(1, n)
# 	temp = path[rand1]
# 	path[rand1] = path[rand2]
# 	path[rand2] = temp
# 	return path

# def createGnome():
# 	gnome = [0]
# 	while (gnmoe.count() != n):
# 		temp = rand.randomint(1, n)
# 		if not repeat(gnome, temp):
# 			gnome.append(temp)
# 	gnome.append(gnome[0])
# 	return gnome








# import time

# tic = time.perf_counter()
# toc = time.perf_counter()
# print (f'{toc - tic: 0.4f}')

# import sys

# listofitems = []
# if len(listofitems) < 2:
#   sys.exit('listofitems not long enough')

# import signal
# from contextlib import contextmanager

# @contextmanager
# def timeout(time):
#     # Register a function to raise a TimeoutError on the signal.
#     signal.signal(signal.SIGALRM, raise_timeout)
#     # Schedule the signal to be sent after ``time``.
#     signal.alarm(time)

#     try:
#         yield
#     except TimeoutError:
#         pass
#     finally:
#         # Unregister the signal so it won't be triggered
#         # if the timeout is not reached.
#         signal.signal(signal.SIGALRM, signal.SIG_IGN)


# def raise_timeout(signum, frame):
# 	# print('tipme exceeds')
#     raise TimeoutError


# # def my_func():
#     # Add a timeout block.
# with timeout(1):
#     print('entering block')
#     import time
#     time.sleep(10)
#     print('This should never get printed because the line before timed out')

import threading
from functools import wraps
def delay(delay=0.):
    """
    Decorator delaying the execution of a function for a while.
    """
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap


class Timer():
    toClearTimer = False
    def setTimeout(self, fn, time):
        isInvokationCancelled = False
        @delay(time)
        def some_fn():
                if (self.toClearTimer is False):
                        fn()
                else:
                    print('Invokation is cleared!')        
        some_fn()
        return isInvokationCancelled
    def setClearTimer(self):
        self.toClearTimer = True


timer = Timer()
def some_fn():
    print('Python is not JS')
timer.setTimeout(some_fn, 3.0) 
#  Above will execute some_fn call after 3 sec

# Above line of codes will not execute some_fn call as timer is cleared before 3 seconds