
class FibIterator(object):
	''' fibonacci series iterator '''
	def __init__(self, n):
		'''
		: param n: int, 指明生成数列的前n个数

		'''
		self.n = n
		# current: the n-th number
		self.current = 0
		# num1: previous number, initial value starts from 1st num 0
		self.num1 = 0
		# num2: previous number, initial value starts from 2nd num 1
		self.num2 = 1


	def __next__(self):
		'''
		被next()函数调用来获取下一个数
		'''
		if self.current < self.n:
			num = self.num1
			self.num1, self.num2 = self.num2, self.num1+self.num2
			self.current += 1
			return num
		else:
			raise StopIteration


	def __iter__(self):
		'''迭代器的iter返回自身即可'''
		return self



if __name__ == '__main__':
	fib = FibIterator(10)
	for num in fib:
		print(num, end=' ')