largestPalindrome = [-1, -1, -1]

for i in range(999, 100, -1):
	for j in range(i, 100, -1):
		product = i * j
		right = str(product)
		reverse = str(product)[::-1]


		if right == reverse and product > largestPalindrome[0]:
			largestPalindrome = [product, i, j]


print "The largest palindrome of the product of two 3-digit numbers is %d: it is the product of %d and %d" % (largestPalindrome[0], largestPalindrome[1], largestPalindrome[2])