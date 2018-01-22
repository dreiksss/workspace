import time

from src.json2xml import Json2xml

def cumar_json2xml(jsonData):
	data = Json2xml.fromstring(jsonData).data
	data_object = Json2xml(data)
	data_object.json2xml()

if __name__ == '__main__':
	with open('C:/Andrey/workspace/PythonApplication1/examples/example.json') as file:
		jsonData = file.read()

	start = time.time()
	for i in range(10000):
		cumar_json2xml(jsonData)
	print('cumar_json2xml -- {0:03.2f}sec'.format(time.time()-start))


