num = 10
flag = False

while True:
	for i in xrange(2, 21):
		if num % i != 0:
			break
		elif i == 20:
			flag = True
			break

	if (flag == True):
		break

	num += 1

print num