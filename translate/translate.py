import sys
import os

#import goslate
from textblob.blob import TextBlob
from textblob.exceptions import NotTranslated

opt = sys.argv[1]
#srcDir = sys.argv[2]
destDir = 'C:\\asemenov\\Panasonic\\Translated'#sys.argv[2]
delim = '\n%%\n'

def readFile(filename):
	text = ''
	try:
		file = open(filename, encoding='utf8')
		text = file.read()
	except UnicodeDecodeError:
		file.close()
		try:
			file = open(filename, encoding='cp932')
			text = file.read()
		except UnicodeDecodeError:
			file.close()
			try:
				file = open(filename, encoding='euc_jp')
				text = file.read()
			except UnicodeDecodeError:
				pass
				#file.close()
				#file = open(filename, 'rb')
				#text = file.read()
	finally:
		file.close()
	return text

def getWords(text):
	word = ''
	isWord = False
	wordList = []
	for char in text:
		if char == '\ufeff' or ord(char) == 8203 or char == '％':
			continue
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
	try:
		blob = TextBlob(forTranslate)
		afterTranslate = str(blob.translate(from_lang="ja", to='en'))
	except: #NotTranslated:
		afterTranslate = forTranslate
	for old, new in zip(forTranslate.split('\n'), afterTranslate.split('\n')):
		new = '<tr>' + new.strip() + '</tr>'
		text = text.replace(old, new, 1)
	return text

def makeSrcFile(root):
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
			if postfix == '.c' or postfix == '.h' or postfix == '.cpp':
				fullFile = path + '\\' + filename
				print(fullFile)
				forTranslate += getWords(readFile(fullFile))
				forTranslate += delim
	srcFile = destDir+'\\'+rootWord+'_src'+'.txt'
	with open(srcFile, 'w', encoding='utf8') as file:
		file.write(forTranslate)

def translateChunk(text):
	blob = TextBlob(text)
	try:
		TranslatedChunk = str(blob.translate(from_lang="ja", to='en'))
	except NotTranslated:
		return text
	if text[0] == '\n':
		TranslatedChunk = '\n'+TranslatedChunk
	if text[-1] == '\n':
		TranslatedChunk +='\n'
	return TranslatedChunk

def translateSrcFile(FileName):
	TranslatedFile = FileName.replace('src', 'tr')
	while True:
		text = ''
		with open(FileName, encoding='utf8') as file:
			text = file.read()
		chunkIndex = text.rfind(delim, 0, 10000)
		if chunkIndex == -1:
			chunkIndex = text.find(delim)
		chunk = text[:chunkIndex]
		print(len(chunk))
		subChunk = chunk[:10000]
		TranslatedChunk = translateChunk(subChunk)
		while len(subChunk) == 10000:
			chunk = chunk[10000:]
			subChunk = chunk[:10000]
			TranslatedChunk += translateChunk(subChunk)
		with open(TranslatedFile, 'a', encoding='utf8') as file:
			file.write(TranslatedChunk+delim)
		text = text[chunkIndex+len(delim):]
		with open(FileName, 'w', encoding='utf8') as file:
			file.write(text)
		if text == '':
			break
	print('success!!!')

def genNewFolders(root):
	makeSrcFile(root)
	root.strip('\\')
	rootWord = root[root.rfind('\\')+1:]
	srcFile = destDir+'\\'+rootWord+'_src'+'.txt'
	forTranslate = readFile(srcFile)
	TranslatedFile = srcFile.replace('src', 'tr')
	afterTranslate = readFile(TranslatedFile)
	for path, dirsList, filesList in os.walk(root):
		if len(filesList) == 0:
			continue
		for filename in filesList:
			postfixIndex = filename.rfind('.')
			postfix = filename[postfixIndex:]
			if postfix == '.c' or postfix == '.h' or postfix == '.cpp':
				cuttedPath = path[path.find(rootWord):]
				newDir = '\\'.join([ dirName + '_tr' for dirName in cuttedPath.split('\\')])
				fullNewDir = destDir + '\\' + newDir
				try:
					os.makedirs(fullNewDir)
				except OSError:
					pass
				fullFile = path + '\\' + filename
				text = readFile(fullFile)
				forTranslateIndex = forTranslate.find(delim)
				afterTranslateIndex = afterTranslate.find(delim)
				for old, new in zip(forTranslate[:forTranslateIndex].split('\n'), \
				 					afterTranslate[:afterTranslateIndex].split('\n')):
					new = ' ' + new.strip() + ' '
					text = text.replace(old, new, 1)
				forTranslate = forTranslate[forTranslateIndex+len(delim):]
				afterTranslate = afterTranslate[afterTranslateIndex+len(delim):]
				fullNewFile = fullNewDir+'\\'+filename[:postfixIndex]+'_tr'+postfix
				with open(fullNewFile, 'w', encoding='utf8') as file:
					file.write(text)

def modifyDir(root):
	root.strip('\\')
	rootWord = root[root.rfind('\\')+1:]
	srcFile = destDir+'\\'+rootWord+'_src'+'.txt'
	forTranslate = readFile(srcFile)
	TranslatedFile = srcFile.replace('src', 'tr')
	afterTranslate = readFile(TranslatedFile)
	for path, dirsList, filesList in os.walk(root):
		if len(filesList) == 0:
			continue
		for filename in filesList:
			postfixIndex = filename.rfind('.')
			postfix = filename[postfixIndex:]
			if postfix == '.c' or postfix == '.h' or postfix == '.cpp':
				fullFile = path + '\\' + filename
				text = readFile(fullFile)
				forTranslateIndex = forTranslate.find(delim)
				afterTranslateIndex = afterTranslate.find(delim)
				for old, new in zip(forTranslate[:forTranslateIndex].split('\n'), \
				 					afterTranslate[:afterTranslateIndex].split('\n')):
					new = ' ' + new.strip() + ' '
					text = text.replace(old, new, 1)
				forTranslate = forTranslate[forTranslateIndex+len(delim):]
				afterTranslate = afterTranslate[afterTranslateIndex+len(delim):]
				with open(fullFile, 'w', encoding='utf8') as file:
					file.write(text)



if __name__ == '__main__':
	if opt == '-s':
		srcDir = sys.argv[2]
		makeSrcFile(srcDir)

	if opt == '-t':
		FileName = sys.argv[2]
		translateSrcFile(FileName)

	if opt == '-g':
		srcDir = sys.argv[2]
		genNewFolders(srcDir)

	if opt == '-m':
		srcDir = sys.argv[2]
		modifyDir(srcDir)
	#translateDir(srcDir)
	#with open('C:/Users/aseme/Documents/GitHub/workspace/translate/output.txt', 'w', encoding='utf8') as file:
	#	file.write(translateFile(srcDir))
