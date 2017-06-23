Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: F:\python\magic_function\itertorer.py ===============
>>> for i in"sangfei":
	print(i)

	
s
a
n
g
f
e
i
>>> links={"sangfei":"SandField"}
>>> for each in links:
	print("%s -> %s"%(each,links(each)))

	
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print("%s -> %s"%(each,links(each)))
TypeError: 'dict' object is not callable
>>> for each in links:
	print("%s -> %s"%(each,links[each]))

	
sangfei -> SandField
>>> String ="hahaha"
>>> it = iter(String)
>>> next(it)
'h'
>>> while True:
	try:
		each=next(it)
	except StopIteration
	
SyntaxError: invalid syntax
>>> while True:
	try:
		each=next(it)
	except StopIteration"
	
SyntaxError: EOL while scanning string literal
>>> while True:
	try:
		each=next(it)
	except StopIteration:
		break
	print(each)

	
a
h
a
h
a
>>> 
