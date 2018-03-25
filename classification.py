from pynput import keyboard
import pickle
import datetime
import subprocess
import math
from copy import deepcopy
class Classifier:
  def __init__(self):
    self.keylog = []
    self.scores = []
    self.params = pickle.load( open( "classifier_params.pkl", "rb" ) )
    try: self.trusted_word_times =pickle.load( open( "profile_avik.pkl", "rb" ) )
    except Exception: self.trusted_word_times = {} 
    self.PRESSED = True
    self.RELEASED = False
    # self.logs = []
    def on_press(key):
      time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
      is_char = True
      try: keychar = key.char
      except AttributeError: 
        keychar = key
        is_char = False
      if True: #self.keylog[-1][1] == self.PRESSED: # filter out repeated self.PRESSED signals
        if keychar in [keyboard.Key.space, keyboard.Key.enter, keyboard.Key.tab]:
          #print 'TESTing WORD JUST TYPED in self.keylog'
          # self.logs.append(deepcopy(self.keylog))
          self.test_word()
          self.keylog = []
        elif is_char:
          self.keylog.append((keychar, self.PRESSED, time))
         # print(keychar, self.PRESSED, time)
      
      if keychar is keyboard.Key.esc:  
        # print self.trusted_word_times
        # pickle.dump( self.trusted_word_times, open( "profile.pkl", "wb" ) )
        exit()
    def on_release(key):
      time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
      if key == keyboard.Key.esc: return False
      self.keylog.append((key, self.RELEASED, time))
      print (key, self.RELEASED, time)
    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
      listener.join()
  def test_word(self):
    try:
      word = ''.join(map(lambda entry: entry[0], self.keylog)) # this is the word entered before the space/tab
      #print word
      if word in self.trusted_word_times and len(word)> 2: # can only test words that we have trusted ddata to compare against
        # print 'word is in record'
        times = map(lambda a: a[2], self.keylog)
        test_word_times = []
        for i in range(1, len(times)):
          test_word_times.append(times[i]-times[i-1])
        distance = math.sqrt(sum([(test_word_times[i]-self.trusted_word_times[word][i])**2 for i in range(len(word)-1)]))
        self.scores.append(self.predict(distance, self.params[len(word)][0], self.params[len(word)][1]))
        #print sum(self.scores)/len(self.scores)
        print len(self.scores)
        print sum(self.scores[-7:])/len(self.scores[-7:])
        if len(self.scores) > 8 and sum(self.scores[-7:])/len(self.scores[-7:]) < 0.47:
          self.scores = []
          subprocess.call('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend', shell=True)
        # TODO some metric to compare trusted to test time diffs - try euclidean distance
      #else:
       # print 'couldnt find word'
    except TypeError:
      pass
  def predict(self,dist, a, b):
    return 1/(1+a*math.e**(b*dist))                               
Classifier()
 