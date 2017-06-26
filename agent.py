import urllib.request
import random

url="https://baike.baidu.com/"
iplist = ['115.213.176.155','60.167.20.87','36.26.152.117','114.115.217.19','115.213.176.155']

proxy_support= urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html= response.read().decode('utf-8')

print(html)
