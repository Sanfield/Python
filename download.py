import urllib.request
reg  = urllib.request.Request("http://placekitten.com/g/500/600")
response= urllib.request.urlopen(reg)
img= response.read()

with open("F:\\python\\爬虫\\img.jpg","wb") as f:
    f.write(img)
