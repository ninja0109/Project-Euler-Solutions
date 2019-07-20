#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def lcm(m,n):
	if m>n:
		i=n
		while i%m!=0:
			i+=n
			print(i)
	else:
		i=m
		while i%n!=0:

			i+=m
			print(i)
	return i
  
  for i in range(1,20):
	p=lcm(i,p)
  
  print(p)
