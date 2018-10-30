
# operator overloading: and then you can add objects

class Day(object):

	def __init__(self, visits, contacts):
		self.visits = visits
		self.contacts = contacts

	def __add__(self,other):
		'''overloading the default + operator'''
		total_visits = self.visits + other.visits
		total_contacts = self.contacts + other.contacts
		return Day(total_visits, total_contacts)

	def __radd__(self, other):
		'''when the reverse add is called'''
		if other ==0:
			return self
		else:
			return self.__add__(other)

	def __str_(self):
		return "Visits: %i, Contacts: %i" %(self.visits, self.contacts)


day1 = Day(10, 1)
day2 = Day(20 ,2)
print(day1)
print(day1.visits)
print(day1.contacts)

print(day2)

day3 = day1 + day2
print(day3)

day4 = sum([day1, day2, day3])
print(day4)
