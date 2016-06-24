first = 1
second = 2
sumOfFibonacci = 0

while second <= 4000000:
	if second % 2 == 0:
		sumOfFibonacci += second

	tmp = first + second
	first = second
	second = tmp

print sumOfFibonacci