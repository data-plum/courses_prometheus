class SuperStr(str):
	def  __init__(self, string):
		self.string = string
		self.string = self.string.lower()
		print self.string

	def is_repeatance(self, s):
		if type(s) == str and len(s) > 0:
			if len(s) <= len(self.string) - len(s):
				print "we are there"
				for i in range(len(self.string) - len(s)):
					s += s[i]
				if self.string == s:
					return True
			elif len(s) == len(self.string) and self.string == s:
				return True
		return False

	def is_palindrom(self):
		if self.string == self.string[::-1]:
			return True
		else:
			return False

s4 = SuperStr('q')
