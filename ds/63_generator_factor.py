
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

# https://letstalkdata.com/2015/05/how-to-use-python-generators-to-save-memory/
# python中的generator类似于C++中的dynamic binding, 只会在需要的每一次动态生成，而不会从一开始就都生成好
