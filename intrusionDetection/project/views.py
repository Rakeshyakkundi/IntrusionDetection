from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pickle



# Create your views here.
k = pickle.load(open('/home/hp/Desktop/jupyter/intrusionDetection/project/knn.pkl','rb'))
s = pickle.load(open('/home/hp/Desktop/jupyter/intrusionDetection/project/svm.pkl','rb'))
l = pickle.load(open('/home/hp/Desktop/jupyter/intrusionDetection/project/logic.pkl','rb'))

r  = pickle.load(open('/home/hp/Desktop/jupyter/intrusionDetection/project/random_LS.pkl','rb'))

def home(request):
    if request.method == 'POST':
        a = request.POST['input_type']
        if a == 'Single_Record':
            return redirect('/single_record')
        if a == 'Single_File':
            return redirect('/files')
    return render(request,'project/Dashboard.html')
def In_type(num):
    if num in [1]:
        return "Normal"
    elif num in [16,11,10,18]:
        return "Probe attack"
    elif num in [6,5,14,9,8,12]:
        return "Dos attack"
    elif num in [20,21,7,15,13,19,17]:
        return "Remote to user attack"
    elif num in [2,23,3,4]:
        return "User to Root attack"
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

def ret_protocol(a):
    if str(a) == "tcp":
        return 1
    elif str(a) == "udp":
        return 2
    elif str(a) == "icmp":
        return 3  

def ret_flag(a):
    if str(a) == "SF":
        return 1
    elif str(a) == "S0":
        return 2
    elif str(a) == "S1":
        return 3
    elif str(a) == "S2":
        return 4
    elif str(a) == "S3":
        return 5
    elif str(a) == "REJ":
        return 6
    elif str(a) == "RSTO":
        return 7
    elif str(a) == "RSTR":
        return 8
    elif str(a) == "RSTOS0":
        return 9
    elif str(a) == "OTH":
        return 10
    elif str(a) == "SH":
        return 11

def single_record(request):
    if request.method == 'POST':
        duration = int(request.POST['Duration'])
        protocol_type = request.POST['protocol_type']
        src_bytes = int(request.POST['src_bytes'])
        dst_bytes = int(request.POST['destination'])
        is_host_login = int(request.POST['is_host_login'])
        is_guest_login = int(request.POST['is_guest_login'])
        diff_srv_rate = float(request.POST['diff_srv_rate'])
        srv_diff_host_rate = float(request.POST['srv_diff_host_rate'])
        flag = request.POST['flag']
        print("="*50)
        print(duration,protocol_type,src_bytes,dst_bytes,is_host_login,is_guest_login,diff_srv_rate,srv_diff_host_rate,flag)
        row = [duration,ret_protocol(protocol_type),src_bytes,dst_bytes,is_host_login,is_guest_login,diff_srv_rate,srv_diff_host_rate,ret_flag(flag)]
        #----------------------------------------------------------
        z0 = list(l.predict([row]))
        z1 = list(k.predict([row]))
        z2 = list(s.predict([row]))
        print("="*50)
        print("Knn :",num_labels(z1[0]),"Svm :",num_labels(z2[0]),"Logistic :",num_labels(z0[0]))
        #-----------------------------------------------------------
        Both = z1+z2 
        a = r.predict([Both])[0]
        print("="*50)
        print("Random Forest :",num_labels(a))
        return render(request,'project/result.html',{"logic":num_labels(z0[0]),"knn":num_labels(z1[0]),"svm":num_labels(z2[0]),"random":num_labels(a),"type":In_type(a)})
    return render(request,'project/single.html')

def files(request):
    return render(request,'project/files.html')

def result(request):
    return render(request,'project/result.html') 