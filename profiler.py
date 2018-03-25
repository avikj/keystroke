from pynput import keyboard
import pickle
import datetime
from copy import deepcopy
class Profiler:
	def __init__(self):
		self.keylog = []

		try: self.word_times =pickle.load( open( "shaurya_profile.pkl", "rb" ) )
		except Exception: self.word_times = {} 
		self.PRESSED = True
		self.RELEASED = False
		self.logs = []
		def on_press(key):
			time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
			is_char = True
			try: keychar = key.char
			except AttributeError: 
				keychar = key
				is_char = False
			if True: #self.keylog[-1][1] == self.PRESSED: # filter out repeated self.PRESSED signals
				if keychar in [keyboard.Key.space, keyboard.Key.enter, keyboard.Key.tab]:
					print 'RESET'
					self.logs.append(deepcopy(self.keylog))
					
					self.add_word()
					self.keylog = []
				elif is_char:
					self.keylog.append((keychar, self.PRESSED, time))
					print(keychar, self.PRESSED, time)
			
			if keychar is keyboard.Key.esc:  
				print self.word_times
				pickle.dump( self.word_times, open( "shaurya_profile.pkl", "wb" ) )
				exit()
		def on_release(key):
			time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
			if key == keyboard.Key.esc: return False
			self.keylog.append((key, self.RELEASED, time))
			print (key, self.RELEASED, time)
		with keyboard.Listener(on_press=on_press, on_release=None) as listener:
			listener.join()
	def add_word(self):
		try:
			word = ''.join(map(lambda entry: entry[0], self.keylog)) # this is the word entered before the space/tab
			print word
			times = map(lambda a: a[2], self.keylog)
			diffs = []
			for i in range(1, len(times)):
				diffs.append(times[i]-times[i-1])
			print diffs
			self.word_times[word] = diffs
		except TypeError:
			pass
Profiler()
 