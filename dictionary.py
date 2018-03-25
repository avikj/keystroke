#all the 0.0 will be replaced with the times for the word from the algorithm
#addWord() will be called when the algorithm creates a new word

import pickle
import os.path


personalDictionary = {}

def main():
	createDict()
	addWord("abcd")
	#test()

def createDict():
	print os.path.exists("PersonalDictionary.pickle")
	if os.path.exists("PersonalDictionary.pickle"):
		with open('PersonalDictionary.pickle', 'rb') as f:  
			global personalDictionary
			personalDictionary = pickle.load(f)
			print personalDictionary


def addWord(word):
	global personalDictionary
	print personalDictionary
	if personalDictionary.has_key(word)==False:
		personalDictionary[word] = 0.0
		print personalDictionary
	with open('PersonalDictionary.pickle', 'wb') as f:
		pickle.dump(personalDictionary, f)

if __name__ == '__main__': main()
