import pickle

class Human:
	def __init__(self, **kwargs):
		self.name = kwargs['name']
		self.lastname = kwargs['lastname']
		self.birth = kwargs['birth']
		self.city = kwargs['city']
		self.street = kwargs['street']
		self.house = kwargs['house']
		self.houseNumber = kwargs['houseNumber']
		self.mobileNumber = kwargs['mobileNumber']

	def __str__(self):
		output = """name -- {}
lastname -- {}
birth -- {}
city -- {}
street -- {}
house -- {}
houseNumber -- {}
mobileNumber -- {}
		""".format(self.name,
				   self.lastname,
				   self.birth,
				   self.city,
				   self.street,
				   self.house,
				   self.houseNumber,
				   self.mobileNumber)
		print(output)


me = Human(name='Andrey',
		   lastname='Semenov',
		   birth='20.11.1987',
		   city = 'Nizniy Novgorod',
		   street = 'Lenskaya',
		   house = '29',
		   houseNumber = '620514',
		   mobileNumber = '9200125290')

voronin = Human(name='Anton',
		   lastname='Voronin',
		   birth='11.09.1987',
		   city = 'Nizniy Novgorod',
		   street = 'Zimina',
		   house = '6',
		   houseNumber = '123456',
		   mobileNumber = '12345678')

bazenov = Human(name='Pavel',
		   lastname='Bazenov',
		   birth='27.04.1988',
		   city='Nizniy Novgorod',
		   street='Vitebskaya',
		   house='9',
		   houseNumber='123456',
		   mobileNumber='91247895')


people = [me, voronin, bazenov]

with open('C:/Andrey/workspace/people', 'wb') as file:
	pickle.dump(people, file)
<<<<<<< HEAD
=======
	
>>>>>>> a19cc895a546c14c69c1fc57032bdc83bb51c8b0
