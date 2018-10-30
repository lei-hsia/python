
# template method pattern

from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
	'''declare as metaclass;
	a metaclass is different from a superclass, in that it
	provides a template for the class definitin itself.
	Since it's now a template, then the ABCMeta declaration
	assures that the constructor for the class raises an error'''

	# our own version of collections.Sequence abstract base class

	@abstractmethod
	def __len__(self):
		'''return the length of the sequence '''

	@abstractmethod
	def __getitem__(self, j):
		'''return the element at index j of the sequence'''

	def __contains__(self, val):
		'''return True of val found in sequence, False otherwise'''
		for j in range(len(self)):
			if self[j] == val:
				return True
			return False

	def index(self, val):
		# return leftmost index at which val is found
		for j in range(len(self)):
			if self[j] == val:
				return j
		raise ValueError("value not in a sequence")

	def count(self, val):
		# retutn # elements equal to given value
		k = 0
		for j in range(len(self)):
			if self[j] == val:
				k += 1
		return k