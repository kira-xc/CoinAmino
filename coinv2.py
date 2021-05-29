
from os import _exit,system
import time,json
import sys

from amino.lib.util import exceptions
try:
    import amino
except:
    print("not have internet")
    _exit
import random,string,hashlib,base64,importlib,threading
def deviceaoss():
    return str('01' + (hardwareInfo := hashlib.sha1(''.join(random.choices(string.ascii_uppercase + string.digits, k = 1000)).encode("utf-8"))).hexdigest() + hashlib.sha1(bytes.fromhex('01') + hardwareInfo.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()).upper()
device=deviceaoss()
print("the new device id : ",device)

def deviceido(device):
    dvvv='{\n\"device_id\": \"'+device+'\", \n\"device_id_sig\": \"AaauX/ZA2gM3ozqk1U5j6ek89SMu\", \n\"user_agent\": \"Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)\"\n}'
    fdev=open("device.json","w+")
    fdev.write(dvvv)
    fdev.close()
deviceido(device)

from datetime import datetime
def num5():
    return {"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}

def timero():  
    return [
num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5()
,num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),
num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5()

]
comlist=['1','3','2','89','74613308','3818252','12126645','12200153','44485556','222306780']
timer=timero()
def joiner(m):
    try:
        client.join_community(m)
        print("joined in ",m)
    except:
        print("error to join to from : "+m)
cpt=0
def taskos(comId):
    sub=amino.SubClient(comId=comId,profile=client.profile)  
    sub.activity_status("on")
    sub.send_active_obj(timers=timer)
    print("filish to log in the email : "+email)
endos=False
while endos==False:
    with open('email.json') as json_file:
        data = json.load(json_file)
        listos=[]
        passwords=[]
        devices=[]
        for d in range(0,len(data)):
            listos.append(data[d]['email'])
            passwords.append(data[d]['password'])
            devices.append(data[d]['device'])
    
    for email,password,device in zip(listos,password,device):
        client=amino.Client(deviceId=device)
        threads=[] 
        threads2=[]
        try:
            client.login(email=email,password=password)
        except Exception as e:
            print(e)
            _exit(1)
        comIds=client.sub_clients(start=0,size=200).comId
        if len(comIds)<10:
            for comos in comlist:
                threads2.append(threading.Thread(target=joiner, args=(comos,)))
            for t2 in threads2:
                if not t2.is_alive():
                    t2.start()
            for t2 in threads2:
                t2.join()
            comIds=client.sub_clients(start=0,size=200).comId
        for comId in comIds:
            timer=timero()
            cpt=0
            threads.append(threading.Thread(target=taskos, args=(comId,)))
        for t in threads:
            if not t.is_alive():
                t.start()
        for t in threads:
            t.join()
        client.logout()
    endos=False if input("to be continued ? y/n : ")!="n" else True
_exit(1)
