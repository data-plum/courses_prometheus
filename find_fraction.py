def find_fraction(summ):
	def nod(numerator, denominator):
		a = numerator
	 	b = denominator
	 	while a != b:
	 		if a > b:
	 			a = a - b
	 		else:
	 			b = b - a
	 	return a

 	if summ <= 2:
 		return False
 	else:
 		if summ % 2 == 0:
 			numerator = (summ - 1) // 2
	 		denominator = numerator + 2
	 	else:
	 		numerator = summ // 2
	 		denominator = numerator + 1
 	
	 	if nod(numerator, denominator) == 1:
	 		return (numerator, denominator)
	 	else:
	 		while numerator != 0:
		 		numerator -= 1
		 		denominator += 1
			 	if nod(numerator, denominator) == 1:
	 				return (numerator, denominator)
		 		if numerator == 0:
		 			return False

print find_fraction(150000001)
 	