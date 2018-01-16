def ExTabs(text, isfile = False):
	if isfile:
		file = open(text, "r")
		text = file.read()
		file.close()
	res = ""
	index1 = 0
	index2 = text.find("\t")
	while index2 != -1:
		res += text[index1:index2]
		res += "    "
		index1 = index2 + 1
		index2 = text.find("\t", index1)
	res += text[index1:]
	return res

