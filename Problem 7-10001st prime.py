# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def isPrime(n):
	i=2
	while i*i<=n:
		if n%i==0:
			return False
		i+=1
	return True

pr=2
i=2
c=1
while c<10002:
	if isPrime(i):
		pr=i
		c+=1
	i+=1

print(pr)
