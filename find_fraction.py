def find_fraction(summ):
	def nod(numerator, denominator):
		a = numerator
	 	b = denominator
	 	if (a % 2 == 0 and b % 2 == 0) or\
	 	(a % 3 == 0 and b % 3 == 0) or\
	 	(a % 5 == 0 and b % 5 == 0) or\
	 	(a % 7 == 0 and b % 7 == 0):
	 		return True

 	if summ <= 2:
 		return False
 	else:
 		if summ % 2 == 0:
 			numerator = (summ - 1) // 2
	 		denominator = numerator + 2
	 	else:
	 		numerator = summ // 2
	 		denominator = numerator + 1
 	
	 	if not nod(numerator, denominator):
	 		return (numerator, denominator)
	 	else:
	 		while numerator != 0:
		 		numerator -= 1
		 		denominator += 1
			 	if not nod(numerator, denominator):
	 				return (numerator, denominator)
	 				break
		 		if numerator == 0:
		 			return False

print find_fraction(150000001)
 	