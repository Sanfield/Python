Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: F:\python\file\find.py ======================
>>> import os
>>> os.getcwd()
'F:\\python\\file'
>>> os.listdir('F;\\')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.listdir('F;\\')
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'F;\\'
>>> os.listdir('F;\\')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    os.listdir('F;\\')
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'F;\\'
>>> os.listdir('f:')
['fei.txt', 'fei_file.txt', 'file.txt', 'file2.txt', 'find.py', 'makeFile.py', 'open.py', 'os.py', 'RWFile.py', 'sang_file.txt']
>>> os.listdir('F:')
['fei.txt', 'fei_file.txt', 'file.txt', 'file2.txt', 'find.py', 'makeFile.py', 'open.py', 'os.py', 'RWFile.py', 'sang_file.txt']
>>> os.listdir('F;\\')

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.listdir('F;\\')
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'F;\\'
>>> os.chdir('F;\\')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.chdir('F;\\')
FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'F;\\'
>>> os.chdir("F:\\")
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'F:\\'
>>> os.listdir("F:\\")
['$RECYCLE.BIN', '100套绝美PPT模板', '15书', '394367.apk.baiduyun.downloading', '394367.apk.baiduyun.downloading.cfg', '51单片机-郭天祥', 'Adobe Photoshop CC 2017 v18.0.0 WIN32.torrent', 'Boost', 'cat', 'C语言', 'c语言大量例程 程序', 'iic', 'JavaWeb入门到精通光盘', 'New_small', 'ov2640', 'ov7620', 'python', 'qq下载', 'SQL', 'System Volume Information', 'win7', '《单片机C语言程序设计实训100例——基于8051+Proteus仿真》下载', '【3】java十大项目', '【小灶】四六级大礼包', '匿名飞行器', '实验报告模板1.doc', '探索杯', '探索者stm32', '权力者游戏', '电子书', '蓝桥杯']
>>> os.system("cmd")
0
>>> os.system("calc")
0
>>> os.curdir()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.curdir()
TypeError: 'str' object is not callable
>>> os.pardir()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    os.pardir()
TypeError: 'str' object is not callable
>>> os.name()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    os.name()
TypeError: 'str' object is not callable
>>> os.name
'nt'
>>> os.pardir
'..'
>>> os.path.basename("F:\\python\\file\\find.py")
'find.py'
>>> os.path.aplit("F:\\python\\file\\find.py")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.path.aplit("F:\\python\\file\\find.py")
AttributeError: module 'ntpath' has no attribute 'aplit'
>>> os.path.split("F:\\python\\file\\find.py")
('F:\\python\\file', 'find.py')
>>> os.path.spliext("F:\\python\\file\\find.py")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    os.path.spliext("F:\\python\\file\\find.py")
AttributeError: module 'ntpath' has no attribute 'spliext'
>>> os.path.splitext("F:\\python\\file\\find.py")
('F:\\python\\file\\find', '.py')
>>> os.path.getatime()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    os.path.getatime()
TypeError: getatime() missing 1 required positional argument: 'filename'
>>> os.path.getatime("F:\\python\\file\\sang_file.txt")
1497018719.5629592
>>> time.localtime(os.path.getatime("F:\\python\\file\\sang_file.txt"))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    time.localtime(os.path.getatime("F:\\python\\file\\sang_file.txt"))
NameError: name 'time' is not defined
>>> time.localtime(os.path.getatime("F:\\python\\file\\sang_file.txt"))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    time.localtime(os.path.getatime("F:\\python\\file\\sang_file.txt"))
NameError: name 'time' is not defined
>>> import time
>>> time.localtime(os.path.getatime("F:\\python\\file\\sang_file.txt"))
time.struct_time(tm_year=2017, tm_mon=6, tm_mday=9, tm_hour=22, tm_min=31, tm_sec=59, tm_wday=4, tm_yday=160, tm_isdst=0)
>>> 
