class Student(object):
	def __init__(self, name, dictionary):
		self.labs_success = []
		self.name = name
		self.m = 0
		self.dictionary = dictionary
		for i in range(self.dictionary['lab_num']):
			self.labs_success.append(0)

	def make_lab(self, m, n = None):
		if float(m) > self.dictionary['lab_max']:
				m = self.dictionary['lab_max']
		if n <= self.dictionary['lab_num'] - 1 and n != None:
			del self.labs_success[n]
			self.labs_success.insert(n, m)
		elif n == None:
			try:
				index = self.labs_success.index(0)
				del self.labs_success[index]
				self.labs_success.insert(index, m)
			except: 
				return self
		self.sum_labs_success = sum(self.labs_success)
		print self.labs_success
		return self

	def make_exam(self, m = 0):
		self.m = float(m)
		if self.m > float(self.dictionary['exam_max']):
			self.m = self.dictionary['exam_max']
		return self

	def is_certified(self):
		certified = []
		if (float(self.m + sum(self.labs_success))) / 100 >= self.dictionary['k']:
			certified = [self.m + sum(self.labs_success), True]
		else:
			certified = [self.m + sum(self.labs_success), False]
		return tuple(certified)

conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1)
print o5.is_certified()
o5.make_lab(7)