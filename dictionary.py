from pynput import keyboard
import datetime
from os import path
import os

def main():
	#openFile()
	#collectData()
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

def openFile():
	filepath = 'CommonWords.txt'  
	with open(filepath) as fp:  
		for cnt, line in enumerate(fp):
  			testWords.append(line) 

