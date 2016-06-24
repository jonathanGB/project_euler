for a in xrange(1, 333):
	flag = False
	limitOfB = (1000 - a) / 2

	for b in xrange(a+1, limitOfB):
		c = 1000 - a - b

		if a**2 + b**2 == c**2:
			print "a(%d) * b(%d) * c(%d) is %d" % (a, b, c, a*b*c)
			flag = True
			break

	if (flag):
		break