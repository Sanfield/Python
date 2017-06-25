Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======================= RESTART: F:\python\爬虫\Test.py =======================
>>> import urllib.request.urlopen("http://www.fishc.com")
SyntaxError: invalid syntax
>>> import urllib.request
>>> response = urllib.request.urlopen("http://www.fishc.com")
>>> html = response.read()
>>> print(html)
b'\xef\xbb\xbf<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n\t<meta charset="UTF-8">\r\n\t<title>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4-7\xe5\x91\xa8\xe5\xb9\xb4\xe4\xb8\xbb\xe9\xa1\xb5</title>\r\n    \r\n    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">\r\n    <meta name="apple-mobile-app-capable" content="yes">\r\n    <meta name="apple-mobile-app-status-bar-style" content="black">\r\n   \r\n    <meta name="description" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4|\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|\xe7\xbc\x96\xe7\xa8\x8b\xe6\x8a\x80\xe6\x9c\xaf\xe4\xba\xa4\xe6\xb5\x81|C\xe8\xaf\xad\xe8\xa8\x80|\xe6\xb1\x87\xe7\xbc\x96|Python|win32|Delphi|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux">\r\n    <meta name="keywords" content="C,C++,Python,Scratch,HTML5,CSS3,JavaScript,Qt,\xe6\xb1\x87\xe7\xbc\x96,WinSDK">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="author" content="cononico">\r\n    <meta name="application-name" content="Cononico" >\r\n\r\n    <link rel="stylesheet" type="text/css" href="css/main.css">\r\n    <link rel="stylesheet" type="text/css" href="css/process.css">\r\n    <link rel="shortcut icon"  type="image/x-icon" href="favicon.ico" />\r\n    \r\n    <script type="text/javascript">\r\n        //\xe8\xae\xbe\xe5\xae\x9arem\xe5\x80\xbc\r\n        document.getElementsByTagName("html")[0].style.fontSize = document.documentElement.clientWidth/20 + \'px\';\r\n    </script>\r\n</head>\r\n<body>\r\n\t<header class="head">\r\n        <div class="head_logo_div">\r\n            <img class="logo_img" src="images/upload/FishC.png"></a>\r\n        </div>\r\n        <div class="head_nav_div">\r\n             <nav class="head_nav">\r\n                <ul id="nav_ul">\r\n                    <li class="nav_li_on nav_ul_li">\xe4\xb8\xbb\xe9\xa1\xb5</li>\r\n                    <li class="nav_ul_li">\xe9\xb1\xbcC\xe9\x87\x8c\xe7\xa8\x8b\xe7\xa2\x91</li>\r\n                    <li class="nav_ul_li">\xe4\xb8\x83\xe5\x91\xa8\xe5\xb9\xb4\xe5\xba\x86\xe5\x85\xb8</li>\r\n                    <li class="nav_ul_li">\xe5\xa4\xa7\xe5\x92\x96\xe7\xa7\x80</li>\r\n                    <li class="nav_ul_li">\xe8\xb6\x85\xe7\xba\xa7\xe4\xbc\xa0\xe9\x80\x81\xe9\x97\xa8</li>\r\n                    <li class="nav_ul_li"><a href="http://fishc.taobao.com", target="_blank">\xe8\xb5\x84\xe6\xba\x90\xe6\x89\x93\xe5\x8c\x85</a></li>\r\n                </ul>\r\n            </nav>\r\n        </div>\r\n        <div class="clear"></div>\r\n    </header>\r\n    \r\n    <ul class="float_btn" id="float_btn">\r\n        <li class="btn_on"></li>\r\n        <li></li>\r\n        <li></li>\r\n        <li></li>\r\n    </ul>\r\n    \r\n    <div class="wrapBox" id="wrapBox">\r\n        <div class="box">\r\n            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg1.jpg">\r\n            <div class="box01_content">\r\n                <div class="head_div">\r\n                    <div class="cycle_item">\r\n                        <a href="https://item.taobao.com/item.htm?id=528146888326" class="taobao" id="taobao" target="_blank">\r\n                            <span class="taobao_icon"></span>\r\n                            <span class="taobao_text"><p class="item_name">\xe4\xbc\x9a\xe5\x91\x98</p></span>\r\n                        </a>\r\n\r\n                        <a href="http://blog.fishc.com" class="weibo_a" id="weibo_a" target="_blank">\r\n                            <span class="weibo_icon"></span>\r\n                            <span class="weibo_text"><p class="item_name">\xe8\xa7\x86\xe9\xa2\x91</p> </span>\r\n                        </a>\r\n                        \r\n                        <a href="http://bbs.fishc.com" class="bbs" id="bbs" target="_blank">\r\n                            <span class="bbs_icon"></span>\r\n                            <span class="bbs_text"><p class="item_name">\xe4\xba\xa4\xe6\xb5\x81</p></span>\r\n                        </a>\r\n\r\n                        <div class="green_cycle">\r\n                            <img class="green_cycle_img" src="images/icon/green_cycle.svg">\r\n                            <div class="yellow_cycle">\r\n                                <img class="yellow_cycle_img" src="images/icon/yellow_cycle.svg">\r\n                                <div class="blue_cycle">\r\n                                    <img class="blue_cycle_img" src="images/icon/blue_cycle.svg">\r\n                                    <div class="head_img_div">\r\n                                        <img class="head_img" src="images/upload/FishC.png">\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n\r\n                <h1 class="title">Change the World by Program</h1>\r\n                <h2 class="title_h2">I love FishC.com!</h2>\r\n\r\n                <div id="box01_text">\r\n                <p class="box01_p">\xe6\xac\xa2\xe8\xbf\x8e\xe4\xbd\xa0\xe7\x9a\x84\xe5\x8a\xa0\xe5\x85\xa5\xef\xbc\x81</p>\r\n                \r\n                \r\n                </div>\r\n            </div>\r\n\r\n            <div class="arrow_div">\r\n                <img class="arrow_img" src="images/icon/arrowhead.png">\r\n            </div>\r\n        </div>\r\n        \r\n        <div class="box">\r\n            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg2.jpg">\r\n            \r\n            <div class="box02_content box_content">\r\n                <div id=\'bar_container\' class="bar_container">\r\n                    <div class=\'bar red\' data-percent=\'70\' data-skill=\'\xe3\x80\x8aWindows\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1\xef\xbc\x88SDK\xef\xbc\x89\xe3\x80\x8b\'></div>\r\n\r\n                    <div class=\'bar lila\' data-percent=\'80\' data-skill=\'\xe3\x80\x8a\xe6\x9e\x81\xe5\xae\xa2\xe9\xa6\x96\xe9\x80\x89\xe4\xb9\x8bPython\xe3\x80\x8b\xe7\xac\xac\xe4\xb8\x80\xe5\xad\xa3\xef\xbc\x9aGit\xe5\xae\x9e\xe7\x94\xa8\xe6\x95\x99\xe7\xa8\x8b\'></div>\r\n\r\n                    <div class=\'bar orange\' data-percent=\'60\' data-skill=\'\xe3\x80\x8a\xe5\xb8\xa6\xe4\xbd\xa0\xe5\xad\xa6C\xe5\xb8\xa6\xe4\xbd\xa0\xe9\xa3\x9e\xe3\x80\x8b\xe7\xac\xac\xe4\xb8\x80\xe5\xad\xa3\xef\xbc\x9a\xe8\xaf\xad\xe6\xb3\x95\xe5\x9f\xba\xe7\xa1\x80\'></div>\r\n\r\n                    <div class=\'bar blue\' data-percent=\'80\' data-skill=\'HTML-\xe5\xba\x96\xe4\xb8\x81\xe8\xa7\xa3\xe7\x89\x9b\xef\xbc\x88\xe5\x9b\xbe\xe6\x96\x87\xef\xbc\x89\'></div>\r\n\r\n                    <div class=\'bar mint\' data-percent=\'60\' data-skill=\'JavaScript-\xe5\xba\x96\xe4\xb8\x81\xe8\xa7\xa3\xe7\x89\x9b\xef\xbc\x88\xe5\x9b\xbe\xe6\x96\x87\xef\xbc\x89\'></div>\r\n\r\n                </div>\r\n\r\n                <div id="box02_text">\r\n                    <h1>\xe9\xb1\xbcC\xe9\x87\x8c\xe7\xa8\x8b\xe7\xa2\x91</h1>\r\n                    <div class="overline"></div>\r\n                    <p>2010\xe5\xb9\xb4 ~ 2011\xe5\xb9\xb4,\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe9\x9b\xb6\xe5\x9f\xba\xe7\xa1\x80\xe5\x85\xa5\xe9\x97\xa8\xe5\xad\xa6\xe4\xb9\xa0C\xe8\xaf\xad\xe8\xa8\x80\xe3\x80\x8b</p>\r\n                    <p>2011\xe5\xb9\xb4 ~2012\xe5\xb9\xb4,\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe9\x9b\xb6\xe5\x9f\xba\xe7\xa1\x80\xe5\x85\xa5\xe9\x97\xa8\xe5\xad\xa6\xe4\xb9\xa0\xe6\xb1\x87\xe7\xbc\x96\xe8\xaf\xad\xe8\xa8\x80\xe3\x80\x8b</p>\r\n                    <p>2011\xe5\xb9\xb4 ~ 2013\xe5\xb9\xb4,\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8aC++\xe5\xbf\xab\xe9\x80\x9f\xe5\x85\xa5\xe9\x97\xa8\xe3\x80\x8b</p>\r\n                    <p>2012\xe5\xb9\xb4 ~ 2014\xe5\xb9\xb4,\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe9\x9b\xb6\xe5\x9f\xba\xe7\xa1\x80\xe5\x85\xa5\xe9\x97\xa8\xe5\xad\xa6\xe4\xb9\xa0DELPHI\xe3\x80\x8b</p>\r\n                    <p>2013\xe5\xb9\xb4 ~ 2014\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe6\x95\xb0\xe6\x8d\xae\xe7\xbb\x93\xe6\x9e\x84\xe5\x92\x8c\xe7\xae\x97\xe6\xb3\x95\xe3\x80\x8b</p>\r\n                    <p>2011\xe5\xb9\xb4 ~ 2012\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe8\xa7\xa3\xe5\xaf\x86\xe7\xb3\xbb\xe5\x88\x97\xe3\x80\x8b\xe5\x9f\xba\xe7\xa1\x80\xe7\xaf\x87</p>\r\n                    <p>2012\xe5\xb9\xb4 ~ 2013\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe8\xa7\xa3\xe5\xaf\x86\xe7\xb3\xbb\xe5\x88\x97\xe3\x80\x8b\xe8\xb0\x83\xe8\xaf\x95\xe7\xaf\x87\xef\xbc\x88OD\xe6\x95\x99\xe7\xa8\x8b\xef\xbc\x89</p>\r\n                    <p>2012\xe5\xb9\xb4 ~ 2013\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe8\xa7\xa3\xe5\xaf\x86\xe7\xb3\xbb\xe5\x88\x97\xe3\x80\x8b\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xaf\x87\xef\xbc\x88PE\xe7\xbb\x93\xe6\x9e\x84\xe8\xaf\xa6\xe8\xa7\xa3\xef\xbc\x89</p>\r\n                    <p>2013\xe5\xb9\xb4 ~ 2013\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe8\xa7\xa3\xe5\xaf\x86\xe7\xb3\xbb\xe5\x88\x97\xe3\x80\x8b\xe8\x84\xb1\xe5\xa3\xb3\xe7\xaf\x87</p>\r\n                    <p>2013\xe5\xb9\xb4 ~ 2013\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe8\xa7\xa3\xe5\xaf\x86\xe7\xb3\xbb\xe5\x88\x97\xe3\x80\x8b\xe5\xb7\xa5\xe5\x85\xb7\xe7\xaf\x87</p>\r\n                    <p>2013\xe5\xb9\xb4 ~ 2015\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe9\x9b\xb6\xe5\x9f\xba\xe7\xa1\x80\xe5\x85\xa5\xe9\x97\xa8\xe5\xad\xa6\xe4\xb9\xa0Python\xe3\x80\x8b</p>\r\n                    <p>2016\xe5\xb9\xb4 ~ 2016\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe7\x95\xaa\xe5\xa4\x96\xe7\xaf\x87\xef\xbc\x9aVIM\xe5\xbf\xab\xe9\x80\x9f\xe5\x85\xa5\xe9\x97\xa8</p>\r\n                    <p>2016\xe5\xb9\xb4 ~ 2016\xe5\xb9\xb4\xef\xbc\x8c\xe5\xae\x8c\xe6\x88\x90\xe3\x80\x8a\xe9\x9b\xb6\xe5\x9f\xba\xe7\xa1\x80\xe5\x85\xa5\xe9\x97\xa8Scratch\xe3\x80\x8b\xef\xbc\x88\xe5\x9b\xbe\xe6\x96\x87\xef\xbc\x89</p>\r\n                </div>\r\n                <div class="clear"></div>\r\n            </div>\r\n            \r\n            <div class="arrow_div">\r\n                <img class="arrow_img" src="images/icon/arrowhead.png">\r\n            </div>\r\n            \r\n        </div>\r\n        \r\n        <div class="box">\r\n            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg3.jpg">\r\n            \r\n            <div class="box_content box03_content">\r\n                <ul id="timeUl" class="timeUl">\r\n                    <li>\r\n                        <div id="fun1">\r\n                            <h1 style="color:#51D9DF">7\xe5\x91\xa8\xe5\xb9\xb4\xe6\xb4\xbb\xe5\x8a\xa8</h1>\r\n                            <p>\xe4\xb8\xba\xe4\xba\x86\xe8\xae\xa9\xe4\xbd\xa0\xe4\xbb\xac\xe7\x9a\x84\xe6\x9a\x91\xe5\x81\x87\xe7\x94\x9f\xe6\xb4\xbb\xe8\xbf\x87\xe5\xbe\x97\xe6\x9b\xb4\xe6\x9c\x89\xe6\x84\x8f\xe4\xb9\x89\xef\xbc\x8c\xe9\xb1\xbcC\xe8\xae\xba\xe5\x9d\x9b\xe7\xad\xb9\xe5\x8a\x9e\xe4\xba\x86\xe6\x9c\xac\xe6\xac\xa1\xe6\xb4\xbb\xe5\x8a\xa8\xe2\x80\xa6\xe2\x80\xa6</p>\r\n                            <p>\xe5\x88\xa9\xe7\x94\xa8\xe6\x9a\x91\xe5\x81\x87\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\x80\xe9\x97\xa8\xe6\x96\xb0\xe7\x9a\x84\xe7\x9f\xa5\xe8\xaf\x86\xef\xbc\x8c\xe5\xb9\xb6\xe5\xb0\x86\xe5\xad\xa6\xe4\xb9\xa0\xe7\x9a\x84\xe8\xbf\x87\xe7\xa8\x8b\xe7\x94\xa8\xe7\xac\x94\xe8\xae\xb0\xe7\x9a\x84\xe5\xbd\xa2\xe5\xbc\x8f\xe8\xae\xb0\xe5\xbd\x95\xe4\xb8\x8b\xe6\x9d\xa5\xef\xbc\x8c\xe9\xa1\xba\xe4\xbe\xbf\xe6\x8a\x8a\xe5\xa5\x96\xe5\xad\xa6\xe9\x87\x91\xe5\xb8\xa6\xe5\x9b\x9e\xe5\xae\xb6 -> <a style="color:#F265B5" href="http://bbs.fishc.com/thread-88041-1-1.html", target="_blank">\xe7\x82\xb9\xe6\x88\x91\xe5\x8f\x82\xe4\xb8\x8e</a></p>\r\n                        </div>\r\n                    </li>\r\n                     <li>\r\n                        <div>\r\n                            <h1 style="color:#F265B5">\xe5\xa5\x96\xe5\x93\x81\xe5\xb1\x95\xe7\xa4\xba\xe5\x8f\xb0</h1>\r\n                            <p>\xe4\xb8\x80\xe7\xad\x89\xe5\xa5\x96\xef\xbc\x9a1000\xe5\x85\x83\xe5\xa5\x96\xe5\xad\xa6\xe9\x87\x91</p>\r\n                            <p>\xe4\xba\x8c\xe7\xad\x89\xe5\xa5\x96\xef\xbc\x9a888\xe5\x85\x83\xe5\xa5\x96\xe5\xad\xa6\xe9\x87\x91</p>\r\n                            <p>\xe4\xb8\x89\xe7\xad\x89\xe5\xa5\x96\xef\xbc\x9a666\xe5\x85\x83\xe5\xa5\x96\xe5\xad\xa6\xe9\x87\x91</p>\r\n                            <p>\xe5\x9b\x9b\xe7\xad\x89\xe5\xa5\x96\xef\xbc\x9a100\xe5\x85\x83\xe5\xa5\x96\xe5\xad\xa6\xe9\x87\x91</p>\r\n                            <p>\xe4\xba\x94\xe7\xad\x89\xe5\xa5\x96\xef\xbc\x9a200\xe9\xb1\xbc\xe5\xb8\x81</p>\r\n                        </div>\r\n                    </li>\r\n                     <li>\r\n                        <div id="fun2">\r\n                            <h1 style="color:#51D9DF">\xe5\x8f\x82\xe4\xb8\x8e\xe6\x96\xb9\xe5\xbc\x8f</h1>\r\n                            <p>\xe2\x80\xa6\xe2\x80\xa6</p>\r\n                            <p><a style="color:#F265B5" href="http://bbs.fishc.com/thread-88041-1-1.html", target="_blank">\xe4\xbc\xa0\xe9\x80\x81\xe9\x97\xa8</a></p>\r\n                            <p>\xe2\x80\xa6\xe2\x80\xa6</p>\r\n\r\n                        </div>\r\n                    </li>\r\n                </ul>\r\n                \r\n\r\n                 <div class="left_div" id="left_div">\r\n                     <img class="left_arrow" src="images/icon/arrowleft.png">\r\n                 </div>\r\n                 <div class="right_div" id="right_div">\r\n                      <img class="right_arrow" src="images/icon/arrowright.png">\r\n                 </div>\r\n            </div>\r\n            \r\n             <div class="arrow_div">\r\n                <img class="arrow_img" src="images/icon/arrowhead.png">\r\n            </div>\r\n        </div>\r\n        \r\n        \r\n        <div class="box">\r\n            \r\n            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg4.jpg">\r\n            <div class="box_content box04_content">\r\n            \r\n                <ul class="hobby_content">\r\n                    <li class="hobby_01">\r\n                        <div class="hobby_img_div">\r\n                            <div class="spinner spinner_01"></div>\r\n                            <div class="hobby_img">\r\n                                <img src="images/upload/xiaojiayu.png">\r\n                            </div>\r\n                            <div class="hobby_img_info">\r\n                                <h1>\xe5\xb0\x8f\xe7\x94\xb2\xe9\xb1\xbc</h1>\r\n                                <h2>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe5\x88\x9b\xe5\xa7\x8b\xe4\xba\xba</h2>\r\n                            </div>\r\n                        </div>\r\n                        <div class="hobby_text_div">\r\n                            <div class="hobby_img_info_mob">\r\n                                <h1>\xe5\xb0\x8f\xe7\x94\xb2\xe9\xb1\xbc/<a>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe5\x88\x9b\xe5\xa7\x8b\xe4\xba\xba</a></h1>\r\n                            </div>\r\n                            <p class="about_p" style="text-align: center;">\r\n                            \xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe5\x88\x9b\xe5\xa7\x8b\xe4\xba\xba\xef\xbc\x9a\xe5\xb0\x8f\xe7\x94\xb2\xe9\xb1\xbc\r\n                            </p>\r\n                            <p>\r\n                            \xe4\xb8\x83\xe5\xb9\xb4\xe6\x9d\xa5\xe5\x88\xb6\xe4\xbd\x9c\xe4\xba\x86N\xe5\xa4\x9a\xe2\x80\x9c\xe5\xb0\x8f\xe8\xa7\x86\xe9\xa2\x91\xe2\x80\x9d\xef\xbc\x8c\xe7\xbb\x8f\xe8\xaf\xb8\xe5\xa4\x9a\xe7\xbd\x91\xe7\xab\x99\xe5\x8f\x91\xe5\xb8\x83\xe5\x90\x8e\xef\xbc\x8c\xe5\xb9\xbf\xe5\x8f\x97\xe5\xa5\xbd\xe8\xaf\x84\xef\xbc\x8c\xe5\xa4\x9a\xe6\xac\xa1\xe8\xa2\xab\xe7\xbd\x91\xe9\xa1\xb5\xe5\x8f\x8a\xe7\x9b\xb8\xe5\x85\xb3\xe4\xb8\x93\xe9\xa2\x98\xe6\x8e\xa8\xe8\x8d\x90\xef\xbc\x8c\xe6\xb7\xb1\xe5\x85\xa5\xe7\xa8\x8b\xe5\xba\x8f\xe7\x8c\xbf\xe5\x8d\x95\xe7\xba\xaf\xe7\x9a\x84\xe5\x86\x85\xe5\xbf\x83\xe3\x80\x82\r\n                            </p>\r\n                        </div>\r\n                    </li>\r\n                    <li class="hobby_02">\r\n                        <div class="hobby_img_div">\r\n                            <div class="spinner spinner_02"></div>\r\n                            <div class="hobby_img">\r\n                                <img src="images/upload/banzhu.png" width="270" height="270">\r\n                            </div>\r\n                            <div class="hobby_img_info">\r\n                                <h1>\xe9\xb1\xbcC\xe7\x89\x88\xe4\xb8\xbb</h1>\r\n                                <h2>\xe7\xae\xa1\xe7\x90\x86\xe5\x9b\xa2\xe9\x98\x9f&\xe7\x89\x88\xe4\xb8\xbb</h2>\r\n                            </div>\r\n                        </div>\r\n                        <div class="hobby_text_div">\r\n                            <div class="hobby_img_info_mob">\r\n                                <h1>\xe9\xb1\xbcC\xe7\x89\x88\xe4\xb8\xbb/<a>\xe7\xae\xa1\xe7\x90\x86\xe5\x9b\xa2\xe9\x98\x9f&\xe7\x89\x88\xe4\xb8\xbb</a></h1>\r\n                            </div>\r\n                            <p class="about_p">\r\n                            \xe7\xae\xa1\xe7\x90\x86\xe5\x9b\xa2\xe9\x98\x9f\xef\xbc\x9a\xe5\xba\xb7\xe5\xb0\x8f\xe6\xb3\xa1\xe3\x80\x81~\xe9\xa3\x8e\xe4\xbb\x8b~\xe3\x80\x81\xe4\xb8\x8d\xe4\xba\x8c\xe5\xa6\x82\xe6\x98\xaf\r\n                            </p>\r\n                            <p>\r\n                            \xe7\x89\x88\xe4\xb8\xbb\xe5\x9b\xa2\xe9\x98\x9f\xef\xbc\x9a\xe4\xba\xba\xe9\x80\xa0\xe4\xba\xba\xe3\x80\x81lumber2388779\xe3\x80\x81wei_Y\xe3\x80\x81\xe5\x86\xac\xe9\x9b\xaa\xe9\x9b\xaa\xe5\x86\xac\xe3\x80\x81hldh214\xe3\x80\x81shuofxz\xe3\x80\x81SixPy\xe3\x80\x81\xe9\x9b\xb6\xe5\xba\xa6\xe9\x9d\x9e\xe5\xae\x89\xe5\x85\xa8\xe3\x80\x81\xe8\xbf\xb7\xe9\x80\x94\xe3\x80\x81\xe7\xa0\xb4\xe6\xb8\x94\xe7\xbd\x91\xe5\x85\x9c\xe5\x85\x9c\xe3\x80\x81Minhal\xe2\x80\xa6\xe2\x80\xa6\r\n                            </p>\r\n                        </div>\r\n                    </li>\r\n                    <li class="hobby_03">\r\n                        <div class="hobby_img_div">\r\n                            <div class="spinner spinner_03"></div>\r\n                            <div class="hobby_img">\r\n                                <img src="images/upload/reading.png">\r\n                            </div>\r\n                            <div class="hobby_img_info">\r\n                                <h1>\xe5\xb0\xb1\xe6\x98\xaf\xe4\xbd\xa0\xef\xbc\x81</h1>\r\n                                <h2>\xe9\xb1\xbc\xe6\xb2\xb9&\xe5\xb0\xbd\xe7\xb2\xbe\xe5\xbe\xae</h2>\r\n                            </div>\r\n                        </div>\r\n                        <div class="hobby_text_div">\r\n                            <div class="hobby_img_info_mob">\r\n                                <h1>\xe5\xb0\xb1\xe6\x98\xaf\xe4\xbd\xa0\xef\xbc\x81/<a>\xe9\xb1\xbc\xe6\xb2\xb9&\xe5\xb0\xbd\xe7\xb2\xbe\xe5\xbe\xae</a></h1>\r\n                            </div>\r\n                            <p class="about_p">\r\n                                \xe6\xb2\xa1\xe6\x9c\x89\xe4\xba\xba\xe6\x98\xaf\xe4\xb8\x80\xe5\xba\xa7\xe5\xad\xa4\xe5\xb2\x9b\xef\xbc\x8c\xe4\xbd\xa0\xe6\x9d\xa5\xe5\x88\xb0\xe9\xb1\xbcC\xef\xbc\x8c\xe5\xb9\xb6\xe5\x86\xb3\xe5\xae\x9a\xe7\x95\x99\xe4\xb8\x8b\xe6\x9d\xa5\xef\xbc\x8c\xe8\xbf\x99\xe5\xb0\xb1\xe6\x98\xaf\xe4\xb8\x80\xe7\xa7\x8d\xe6\x97\xa0\xe5\xb0\x9a\xe8\x8d\xa3\xe8\x80\x80\xef\xbc\x81\r\n                            </p>\r\n                            <p>\r\n                                \xe6\xac\xa2\xe8\xbf\x8e\xe6\x9d\xa5\xe5\x88\xb0\xe9\xb1\xbcC\xef\xbc\x8c\xe5\xbe\x88\xe5\xbf\xab\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\x86\xe4\xbf\xaf\xe8\xa7\x86\xe5\xa4\xa7\xe5\x9c\xb0\xef\xbc\x8c\xe9\xa9\xb0\xe9\xaa\x8b\xe4\xb9\x9d\xe5\xa4\xa9\xe3\x80\x82\r\n                            </p>\r\n                        </div>\r\n                    </li>\r\n                    <div class="clear"></div>\r\n                </ul>\r\n            </div>\r\n             <div class="arrow_div">\r\n                <img class="arrow_img" src="images/icon/arrowhead.png">\r\n            </div>\r\n        </div>\r\n        \r\n        <foot id="foot" class="foot">\r\n            <h1 class="foot_title">\xe9\xb1\xbcC\xe8\xb6\x85\xe7\xba\xa7\xe4\xbc\xa0\xe9\x80\x81\xe9\x97\xa8</h1>\r\n            <div class="foot_info_main">\r\n                <ul>\r\n                    <li class="one">\r\n                        <a href="http://bbs.fishc.com/forum-38-1.html" target="_blank">C\\C++\xe4\xba\xa4\xe6\xb5\x81 </a>\r\n                    </li>\r\n                    <li class="two">\r\n                        <a href="http://bbs.fishc.com/forum-79-1.html" target="_blank">\xe6\x95\xb0\xe6\x8d\xae\xe7\xbb\x93\xe6\x9e\x84\xe4\xb8\x8e\xe7\xae\x97\xe6\xb3\x95</a>\r\n                    \r\n                    </li>\r\n                    <li class="three">\r\n                        <a href="http://bbs.fishc.com/forum-171-1.html" target="_blank">WEB\xe5\xbc\x80\xe5\x8f\x91</a>\r\n                    \r\n                    </li>\r\n                    <li class="four">\r\n                        <a href="http://bbs.fishc.com/forum-39-1.html" target="_blank">\xe6\xb1\x87\xe7\xbc\x96\xe8\xaf\xad\xe8\xa8\x80\xe4\xba\xa4\xe6\xb5\x81</a>\r\n                    \r\n                    </li>\r\n                    <li class="five">\r\n                        <a href="http://bbs.fishc.com/forum-241-1.html" target="_blank">JAVA\xe8\xaf\xad\xe8\xa8\x80\xe4\xba\xa4\xe6\xb5\x81</a>\r\n                    \r\n                    </li>\r\n                    <li class="six">\r\n                        <a href="http://bbs.fishc.com/forum-337-1.html" target="_blank">\xe5\xb0\x8f\xe5\xa4\xa9\xe6\x89\x8d\xe5\x85\xbb\xe6\xae\x96\xe5\x9c\xba</a>\r\n                    \r\n                     </li>\r\n                     <li class="seven">\r\n                        <a href="http://bbs.fishc.com/forum-173-1.html" target="_blank">Python\xe4\xba\xa4\xe6\xb5\x81</a>\r\n                    \r\n                     </li>\r\n                     <li class="eight">\r\n                        <a href="http://bbs.fishc.com/forum-207-1.html" target="_blank">Win\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1 </a>\r\n                    </li>\r\n\r\n                     </li>\r\n                    <li class="nine">\r\n                        <a href="http://bbs.fishc.com/forum-219-1.html" target="_blank">\xe5\x93\x87\xef\xbc\x81Linux</a>\r\n                    \r\n                    </li>\r\n                    <li class="ten">\r\n                        <a href="http://bbs.fishc.com/forum-219-1.html" target="_blank">\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86</a>\r\n                    \r\n                     </li>\r\n                     <li class="eleven">\r\n                        <a href="http://bbs.fishc.com/forum-120-1.html" target="_blank">Delphi\xe4\xba\xa4\xe6\xb5\x81</a>\r\n                    \r\n                     </li>\r\n                     <li class="twelve">\r\n                        <a href="http://bbs.fishc.com/forum-33-1.html" target="_blank">\xe5\x90\xb9\xe6\xb0\xb4\xe9\x98\x81</a>\r\n                    </li>\r\n\r\n                    <div class="clear"></div>\r\n                </ul>\r\n                <div class="qrcode_div">\r\n                    <span class="weixin">\r\n                        <a class="weixin_icon"></a>\r\n                        <img class="weixin_img" src="images/upload/weixin_qr.png">\r\n                    </span>\r\n                  \r\n                </div>\r\n            </div>\r\n            <div class="foot_power">\r\n                <h3>\xc2\xa92017 Pwoerd Unique\r\n                    <a href="http://www.fishc.com" title="FishC" target="_blank">FishC</a>\r\n                    <a href="http://bbs.fishc.com/forum.php" title="IceEnd">#\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4#</a>\r\n                    <a href="https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-2468366367.8.8gs6zK&id=528146888326" title="vip" target="_blank">  @VIP\xe5\xbf\xab\xe9\x80\x9f\xe5\x85\x85\xe5\x80\xbc\xe5\x8f\xa3</a>\r\n                </h3>\r\n            </div>\r\n        </foot>\r\n    </div>\r\n    <script type="text/javascript" src="js/main.js"></script>\r\n</body>\r\n    \r\n</html>\r\n\r\n \r\n'
>>> html= = html.decode("utf=8")
SyntaxError: invalid syntax
>>> html=html.decode("utf-8")
>>> print(html)
﻿<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>鱼C工作室-7周年主页</title>
    
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <meta name="apple-mobile-app-capable" content="yes">
    <meta name="apple-mobile-app-status-bar-style" content="black">
   
    <meta name="description" content="鱼C工作室|免费编程视频教学|编程技术交流|C语言|汇编|Python|win32|Delphi|加密与解密|Linux">
    <meta name="keywords" content="C,C++,Python,Scratch,HTML5,CSS3,JavaScript,Qt,汇编,WinSDK">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="author" content="cononico">
    <meta name="application-name" content="Cononico" >

    <link rel="stylesheet" type="text/css" href="css/main.css">
    <link rel="stylesheet" type="text/css" href="css/process.css">
    <link rel="shortcut icon"  type="image/x-icon" href="favicon.ico" />
    
    <script type="text/javascript">
        //设定rem值
        document.getElementsByTagName("html")[0].style.fontSize = document.documentElement.clientWidth/20 + 'px';
    </script>
