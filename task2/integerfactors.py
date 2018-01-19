def int_sums(number):
	"""int_sums(number) -- return list of all integer sums for number
	number = a + b + c

	"""

	if number == 1:
		return [[1]]
	res = []
	for i in range(1, number):
		for sublist in int_sums(i):
			isSkip = False
			for item in sublist:
				if item > number-i:
					isSkip = True
					break
			if isSkip:
				continue
			res.append([number-i])
			res[-1].extend(sublist)
	return res
