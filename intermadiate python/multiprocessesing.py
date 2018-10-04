#hızlandırmayı işletim sistemine bırakıyor ve
#GIL gibi görüntü işleme kütüphaneleri thread açmayı ve thread çalıştırmayı önlüyor. GIL opencvnin kullandığı kütüphane
#çünkü güvenli ve sıralı veri kayıt işlemi değil. o zaman bizde verileri işletim sisteminde
#ayrı işlemlermiş gibi açarak önlemelere takılmayız.
#thread aynı hafıza üzerinde çalışabilirsiniz. processler ise aynı hafıza kümesini kullanmazlar
import multiprocessing
from multiprocessing import *
import bs4 as bs
import random
import requests
import string

def yaz(num, num2):
    print("yazıyor!! yazıyoooorrr!!! {} {}".format(num, num2))
def beginning():
    for i in range(5):
        p=multiprocessing.Process(target=yaz,args=(i,i+1))
        p.start()
        #p.join() #işlemleri sırasıyla ana processe göre yaptırmayı sağlar. böyle olursa daha stabil, olmazsa çok process açıyor.

def iş(num):
    return num*2
def inter():
    with Pool(processes=20) as p:
        data=p.map(iş,range(10))
    print(data)


randiter=1
def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(randiter))
    url = ''.join(['http://', starting, '.com'])
    print(url)
    return url
def handle_local_links(url,link):# local linkler yeni web sitelerini bbulmamızı engeller. bu yüzden bunlar elenir.
    if link.startswith('/'):
        return ''.join([url,link])
    else:
        return link
def get_links(url):
    # random_start_url fonksiyonu rastgele çalışır yani link kırıktır yada öyle bir domöain olmamış olabilir.
    try:
        resp = requests.get(url)  # tüm sayfayı strgin olarak alır ve soup ile text ayrıştırılır.
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]  # htmlde href kısmı bir linke yönlendirmedir ve böylece yeni linkler bulunabilir.
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links
    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        randiter=+1
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None for links, so we are throwing this')
        return []
    except Exception as e:
        print(str(e))
        # log this error
        return []




def spider():
    kactane=50
    p = Pool(processes=kactane)
    parse_us = [random_starting_url() for _ in range(kactane)]# artık linkler utf olarak da yapıldığından ben buradan ingilizce olanları seçiyorum
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]# veri liste içinde listeler olduğundan veriler ayrıştırılmalı
    p.close()
    with open('urls.txt','w') as dosya:
        dosya.write(str(data))

if __name__=="__main__":
    #beginning()
    #inter()
    spider()









