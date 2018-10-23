class MyList(object):
	'''自定义一个可迭代对象'''
	def __init__(self):
		self.items = []

	def add(self,val):
		self.items.append(val)

	# __iter__ method returns a Iterator
	def __iter__(self):
		my_iterator = MyIterator(self)
		return my_iterator


class MyIterator(object):
	'''自定义一个供上面可迭代对象使用的迭代器'''
	def __init__(self, mylist):
		self.mylist = mylist 
		# current record the current index
		self.current = 0

	def __next__(self):
		if self.current < len(self.mylist.items):
			item = self.mylist.items[self.current]
			self.current += 1
			return item
		else:
			raise StopIteration

	def __iter__(self):
		return self

if __name__ == '__main__':
	mylist = MyList()
	'''
	mylist是可迭代对象的一个instance, 可迭代对象的iter方法返回一个迭代器，
	这个迭代器的类中需要iter和next两个方法，一个获取迭代器，一个用这个迭代器获取
	下一个数据 ''' 
	mylist.add(1)
	mylist.add(2)
	mylist.add(3)
	for num in mylist:
		print(num)