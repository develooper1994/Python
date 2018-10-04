import datetime
now=datetime.datetime.now() #extracts your O.S. time
print("now: ",now)
print("type(datetime.datetime.now()): ",type(datetime.datetime.now()))

s=str(now)
print("now: ",s)
print("type(str(now)): ",type(s))

yesterday=datetime.datetime(2018,2,10)
print("yesterday: ",yesterday)
delta=now-yesterday
print("differance: ",delta)
print("differance: ",delta.total_seconds())
print("differance: ",delta.days)

print("now.strftime('%Y-%m-%d-%H-%M-%S-%f'): ",now.strftime("%Y-%m-%d-%H-%M-%S-%f")) #http://strftime.org/
print("now.strftime('%B %Y %d'): ",now.strftime("%B %Y %d"))

TwoDaysAfter=now+datetime.timedelta(days=2,seconds=1000)
print("TwoDaysAfter: ",TwoDaysAfter)

import CommentAndDocument as mc
mc.create_file(str(delta))

print("---time module---")

import time

lst=[]
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)
print(lst)


