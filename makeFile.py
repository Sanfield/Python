Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f=open("F:\\python\\file\\file.txt","a")
>>> msg=f.readlines()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    msg=f.readlines()
io.UnsupportedOperation: not readable
>>> msg=f.read
>>> msg
<built-in method read of _io.TextIOWrapper object at 0x000002DCE69478B8>
>>> msg=f.readlin()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    msg=f.readlin()
AttributeError: '_io.TextIOWrapper' object has no attribute 'readlin'
>>> msg=f.readline()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    msg=f.readline()
io.UnsupportedOperation: not readable
>>> f.write("jha")
3
>>> f.close()
>>> f=open("F:\\python\\file\\file.txt","r")
>>> msg=f.readline()
>>> msg
'i love python\n'
>>> msgs=f.readlines()
>>> msgs[0]
'Hello,wordjha'
>>> msgs[2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    msgs[2]
IndexError: list index out of range
>>> msgs[]
SyntaxError: invalid syntax
>>> msgs[1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    msgs[1]
IndexError: list index out of range
>>> list(msgs)
['Hello,wordjha']
>>> msg=f.readlines()
>>> list(msg)
['ha\n', 'Drag 和 Drop 是一种直接操作动作，在许多图形用户界面系统中都会遇到它，它提供了一种机制，能够在两个与 GUI 中显示元素逻辑相关的实体之间传输信息。 \n', 'java.awt.event 提供处理由 AWT 组件所激发的各类事件的接口和类。 \n']
>>> f.close()
>>> f=open("F:\\python\\file\\file.t2xt","w")
>>> f.write("hahhaa")
6
>>> f.close()
>>> 
