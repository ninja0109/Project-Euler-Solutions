#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def isPal(n):
	if str(n)==str(n)[::-1]:
		return True
	else:
		return False

largestNumber=0

for i in range(100,999):
	for j in range(100,999):
		if isPal(i*j) and i*j>largestNumber:
			largestNumber=i*j

print(largestNumber)
