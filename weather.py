import urllib.parse  
import urllib.request  
from xml.dom.minidom import parseString  
url = "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName"  
values = {"theCityName":u"西安"}  
data = urllib.parse.urlencode(values).encode(encoding='UTF8')  
req = urllib.request.Request(url, data)  
response = urllib.request.urlopen(req)  
the_page = response.read().decode("utf8")  
dom = parseString(the_page)  
string = dom.getElementsByTagName("string")  
for s in string:  
    try:  
        data = s.childNodes[0].data  
        print(data)  
    except IndexError as e:  
        next 
