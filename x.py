Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: F:\python\magic_function\attribute.py ===============
>>> c= C()
>>> c.x
'x=man'
>>> getattr(c,'x','木有这个属性')
'x=man'
>>> getattr(c,'y','木有这个属性')
'木有这个属性'
>>> delattr(c,'x')
>>> c.x
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c.x
AttributeError: 'C' object has no attribute 'x'
>>> 
