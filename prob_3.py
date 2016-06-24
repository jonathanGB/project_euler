import time

num = 600851475143
i = 2
largest = 1

start = time.clock()

while i <= num:
	if num % i == 0:
		largest = i
		num /= i
		i = 2
	else:
		i += 1

stop = time.clock()

print largest

print "Process time (in milliseconds): %f ms" % ((stop - start) * 1000)