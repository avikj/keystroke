from pynput import keyboard
import datetime

keylog = []

def on_press(key):
	time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
	try: keychar = key.char
	except AttributeError: keychar = key
	keylog.append((keychar, 'press', time))

def on_release(key):
	time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
	if key == keyboard.Key.esc: return False

	i = len(keylog)-1
        # remove duplicated key pressed data
        # while keylog[i][1]


	for i in reversed(xrange(len(keylog))):
		keylog[i][1]
	keylog.append((key, 'release', time))

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
