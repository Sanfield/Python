Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: F:\python\file\open.py ======================
>>> f
<_io.TextIOWrapper name='F:\\python\\file\\file.txt' mode='r' encoding='cp936'>
>>> f=open("F:\\python\\file\\file.txt")
>>> f
<_io.TextIOWrapper name='F:\\python\\file\\file.txt' mode='r' encoding='cp936'>
>>>  f=open("F:\\python\\file\\file.txt","w")
 
SyntaxError: unexpected indent
>>> f=open("F:\\python\\file\\file.txt","w")
>>> f
<_io.TextIOWrapper name='F:\\python\\file\\file.txt' mode='w' encoding='cp936'>
>>> f.write("i love python\nHello,word")
24
>>> f.close()
>>> f
<_io.TextIOWrapper name='F:\\python\\file\\file.txt' mode='w' encoding='cp936'>
>>> f.open("F:\\python\\file\\file.txt")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    f.open("F:\\python\\file\\file.txt")
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> f= open(""F:\\python\\file\\file.txt"")
SyntaxError: invalid syntax
>>> f= open("F:\\python\\file\\file.txt")
>>> msg=f.readline()
>>> msg
'i love python\n'
>>> msgs=f.readlines()
>>> msgs
['Hello,word']
>>> msgs[0]
'Hello,word'
>>> msgs[1]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    msgs[1]
IndexError: list index out of range
>>> f.close()
>>> f
<_io.TextIOWrapper name='F:\\python\\file\\file.txt' mode='r' encoding='cp936'>
>>> f=open("F:\\python\\file\\file.txt","r")
>>> msg=g.readlines()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    msg=g.readlines()
NameError: name 'g' is not defined
>>> msg=f.readlines()
>>> msg
['i love python\n', 'Hello,word']
>>> msg[0]
'i love python\n'
>>> msg[1]
'Hello,word'
>>> 
