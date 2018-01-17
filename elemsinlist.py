testList = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2]

def elems_in_list(mylist):
	"""elems_in_list(list)

	 -- return new list with unique elements of list in order from rarer to often

	"""

	res = []
	dictSort = {}
	for item in mylist:
		occur = mylist.count(item)
		if occur in dictSort:
			if item not in dictSort[occur]:
				dictSort[occur].append(item)
		else:
			dictSort[occur] = [item]
	occurList = list(dictSort.keys())
	occurList.sort()
	for occur in occurList:
		for num in dictSort[occur]:
			res.append(num)
	return res