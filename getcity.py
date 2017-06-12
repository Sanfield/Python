# -*- coding: utf-8 -*-  
import os  
import urllib  
  
#根据url得到html代码  
def getHtml(url):  
    page = urllib.request.urlopen(url)  
    html = page.read()  
    return html  
  
#讲字符串分割后整理为编号和对应城市的dictionary  
def getDictionary(str):  
    str_split = str.split(',')  
    dics = {}  
    for each in str_split:  
        tmp = each.split('|')  
        dics[tmp[0]] = tmp[1]  
    return dics  
  
#得到编号和对应的省或直辖市dictionary  
def getProvience(url):  
    res = getHtml(url)  
    pro_dic = getDictionary(res)  
    return pro_dic  
  
#得到编号和对应的二级城市的dictionary  
def getCity(url):  
    res = getHtml(url)  
    city_dic = getDictionary(res)  
    return city_dic  
  
#得到编号和对应的区域的dictionary  
def getField(url):  
    res = getHtml(url)  
    field_dic = getDictionary(res)  
    return field_dic  
  
if __name__ == '__main__':  
    #打开文件  
    city_code_file = open('city.py', 'w')  
    city_code_file.write('# -*- coding: utf-8 -*-\n')  
    city_code_file.write('city = {}\n')  
    print ('获取省以及直辖市编号')  
    province_url = 'http://m.weather.com.cn/data5/city.xml'  
    pro_dic = getProvience(province_url)  
    #获取每个省的城市编号  
    print ('获取二级区域编号')  
    for pro in pro_dic:  
        city_url = 'http://m.weather.com.cn/data5/city' + pro + '.xml'  
        city_dic = getCity(city_url)  
        #获取每个城市的地区编号  
        for city in city_dic:  
            field_url = 'http://m.weather.com.cn/data5/city' + city + '.xml'  
            field_dic = getField(field_url)  
            #对于每一个编号和对应的地区存入dictionary  
            for field in field_dic:  
                city_code_file.write('city[\'' + field_dic[field] + '\'] = ' + '101' + str(field) + '\n')   
                print ('city[\'' + field_dic[field].decode('utf-8') + '\'] = ' + '101' + str(field)  
)
    #关闭文件  
    city_code_file.close()  
    print ('获取完成') 
