longestChain = {"length": 0, "number": 0}

def collatzEven(number):
	return number/2

def collatzOdd(number):
	return 3*number + 1


for i in range(2, 1000000):
	collatzNumber = i
	length = 0

	while  collatzNumber != 1:
		length += 1

		if collatzNumber % 2 == 0:
			collatzNumber = collatzEven(collatzNumber)
		else:
			collatzNumber = collatzOdd(collatzNumber)

	if length > longestChain['length']:
		longestChain = {"length": length, "number": i}

print "%r" % longestChain