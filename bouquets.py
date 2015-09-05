def bouquets(narcissus_price, tulip_price, rose_price, summ):

	counter = 0

	for f1 in range(1 + int(1.0 * summ / narcissus_price)):
		for f2 in range(1 + int((1.0 * summ - f1 * narcissus_price) / tulip_price)):
			for f3 in range(1 + int((1.0 * summ - f1 * narcissus_price - f2 * tulip_price) / rose_price)):
				if (f1+f2+f3) % 2:
					counter += 1

	return counter

print bouquets(1, 1, 1, 5)