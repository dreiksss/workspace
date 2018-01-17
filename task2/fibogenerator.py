def fibo_generator(n):
	"""fibo_generator(n) -- return generator for first n fibonachi numbers"""

	a = 1
	b = 1
	for i in range(n):
		print("before yield")
		yield a
		print("after yield")
		a, b = b, a + b
		print("end code")
