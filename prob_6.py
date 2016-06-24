squareOfTheSum = sumOfTheSquares = 0

for i in range(1, 101):
	sumOfTheSquares += i**2
	squareOfTheSum += i

squareOfTheSum **= 2

print squareOfTheSum - sumOfTheSquares