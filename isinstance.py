Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: F:\python\object\issub.py =====================
>>> issubclass(A,B)
False
>>> issubclass(B,A)
True
>>> isinstance(b,A)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    isinstance(b,A)
NameError: name 'b' is not defined
>>> b1=B()
>>> isinstance(b1,B)
True
>>> isinstance(b1,A)
True
>>> isinstance(b1,(A,B))
True
>>> 
