def fibo_generator(n):
	"""fibo_generator(n) -- return generator for first n fibonachi numbers"""

	a = 1
	b = 1
	for i in range(n):
		yield a
		a, b = b, a + b
