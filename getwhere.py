import get_city  
import json  
import city  
  
field_name = raw_input('哪里的天气？')  
field_no = city.city.get(field_name)  
if field_no:  
    url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % field_no  
    html = get_city.getHtml(url)  
    weather_dic = json.loads(html)  
    weather_info = weather_dic.get('weatherinfo')  
    print weather_info['weather'] + ' ' + weather_info['temp2'] + '~' + weather_info['temp1']   
else:  
    print '没有这个地名的天气信息' 
