import time
from datetime import datetime as dt

hosts_temp=r"D:\Dropbox\pp\block_websites\Demo\hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working")

    else:
        print("funn")

    time.sleep(5)




