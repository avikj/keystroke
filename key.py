from pynput import keyboard
import datetime
from copy import deepcopy
class Keyshit:
	def __init__(self):
		self.keylog = []
		self.PRESSED = True
		self.RELEASED = False
		self.logs = []
		def on_press(key):
			time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
			try: keychar = key.char
			except AttributeError: keychar = key
			if len(self.keylog) == 0 or not (self.keylog[-1][0] == keychar and self.keylog[-1][1] == self.PRESSED): # filter out repeated self.PRESSED signals
				self.keylog.append((keychar, self.PRESSED, time))
				print(keychar, self.PRESSED, time)
			if keychar in [keyboard.Key.space, keyboard.Key.enter, keyboard.Key.tab]:
				print 'RESET'
				self.logs.append(deepcopy(self.keylog))
				self.keylog = []
		def on_release(key):
			time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
			if key == keyboard.Key.esc: return False
			self.keylog.append((key, self.RELEASED, time))
			print (key, self.RELEASED, time)
		with keyboard.Listener(on_press=on_press, on_release=None) as listener:
			listener.join()

Keyshit()