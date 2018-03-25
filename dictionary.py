
dictionary = {}

def main():
	createDict()
	#test()

def createDict():
	filepath = 'CommonWords.txt'  
	with open(filepath) as fp:  
		for cnt, line in enumerate(fp):
  			dictionary[line[:-1]] = 0.0

def test():
	print len(dictionary)
	for key in dictionary.keys():
		print key
	print dictionary["the"]
	print dictionary["of"]
	print dictionary["a"]
	print dictionary["stuff"]

if __name__ == '__main__': main()