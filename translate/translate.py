import sys
import os

#import goslate
from textblob.blob import TextBlob

srcDir = sys.argv[1]
destDir = 'C:\\asemenov\\Panasonic\\Translated'#sys.argv[2]

def readFile(filename):
	text = ''
	try:
		file = open(filename, encoding='utf8')
		text = file.read()
	except UnicodeDecodeError:
		file.close()
		file = open(filename, encoding='cp932')
		text = file.read()
	finally:
		file.close()
	return text

def getWords(text):
	word = ''
	isWord = False
	wordList = []
	for char in text:
		if ord(char) > 127 and isWord == True:
			word += char
		if ord(char) > 127 and isWord == False:
			word += char
			isWord = True
		if ord(char) <= 127 and isWord == True:
			wordList.append(word)
			word = ''
			isWord = False
	return '\n'.join(wordList)


def translateFile(filename):
	text = readFile(filename)
	forTranslate = getWords(text)
	#gs = goslate.Goslate()
	#afterTranslate = gs.translate(forTranslate, 'en')
	blob = TextBlob(forTranslate)
	afterTranslate = str(blob.translate(from_lang="ja", to='en'))
	for old, new in zip(forTranslate.split('\n'), afterTranslate.split('\n')):
		new = '<tr>' + new.strip() + '</tr>'
		text = text.replace(old, new, 1)
	return text

def translateDir(root):
	root.strip('\\')
	rootWord = root[root.rfind('\\')+1:]
	forTranslate = ''
	allFiles = []
	for path, dirsList, filesList in os.walk(root):
		if len(filesList) == 0:
			continue
		allFiles.append((path, dirsList, filesList))
		for filename in filesList:
			postfix = filename[filename.rfind('.'):]
			if postfix == '.c' or postfix == '.h':
				fullFile = path + '\\' + filename
				print(fullFile)
				forTranslate += getWords(readFile(fullFile))
				forTranslate += '\n%%\n'
	#gs = goslate.Goslate(service_urls=['http://translate.google.de'])
	#afterTranslate = gs.translate(forTranslate, 'en')
	blob = TextBlob(forTranslate)
	chunk = blob[:10000]
	afterTranslate = str(chunk.translate(from_lang="ja", to='en'))
	print(len(chunk))
	while len(chunk) == 10000:
		blob = blob[10000:]
		chunk = blob[:10000]
		print(len(chunk))
		afterTranslate += str(chunk.translate(from_lang="ja", to='en'))
	with open('C:/Users/aseme/Documents/GitHub/workspace/translate/output.txt', 'w', encoding='utf8') as file:
		file.write(afterTranslate)
	for path, dirsList, filesList in allFiles:
		if len(filesList) == 0:
			continue
		for filename in filesList:
			postfixIndex = filename.rfind('.')
			postfix = filename[postfixIndex:]
			if postfix == '.c' or postfix == '.h':
				cuttedPath = path[path.rfind(rootWord):]
				newDir = '\\'.join([ dirName + '_tr' for dirName in cuttedPath.split('\\')])
				fullNewDir = destDir + '\\' + newDir
				try:
					os.makedirs(fullNewDir)
				except OSError:
					pass
				fullFile = path + '\\' + filename
				text = readFile(fullFile)
				forTranslateIndex = forTranslate.find('\n%%\n')
				afterTranslateIndex = afterTranslate.find('\n%%\n')
				for old, new in zip(forTranslate[:forTranslateIndex].split('\n'), \
				 					afterTranslate[:afterTranslateIndex].split('\n')):
					new = ' ' + new.strip() + ' '
					text = text.replace(old, new, 1)
				forTranslate = forTranslate[forTranslateIndex+4:]
				afterTranslate = afterTranslate[afterTranslateIndex+4:]
				fullNewFile = fullNewDir+'\\'+filename[:postfixIndex]+'_tr'+postfix
				with open(fullNewFile, 'w', encoding='utf8') as file:
					file.write(text)




if __name__ == '__main__':
	translateDir(srcDir)
	#with open('C:/Users/aseme/Documents/GitHub/workspace/translate/output.txt', 'w', encoding='utf8') as file:
	#	file.write(translateFile(srcDir))
