import pickle
import math
import random
def main():
  avik1 = pickle.load( open( "profile_avik.pkl", "rb" ) )
  avik2 = pickle.load( open( "profile_avik2.pkl", "rb" ) )
  shaurya1 = pickle.load(open("shaurya_profile.pkl", "rb"))
  shaurya2 = pickle.load(open("shaurya_profile2.pkl", "rb"))
  params = []
  for wordlen in range(15):
    try: 
      data = create_data(avik1, avik2, wordlen, 1)+create_data(shaurya1, shaurya2, wordlen, 1)+create_data(avik1, shaurya2, wordlen, 0)+create_data(avik1, shaurya1, wordlen, 0)+create_data(avik2, shaurya2, wordlen, 0)+create_data(avik2, shaurya1, wordlen, 0)
      data.sort()
      #print data
      a = random.random()
      b = -random.random()
      learning_rate = 0.01
      delta = 0.001
      loss = float('inf')
      improvement = float('inf')
      while improvement > 1e-8:
        da = (compute_loss(data, a+delta, b)-compute_loss(data, a, b))/delta
        db = (compute_loss(data, a, b+delta)-compute_loss(data, a, b))/delta
        a -= da*learning_rate
        b -= db*learning_rate
        prev_loss = loss
        loss = compute_loss(data, a, b)
        improvement = prev_loss-loss
        #print improvement
      params.append((a, b))
      print accuracy(data,a,b)
    except Exception: pass
  pickle.dump( params, open( "classifier_params.pkl", "wb" ) )
def create_data(d1, d2, wordlen, truth):
  k1 = {k for k in d1.keys() if len(k) == wordlen}
  k2 = {k for k in d2.keys() if len(k) == wordlen}
  trainable_words = k1.intersection(k2)
  print trainable_words
  data = []
  for word in trainable_words:
    distance = math.sqrt(sum([(d1[word][i]-d2[word][i])**2 for i in range(len(word)-1)]))
    # classifier will just be a sigmoid of distance, with two trainable parameters
    data.append((distance, truth))
  return data
def compute_loss(data, a, b):
  J = 0
  for dist, y in data:
    p = predict(dist, a, b)
    J -= y*math.log(p)+(1-y)*math.log(1-p)
  return J
def accuracy(data, a, b):
  correct = 0
  for dist, y in data:
    p = predict(dist, a, b)
    #print dist, a, b, p, round(p), y
    if round(p) == float(y):
      correct += 1.0
  return correct/len(data) if len(data)>0 else 'nan'
def predict(dist, a, b):
  return 1/(1+a*math.e**(b*dist))
main()

