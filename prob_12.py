# get first triangular number >= 500
# loop (0, num)
	# if no good, get next triangular number. restart the loop with the new num
	# otherwise, we have our desired triangular number

import time
import math

value = 0
term = 1

start = time.clock()

def numOfDivisors(value):
	divisors = 0
	limit = int(math.sqrt(value))

	for i in range(1, limit+1):
		if value % i == 0:
			divisors += 2

	if limit**2 == value:
		divisors -= 1

	return divisors

while numOfDivisors(value) < 500:
	value += term
	term += 1
			

stop = time.clock()

print "The first triangular number with at least 500 divisors is %i / Process took %fs" % (value, stop-start)