Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: F:\python\object\new.py ======================
>>> a= C()
>>> b= C()
>>> c=C()
>>> print(a.count,b.count,c.count)
0 0 0
>>> c.count +=10
>>> print(a.count,b.count,c.count)
0 0 10
>>> C.count +=100
>>> print(a.count,b.count,c.count)
100 100 10
>>> 