</head>
<body>
	<header class="head">
        <div class="head_logo_div">
            <img class="logo_img" src="images/upload/FishC.png"></a>
        </div>
        <div class="head_nav_div">
             <nav class="head_nav">
                <ul id="nav_ul">
                    <li class="nav_li_on nav_ul_li">主页</li>
                    <li class="nav_ul_li">鱼C里程碑</li>
                    <li class="nav_ul_li">七周年庆典</li>
                    <li class="nav_ul_li">大咖秀</li>
                    <li class="nav_ul_li">超级传送门</li>
                    <li class="nav_ul_li"><a href="http://fishc.taobao.com", target="_blank">资源打包</a></li>
                </ul>
            </nav>
        </div>
        <div class="clear"></div>
    </header>
    
    <ul class="float_btn" id="float_btn">
        <li class="btn_on"></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
    
    <div class="wrapBox" id="wrapBox">
        <div class="box">
            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg1.jpg">
            <div class="box01_content">
                <div class="head_div">
                    <div class="cycle_item">
                        <a href="https://item.taobao.com/item.htm?id=528146888326" class="taobao" id="taobao" target="_blank">
                            <span class="taobao_icon"></span>
                            <span class="taobao_text"><p class="item_name">会员</p></span>
                        </a>

                        <a href="http://blog.fishc.com" class="weibo_a" id="weibo_a" target="_blank">
                            <span class="weibo_icon"></span>
                            <span class="weibo_text"><p class="item_name">视频</p> </span>
                        </a>
                        
                        <a href="http://bbs.fishc.com" class="bbs" id="bbs" target="_blank">
                            <span class="bbs_icon"></span>
                            <span class="bbs_text"><p class="item_name">交流</p></span>
                        </a>

                        <div class="green_cycle">
                            <img class="green_cycle_img" src="images/icon/green_cycle.svg">
                            <div class="yellow_cycle">
                                <img class="yellow_cycle_img" src="images/icon/yellow_cycle.svg">
                                <div class="blue_cycle">
                                    <img class="blue_cycle_img" src="images/icon/blue_cycle.svg">
                                    <div class="head_img_div">
                                        <img class="head_img" src="images/upload/FishC.png">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <h1 class="title">Change the World by Program</h1>
                <h2 class="title_h2">I love FishC.com!</h2>

                <div id="box01_text">
                <p class="box01_p">欢迎你的加入！</p>
                
                
                </div>
            </div>

            <div class="arrow_div">
                <img class="arrow_img" src="images/icon/arrowhead.png">
            </div>
        </div>
        
        <div class="box">
            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg2.jpg">
            
            <div class="box02_content box_content">
                <div id='bar_container' class="bar_container">
                    <div class='bar red' data-percent='70' data-skill='《Windows程序设计（SDK）》'></div>

                    <div class='bar lila' data-percent='80' data-skill='《极客首选之Python》第一季：Git实用教程'></div>

                    <div class='bar orange' data-percent='60' data-skill='《带你学C带你飞》第一季：语法基础'></div>

                    <div class='bar blue' data-percent='80' data-skill='HTML-庖丁解牛（图文）'></div>

                    <div class='bar mint' data-percent='60' data-skill='JavaScript-庖丁解牛（图文）'></div>

                </div>

                <div id="box02_text">
                    <h1>鱼C里程碑</h1>
                    <div class="overline"></div>
                    <p>2010年 ~ 2011年,完成《零基础入门学习C语言》</p>
                    <p>2011年 ~2012年,完成《零基础入门学习汇编语言》</p>
                    <p>2011年 ~ 2013年,完成《C++快速入门》</p>
                    <p>2012年 ~ 2014年,完成《零基础入门学习DELPHI》</p>
                    <p>2013年 ~ 2014年，完成《数据结构和算法》</p>
                    <p>2011年 ~ 2012年，完成《解密系列》基础篇</p>
                    <p>2012年 ~ 2013年，完成《解密系列》调试篇（OD教程）</p>
                    <p>2012年 ~ 2013年，完成《解密系列》系统篇（PE结构详解）</p>
                    <p>2013年 ~ 2013年，完成《解密系列》脱壳篇</p>
                    <p>2013年 ~ 2013年，完成《解密系列》工具篇</p>
                    <p>2013年 ~ 2015年，完成《零基础入门学习Python》</p>
                    <p>2016年 ~ 2016年，完成番外篇：VIM快速入门</p>
                    <p>2016年 ~ 2016年，完成《零基础入门Scratch》（图文）</p>
                </div>
                <div class="clear"></div>
            </div>
            
            <div class="arrow_div">
                <img class="arrow_img" src="images/icon/arrowhead.png">
            </div>
            
        </div>
        
        <div class="box">
            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg3.jpg">
            
            <div class="box_content box03_content">
                <ul id="timeUl" class="timeUl">
                    <li>
                        <div id="fun1">
                            <h1 style="color:#51D9DF">7周年活动</h1>
                            <p>为了让你们的暑假生活过得更有意义，鱼C论坛筹办了本次活动……</p>
                            <p>利用暑假的时间学习一门新的知识，并将学习的过程用笔记的形式记录下来，顺便把奖学金带回家 -> <a style="color:#F265B5" href="http://bbs.fishc.com/thread-88041-1-1.html", target="_blank">点我参与</a></p>
                        </div>
                    </li>
                     <li>
                        <div>
                            <h1 style="color:#F265B5">奖品展示台</h1>
                            <p>一等奖：1000元奖学金</p>
                            <p>二等奖：888元奖学金</p>
                            <p>三等奖：666元奖学金</p>
                            <p>四等奖：100元奖学金</p>
                            <p>五等奖：200鱼币</p>
                        </div>
                    </li>
                     <li>
                        <div id="fun2">
                            <h1 style="color:#51D9DF">参与方式</h1>
                            <p>……</p>
                            <p><a style="color:#F265B5" href="http://bbs.fishc.com/thread-88041-1-1.html", target="_blank">传送门</a></p>
                            <p>……</p>

                        </div>
                    </li>
                </ul>
                

                 <div class="left_div" id="left_div">
                     <img class="left_arrow" src="images/icon/arrowleft.png">
                 </div>
                 <div class="right_div" id="right_div">
                      <img class="right_arrow" src="images/icon/arrowright.png">
                 </div>
            </div>
            
             <div class="arrow_div">
                <img class="arrow_img" src="images/icon/arrowhead.png">
            </div>
        </div>
        
        
        <div class="box">
            
            <img class="box_bg" src="http://fishc.oss-cn-hangzhou.aliyuncs.com/Home/bg4.jpg">
            <div class="box_content box04_content">
            
                <ul class="hobby_content">
                    <li class="hobby_01">
                        <div class="hobby_img_div">
                            <div class="spinner spinner_01"></div>
                            <div class="hobby_img">
                                <img src="images/upload/xiaojiayu.png">
                            </div>
                            <div class="hobby_img_info">
                                <h1>小甲鱼</h1>
                                <h2>鱼C工作室创始人</h2>
                            </div>
                        </div>
                        <div class="hobby_text_div">
                            <div class="hobby_img_info_mob">
                                <h1>小甲鱼/<a>鱼C工作室创始人</a></h1>
                            </div>
                            <p class="about_p" style="text-align: center;">
                            鱼C工作室创始人：小甲鱼
                            </p>
                            <p>
                            七年来制作了N多“小视频”，经诸多网站发布后，广受好评，多次被网页及相关专题推荐，深入程序猿单纯的内心。
                            </p>
                        </div>
                    </li>
                    <li class="hobby_02">
                        <div class="hobby_img_div">
                            <div class="spinner spinner_02"></div>
                            <div class="hobby_img">
                                <img src="images/upload/banzhu.png" width="270" height="270">
                            </div>
                            <div class="hobby_img_info">
                                <h1>鱼C版主</h1>
                                <h2>管理团队&版主</h2>
                            </div>
                        </div>
                        <div class="hobby_text_div">
                            <div class="hobby_img_info_mob">
                                <h1>鱼C版主/<a>管理团队&版主</a></h1>
                            </div>
                            <p class="about_p">
                            管理团队：康小泡、~风介~、不二如是
                            </p>
                            <p>
                            版主团队：人造人、lumber2388779、wei_Y、冬雪雪冬、hldh214、shuofxz、SixPy、零度非安全、迷途、破渔网兜兜、Minhal……
                            </p>
                        </div>
                    </li>
                    <li class="hobby_03">
                        <div class="hobby_img_div">
                            <div class="spinner spinner_03"></div>
                            <div class="hobby_img">
                                <img src="images/upload/reading.png">
                            </div>
                            <div class="hobby_img_info">
                                <h1>就是你！</h1>
                                <h2>鱼油&尽精微</h2>
                            </div>
                        </div>
                        <div class="hobby_text_div">
                            <div class="hobby_img_info_mob">
                                <h1>就是你！/<a>鱼油&尽精微</a></h1>
                            </div>
                            <p class="about_p">
                                没有人是一座孤岛，你来到鱼C，并决定留下来，这就是一种无尚荣耀！
                            </p>
                            <p>
                                欢迎来到鱼C，很快我们将俯视大地，驰骋九天。
                            </p>
                        </div>
                    </li>
                    <div class="clear"></div>
                </ul>
            </div>
             <div class="arrow_div">
                <img class="arrow_img" src="images/icon/arrowhead.png">
            </div>
        </div>
        
        <foot id="foot" class="foot">
            <h1 class="foot_title">鱼C超级传送门</h1>
            <div class="foot_info_main">
                <ul>
                    <li class="one">
                        <a href="http://bbs.fishc.com/forum-38-1.html" target="_blank">C\C++交流 </a>
                    </li>
                    <li class="two">
                        <a href="http://bbs.fishc.com/forum-79-1.html" target="_blank">数据结构与算法</a>
                    
                    </li>
                    <li class="three">
                        <a href="http://bbs.fishc.com/forum-171-1.html" target="_blank">WEB开发</a>
                    
                    </li>
                    <li class="four">
                        <a href="http://bbs.fishc.com/forum-39-1.html" target="_blank">汇编语言交流</a>
                    
                    </li>
                    <li class="five">
                        <a href="http://bbs.fishc.com/forum-241-1.html" target="_blank">JAVA语言交流</a>
                    
                    </li>
                    <li class="six">
                        <a href="http://bbs.fishc.com/forum-337-1.html" target="_blank">小天才养殖场</a>
                    
                     </li>
                     <li class="seven">
                        <a href="http://bbs.fishc.com/forum-173-1.html" target="_blank">Python交流</a>
                    
                     </li>
                     <li class="eight">
                        <a href="http://bbs.fishc.com/forum-207-1.html" target="_blank">Win程序设计 </a>
                    </li>

                     </li>
                    <li class="nine">
                        <a href="http://bbs.fishc.com/forum-219-1.html" target="_blank">哇！Linux</a>
                    
                    </li>
                    <li class="ten">
                        <a href="http://bbs.fishc.com/forum-219-1.html" target="_blank">加密与解密</a>
                    
                     </li>
                     <li class="eleven">
                        <a href="http://bbs.fishc.com/forum-120-1.html" target="_blank">Delphi交流</a>
                    
                     </li>
                     <li class="twelve">
                        <a href="http://bbs.fishc.com/forum-33-1.html" target="_blank">吹水阁</a>
                    </li>

                    <div class="clear"></div>
                </ul>
                <div class="qrcode_div">
                    <span class="weixin">
                        <a class="weixin_icon"></a>
                        <img class="weixin_img" src="images/upload/weixin_qr.png">
                    </span>
                  
                </div>
            </div>
            <div class="foot_power">
                <h3>©2017 Pwoerd Unique
                    <a href="http://www.fishc.com" title="FishC" target="_blank">FishC</a>
                    <a href="http://bbs.fishc.com/forum.php" title="IceEnd">#鱼C工作室#</a>
                    <a href="https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-2468366367.8.8gs6zK&id=528146888326" title="vip" target="_blank">  @VIP快速充值口</a>
                </h3>
            </div>
        </foot>
    </div>
    <script type="text/javascript" src="js/main.js"></script>
</body>
    
</html>

 

>>> 
