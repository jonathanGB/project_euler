import time

sumOfPrimes = 2
primes = [2]

start = time.clock()

for i in range(3, 2000000, 2):
	for j in xrange(0, len(primes)):
		if i % primes[j] == 0:
			break
		elif j == len(primes) - 1:
			sumOfPrimes += i
			primes.append(i)
	
stop = time.clock()

print "The sum is %i: processed in %f seconds" % (sumOfPrimes, stop-start)