
# generator that computes factors
def factor(n):
	k  = 1
	while k * k < n:
		if n % k ==0:
			yield k
			yield n/k
		k += 1
	if k * k == n:  # special case if n is perfect square
		yield k

