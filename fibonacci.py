import sys

'''
Fibonacci Sequence implementation using Python 3
@Author AJ Catambay
'''

def fibonacci( sequenceLength ):
	current = 0
	next = 1
	hold = 0
	fibo = []

	for x in range(0,sequenceLength): # loops until reached the specified length of sequence

		if x == 0: # Important! pushes 0 as the first and current number during first iteration
			fibo.append(current)
		else:
			hold = current # holds the current value, to be used to get the next value, later
			current = next # moves the next value as the current value
			next = hold + current
			fibo.append(current)

	return fibo

# for testing purposes, uncomment the prin function and run 'python3 fibonacci.py [sequenceLength]' 
# print( fibonacci( int(sys.argv[1]) ) )