import pickle
k = pickle.load(open('knn.pkl','rb'))
s = pickle.load(open('svm.pkl','rb'))
l = pickle.load(open('logic.pkl','rb'))

r  = pickle.load(open('random.pkl','rb'))



def num_labels(a):
  if (a)== 1:
    return "normal"
  elif (a) == 2:
    return "buffer_overflow"
  elif (a) == 3:
    return "loadmodule"
  elif (a) == 4:
    return "perl"
  elif (a) == 5:
    return "neptune"
  elif (a) == 6:
    return "smurf"
  elif (a) == 7:
    return "guess_passwd"
  elif (a) == 8:
    return "pod"
  elif (a) == 9:
    return "teardrop"
  elif (a) == 10:
    return "portsweep"
  elif (a) == 11:
    return "ipsweep"
  elif (a) == 12:
    return "land"
  elif (a) == 13:
    return "ftp_write"
  elif (a) == 14:
    return "back"
  elif (a) == 15:
    return "imap"
  elif (a) == 16:
    return "satan"
  elif (a) == 17:
    return "phf"
  elif (a) == 18:
    return "nmap"
  elif (a) == 19:
    return "multihop"
  elif (a) == 20:
    return "warezmaster"
  elif (a) == 21:
    return "warezclient"
  elif (a) == 22:
    return "spy"
  elif (a) == 23:
    return "rootkit"

def predict_values_row(row):
    z1 = list(k.predict([row]))
    z2 = list(s.predict([row]))
    Both = z1+z2 
    a = r.predict([Both])[0]
    
    return num_labels(a)
ans = predict_values_row([0,	3	,1480,	0	,0,	0	,0,	0,	1])
print(ans)