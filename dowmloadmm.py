import urllib.request
import os
import random
def url_open(url):
    req= urllib.request.Request(url)

    req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
    proxies = ['175.154.50.30:80', '221.202.249.30:80', '123.169.91.221:80']
    proxy = random.choice(proxies)

    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()

    return html
def get_page(url):
    
    html =url_open(url).decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    
    return html[a:b]
def find_imgs(url):
    html  =url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
            
        b= html.find('.jpg',a,a+255)

        if b!= -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b =a+9
        a=html.find('img src=',b)

    return img_addrs

def save_imgs(folder,img_addrs):

    for each in img_addrs:
        filename= each.split('/')[-1]
        with open(filename,'wb') as f:
            print(filename)
            img = url_open(each)
            f.write(img)
    
  
def download_mm(folder='F:\\python\\ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url="http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url=url+'page-'+str(page_num)+"#comments"
        img_addres=find_imgs(page_url)
        save_imgs(folder,img_addres)
if __name__=="__main__":
    download_mm()
