import urllib.request
import urllib.parse
url="http://impservice.dictapp.youdao.com/imp/Rookie.js?http://shared.ydstatic.com/ead/swf/rookie.swf"

date = {}
date['i']= '资本'
date['from']='AUTO'
date['to]']='AUTO'
date['smartresult']='dict'
date['client']='fanyideskweb'
date['salt']='1498402144898'
date['sign']='82d16969c3f2c846c14c0b2b0283548e'
date['doctype']='json'
date['version']='2.1'
date['keyfrom']='fanyi.web'
date['action']='FY_BY_CLICKBUTTON'
date['typoResult']='true'
date= urllib.parse.urlencode(date).encode("UTF-8")
response = urllib.request.urlopen(url,date)
html=  response.read().decode("utf-8")
print(html)
