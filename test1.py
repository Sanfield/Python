Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: F:\python\function\dict.py ====================
>>> dict.key()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dict.key()
AttributeError: type object 'dict' has no attribute 'key'
>>> dict1.key
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dict1.key
AttributeError: 'dict' object has no attribute 'key'
>>> dict.key()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dict.key()
AttributeError: type object 'dict' has no attribute 'key'
>>> dict1.keys()
dict_keys(['三号', '一号', '四号', '二号'])
>>> a.keys()
dict_keys(['one', 'three', 'two'])
>>> dict1.values()
dict_values(['潮狗', '桑飞', '主席', '死域名'])
>>> dict1.get('一号')
'桑飞'
>>> a.clear()
>>> a
{}
>>> 
