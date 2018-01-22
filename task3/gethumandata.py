import task3.human
import pickle

def print_people():
	with open('C:/Andrey/workspace/people', 'rb') as file:
		people = pickle.load(file)
		for person in people:
			print(person)
