
'''
实现一个迭代器时, 当前迭代的状态需要我们自己记录, i.e. self.current,
进而很具当前状态生成下一条数据; 
为了达到纪录当前的状态，并配合next()函数进行迭代使用，可以采取更简单的方法，
i.e. 用生成器，生成器是一种特殊的迭代器

'''

### 1
# the first way to create a generator
G = ( x*2 for x in range(5))
G

### 2
# in the previous Iterator way of implementing an Iteratot,
# we have:
def __next__(self):
	if self.current < self.n:
		num = self.num1
		self.num1, self.num2 = self.num2, self.num1+self.num2
		self.current += 1
		return num
	else:
		raise StopIteration

# use a function via Generator to implement iteration:
def fib(n):
	current = 0
	num1, num2 = 0, 1
	while current < n:
		num = num1
		num1, num2 = num2, num1+num2
		current += 1
		yield num
	return 'done'
'''
each time the return is changed to yield, now the function is 
not a function, but a Generator.
In a word, inside def there is a yield, then it is a generator


yield 关键字的作用: 
1. 保存当前运行状态(断点), 然后暂停执行，将生成器挂起；
2. 将yield关键字后面的表达式的值作为返回值返回，理解为起到了return的作用

使用 next() 函数让生成器从断点处继续执行，唤醒生成器
除了用 next() 唤醒生成器之外, 还可以用 send() 函数唤醒； 
使用 send() 的好处是可以在唤醒的同时向断点处传入一个附加数据
''' 