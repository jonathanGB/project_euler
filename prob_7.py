import time

num = 2
numOfPrimes = 1

start = time.clock()
while numOfPrimes < 10001:
	num += 1

	for i in xrange(2, num):
		if num % i == 0:
			break
		elif i == num-1:
			numOfPrimes += 1
stop = time.clock()

print "The %ist is %i: processed in %f seconds" % (numOfPrimes, num, stop-start)